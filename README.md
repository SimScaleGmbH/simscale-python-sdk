# SimScale Python SDK

API access is currently part of our paid Enterprise plan. However, if you have an idea for an integration or app and would like to become a development partner, please contact us at api@simscale.com!

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

You can install the Python package directly from the hosted git repository.

To install the lastest version:

```sh
pip install git+https://gitlab.com/simscale-gmbh/public/simscale-python-sdk.git
```

To install a specific version:

```sh
pip install git+https://gitlab.com/simscale-gmbh/public/simscale-python-sdk.git@0.0.10
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

## Examples

The `examples` folder contains executable code examples to demonstrate how the SDK can be used.

In order to run them the following environment variables need to be set:

```
export SIMSCALE_API_URL="https://api.simscale.com"
export SIMSCALE_API_KEY="your-api-key"
```
