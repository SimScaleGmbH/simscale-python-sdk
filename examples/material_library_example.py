#!/usr/bin/env python

import os

import urllib3

from simscale_sdk import Configuration, ApiClient, MaterialsApi
from simscale_sdk import CreateMaterialGroupRequest, CreateMaterialRequest, FixedMaterialProperty, PropertyDataType, \
    CreateNestedMaterialGroupRequest, ParametricMaterialProperty, MaterialPropertyParameter, MaterialResponse, \
    MaterialListResponse, MaterialGroupListResponse

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

# API client
materials_api = MaterialsApi(api_client)

# Create Material Group
create_material_group_request = CreateMaterialGroupRequest(name="My custom materials")
create_material_group_response = materials_api.create_material_group(
    create_material_group_request=create_material_group_request
)
material_group_id = create_material_group_response.material_group_id

# Create Nested Material Group
create_nested_material_group_request = CreateNestedMaterialGroupRequest(name="My custom solids")
create_nested_material_group_response = materials_api.create_nested_material_group(
    material_group_id,
    create_nested_material_group_request=create_nested_material_group_request
)
nested_material_group_id = create_nested_material_group_response.material_group_id

# Create Material
create_material_request = CreateMaterialRequest(
    name="My custom Aluminium",
    metadata={
        "description": "Post-transition metal in the boron group",
        "tags": ["solid", "thermal", "acoustic", "thermomechanical"]
    },
    properties={
        "density": FixedMaterialProperty(
            name="Density",
            unit="kg/m³",
            data_type=PropertyDataType.NUMERIC,
            value=2730.0
        ),
        "conductivity": ParametricMaterialProperty(
            name="Conductivity",
            unit="W/(m·K)",
            data_type=PropertyDataType.NUMERIC,
            parameters=[
                MaterialPropertyParameter(
                    key="temperature",
                    name="Temperature",
                    unit="C"
                )
            ],
            parametric_values=[
                {
                    "value": 31.4,
                    "temperature": 100
                },
                {
                    "value": 30.8,
                    "temperature": 500
                }
            ]
        )
    }
)
materials_api.create_material(
    material_group_id=nested_material_group_id,
    create_material_request=create_material_request
)

# List Material Groups
material_groups_response: MaterialGroupListResponse = materials_api.get_material_groups()
for group in material_groups_response.embedded:
    print(f"Material Group with id {group.material_group_id}: {group}")

# List Materials in Material Group
sample_material_group_id = material_groups_response.embedded[0].material_group_id
materials_list_response: MaterialListResponse = materials_api.get_materials(material_group_id=sample_material_group_id)
for material in materials_list_response.embedded:
    print(f"Material Group with id {sample_material_group_id} contains Material with id {material.id}")

# List Material properties
sample_material_id = materials_list_response.embedded[0].id
material_response: MaterialResponse = materials_api.get_material_data(
    material_group_id=sample_material_group_id,
    material_id=sample_material_id
)
for material_property in material_response.properties:
    print(f"Material with id {sample_material_id} has property {material_property}: {material_response.properties[material_property]}")
