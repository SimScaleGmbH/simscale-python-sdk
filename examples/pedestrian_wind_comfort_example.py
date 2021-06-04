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
api_key_header = 'X-API-KEY'
api_key = os.getenv('SIMSCALE_API_KEY')
configuration = Configuration()
configuration.host = os.getenv('SIMSCALE_API_URL') + '/v0'
configuration.api_key = {
    api_key_header: api_key,
}
api_client = ApiClient(configuration)
retry_policy = urllib3.Retry(connect=5, read=5, redirect=0, status=5, backoff_factor=0.2)
api_client.rest_client.pool_manager.connection_pool_kw['retries'] = retry_policy

# API clients
project_api = ProjectsApi(api_client)
storage_api = StorageApi(api_client)
geometry_import_api = GeometryImportsApi(api_client)
geometry_api = GeometriesApi(api_client)
simulation_api = SimulationsApi(api_client)
simulation_run_api = SimulationRunsApi(api_client)

# Create project
project = Project(name='Pedestrian Wind Comfort via Python SDK', description='Pedestrian Wind Comfort via Python SDK', measurement_system='SI')
project = project_api.create_project(project)
project_id = project.project_id
print(f'projectId: {project_id}')

# Read project information and update with the deserialized model
project = project_api.get_project(project_id)
project_api.update_project(project_id, project)

# Upload CAD
storage = storage_api.create_storage()
with open('fixtures/Cylinder.stl', 'rb') as file:
    api_client.rest_client.PUT(url=storage.url, headers={'Content-Type': 'application/octet-stream'}, body=file.read())
storage_id = storage.storage_id
print(f'storageId: {storage_id}')

# Import CAD
geometry_import = GeometryImportRequest(
    name='Cylinder',
    location=GeometryImportRequestLocation(storage_id),
    format='STL',
    input_unit='m',
    options=GeometryImportRequestOptions(facet_split=False, sewing=False, improve=True, optimize_for_lbm_solver=True),
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

# Define simulation spec
model = WindComfort(
    region_of_interest=RegionOfInterest(
        disc_radius=DimensionalLength(100, "m"),
        center_point=DimensionalVector2dLength(DecimalVector2d(0, 0), "m"),
        ground_height=DimensionalLength(0, "m"),
        north_angle=DimensionalAngle(0, "°"),
        advanced_settings=AdvancedROISettings(WindTunnelSizeModerate())
    ),
    wind_conditions=WindConditions(
        geographical_location=GeographicalLocation(latitude=DimensionalAngle(48.135125, "°"),
                                                   longitude=DimensionalAngle(11.581981, "°")),
        wind_rose=WindRose(
            num_directions=4,
            velocity_buckets=[
                WindRoseVelocityBucket(_from=None,  to=1.234, fractions=[0.1, 0.1, 0.1, 0.1]),
                WindRoseVelocityBucket(_from=1.234, to=2.345, fractions=[0.0, 0.1, 0.1, 0.1]),
                WindRoseVelocityBucket(_from=2.345, to=3.456, fractions=[0.0, 0.0, 0.1, 0.1]),
                WindRoseVelocityBucket(_from=3.456, to=None,  fractions=[0.0, 0.0, 0.0, 0.1]),
            ],
            velocity_unit="m/s",
            exposure_categories=["EC4", "EC4", "EC4", "EC4"],
            wind_engineering_standard="EU",
            wind_data_source="USER_UPLOAD",
            add_surface_roughness=False
        )
    ),
    pedestrian_comfort_map=[
        PedestrianComfortSurface(
            name="Pedestrian level 1",
            height_above_ground=DimensionalLength(1.5, "m"),
            ground=GroundAbsolute()
        )
    ],
    simulation_control=WindComfortSimulationControl(
        max_direction_run_time=DimensionalTime(10000, "s"),
        number_of_fluid_passes=0.2
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
    mesh_settings=WindComfortMesh(wind_comfort_fineness=PacefishFinenessVeryCoarse())
)
simulation_spec = SimulationSpec(name='Pedestrian Wind Comfort via Python SDK', geometry_id=geometry_id, model=model)

# Create simulation
simulation_id = simulation_api.create_simulation(project_id, simulation_spec).simulation_id
print(f'simulationId: {simulation_id}')

# # Read simulation spec and update with the deserialized model
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
    max_runtime = max(3600, max_runtime * 2)
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
statistical_surface_solution_info = [r for r in results._embedded if r.category == 'STATISTICAL_SURFACE_SOLUTION'][0]
statistical_surface_solution_response = api_client.rest_client.GET(url=statistical_surface_solution_info.download.url, headers={api_key_header: api_key}, _preload_content=False)
with open('statistical_surface_solution.zip', 'wb') as file:
    file.write(statistical_surface_solution_response.data)
zip = zipfile.ZipFile('statistical_surface_solution.zip')
print(f'Statistical surface solution solution ZIP file content: {zip.namelist()}')
