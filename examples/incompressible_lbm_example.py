#!/usr/bin/env python

import os
import time
import zipfile

import isodate
import urllib3
from simscale_sdk import Configuration, ApiClient, ProjectsApi, StorageApi, GeometryImportsApi, GeometriesApi, \
    SimulationsApi, SimulationRunsApi, ReportsApi, Project, GeometryImportRequest, ApiException, TableImportsApi
from simscale_sdk import GeometryImportRequestLocation, GeometryImportRequestOptions, DimensionalVectorLength, \
    DecimalVector, TableImportRequest, TableImportRequestLocation
from simscale_sdk import IncompressibleMaterial, TopologicalReference, DimensionalKinematicViscosity, \
    DimensionalDensity, DimensionalTemperature, VelocityInletBC, ConstantFunction, PressureOutletBC, WallBC, NoSlipVBC, \
    FluidSimulationControl, DimensionalTime, FluidResultControls, ProbePointsResultControl, NewtonianViscosityModel, \
    RotatableCartesianBox, DimensionalVectorAngle, LocalCartesianBox, IncompressiblePacefish, DimensionalMolarMass, \
    FlowDomainBoundaries, FixedMagnitudeVBC, DimensionalFunctionSpeed, TableDefinedFunction, TableFunctionParameter, \
    TurbulenceIntensityTIBC, DimensionalFunctionDimensionless, CustomOmegaDissipation, \
    DimensionalFunctionSpecificTurbulenceDissipationRate, SlipVBC, DimensionalLength, AdvancedModelling, \
    ForcesMomentsResultControl, HighResolution, ModerateResolution, TableDefinedProbeLocations, TransientResultControl, \
    CoarseResolution, StatisticalAveragingResultControlV2, SnapshotResultControl, PacefishFinenessCoarse, \
    PacefishAutomesh, AutomaticReferenceLength, Region
from simscale_sdk import SimulationSpec, SimulationRun
from simscale_sdk import UserInputCameraSettings, ProjectionType, Vector3D, ModelSettings, Part, ScalarField, \
    ScreenshotOutputSettings, Color, ResolutionInfo, ScreenshotReportProperties, ReportRequest

if not os.getenv("SIMSCALE_API_KEY") or not os.getenv("SIMSCALE_API_URL"):
    raise Exception("Either `SIMSCALE_API_KEY` or `SIMSCALE_API_URL` environment variable is missing.")

# API client configuration
api_key_header = "X-API-KEY"
api_key = os.getenv("SIMSCALE_API_KEY")
configuration = Configuration()
configuration.host = os.getenv("SIMSCALE_API_URL") + "/v0"
configuration.api_key = {
    api_key_header: api_key,
}
api_client = ApiClient(configuration)
retry_policy = urllib3.Retry(connect=5, read=5, redirect=0, status=5, backoff_factor=0.2)
api_client.rest_client.pool_manager.connection_pool_kw["retries"] = retry_policy

# API clients
project_api = ProjectsApi(api_client)
storage_api = StorageApi(api_client)
geometry_import_api = GeometryImportsApi(api_client)
geometry_api = GeometriesApi(api_client)
simulation_api = SimulationsApi(api_client)
simulation_run_api = SimulationRunsApi(api_client)
table_import_api = TableImportsApi(api_client)
reports_api = ReportsApi(api_client)

# Create project
project = Project(
    name="Incompressible LBM via Python SDK", description="Incompressible LBM via Python SDK", measurement_system="SI"
)
project = project_api.create_project(project)
project_id = project.project_id
print(f"projectId: {project_id}")

# Read project information and update with the deserialized model
project = project_api.get_project(project_id)
project_api.update_project(project_id, project)

# Upload CAD
storage = storage_api.create_storage()
with open("fixtures/Shapes.stl", "rb") as file:
    api_client.rest_client.PUT(url=storage.url, headers={"Content-Type": "application/octet-stream"}, body=file.read())
storage_id = storage.storage_id
print(f"geometry storageId: {storage_id}")

# Import CAD
geometry_import = GeometryImportRequest(
    name="Shapes",
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

# Get geometry mappings
geometry_mappings = geometry_api.get_geometry_mappings(
    project_id, geometry_id, _class="face", entities=["Cylinder", "Cube 2", "Sphere"]
)
entities = [mapping.name for mapping in geometry_mappings._embedded]
print(f"entities: {entities}")

# Upload table containing Probe Points information
probe_points_csv_storage = storage_api.create_storage()
with open("fixtures/ProbePoints.csv", "rb") as file:
    api_client.rest_client.PUT(
        url=probe_points_csv_storage.url, headers={"Content-Type": "application/octet-stream"}, body=file.read()
    )
probe_point_csv_storage_id = probe_points_csv_storage.storage_id
print(f"Probe Points table storageId: {probe_point_csv_storage_id}")

# Import table containing Probe Points information
probe_points_table_import = TableImportRequest(location=TableImportRequestLocation(probe_point_csv_storage_id))
probe_points_table_import_response = table_import_api.import_table(project_id, probe_points_table_import)
probe_points_table_id = probe_points_table_import_response.table_id

# Upload table containing Inlet Profile information
inlet_profile_csv_storage = storage_api.create_storage()
with open("fixtures/InletProfile.csv", "rb") as file:
    api_client.rest_client.PUT(
        url=inlet_profile_csv_storage.url, headers={"Content-Type": "application/octet-stream"}, body=file.read()
    )
inlet_profile_csv_storage_id = inlet_profile_csv_storage.storage_id
print(f"Inlet Profile table storageId: {inlet_profile_csv_storage_id}")

# Import table containing Inlet Profile information
inlet_profile_table_import = TableImportRequest(location=TableImportRequestLocation(inlet_profile_csv_storage_id))
inlet_profile_table_import_response = table_import_api.import_table(project_id, inlet_profile_table_import)
inlet_profile_table_id = inlet_profile_table_import_response.table_id

# Create geometry primitives
external_flow_domain = RotatableCartesianBox(
    name="External Flow Domain",
    min=DimensionalVectorLength(value=DecimalVector(x=-350, y=-100, z=0), unit="m"),
    max=DimensionalVectorLength(value=DecimalVector(x=650, y=100, z=300), unit="m"),
    rotation_point=DimensionalVectorLength(value=DecimalVector(x=0, y=0, z=0), unit="m"),
    rotation_angles=DimensionalVectorAngle(value=DecimalVector(x=0, y=0, z=0), unit="°"),
)
external_flow_domain_uuid = simulation_api.create_geometry_primitive(
    project_id, external_flow_domain
).geometry_primitive_id
mesh_region = LocalCartesianBox(
    name="Mesh Region",
    orientation_reference="GEOMETRY",
    min=DimensionalVectorLength(value=DecimalVector(x=-30, y=-30, z=0), unit="m"),
    max=DimensionalVectorLength(value=DecimalVector(x=30, y=30, z=120), unit="m"),
)
mesh_region_uuid = simulation_api.create_geometry_primitive(project_id, mesh_region).geometry_primitive_id

# Define simulation spec
model = IncompressiblePacefish(
    bounding_box_uuid=external_flow_domain_uuid,
    material=IncompressibleMaterial(
        name="Air",
        viscosity_model=NewtonianViscosityModel(
            kinematic_viscosity=DimensionalKinematicViscosity(value=0.00001529, unit="m²/s")
        ),
        density=DimensionalDensity(value=1.1965, unit="kg/m³"),
        reference_temperature=DimensionalTemperature(value=293.15, unit="K"),
        molar_weight=DimensionalMolarMass(value=28.97, unit="kg/kmol"),
    ),
    flow_domain_boundaries=FlowDomainBoundaries(
        xmin=VelocityInletBC(
            name="Velocity inlet (A)",
            velocity=FixedMagnitudeVBC(
                value=DimensionalFunctionSpeed(
                    value=TableDefinedFunction(
                        table_id=inlet_profile_table_id,
                        result_index=[2],
                        independent_variables=[TableFunctionParameter(reference=1, parameter="HEIGHT", unit="m")],
                    ),
                    unit="m/s",
                )
            ),
            turbulence_intensity=TurbulenceIntensityTIBC(
                value=DimensionalFunctionDimensionless(value=ConstantFunction(value=0.015), unit="")
            ),
            dissipation_type=CustomOmegaDissipation(
                value=DimensionalFunctionSpecificTurbulenceDissipationRate(
                    value=TableDefinedFunction(
                        table_id=inlet_profile_table_id,
                        result_index=[3],
                        independent_variables=[TableFunctionParameter(reference=1, parameter="HEIGHT", unit="m")],
                    ),
                    unit="1/s",
                )
            ),
        ),
        xmax=PressureOutletBC(name="Pressure outlet (B)"),
        ymin=WallBC(name="Side (C)", velocity=SlipVBC()),
        ymax=WallBC(name="Side (D)", velocity=SlipVBC()),
        zmin=WallBC(
            name="Ground (E)",
            velocity=NoSlipVBC(
                surface_roughness=DimensionalLength(value=0, unit="m"),
            ),
        ),
        zmax=WallBC(name="Top (F)", velocity=SlipVBC()),
    ),
    simulation_control=FluidSimulationControl(
        end_time=DimensionalTime(value=5, unit="s"),
    ),
    advanced_modelling=AdvancedModelling(),
    result_control=FluidResultControls(
        forces_moments=[
            ForcesMomentsResultControl(
                name="Forces and moments 1",
                center_of_rotation=DimensionalVectorLength(value=DecimalVector(x=0, y=0, z=0), unit="m"),
                write_control=HighResolution(),
                export_statistics=False,
                group_assignments=False,
                topological_reference=TopologicalReference(
                    entities=entities,
                ),
            ),
            ForcesMomentsResultControl(
                name="Forces and moments 2",
                center_of_rotation=DimensionalVectorLength(value=DecimalVector(x=0, y=0, z=0), unit="m"),
                write_control=HighResolution(),
                fraction_from_end=0.3,
                topological_reference=TopologicalReference(
                    entities=entities,
                ),
            ),
        ],
        probe_points=[
            ProbePointsResultControl(
                name="Probe point 1",
                write_control=ModerateResolution(),
                probe_locations=TableDefinedProbeLocations(table_id=probe_points_table_id),
            )
        ],
        transient_result_control=TransientResultControl(
            write_control=CoarseResolution(),
            export_surface=True,
            geometry_primitive_uuids=[external_flow_domain_uuid],
        ),
        statistical_averaging_result_control=StatisticalAveragingResultControlV2(
            sampling_interval=CoarseResolution(),
            export_surface=True,
            geometry_primitive_uuids=[external_flow_domain_uuid],
        ),
        snapshot_result_control=SnapshotResultControl(
            export_surface=True,
            geometry_primitive_uuids=[external_flow_domain_uuid],
        ),
    ),
    mesh_settings_new=PacefishAutomesh(
        new_fineness=PacefishFinenessCoarse(),
        reference_length_computation=AutomaticReferenceLength(),
        primary_topology=Region(geometry_primitive_uuids=[mesh_region_uuid]),
    ),
)
simulation_spec = SimulationSpec(name="Incompressible LBM via Python SDK", geometry_id=geometry_id, model=model)

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

# Get result metadata and download results

results = simulation_run_api.get_simulation_run_results(project_id, simulation_id, run_id)

probe_point_plot_statistical_data_info = [
    r for r in results._embedded if r.category == "PROBE_POINT_PLOT_STATISTICAL_DATA"
][0]
probe_point_plot_statistical_data_response = api_client.rest_client.GET(
    url=probe_point_plot_statistical_data_info.download.url,
    headers={api_key_header: api_key},
    _preload_content=False,
)
probe_point_plot_statistical_data_csv = probe_point_plot_statistical_data_response.data.decode("utf-8")
print(f"Probe point plot statistical data as CSV: {probe_point_plot_statistical_data_csv}")

# Write probe points to CSV file
with open("probe_points.csv", "w") as file:
    file.write(probe_point_plot_statistical_data_csv)

averaged_solution_info = [r for r in results._embedded if r.category == "AVERAGED_SOLUTION"][0]
averaged_solution_response = api_client.rest_client.GET(
    url=averaged_solution_info.download.url,
    headers={api_key_header: api_key},
    _preload_content=False,
)
with open("averaged_solution.zip", "wb") as file:
    file.write(averaged_solution_response.data)
zip = zipfile.ZipFile("averaged_solution.zip")
print(f"Averaged solution ZIP file content: {zip.namelist()}")

# Generating simulation run report

camera_settings = UserInputCameraSettings(
    projection_type=ProjectionType.ORTHOGONAL,
    up=Vector3D(0.5, 0.3, 0.2),
    eye=Vector3D(0.0, 5.0, 10.0),
    center=Vector3D(10.0, 12.0, 1.0),
    front_plane_frustum_height=0.5,
)
model_settings = ModelSettings(
    parts=[
        Part(
            part_identifier="data - mesh_solid-volume-reference-of-all-face-topo-entities",
            solid_color=Color(0.8, 0.2, 0.4),
        )
    ],
    scalar_field=ScalarField(field_name="Velocity", component="X", data_type="CELL"),
)
output_settings = ScreenshotOutputSettings(name="Output 1", format="PNG", resolution=ResolutionInfo(800, 800),
                                           frame_index=0)
report_properties = ScreenshotReportProperties(
    model_settings=model_settings,
    filters=None,
    camera_settings=camera_settings,
    output_settings=output_settings,
)
report_request = ReportRequest(
    name="Report 1",
    description="Simulation report",
    result_ids=[averaged_solution_info.result_id],
    report_properties=report_properties,
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
