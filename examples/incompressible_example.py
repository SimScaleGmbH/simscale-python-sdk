#!/usr/bin/env python

import os
import time
import zipfile

import isodate
import urllib3
from simscale_sdk import Configuration, ApiClient, ProjectsApi, StorageApi, GeometryImportsApi, GeometriesApi, \
    MeshOperationsApi, SimulationsApi, SimulationRunsApi, ReportsApi, Project, GeometryImportRequest, ApiException, \
    MaterialsApi, MaterialGroupType, MaterialUpdateRequest, MaterialUpdateOperation, MaterialUpdateOperationReference
from simscale_sdk import GeometryImportRequestLocation, GeometryImportRequestOptions, Point, DimensionalVectorLength, \
    DecimalVector
from simscale_sdk import Incompressible, IncompressibleFluidMaterials, FluidModel, FluidInitialConditions, \
    AdvancedConcepts, TopologicalReference, FluidNumerics, RelaxationFactor, DimensionalPressure, \
    ProbePointsResultControl, \
    ResidualControls, Tolerance, FluidSolvers, Schemes, TimeDifferentiationSchemes, GradientSchemes, DivergenceSchemes, \
    LaplacianSchemes, InterpolationSchemes, SurfaceNormalGradientSchemes, VelocityInletBC, FixedValueVBC, \
    ComponentVectorFunction, ConstantFunction, PressureOutletBC, FixedValuePBC, DimensionalFunctionPressure, \
    FluidSimulationControl, DimensionalTime, TimeStepWriteControl, ScotchDecomposeAlgorithm, FluidResultControls, \
    DimensionalVectorFunctionSpeed
from simscale_sdk import SimulationSpec, MeshOperation, SimmetrixMeshingFluid, AutomaticLayerOn, SimulationRun
from simscale_sdk import UserInputCameraSettings, ProjectionType, Vector3D, ModelSettings, Part, ScalarField, \
    Color, ResolutionInfo, ReportRequest, TimeStepAnimationOutputSettings, AnimationReportProperties

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
configuration.debug = True
api_client = ApiClient(configuration)
retry_policy = urllib3.Retry(connect=5, read=5, redirect=0, status=5, backoff_factor=0.2)
api_client.rest_client.pool_manager.connection_pool_kw["retries"] = retry_policy

# API clients
project_api = ProjectsApi(api_client)
storage_api = StorageApi(api_client)
geometry_import_api = GeometryImportsApi(api_client)
geometry_api = GeometriesApi(api_client)
mesh_operation_api = MeshOperationsApi(api_client)
simulation_api = SimulationsApi(api_client)
simulation_run_api = SimulationRunsApi(api_client)
reports_api = ReportsApi(api_client)
materials_api = MaterialsApi(api_client)

# Create project
project = Project(
    name="Incompressible via Python SDK", description="Incompressible via Python SDK", measurement_system="SI"
)
project = project_api.create_project(project)
project_id = project.project_id
print(f"project_id: {project_id}")

# Read project information and update with the deserialized model
project = project_api.get_project(project_id)
project_api.update_project(project_id, project)

# Upload CAD
storage = storage_api.create_storage()
with open("fixtures/pipe_junction_model_tutorial.x_t", "rb") as file:
    api_client.rest_client.PUT(url=storage.url, headers={"Content-Type": "application/octet-stream"}, body=file.read())
storage_id = storage.storage_id
print(f"storage_id: {storage_id}")

# Import CAD
geometry_import = GeometryImportRequest(
    name="CAD-pipe-junction_v1",
    location=GeometryImportRequestLocation(storage_id),
    format="PARASOLID",
    input_unit="m",
    options=GeometryImportRequestOptions(facet_split=False, sewing=False, improve=True, optimize_for_lbm_solver=False),
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
print(f"geometry_id: {geometry_id}")

# Read geometry information and update with the deserialized model
geometry = geometry_api.get_geometry(project_id, geometry_id)
geometry_api.update_geometry(project_id, geometry_id, geometry)


# Get geometry mappings
def get_single_entity_name(project_id, geometry_id, **kwargs):
    entities = geometry_api.get_geometry_mappings(project_id, geometry_id, **kwargs)._embedded
    if len(entities) == 1:
        return entities[0].name
    else:
        raise Exception(f"Found {len(entities)} entities instead of 1: {entities}")


material_entity = get_single_entity_name(project_id, geometry_id, attributes=["SDL/TYSA_NAME"], values=["Fluid Region"])
inlet1_entity = get_single_entity_name(project_id, geometry_id, attributes=["SDL/TYSA_NAME"], values=["Face ZMAX"])
inlet2_entity = get_single_entity_name(project_id, geometry_id, attributes=["SDL/TYSA_NAME"], values=["Face Junction"])
outlet_entity = get_single_entity_name(project_id, geometry_id, attributes=["SDL/TYSA_NAME"], values=["Face YMAX"])

geometry_primitive_point = Point(
    name="Point 1",
    center=DimensionalVectorLength(
        value=DecimalVector(x=0.0035744310360600745, y=0.4499999880790711, z=-0.4507558972231502), unit="m"
    ),
)
geometry_primitive_uuid = simulation_api.create_geometry_primitive(
    project_id, geometry_primitive_point
).geometry_primitive_id
print(f"geometry_primitive_uuid: {geometry_primitive_uuid}")

# create simulation spec to pass as reference to mesh operation
model = Incompressible(
    model=FluidModel(),
    initial_conditions=FluidInitialConditions(),
    advanced_concepts=AdvancedConcepts(),
    materials=IncompressibleFluidMaterials(),
    numerics=FluidNumerics(
        relaxation_factor=RelaxationFactor(),
        pressure_reference_value=DimensionalPressure(value=0, unit="Pa"),
        residual_controls=ResidualControls(
            velocity=Tolerance(),
            pressure=Tolerance(),
            turbulent_kinetic_energy=Tolerance(),
            omega_dissipation_rate=Tolerance(),
        ),
        solvers=FluidSolvers(),
        schemes=Schemes(
            time_differentiation=TimeDifferentiationSchemes(),
            gradient=GradientSchemes(),
            divergence=DivergenceSchemes(),
            laplacian=LaplacianSchemes(),
            interpolation=InterpolationSchemes(),
            surface_normal_gradient=SurfaceNormalGradientSchemes(),
        ),
    ),
    boundary_conditions=[
        VelocityInletBC(
            name="Velocity inlet 1",
            velocity=FixedValueVBC(
                value=DimensionalVectorFunctionSpeed(
                    value=ComponentVectorFunction(
                        x=ConstantFunction(value=0), y=ConstantFunction(value=0), z=ConstantFunction(value=-1.5)
                    )
                )
            ),
            topological_reference=TopologicalReference(entities=[inlet1_entity]),
        ),
        VelocityInletBC(
            name="Velocity inlet 2",
            velocity=FixedValueVBC(
                value=DimensionalVectorFunctionSpeed(
                    value=ComponentVectorFunction(
                        x=ConstantFunction(value=0), y=ConstantFunction(value=-1), z=ConstantFunction(value=0)
                    )
                )
            ),
            topological_reference=TopologicalReference(entities=[inlet2_entity]),
        ),
        PressureOutletBC(
            name="Pressure outlet 3",
            gauge_pressure=FixedValuePBC(value=DimensionalFunctionPressure(value=ConstantFunction(value=0), unit="Pa")),
            topological_reference=TopologicalReference(entities=[outlet_entity]),
        ),
    ],
    simulation_control=FluidSimulationControl(
        end_time=DimensionalTime(value=1000, unit="s"),
        delta_t=DimensionalTime(value=1, unit="s"),
        write_control=TimeStepWriteControl(write_interval=1000),
        max_run_time=DimensionalTime(value=10000, unit="s"),
        decompose_algorithm=ScotchDecomposeAlgorithm(),
    ),
    result_control=FluidResultControls(
        probe_points=[
            ProbePointsResultControl(
                name="Probe point 1",
                write_control=TimeStepWriteControl(write_interval=1),
                geometry_primitive_uuids=[geometry_primitive_uuid],
            )
        ]
    ),
)

simulation_spec = SimulationSpec(name="Incompressible via Python SDK", geometry_id=geometry_id, model=model)
# Create simulation
simulation_id = simulation_api.create_simulation(project_id, simulation_spec).simulation_id
print(f"simulation_id: {simulation_id}")

# Add a material to the simulation
material_groups = materials_api.get_material_groups().embedded
default_material_group = next((group for group in material_groups if group.group_type == MaterialGroupType.SIMSCALE_DEFAULT), None)
if not default_material_group:
    raise Exception(f"Couldn't find default material group in {material_groups}")

default_materials = materials_api.get_materials(material_group_id=default_material_group.material_group_id).embedded
material_water = next((material for material in default_materials if material.name == "Water"), None)
if not material_water:
    raise Exception(f"Couldn't find default Water material in {default_materials}")

material_data = materials_api.get_material_data(
    material_group_id=default_material_group.material_group_id,
    material_id=material_water.id
)
material_update_request = MaterialUpdateRequest(
    operations=[
        MaterialUpdateOperation(
            path="/materials/fluids",
            material_data=material_data,
            reference=MaterialUpdateOperationReference(
                material_group_id=default_material_group.material_group_id,
                material_id=material_water.id
            )
        )
    ]
)
material_update_response = simulation_api.update_simulation_materials(project_id, simulation_id, material_update_request)

# Add assignments to the new material
simulation_spec = simulation_api.get_simulation(project_id, simulation_id)
simulation_spec.model.materials.fluids[0].topological_reference = TopologicalReference(entities=[material_entity])
simulation_api.update_simulation(project_id, simulation_id, simulation_spec)

# Start of mesh operation
mesh_operation = mesh_operation_api.create_mesh_operation(
    project_id,
    MeshOperation(
        name="Pipe junction mesh",
        geometry_id=geometry_id,
        model=SimmetrixMeshingFluid(physics_based_meshing=True, automatic_layer_settings=AutomaticLayerOn()),
    ),
)
mesh_operation_api.update_mesh_operation(project_id, mesh_operation.mesh_operation_id, mesh_operation)
mesh_operation_id = mesh_operation.mesh_operation_id

mesh_check = mesh_operation_api.check_mesh_operation_setup(project_id, mesh_operation_id, simulation_id=simulation_id)
warnings = [entry for entry in mesh_check.entries if entry.severity == "WARNING"]
print(f"Meshing check warnings: {warnings}")
errors = [entry for entry in mesh_check.entries if entry.severity == "ERROR"]
if errors:
    raise Exception("Meshing check failed", mesh_check)

# Estimate Mesh operation
try:
    mesh_estimation = mesh_operation_api.estimate_mesh_operation(project_id, mesh_operation_id)
    print(f"Mesh operation estimation: {mesh_estimation}")

    if mesh_estimation.compute_resource is not None and mesh_estimation.compute_resource.value > 10.0:
        raise Exception("Too expensive", mesh_estimation)

    if mesh_estimation.duration is not None:
        mesh_max_runtime = isodate.parse_duration(mesh_estimation.duration.interval_max).total_seconds()
        mesh_max_runtime = max(3600, mesh_max_runtime * 2)
    else:
        mesh_max_runtime = 36000
        print(f"Mesh operation estimated duration not available, assuming max runtime of {mesh_max_runtime} seconds")
except ApiException as ae:
    if ae.status == 422:
        mesh_max_runtime = 36000
        print(f"Mesh operation estimation not available, assuming max runtime of {mesh_max_runtime} seconds")
    else:
        raise ae

mesh_operation_api.start_mesh_operation(project_id, mesh_operation_id, simulation_id=simulation_id)

# Wait until the meshing operation is complete
mesh_operation = mesh_operation_api.get_mesh_operation(project_id, mesh_operation_id)
mesh_operation_start = time.time()
while mesh_operation.status not in ("FINISHED", "CANCELED", "FAILED"):
    if time.time() > mesh_operation_start + mesh_max_runtime:
        raise TimeoutError()
    time.sleep(30)
    mesh_operation = mesh_operation_api.get_mesh_operation(project_id, mesh_operation_id)
    print(f"Meshing run status: {mesh_operation.status} - {mesh_operation.progress}")

mesh_operation = mesh_operation_api.get_mesh_operation(project_id, mesh_operation_id)
print(f"final mesh_operation: {mesh_operation}")

# Get the simulation spec and update it with mesh_id from the previous mesh operation
simulation_spec = simulation_api.get_simulation(project_id, simulation_id)
simulation_spec.mesh_id = mesh_operation.mesh_id
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
print(f"results: {results}")

probe_point_plot_info = [r for r in results._embedded if r.category == "PROBE_POINT_PLOT"][0]
probe_point_plot_data_response = api_client.rest_client.GET(
    url=probe_point_plot_info.download.url,
    headers={api_key_header: api_key},
    _preload_content=False,
)
probe_point_plot_data_csv = probe_point_plot_data_response.data.decode("utf-8")
print(f"Probe point plot data as CSV: {probe_point_plot_data_csv}")

# Write probe points to CSV file
with open("probe_points.csv", "w") as file:
    file.write(probe_point_plot_data_csv)

solution_info = [r for r in results._embedded if r.category == "SOLUTION"][0]
solution_response = api_client.rest_client.GET(
    url=solution_info.download.url,
    headers={api_key_header: api_key},
    _preload_content=False,
)
with open("solution.zip", "wb") as file:
    file.write(solution_response.data)
zip = zipfile.ZipFile("solution.zip")
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
    parts=[Part(part_identifier="default_region", solid_color=Color(0.8, 0.2, 0.4))],
    scalar_field=ScalarField(field_name="Velocity", component="X", data_type="CELL"),
)
output_settings = TimeStepAnimationOutputSettings(
    type="TIME_STEP",
    name="Output 1",
    format="GIF",
    resolution=ResolutionInfo(800, 800),
    from_frame_index=0,
    to_frame_index=1,
    skip_frames=0,
)
report_properties = AnimationReportProperties(
    model_settings=model_settings,
    filters=None,
    camera_settings=camera_settings,
    output_settings=output_settings,
)
report_request = ReportRequest(name="Report 1", description="Simulation report", result_ids=[solution_info.result_id],
                               report_properties=report_properties)

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
