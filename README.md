# SimScale Python SDK

API access is currently part of our paid Enterprise plan. However, if you have an idea for an integration or app and would like to become a development partner, please contact us at api@simscale.com!

## Requirements

Python >= 3.6

## Installation
### pip install

You can install the Python package directly from the hosted git repository.

To install a specific version:

```sh
pip install git+https://github.com/SimScaleGmbH/simscale-python-sdk.git@3.0.1
```

Check the Releases section for the list of available versions: https://github.com/SimScaleGmbH/simscale-python-sdk/releases.

To install the latest version:

```sh
pip install git+https://github.com/SimScaleGmbH/simscale-python-sdk.git
```

Then import the package:
```python
import simscale_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import simscale_sdk
```

## Usage
### API client configuration

Authentication with the SimScale API is done using the `X-API-KEY` request header. You must initialize and configure a
`simscale_sdk.ApiClient` object with the correct host, headers and API key information.

As reference, the following snippet shows how to configure the API client using environment variables to store the API
key and the target URL.

```python
import os
from simscale_sdk import Configuration, ApiClient

# API client configuration
api_key = os.getenv("SIMSCALE_API_KEY")
api_url = os.getenv("SIMSCALE_API_URL")
api_key_header = "X-API-KEY"

configuration = Configuration()
configuration.host = api_url + "/v0"
configuration.api_key = {
    api_key_header: api_key
}

api_client = ApiClient(configuration)
```

You must then pass this object to initialize the domain-specific clients that will perform the API operations. For example:

```python
# API clients
project_api = ProjectsApi(api_client)
geometry_api = GeometriesApi(api_client)
mesh_operation_api = MeshOperationsApi(api_client)
simulation_api = SimulationsApi(api_client)
```

### HTTP Proxy

To use the API client with an HTTP proxy, you must set `configuration.proxy` with the proxy URL. You can use `configuration.proxy_headers`
to set up authentication.
```python
configuration.proxy = "http://myProxyUrl:myProxyPort/"
configuration.proxy_headers = urllib3.util.make_headers(proxy_basic_auth='username:password') # Optional - example with Basic authentication

api_client = ApiClient(configuration)
```

For more details check https://urllib3.readthedocs.io/en/stable/advanced-usage.html#proxies.

## Examples

The `examples` folder contains executable code examples to demonstrate how the SDK can be used.

In order to run them, the following environment variables need to be set:

| Name               | Value                      |
|--------------------|----------------------------|
| `SIMSCALE_API_URL` | `https://api.simscale.com` |
| `SIMSCALE_API_KEY` | `your-api-key`             |

### Set environment variables

This section explains how to set environment variables for the current terminal session only. This means that the
variables will not be accessible if you use a different terminal to run the examples.

#### Linux/macOS
Run:
```sh
export SIMSCALE_API_URL="https://api.simscale.com"
export SIMSCALE_API_KEY="your-api-key"
```

#### Windows CMD
Run:
```console
set SIMSCALE_API_URL="https://api.simscale.com"
set SIMSCALE_API_KEY="your-api-key"
```

#### Windows PowerShell
Run:
```powershell
$env:SIMSCALE_API_URL="https://api.simscale.com"
$env:SIMSCALE_API_KEY="your-api-key"
```

## SDK Documentation

SDK documentation can be found in https://simscalegmbh.github.io/simscale-python-sdk/