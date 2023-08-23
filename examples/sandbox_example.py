#!/usr/bin/env python

import os
import time
import zipfile
import urllib3

import isodate
from simscale_sdk import Configuration, ApiClient, ProjectsApi, StorageApi, GeometryImportsApi, GeometriesApi, \
    SimulationsApi, SimulationRunsApi, Project, GeometryImportRequest
from simscale_sdk import GeometryImportRequestLocation, GeometryImportRequestOptions
from simscale_sdk import SimulationSpec, SimulationRun
from simscale_sdk import WindComfort, RegionOfInterest, DimensionalLength, DimensionalVector2dLength, DecimalVector2d, \
    DimensionalAngle, AdvancedROISettings, WindTunnelSizeModerate, WindConditions, GeographicalLocation, WindRose, \
    WindRoseVelocityBucket, PedestrianComfortSurface, GroundAbsolute, WindComfortSimulationControl, WindComfortMesh, \
    DimensionalTime, FluidResultControls, PacefishFinenessCoarse

if not os.getenv("SIMSCALE_API_KEY") or not os.getenv("SIMSCALE_API_URL"):
    raise Exception("Either `SIMSCALE_API_KEY` or `SIMSCALE_API_URL` environment variable is missing.")

# API client configuration
configuration = Configuration()
configuration.host = os.getenv("SIMSCALE_API_URL") + "/sandbox/v0"
configuration.api_key = {
    "X-API-KEY": "sandbox-example-api-key",
    "apiKey": "sandbox-example-api-key",
}
api_client = ApiClient(configuration)

retry_policy = urllib3.Retry(connect=5, read=5, redirect=0, status=5, backoff_factor=0.2)
api_client.rest_client.pool_manager.connection_pool_kw["retries"] = retry_policy

# API clients
projects_api = ProjectsApi(api_client)
storage_api = StorageApi(api_client)
geometry_import_api = GeometryImportsApi(api_client)
geometry_api = GeometriesApi(api_client)
simulation_api = SimulationsApi(api_client)
simulation_run_api = SimulationRunsApi(api_client)

# Create project: POST /projects/
project = Project(name="My first project", description="My first project description")
project = projects_api.create_project(project)
project_id = project.project_id

# Upload CAD: POST /storage + PUT {storage.url}
storage = storage_api.create_storage()
cad_file_content = "dummy"  # load CAD file content
api_client.rest_client.PUT(url=storage.url, body=cad_file_content)

# Import CAD: POST /projects/{projectId}/geometryimports
geometry_import = GeometryImportRequest(
    name="My first CAD",
    location=GeometryImportRequestLocation(storage.storage_id),
    format="STL",
    input_unit="m",
    options=GeometryImportRequestOptions(facet_split=False, sewing=False, improve=True, optimize_for_lbm_solver=True),
)
geometry_import = geometry_import_api.import_geometry(project_id, geometry_import)
geometry_import_id = geometry_import.geometry_import_id

# Wait until CAD import is finished: GET /projects/{projectId}/geometryimports/{geometryId}
geometry_import = geometry_import_api.get_geometry_import(project_id, geometry_import_id)
geometry_import_start = time.time()
while geometry_import.status not in ("FINISHED", "CANCELED", "FAILED"):
    if time.time() > geometry_import_start + 900:
        raise TimeoutError()
    geometry_import = geometry_import_api.get_geometry_import(project_id, geometry_import_id)
    time.sleep(10)
geometry_id = geometry_import.geometry_id

#  Create simulation setup: POST /projects/{projectId}/simulations
model = WindComfort(
    region_of_interest=RegionOfInterest(
        disc_radius=DimensionalLength(279, "m"),
        center_point=DimensionalVector2dLength(DecimalVector2d(11.72, 14.6), "m"),
        ground_height=DimensionalLength(-12.8, "m"),
        north_angle=DimensionalAngle(0, "°"),
        advanced_settings=AdvancedROISettings(WindTunnelSizeModerate()),
    ),
    wind_conditions=WindConditions(
        geographical_location=GeographicalLocation(
            latitude=DimensionalAngle(41.385064, "°"), longitude=DimensionalAngle(2.173404, "°")
        ),
        wind_rose=WindRose(
            num_directions=4,
            velocity_buckets=[WindRoseVelocityBucket(), WindRoseVelocityBucket()],  # TODO: incomplete
            velocity_unit="m/s",
            exposure_categories=["EC4", "EC4", "EC4", "EC4"],
            wind_engineering_standard="AS_NZS",
            add_surface_roughness=False,
        ),
    ),
    pedestrian_comfort_map=[
        PedestrianComfortSurface(
            name="Pedestrian level 1", height_above_ground=DimensionalLength(1.5, "m"), ground=GroundAbsolute()
        )
    ],
    simulation_control=WindComfortSimulationControl(
        max_direction_run_time=DimensionalTime(10000, "s"), number_of_fluid_passes=0.2
    ),
    additional_result_export=FluidResultControls(),  # TODO: incomplete
    mesh_settings=WindComfortMesh(wind_comfort_fineness=PacefishFinenessCoarse()),
)
simulation_spec = SimulationSpec(name="My first simulation", geometry_id=geometry_id, model=model)
simulation_spec = simulation_api.create_simulation(project_id, simulation_spec)
simulation_id = simulation_spec.simulation_id

# Get simulation: GET /projects/{projectId}/simulations/{simulationId}
simulation_spec = simulation_api.get_simulation(project_id, simulation_id)
if simulation_spec.model.type != "WIND_COMFORT":
    raise Exception("Retrieved simulation spec has wrong type", simulation_spec)

# Check simulation: POST /projects/{projectId}/simulations/{simulationId}/check
check = simulation_api.check_simulation_setup(project_id, simulation_id)
errors = [entry for entry in check.entries if entry.severity == "ERROR"]
if errors:
    raise Exception("Simulation check failed", check)

# Estimate simulation: POST /projects/{projectId}/simulations/{simulationId}/estimate
estimation = simulation_api.estimate_simulation_setup(project_id, simulation_id)
too_expensive = estimation.compute_resource.value > 10.0
if too_expensive:
    raise Exception("Too expensive", estimation)
max_runtime = isodate.parse_duration(estimation.duration.interval_max).total_seconds()
max_runtime = max_runtime + 600  # 10 min buffer

# Create simulation run: POST /projects/{projectId}/simulations/{simulationId}/runs
simulation_run = SimulationRun(name="My first simulation run")
simulation_run = simulation_run_api.create_simulation_run(project_id, simulation_id, simulation_run)
run_id = simulation_run.run_id

# Start simulation run: POST /projects/{projectId}/simulations/{simulationId}/runs/{runId}/start
simulation_run_api.start_simulation_run(project_id, simulation_id, run_id)

# Wait until simulation run is finished: GET /projects/{projectId}/simulations/{simulationId}/runs/{runId}
simulation_run = simulation_run_api.get_simulation_run(project_id, simulation_id, run_id)
simulation_run_start = time.time()
while simulation_run.status not in ("FINISHED", "CANCELED", "FAILED"):
    if time.time() > simulation_run_start + max_runtime:
        raise TimeoutError()
    simulation_run = simulation_run_api.get_simulation_run(project_id, simulation_id, run_id)
    time.sleep(10)

# Get result metadata: GET /projects/{projectId}/simulations/{simulationId}/runs/{runId}/results (response is paginated)
results = simulation_run_api.get_simulation_run_results(
    project_id,
    simulation_id,
    run_id,
    page=1,
    limit=100,
    category="STATISTICAL_SURFACE_SOLUTION"
)
solution = results.embedded[0]
too_large = solution.download.uncompressed_size_in_bytes > 100000000
if too_large:
    raise Exception("Solution is too large", solution)

try:
    solution_response = api_client.rest_client.GET(url=solution.download.url, _preload_content=False)
    with open("solution.zip", "wb") as file:
        file.write(solution_response.data)
    zip_file = zipfile.ZipFile("solution.zip")
    print(f"Solution ZIP file content: {zip_file.namelist()}")
except BaseException as e:
    print(f"Error while downloading results: ")
    print(e)
