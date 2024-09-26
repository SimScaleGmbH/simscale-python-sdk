#!/usr/bin/env python

import os

import urllib3
from simscale_sdk import Configuration, ApiClient, ProjectsApi, FoldersApi, SpacesApi, Folder, \
    Project, MoveContentRequest, ResourceToMove, ResourceLocation

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
spaces_api = SpacesApi(api_client)
folders_api = FoldersApi(api_client)

# Get info about the user Personal Space
user_spaces = spaces_api.get_user_spaces()
personal_space_id = user_spaces.personal_spaces[0].space_id
personal_space_info = spaces_api.get_space_info(space_id=personal_space_id)
print(f"Personal Space ID: {personal_space_id} - Space info: {personal_space_info}")

# Create Folders in the Space root
folder_a = Folder(name="Folder A")
folder_a = folders_api.create_folder(space_id=personal_space_id, folder=folder_a)
print(f"Created a folder with ID '{folder_a.folder_id}' and name '{folder_a.name}' in the Space root")

folder_b = Folder(name="Folder B")
folder_b = folders_api.create_folder(space_id=personal_space_id, folder=folder_b)
print(f"Created a folder with ID '{folder_b.folder_id}' and name '{folder_b.name}' in the Space root")

# Create a Project in the Space root
project_a = Project(
    name="Project A",
    description="Project in Space root",
    measurement_system="SI",
    space_id=personal_space_id
)
project_a = project_api.create_project(project=project_a)
print(f"Created a project with ID '{project_a.project_id}' and name '{project_a.name}' in the Space root")

# Create a Project inside Folder A
project_b = Project(
    name="Project B",
    description="Project in Folder A",
    measurement_system="SI",
    space_id=personal_space_id,
    parent_folder_id=folder_a.folder_id
)
project_b = project_api.create_project(project=project_b)
print(f"Created a project with ID '{project_b.project_id}' and name '{project_b.name}' inside Folder A")

# Create a Folder inside Folder A
folder_c = Folder(
    name="Folder C",
    parent_folder_id=folder_a.folder_id
)
folder_c = folders_api.create_folder(space_id=personal_space_id, folder=folder_c)
print(f"Created a folder with ID '{folder_c.folder_id}' and name '{folder_c.name}' inside Folder A")

# Rename Folder C
folder_c = folders_api.update_folder(space_id=personal_space_id, folder_id=folder_c.folder_id, folder=Folder(name="New name for Folder C"))
print(f"Updated folder with ID '{folder_c.folder_id}'. New name: '{folder_c.name}'")

# List the contents of the Space root
folders_in_space_root = folders_api.list_folders_in_space_root(space_id=personal_space_id)
print(f"Number of folders in Space root: {folders_in_space_root.meta.total} - Sample Folder info: {folders_in_space_root.embedded[0]}")

projects_in_space_root = folders_api.list_projects_in_space_root(space_id=personal_space_id)
print(f"Number of projects in Space root: {projects_in_space_root.meta.total} - Sample Projects info: {projects_in_space_root.embedded[0]}")

# List the contents of a Folder
folders_in_folder = folders_api.list_folders_in_folder(space_id=personal_space_id, folder_id=folder_a.folder_id)
print(f"Number of folders in Folder A: {folders_in_folder.meta.total} - Folders: {folders_in_folder.embedded}")

projects_in_folder = folders_api.list_projects_in_folder(space_id=personal_space_id, folder_id=folder_a.folder_id)
print(f"Number of projects in Folder A: {projects_in_folder.meta.total} - Projects: {projects_in_folder.embedded}")

# Move content from the Space root to Folder B
move_content_request = MoveContentRequest(
    entries=[
        ResourceToMove(project_id=project_a.project_id),  # move Project A
        ResourceToMove(folder_id=folder_a.folder_id),  # move Folder A
    ],
    to=ResourceLocation(space_id=personal_space_id, parent_folder_id=folder_b.folder_id)
)
folders_api.move_content_from_space_root(space_id=personal_space_id, move_content_request=move_content_request)

# Move content from Folder A to the Space root
move_content_request = MoveContentRequest(
    entries=[
        ResourceToMove(project_id=project_b.project_id),  # move Project B
        ResourceToMove(folder_id=folder_c.folder_id),  # move Folder C
    ],
    to=ResourceLocation(space_id=personal_space_id)
)
folders_api.move_content_from_folder(
    space_id=personal_space_id,
    folder_id=folder_a.folder_id,
    move_content_request=move_content_request
)

# Delete Folder C
folders_api.delete_folder(space_id=personal_space_id, folder_id=folder_c.folder_id)
