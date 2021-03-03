#!/usr/bin/env python

import isodate
import os
import time
import itertools
from simscale_sdk import *

# As of this writing, meshing geometries is not yet supported via the API and neither is setting up non-LBM simulations.
# A simple way to work around this limitation is to conveniently set up a project in the workbench and then to only drive
# settings changes and later workflow steps via the API. This example shows this workflow assuming a fully set up
# "Fluid Flow Simulation" tutorial project (see https://www.simscale.com/tutorials).
#
# The example explores a few combinations of velocities for both inlets and downloads probe point and
# solution field results into the working directory.
# A post-processing and results comparison API is in internal testing.
#
# To get started:
# Enter the project ID visible in your browser's address bar: "https://www.simscale.com/workbench/?pid=[this part]&mi[...]"

project_id = ''

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

# Fetch a simulation based on its name


def get_simulation(project, simulations, simulation_name):
    simulation = [
        simulation for simulation in simulations if simulation.name == simulation_name][0]
    simulation_setup = simulation_api.get_simulation(
        project.project_id, simulation.simulation_id)
    return simulation_setup

# Check simulation setup and get run time estimate


def check_and_estimate(project, simulation):
    check = simulation_api.check_simulation_setup(
        project.project_id, simulation.simulation_id)
    errors = [entry for entry in check.entries if entry.severity == 'ERROR']
    if errors:
        raise Exception('Simulation check failed', check)
    try:
        estimation = simulation_api.estimate_simulation_setup(
            project.project_id, simulation.simulation_id)
        max_runtime = isodate.parse_duration(
            estimation.duration.interval_max).total_seconds()
        max_runtime = max_runtime + 600  # 10 min buffer
        return max_runtime
    except ApiException as ae:
        if ae.status == 422:
            max_runtime = 36000
            print(ae)
            print(
                f'Simulation estimation not available, assuming max runtime of {max_runtime} seconds')
        else:
            raise ae

# Change simulation settings, create a run snapshot and start it


def setup_and_start_simulation_run(simulation, inlet_1_velocity, inlet_2_velocity):
    # Update inlet velocities
    bcs = simulation.model.boundary_conditions
    bc = [bc for bc in bcs if bc.name == "Velocity inlet 1"][0]
    bc.velocity.value.value.z.value = -inlet_1_velocity

    bc = [bc for bc in bcs if bc.name == "Velocity inlet 2"][0]
    bc.velocity.value.value.y.value = -inlet_2_velocity

    # As an example - here you could also control run time and results export
    simulation.model.simulation_control.end_time.value = 1000
    simulation.model.simulation_control.write_control.write_interval = 1000

    # Update simulation spec
    simulation_api.update_simulation(project_id, simulation_id, simulation)

    # Check and estimate
    max_runtime = check_and_estimate(project, simulation)

    # Run
    run_name = f"{simulation.name}_inlet-1={inlet_1_velocity}_inlet-2={inlet_2_velocity}"
    simulation_run = SimulationRun(name=run_name)
    simulation_run = simulation_run_api.create_simulation_run(
        project_id, simulation_id, simulation_run)
    run_id = simulation_run.run_id
    simulation_run_api.start_simulation_run(project_id, simulation_id, run_id)
    print(f"Run {run_name} started, id {run_id}")
    return run_id, max_runtime


# Get existing project
project = project_api.get_project(project_id)
print(f"Project ID {project_id}")

# Get existing simulation
simulations = simulation_api.get_simulations(project_id)._embedded
simulation = get_simulation(
    project, simulations, 'Incompressible')
simulation_id = simulation.simulation_id
print(f"Simulation ID {simulation_id}")

run_ids_and_max_runtimes = []
for inlet_1_velocity, inlet_2_velocity in itertools.product([1, 1.5, 2], [0.5, 1, 1.5]):
    print(
        f"Setting up run with inlet 1 velocity {inlet_1_velocity}, inlet 2 velocity {inlet_2_velocity}")
    try:
        run_id, max_runtime = setup_and_start_simulation_run(
            simulation, inlet_1_velocity, inlet_2_velocity)
        run_ids_and_max_runtimes.append((run_id, max_runtime))
    except Exception as e:
        print(e)

# Wait until all runs are finished
ongoing_runs = True
while (ongoing_runs):
    ongoing_runs = False
    for run_id, max_runtime in run_ids_and_max_runtimes:
        simulation_run = simulation_run_api.get_simulation_run(
            project_id, simulation_id, run_id)
        simulation_run_start = time.time()
        print(
            f'{simulation_run.name} status: {simulation_run.status} - {100 * simulation_run.progress:.1f}%')
        if simulation_run.status not in ('FINISHED', 'CANCELED', 'FAILED'):
            ongoing_runs = True
            if time.time() > simulation_run_start + max_runtime:
                raise TimeoutError()
    time.sleep(30)

# Fetch and write results
for run_id, _ in run_ids_and_max_runtimes:
    simulation_run = simulation_run_api.get_simulation_run(
        project_id, simulation_id, run_id)
    run_name = simulation_run.name

    results = simulation_run_api.get_simulation_run_results(
        project_id, simulation_id, run_id)

    solution_field = [
        r for r in results._embedded if r.category == 'SOLUTION'][0]
    solution_field_response = api_client.rest_client.GET(
        url=solution_field.download.url, headers={api_key_header: api_key}, _preload_content=False)
    with open(f"{run_name}_solution-field.zip", 'wb') as file:
        file.write(solution_field_response.data)

    for quantity in ["Ux", "Uy", "Uz", "nut", "omega", "k", "p"]:
        quantity_probe_point = [r for r in results._embedded if (
            r.category == 'PROBE_POINT_PLOT' and r.name == 'Probe point 1' and r.quantity == quantity)][0]
        quantity_probe_point_response = api_client.rest_client.GET(
            url=quantity_probe_point.download.url, headers={api_key_header: api_key}, _preload_content=False)
        quantity_probe_point_csv = quantity_probe_point_response.data.decode(
            'utf-8')
        quantity_probe_point_file_name = f"P{run_name}_probe-point_{quantity}.csv"
        with open(quantity_probe_point_file_name, 'w') as file:
            file.write(quantity_probe_point_csv)
            print(f"Probe point data {quantity_probe_point_file_name} saved")
