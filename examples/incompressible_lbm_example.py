#!/usr/bin/env python

import os
import time
import zipfile

import isodate
from simscale_sdk import *

# API client configuration
api_key_header = 'X-API-KEY'
api_key = os.getenv('SIMSCALE_API_KEY')
configuration = Configuration()
configuration.host = os.getenv('SIMSCALE_API_URL') + '/v0'
configuration.api_key = {
    api_key_header: api_key,
}
api_client = ApiClient(configuration)

# API clients
project_api = ProjectsApi(api_client)
storage_api = StorageApi(api_client)
geometry_import_api = GeometryImportsApi(api_client)
geometry_api = GeometriesApi(api_client)
simulation_api = SimulationsApi(api_client)
simulation_run_api = SimulationRunsApi(api_client)
table_import_api = TableImportsApi(api_client)

# Create project
project = Project(name='Incompressible LBM via Python SDK', description='Incompressible LBM via Python SDK', measurement_system='SI')
project = project_api.create_project(project)
project_id = project.project_id
print(f'projectId: {project_id}')

# Read project information and update with the deserialized model
project = project_api.get_project(project_id)
project_api.update_project(project_id, project)

# Upload CAD
storage = storage_api.create_storage()
with open('fixtures/Shapes.stl', 'rb') as file:
    api_client.rest_client.PUT(url=storage.url, headers={'Content-Type': 'application/octet-stream'}, body=file.read())
storage_id = storage.storage_id
print(f'geometry storageId: {storage_id}')

# Import CAD
geometry_import = GeometryImportRequest(
    name='Shapes',
    location=GeometryImportRequestLocation(storage_id),
    format='STL',
    input_unit='m',
    options=GeometryImportRequestOptions(facet_split=False, sewing=True, improve=True, optimize_for_lbm_solver=True),
)
geometry_import = geometry_import_api.import_geometry(project_id, geometry_import)
geometry_import_id = geometry_import.geometry_import_id
geometry_import_start = time.time()
while geometry_import.status not in ('FINISHED', 'CANCELED', 'FAILED'):
    # adjust timeout for larger geometries
    if time.time() > geometry_import_start + 900:
        raise TimeoutError()
    time.sleep(10)
    geometry_import = geometry_import_api.get_geometry_import(project_id, geometry_import_id)
    print(f'Geometry import status: {geometry_import.status}')
geometry_id = geometry_import.geometry_id
print(f'geometryId: {geometry_id}')

# Read geometry information and update with the deserialized model
geometry = geometry_api.get_geometry(project_id, geometry_id)
geometry_api.update_geometry(project_id, geometry_id, geometry)

# Get geometry mappings
geometry_mappings = geometry_api.get_geometry_mappings(project_id, geometry_id, _class='face', entities=['Cylinder', 'Cube 2', 'Sphere'])
entities = [mapping.name for mapping in geometry_mappings._embedded]
print(f'entities: {entities}')

# upload probe points
csv_storage = storage_api.create_storage()
with open('fixtures/ProbePoint.csv', 'rb') as file:
    api_client.rest_client.PUT(url=csv_storage.url, headers={'Content-Type': 'application/octet-stream'}, body=file.read())
csv_storage_id = csv_storage.storage_id
print(f'Probepoint storageId: {csv_storage_id}')

# import probe points
table_import = TableImportRequest(location=TableImportRequestLocation(csv_storage_id))
table_import_response = table_import_api.import_table(project_id, table_import)
table_id = table_import_response.table_id

# Create geometry primitives
external_flow_domain = RotatableCartesianBox(
    name='External Flow Domain',
    min=DimensionalVectorLength(value=DecimalVector(x=-350, y=-100, z=0), unit='m'),
    max=DimensionalVectorLength(value=DecimalVector(x=650, y=100, z=300), unit='m'),
    rotation_point=DimensionalVectorLength(value=DecimalVector(x=0, y=0, z=0), unit='m'),
    rotation_angles=DimensionalVectorAngle(value=DecimalVector(x=0, y=0, z=0), unit='°'),
)
external_flow_domain_uuid = simulation_api.create_geometry_primitive(project_id, external_flow_domain).geometry_primitive_id
mesh_region = LocalCartesianBox(
    name='Mesh Region',
    orientation_reference='GEOMETRY',
    min=DimensionalVectorLength(value=DecimalVector(x=-30, y=-30, z=0), unit='m'),
    max=DimensionalVectorLength(value=DecimalVector(x=30, y=30, z=120), unit='m'),
)
mesh_region_uuid = simulation_api.create_geometry_primitive(project_id, mesh_region).geometry_primitive_id

# Define simulation spec
model = IncompressiblePacefish(
    bounding_box_uuid=external_flow_domain_uuid,
    material=IncompressibleMaterial(
        name='Air',
        viscosity_model=NewtonianViscosityModel(
            kinematic_viscosity=DimensionalKinematicViscosity(value=0.00001529, unit='m²/s')
        ),
        density=DimensionalDensity(value=1.1965, unit='kg/m³'),
        reference_temperature=DimensionalTemperature(value=293.15, unit='K'),
        molar_weight=DimensionalMolarMass(value=28.97, unit='kg/kmol'),
    ),
    flow_domain_boundaries=FlowDomainBoundaries(
        xmin=VelocityInletBC(
            name='Velocity inlet (A)',
            velocity=FixedMagnitudeVBC(value=DimensionalFunctionSpeed(value=ConstantFunction(value=10.5), unit='m/s')),
            turbulence_intensity=TurbulenceIntensityTIBC(value=DimensionalFunctionDimensionless(value=ConstantFunction(value=0.015), unit='')),
            dissipation_type=AutomaticOmegaDissipation()
        ),
        xmax=PressureOutletBC(
            name='Pressure outlet (B)'
        ),
        ymin=WallBC(
            name='Side (C)',
            velocity=SlipVBC()
        ),
        ymax=WallBC(
            name='Side (D)',
            velocity=SlipVBC()
        ),
        zmin=WallBC(
            name='Ground (E)',
            velocity=NoSlipVBC(
                surface_roughness=DimensionalLength(value=0, unit='m'),
            )
        ),
        zmax=WallBC(
            name='Top (F)',
            velocity=SlipVBC()
        )
    ),
    simulation_control=FluidSimulationControl(
        end_time=DimensionalTime(value=5, unit='s'),
    ),
    advanced_modelling=AdvancedModelling(),
    result_control=FluidResultControls(
        forces_moments=[
            ForcesMomentsResultControl(
                name='Forces and moments 1',
                center_of_rotation=DimensionalVectorLength(value=DecimalVector(x=0, y=0, z=0), unit='m'),
                write_control=HighResolution(),
                export_statistics=False,
                group_assignments=False,
                topological_reference=TopologicalReference(
                    entities=entities,
                ),
            ),
            ForcesMomentsResultControl(
                name='Forces and moments 2',
                center_of_rotation=DimensionalVectorLength(value=DecimalVector(x=0, y=0, z=0), unit='m'),
                write_control=HighResolution(),
                fraction_from_end=0.3,
                topological_reference=TopologicalReference(
                    entities=entities,
                ),
            ),
        ],
        probe_points=[
            ProbePointsResultControl(
                name='Probe point 1',
                write_control=ModerateResolution(),
                probe_locations=TableDefinedProbeLocations(table_id=table_id)
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
simulation_spec = SimulationSpec(name='Incompressible LBM', geometry_id=geometry_id, model=model)

# Create simulation
simulation_id = simulation_api.create_simulation(project_id, simulation_spec).simulation_id
print(f'simulationId: {simulation_id}')

# Read simulation spec and update with the deserialized model
simulation_spec = simulation_api.get_simulation(project_id, simulation_id)
simulation_api.update_simulation(project_id, simulation_id, simulation_spec)

# Check simulation
check = simulation_api.check_simulation_setup(project_id, simulation_id)
warnings = [entry for entry in check.entries if entry.severity == 'WARNING']
print(f'Simulation check warnings: {warnings}')
errors = [entry for entry in check.entries if entry.severity == 'ERROR']
if errors:
    raise Exception('Simulation check failed', check)

# Estimate simulation
try:
    estimation = simulation_api.estimate_simulation_setup(project_id, simulation_id)
    print(f'Simulation estimation: {estimation}')
    too_expensive = estimation.compute_resource.value > 10.0
    if too_expensive:
        raise Exception('Too expensive', estimation)
    max_runtime = isodate.parse_duration(estimation.duration.interval_max).total_seconds()
    max_runtime = max_runtime + 600  # 10 min buffer
except ApiException as ae:
    if ae.status == 422:
        max_runtime = 36000
        print(f'Simulation estimation not available, assuming max runtime of {max_runtime} seconds')
    else:
        raise ae

# Create simulation run
simulation_run = SimulationRun(name='Run 1')
simulation_run = simulation_run_api.create_simulation_run(project_id, simulation_id, simulation_run)
run_id = simulation_run.run_id
print(f'runId: {run_id}')

# Read simulation run and update with the deserialized model
simulation_run = simulation_run_api.get_simulation_run(project_id, simulation_id, run_id)
simulation_run_api.update_simulation_run(project_id, simulation_id, run_id, simulation_run)

# Start simulation run and wait until it's finished
simulation_run_api.start_simulation_run(project_id, simulation_id, run_id)
simulation_run = simulation_run_api.get_simulation_run(project_id, simulation_id, run_id)
simulation_run_start = time.time()
while simulation_run.status not in ('FINISHED', 'CANCELED', 'FAILED'):
    if time.time() > simulation_run_start + max_runtime:
        raise TimeoutError()
    time.sleep(30)
    simulation_run = simulation_run_api.get_simulation_run(project_id, simulation_id, run_id)
    print(f'Simulation run status: {simulation_run.status} - {simulation_run.progress}')

# Get result metadata and download results
results = simulation_run_api.get_simulation_run_results(project_id, simulation_id, run_id)

probe_point_plot_statistical_data_info = [r for r in results._embedded if r.category == 'PROBE_POINT_PLOT_STATISTICAL_DATA'][0]
probe_point_plot_statistical_data_response = api_client.rest_client.GET(url=probe_point_plot_statistical_data_info.download.url, headers={api_key_header: api_key}, _preload_content=False)
probe_point_plot_statistical_data_csv = probe_point_plot_statistical_data_response.data.decode('utf-8')
print(f'Probe point plot statistical data as CSV: {probe_point_plot_statistical_data_csv}')

# Write probe points to CSV file
with open('probe_points.csv', 'w') as file:
    file.write(probe_point_plot_statistical_data_csv)

averaged_solution_info = [r for r in results._embedded if r.category == 'AVERAGED_SOLUTION'][0]
averaged_solution_response = api_client.rest_client.GET(url=averaged_solution_info.download.url, headers={api_key_header: api_key}, _preload_content=False)
with open('averaged_solution.zip', 'wb') as file:
    file.write(averaged_solution_response.data)
zip = zipfile.ZipFile('averaged_solution.zip')
print(f'Averaged solution ZIP file content: {zip.namelist()}')
