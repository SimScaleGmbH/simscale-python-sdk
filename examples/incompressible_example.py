#!/usr/bin/env python

import isodate
import os
import time
import zipfile
from simscale_sdk import *


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

# API clients
project_api = ProjectsApi(api_client)
storage_api = StorageApi(api_client)
geometry_import_api = GeometryImportsApi(api_client)
geometry_api = GeometriesApi(api_client)
mesh_operation_api = MeshOperationsApi(api_client)
simulation_api = SimulationsApi(api_client)
simulation_run_api = SimulationRunsApi(api_client)

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
material_entity = get_single_entity_name(project_id, geometry_id, _class="region")
inlet1_entity = get_single_entity_name(project_id, geometry_id, _class="face", attributes=["SDL/TYSA_NAME"], values=["Face ZMAX"])
inlet2_entity = get_single_entity_name(project_id, geometry_id, _class="face", attributes=["SDL/TYSA_NAME"], values=["Face Junction"])
outlet_entity = get_single_entity_name(project_id, geometry_id, _class="face", attributes=["SDL/TYSA_NAME"], values=["Face YMAX"])

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
    materials=IncompressibleFluidMaterials(
        fluids=[
            IncompressibleMaterial(
                name="Water",
                viscosity_model=NewtonianViscosityModel(
                    kinematic_viscosity=DimensionalKinematicViscosity(value=9.3379e-7, unit="m²/s")
                ),
                density=DimensionalDensity(value=997.33, unit="kg/m³"),
                topological_reference=TopologicalReference(entities=[material_entity]),
            )
        ]
    ),
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

# start of mesh operation
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

# Estimate Meshing
try:
    mesh_estimation = mesh_operation_api.estimate_mesh_operation(project_id, mesh_operation_id)
    print(f"Meshing estimation: {mesh_estimation}")
    too_expensive = mesh_estimation.compute_resource.value > 10.0
    if too_expensive:
        raise Exception("Too expensive", mesh_estimation)
    mesh_max_runtime = isodate.parse_duration(mesh_estimation.duration.interval_max).total_seconds()
    mesh_max_runtime = mesh_max_runtime + 600  # 10 min buffer
except ApiException as ae:
    if ae.status == 422:
        mesh_max_runtime = 36000
        print(f"Meshing estimation not available, assuming max runtime of {mesh_max_runtime} seconds")
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

# # Get the simulation spec and update it with mesh_id from the previous mesh operation
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
    too_expensive = estimation.compute_resource.value > 10.0
    if too_expensive:
        raise Exception("Too expensive", estimation)
    max_runtime = isodate.parse_duration(estimation.duration.interval_max).total_seconds()
    max_runtime = max_runtime + 600  # 10 min buffer
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
    url=probe_point_plot_info.download.url, headers={api_key_header: api_key}, _preload_content=False
)
probe_point_plot_data_csv = probe_point_plot_data_response.data.decode("utf-8")
print(f"Probe point plot data as CSV: {probe_point_plot_data_csv}")

# Write probe points to CSV file
with open("probe_points.csv", "w") as file:
    file.write(probe_point_plot_data_csv)

solution_info = [r for r in results._embedded if r.category == "SOLUTION"][0]
solution_response = api_client.rest_client.GET(
    url=solution_info.download.url, headers={api_key_header: api_key}, _preload_content=False
)
with open("solution.zip", "wb") as file:
    file.write(solution_response.data)
zip = zipfile.ZipFile("solution.zip")
print(f"Averaged solution ZIP file content: {zip.namelist()}")
