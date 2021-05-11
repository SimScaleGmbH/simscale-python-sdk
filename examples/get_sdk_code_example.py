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

# Create project
project = Project(
    name="Get SDK Code for Project via Python SDK",
    description="Get SDK Code for Project via Python SDK",
    measurement_system="SI",
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
print(f"geometry_id: {geometry_id}")

# Read geometry information and update with the deserialized model
geometry = geometry_api.get_geometry(project_id, geometry_id)
geometry_api.update_geometry(project_id, geometry_id, geometry)

# Populate the project with some simulations
# This example creates the simulations to not depend on an existing project, but
# a more useful purpose would be to generate SDK code for Workbench-generated projects
def create_simulation(name):
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
    simulation_spec = SimulationSpec(name=f'Pedestrian Wind Comfort {name}', geometry_id=geometry_id, model=model)

    # Create simulation
    simulation_id = simulation_api.create_simulation(project_id, simulation_spec).simulation_id
    print(f'simulationId: {simulation_id}')

for name in range(3):
    create_simulation(name)

# Get list of all simulations created
simulations = simulation_api.get_simulations(project_id).embedded

# For each, print out generated SDK code
for simulation in simulations:
    simulation_id = simulation.simulation_id
    print(f"Simulation {simulation.name} ({simulation_id}):")
    print(simulation_api.get_simulation_sdk_code(project_id, simulation_id))
