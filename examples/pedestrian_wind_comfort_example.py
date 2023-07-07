#!/usr/bin/env python

import os
import time
import zipfile

import isodate
import urllib3
from simscale_sdk import Configuration, ApiClient, ProjectsApi, StorageApi, GeometryImportsApi, GeometriesApi, \
    WindApi, SimulationsApi, SimulationRunsApi, ReportsApi, Project, GeometryImportRequest, ApiException, WindData
from simscale_sdk import GeometryImportRequestLocation, GeometryImportRequestOptions
from simscale_sdk import SimulationSpec, SimulationRun
from simscale_sdk import UserInputCameraSettings, ProjectionType, Vector3D, ModelSettings, Part, \
    ScreenshotOutputSettings, Color, ResolutionInfo, ScreenshotReportProperties, ReportRequest
from simscale_sdk import WindComfort, RegionOfInterest, DimensionalLength, DimensionalVector2dLength, DecimalVector2d, \
    DimensionalAngle, AdvancedROISettings, WindTunnelSizeModerate, WindConditions, GeographicalLocation, WindRose, \
    WindRoseVelocityBucket, PedestrianComfortSurface, GroundAbsolute, WindComfortSimulationControl, AdvancedModelling, \
    TransientResultControl, CoarseResolution, StatisticalAveragingResultControlV2, PacefishFinenessVeryCoarse, \
    WindComfortMesh, DimensionalTime, FluidResultControls

# Check that the environment variables are set
if not os.getenv("SIMSCALE_API_KEY") or not os.getenv("SIMSCALE_API_URL"):
    raise Exception("Either `SIMSCALE_API_KEY` or `SIMSCALE_API_URL` environment variable is missing.")

# API client configuration
api_key = os.getenv("SIMSCALE_API_KEY")
api_url = os.getenv("SIMSCALE_API_URL")
api_key_header = "X-API-KEY"

configuration = Configuration()
configuration.debug = True
configuration.host = api_url + "/v0"
configuration.api_key = {
    api_key_header: api_key
}

api_client = ApiClient(configuration)

retry_policy = urllib3.Retry(connect=5, read=5, redirect=0, status=5, backoff_factor=0.2)
api_client.rest_client.pool_manager.connection_pool_kw["retries"] = retry_policy
# API clients
project_api = ProjectsApi(api_client)
storage_api = StorageApi(api_client)
geometry_import_api = GeometryImportsApi(api_client)
geometry_api = GeometriesApi(api_client)
wind_api = WindApi(api_client)
simulation_api = SimulationsApi(api_client)
simulation_run_api = SimulationRunsApi(api_client)
reports_api = ReportsApi(api_client)

# Create project
project = Project(
    name="Pedestrian Wind Comfort via Python SDK",
    description="Pedestrian Wind Comfort via Python SDK",
    measurement_system="SI",
)
project = project_api.create_project(project)
project_id = project.project_id
print(f"projectId: {project_id}")

# Read project information and update with the deserialized model
project = project_api.get_project(project_id)
project_api.update_project(project_id, project)

# Upload CAD
storage = storage_api.create_storage()
with open("fixtures/Cylinder.stl", "rb") as file:
    api_client.rest_client.PUT(url=storage.url, headers={"Content-Type": "application/octet-stream"}, body=file.read())
storage_id = storage.storage_id
print(f"storageId: {storage_id}")

# Import CAD
geometry_import = GeometryImportRequest(
    name="Cylinder",
    location=GeometryImportRequestLocation(storage_id),
    format="STL",
    input_unit="m",
    options=GeometryImportRequestOptions(facet_split=False, sewing=False, improve=True, optimize_for_lbm_solver=True),
)
geometry_import = geometry_import_api.import_geometry(project_id, geometry_import)
geometry_import_id = geometry_import.geometry_import_id
geometry_import_start = time.time()
while geometry_import.status not in ("FINISHED", "CANCELED", "FAILED"):
    # adjust timeout for larger geometries
    if time.time() > geometry_import_start + 900:
        raise TimeoutError()
    time.sleep(10)
    geometry_import = geometry_import_api.get_geometry_import(project_id, geometry_import_id)
    print(f"Geometry import status: {geometry_import.status}")
geometry_id = geometry_import.geometry_id
print(f"geometryId: {geometry_id}")

# Read geometry information and update with the deserialized model
geometry = geometry_api.get_geometry(project_id, geometry_id)
geometry_api.update_geometry(project_id, geometry_id, geometry)

# The wind data can be user-defined or obtained from the WindApi, as shown in the following two examples:

# 1. User-defined wind data for simulation spec
wind_rose = WindRose(
    num_directions=4,
    velocity_buckets=[
        WindRoseVelocityBucket(_from=None, to=1.234, fractions=[0.1, 0.1, 0.1, 0.1]),
        WindRoseVelocityBucket(_from=1.234, to=2.345, fractions=[0.0, 0.1, 0.1, 0.1]),
        WindRoseVelocityBucket(_from=2.345, to=3.456, fractions=[0.0, 0.0, 0.1, 0.1]),
        WindRoseVelocityBucket(_from=3.456, to=None, fractions=[0.0, 0.0, 0.0, 0.1]),
    ],
    velocity_unit="m/s",
    exposure_categories=["EC4", "EC4", "EC4", "EC4"],
    wind_engineering_standard="EU",
    wind_data_source="USER_UPLOAD",
    add_surface_roughness=False,
)

# 2. Get wind data from the WindApi for simulation spec
try:
    wind_rose_response = wind_api.get_wind_data("48.135125", "11.581981")
    wind_rose = wind_rose_response.wind_rose
    wind_rose.num_directions = 4
    wind_rose.exposure_categories = ["EC4"] * wind_rose.num_directions
    wind_rose.wind_engineering_standard = "EU"
    wind_rose.add_surface_roughness = False
except ApiException as ae:
    if ae.status == 429:
        print(
            f"Exceeded max amount requests, please retry in {ae.headers.get('X-Rate-Limit-Retry-After-Minutes')} minutes")
        raise ApiException(ae)
    else:
        raise ae

# Define simulation spec
model = WindComfort(
    region_of_interest=RegionOfInterest(
        disc_radius=DimensionalLength(100, "m"),
        center_point=DimensionalVector2dLength(DecimalVector2d(0, 0), "m"),
        ground_height=DimensionalLength(0, "m"),
        north_angle=DimensionalAngle(0, "°"),
        advanced_settings=AdvancedROISettings(WindTunnelSizeModerate()),
    ),
    wind_conditions=WindConditions(
        geographical_location=GeographicalLocation(
            latitude=DimensionalAngle(48.135125, "°"), longitude=DimensionalAngle(11.581981, "°")
        ),
        wind_rose=wind_rose,
    ),
    pedestrian_comfort_map=[
        PedestrianComfortSurface(
            name="Pedestrian level 1", height_above_ground=DimensionalLength(1.5, "m"), ground=GroundAbsolute()
        )
    ],
    simulation_control=WindComfortSimulationControl(
        max_direction_run_time=DimensionalTime(10000, "s"), number_of_fluid_passes=0.2
    ),
    advanced_modelling=AdvancedModelling(),
    additional_result_export=FluidResultControls(
        transient_result_control=TransientResultControl(
            write_control=CoarseResolution(),
            fraction_from_end=0.1,
        ),
        statistical_averaging_result_control=StatisticalAveragingResultControlV2(
            sampling_interval=CoarseResolution(),
            fraction_from_end=0.1,
        ),
    ),
    mesh_settings=WindComfortMesh(wind_comfort_fineness=PacefishFinenessVeryCoarse()),
)

simulation_spec = SimulationSpec(name="Pedestrian Wind Comfort via Python SDK", geometry_id=geometry_id, model=model)

# Create simulation
simulation_id = simulation_api.create_simulation(project_id, simulation_spec).simulation_id
print(f"simulationId: {simulation_id}")

# Read simulation spec and update with the deserialized model
simulation_spec = simulation_api.get_simulation(project_id, simulation_id)
simulation_api.update_simulation(project_id, simulation_id, simulation_spec)

# Check simulation
check = simulation_api.check_simulation_setup(project_id, simulation_id)
warnings = [entry for entry in check.entries if entry.severity == "WARNING"]
print(f"Simulation check warnings: {warnings}")
errors = [entry for entry in check.entries if entry.severity == "ERROR"]
if errors:
    raise Exception("Simulation check failed", check)

# Estimate simulation
try:
    estimation = simulation_api.estimate_simulation_setup(project_id, simulation_id)
    print(f"Simulation estimation: {estimation}")

    if estimation.compute_resource is not None and estimation.compute_resource.value > 10.0:
        raise Exception("Too expensive", estimation)

    if estimation.duration is not None:
        max_runtime = isodate.parse_duration(estimation.duration.interval_max).total_seconds()
        max_runtime = max(3600, max_runtime * 2)
    else:
        max_runtime = 36000
        print(f"Simulation estimated duration not available, assuming max runtime of {max_runtime} seconds")
except ApiException as ae:
    if ae.status == 422:
        max_runtime = 36000
        print(f"Simulation estimation not available, assuming max runtime of {max_runtime} seconds")
    else:
        raise ae

# Create simulation run
simulation_run = SimulationRun(name="Run 1")
simulation_run = simulation_run_api.create_simulation_run(project_id, simulation_id, simulation_run)
run_id = simulation_run.run_id
print(f"runId: {run_id}")

# Read simulation run and update with the deserialized model
simulation_run = simulation_run_api.get_simulation_run(project_id, simulation_id, run_id)
simulation_run_api.update_simulation_run(project_id, simulation_id, run_id, simulation_run)

# Start simulation run and wait until it's finished
simulation_run_api.start_simulation_run(project_id, simulation_id, run_id)
simulation_run = simulation_run_api.get_simulation_run(project_id, simulation_id, run_id)
simulation_run_start = time.time()
while simulation_run.status not in ("FINISHED", "CANCELED", "FAILED"):
    if time.time() > simulation_run_start + max_runtime:
        raise TimeoutError()
    time.sleep(30)
    simulation_run = simulation_run_api.get_simulation_run(project_id, simulation_id, run_id)
    print(f"Simulation run status: {simulation_run.status} - {simulation_run.progress}")

# Get result metadata and download results (response is paginated)
results = simulation_run_api.get_simulation_run_results(
    project_id,
    simulation_id,
    run_id,
    page=1,
    limit=100,
    category="STATISTICAL_SURFACE_SOLUTION"
)
print(f"Results: {results}")

# Download statistical surface solution
statistical_surface_solution_info = results.embedded[0]
statistical_surface_solution_response = api_client.rest_client.GET(
    url=statistical_surface_solution_info.download.url, headers={api_key_header: api_key}, _preload_content=False
)
with open("statistical_surface_solution.zip", "wb") as file:
    file.write(statistical_surface_solution_response.data)
zip_file = zipfile.ZipFile("statistical_surface_solution.zip")
print(f"Statistical surface solution solution ZIP file content: {zip_file.namelist()}")

# Generating simulation run report
camera_settings = UserInputCameraSettings(
    projection_type=ProjectionType.ORTHOGONAL,
    up=Vector3D(0.5, 0.3, 0.2),
    eye=Vector3D(0.0, 5.0, 10.0),
    center=Vector3D(10.0, 12.0, 1.0),
    front_plane_frustum_height=0.5,
)
model_settings = ModelSettings(
    parts=[Part(part_identifier="Pedestrian level 1", solid_color=Color(0.8, 0.2, 0.4))],
)
output_settings = ScreenshotOutputSettings("Output 1", "PNG", ResolutionInfo(800, 800), frame_index=0)
report_properties = ScreenshotReportProperties(
    model_settings=model_settings,
    filters=None,
    camera_settings=camera_settings,
    output_settings=output_settings,
)
report_request = ReportRequest(
    name="Report 1", description="Simulation report", result_ids=[statistical_surface_solution_info.result_id],
    report_properties=report_properties
)

create_report_response = reports_api.create_report(project_id, report_request)
report_id = create_report_response.report_id

# Start report job
print(f"Starting report with ID {report_id}")
report_job = reports_api.start_report_job(project_id, report_id)

report = reports_api.get_report(project_id, report_id)

while report.status not in ("FINISHED", "CANCELED", "FAILED"):
    time.sleep(30)
    report = reports_api.get_report(project_id, report_id)

print(f"Report finished with status {report.status}")

if report.status == "FINISHED":
    # Download the report
    print("Downloading report result")
    report_response = api_client.rest_client.GET(
        url=report.download.url,
        headers={api_key_header: api_key},
        _preload_content=False,
    )

    file_name = f"report.{report.download.format}"
    with open(file_name, "wb") as file:
        file.write(report_response.data)
        print(f"Finished downloading report with name {file_name}")
elif report.status == "FAILED":
    raise Exception("Report generation failed", report.failure_reason)

# The following sections show a use case of the "additional wind data" functionality. This part is optional when
# running a simple PWC simulation, but it can be helpful when running the same simulation multiple times with different
# wind data. In this case, the directional results will be reused from the original simulation run, only the statistical
# surface solution will be re-calculated.

# Update the simulation spec
model = simulation_api.get_simulation(project_id, simulation_id).model
model.pedestrian_comfort_map[0].height_above_ground = DimensionalLength(1.8, "m")

updated_simulation_spec = SimulationSpec(
    name="Pedestrian Wind Comfort with additional data", geometry_id=geometry_id, model=model
)
simulation_api.update_simulation(project_id, simulation_id, updated_simulation_spec)

# Create a simulation run based on the updated spec and the previous run
wind_data = WindData("Additional wind rose run")
additional_run = simulation_run_api.add_wind_data_to_simulation_run(
    project_id, simulation_id, simulation_run.run_id, wind_data
)
additional_run_id = additional_run.run_id

# Start additional simulation run and wait until it's finished
additional_run = simulation_run_api.get_simulation_run(project_id, simulation_id, additional_run_id)
simulation_run_start = time.time()
while additional_run.status not in ("FINISHED", "CANCELED", "FAILED"):
    if time.time() > simulation_run_start + max_runtime:
        raise TimeoutError()
    time.sleep(30)
    additional_run = simulation_run_api.get_simulation_run(project_id, simulation_id, additional_run_id)
    print(f"Simulation run status: {additional_run.status} - {additional_run.progress}")

# Get result metadata and download results
updated_results = simulation_run_api.get_simulation_run_results(
    project_id,
    simulation_id,
    run_id,
    page=1,
    limit=100,
    category="STATISTICAL_SURFACE_SOLUTION"
)
print(f"Updated results: {results}")

# Download statistical surface solution once again
updated_statistical_surface_solution_info = updated_results.embedded[0]
updated_statistical_surface_solution_response = api_client.rest_client.GET(
    url=updated_statistical_surface_solution_info.download.url, headers={api_key_header: api_key}, _preload_content=False
)
with open("statistical_surface_solution_2.zip", "wb") as file:
    file.write(updated_statistical_surface_solution_response.data)
zip_file = zipfile.ZipFile("statistical_surface_solution_2.zip")
print(f"Updated statistical surface solution solution ZIP file content: {zip_file.namelist()}")
