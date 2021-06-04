#!/usr/bin/env python

import isodate
import os
import time
import zipfile
import urllib3
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
retry_policy = urllib3.Retry(connect=5, read=5, redirect=0, status=5, backoff_factor=0.2)
api_client.rest_client.pool_manager.connection_pool_kw['retries'] = retry_policy

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
    name="Compressible via Python SDK", description="Compressible via Python SDK", measurement_system="SI"
)
project = project_api.create_project(project)
project_id = project.project_id
print(f"projectId: {project_id}")

# Read project information and update with the deserialized model
project = project_api.get_project(project_id)
project_api.update_project(project_id, project)

# Upload CAD
storage = storage_api.create_storage()
with open("fixtures/flow-around-sphere-v3.x_t", "rb") as file:
    api_client.rest_client.PUT(url=storage.url, headers={"Content-Type": "application/octet-stream"}, body=file.read())
storage_id = storage.storage_id
print(f"storageId: {storage_id}")

# Import CAD
geometry_import = GeometryImportRequest(
    name="CAD-sphere_coarse",
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
print(f"geometryId: {geometry_id}")

# Read geometry information and update with the deserialized model
geometry = geometry_api.get_geometry(project_id, geometry_id)
geometry_api.update_geometry(project_id, geometry_id, geometry)

# Get geometry mappings
def get_entity_names(project_id, geometry_id, num, **kwargs):
    entities = geometry_api.get_geometry_mappings(project_id, geometry_id, **kwargs)._embedded
    if len(entities) == num:
        return [e.name for e in entities]
    else:
        raise Exception(f"Found {len(entities)} entities instead of {num}: {entities}") 
material_entities = get_entity_names(project_id, geometry_id, 1, attributes=["SDL/TYSA_NAME"], values=["box"])
bc1_entities = get_entity_names(project_id, geometry_id, 1, attributes=["SDL/TYSA_NAME"], values=["Box ZMAX"])
bc2_entities = get_entity_names(project_id, geometry_id, 1, attributes=["SDL/TYSA_NAME"], values=["Box ZMIN"])
bc3_entities = get_entity_names(project_id, geometry_id, 4, attributes=["SDL/TYSA_NAME"], values=["Box XMIN", "Box XMAX","Box YMIN","Box YMAX"])
bc4_entities = get_entity_names(project_id, geometry_id, 2, attributes=["SDL/TYSA_NAME"], values=["Sphere"])

# create simulation spec first to pass as reference to mesh operation for physics based meshing
model = Compressible(
    turbulence_model="KOMEGASST",
    model=FluidModel(),
    initial_conditions=FluidInitialConditions(),
    advanced_concepts=AdvancedConcepts(),
    materials=CompressibleFluidMaterials(
        fluids=[
            FluidCompressibleMaterial(
                name="Air",
                topological_reference=TopologicalReference(entities=material_entities),
                specie=SpecieDefault(molar_weight=DimensionalMolarMass(value=28.97, unit="kg/kmol")),
                transport=ConstTransport(
                    dynamic_viscosity=DimensionalDynamicViscosity(value=0.0000183, unit="kg/(s·m)"),
                    prandtl_number=0.713,
                    thermo=HConstThermo(equation_of_state=PerfectGasEquationOfState()),
                ),
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
                        x=ConstantFunction(value=0), y=ConstantFunction(value=0), z=ConstantFunction(value=-1)
                    )
                )
            ),
            temperature=FixedValueTBC(
                value=DimensionalFunctionTemperature(value=ConstantFunction(value=19.85), unit="°C")
            ),
            topological_reference=TopologicalReference(entities=bc1_entities),
        ),
        PressureOutletBC(
            name="Pressure outlet 2",
            pressure=FixedValuePBC(value=DimensionalFunctionPressure(value=ConstantFunction(value=101325), unit="Pa")),
            topological_reference=TopologicalReference(entities=bc2_entities),
        ),
        WallBC(
            name="Wall 3",
            velocity=SlipVBC(),
            temperature=FixedValueTBC(
                value=DimensionalFunctionTemperature(value=ConstantFunction(value=19.85), unit="°C")
            ),
            topological_reference=TopologicalReference(entities=bc3_entities),
        ),
        WallBC(
            name="Wall 4",
            velocity=NoSlipVBC(turbulence_wall="WALL_FUNCTION"),
            temperature=AdiabaticTBC(),
            topological_reference=TopologicalReference(entities=bc4_entities),
        ),
    ],
    simulation_control=FluidSimulationControl(
        end_time=DimensionalTime(value=100, unit="s"),
        delta_t=DimensionalTime(value=1, unit="s"),
        write_control=TimeStepWriteControl(write_interval=100),
        max_run_time=DimensionalTime(value=1000, unit="s"),
        decompose_algorithm=ScotchDecomposeAlgorithm(),
    ),
    result_control=FluidResultControls(
        forces_moments=[
            ForcesMomentsResultControl(
                name="Forces and moments 1",
                write_control=TimeStepWriteControl(write_interval=1),
                topological_reference=TopologicalReference(entities=bc4_entities),
            )
        ],
        surface_data=[
            AreaAverageResultControl(
                name="Area average 1",
                write_control=TimeStepWriteControl(write_interval=1),
                topological_reference=TopologicalReference(entities=bc3_entities),
            )
        ],
    ),
)

simulation_spec = SimulationSpec(name="Compressible via Python SDK", geometry_id=geometry_id, model=model)
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
    mesh_max_runtime = max(3600, mesh_max_runtime * 2)
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
    max_runtime = max(3600, max_runtime * 2)
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

area_average_info = [r for r in results._embedded if r.category == "AREA_AVERAGE"][0]
area_average_data_response = api_client.rest_client.GET(
    url=area_average_info.download.url, headers={api_key_header: api_key}, _preload_content=False
)
area_average_data_csv = area_average_data_response.data.decode("utf-8")
print(f"Area average data as CSV: {area_average_data_csv}")

# Write Area average to CSV file
with open("area_average.csv", "w") as file:
    file.write(area_average_data_csv)

solution_info = [r for r in results._embedded if r.category == "SOLUTION"][0]
solution_response = api_client.rest_client.GET(
    url=solution_info.download.url, headers={api_key_header: api_key}, _preload_content=False
)
with open("solution.zip", "wb") as file:
    file.write(solution_response.data)
zip = zipfile.ZipFile("solution.zip")
print(f"Averaged solution ZIP file content: {zip.namelist()}")
