# comicvine-client
OpenAPI specification for the ComicVine API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/guillaumedsde/comicvine-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/guillaumedsde/comicvine-client-python.git`)

Then import the package:
```python
import comicvine_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import comicvine_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import comicvine_client
from comicvine_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://comicvine.gamespot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicvine_client.Configuration(
    host = "https://comicvine.gamespot.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = comicvine_client.Configuration(
    host = "https://comicvine.gamespot.com/api",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'


# Enter a context with an instance of the API client
with comicvine_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicvine_client.CharacterApi(api_client)
    id = '4050-87668' # str | Unique ID of the entity.
format = 'xml' # str | The data format of the response takes either xml, json, or jsonp. (optional) (default to 'xml')
field_list = 'id,birth,description' # str | List of field names to include in the response. Use this if you want to reduce the size of the response payload. This filter can accept multiple arguments, each delimited with a \",\" (optional)

    try:
        # Get a particular character
        api_response = api_instance.get_character(id, format=format, field_list=field_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CharacterApi->get_character: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://comicvine.gamespot.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CharacterApi* | [**get_character**](docs/CharacterApi.md#get_character) | **GET** /character/{id} | Get a particular character
*IssueApi* | [**get_issue**](docs/IssueApi.md#get_issue) | **GET** /issue/{id} | Get a particular issue
*PersonApi* | [**get_person**](docs/PersonApi.md#get_person) | **GET** /person/{id} | Get a particular person
*SearchApi* | [**search**](docs/SearchApi.md#search) | **GET** /search | Search to ComicVine database
*VolumeApi* | [**get_volume**](docs/VolumeApi.md#get_volume) | **GET** /volume/{id} | Get a particular volume


## Documentation For Models



## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string


## Author




