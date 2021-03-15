# osis-internship-sdk
This API delivers data for the Internship project.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.0
- Package version: 1.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/uclouvain/osis](https://github.com/uclouvain/osis)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import osis_internship_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import osis_internship_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import osis_internship_sdk
from pprint import pprint
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.allocation_get import AllocationGet
from osis_internship_sdk.model.allocation_paging import AllocationPaging
from osis_internship_sdk.model.cohort_get import CohortGet
from osis_internship_sdk.model.cohort_paging import CohortPaging
from osis_internship_sdk.model.inline_response404 import InlineResponse404
from osis_internship_sdk.model.internship_get import InternshipGet
from osis_internship_sdk.model.internship_paging import InternshipPaging
from osis_internship_sdk.model.master_get import MasterGet
from osis_internship_sdk.model.master_paging import MasterPaging
from osis_internship_sdk.model.organization_get import OrganizationGet
from osis_internship_sdk.model.organization_paging import OrganizationPaging
from osis_internship_sdk.model.period_get import PeriodGet
from osis_internship_sdk.model.period_paging import PeriodPaging
from osis_internship_sdk.model.score_get import ScoreGet
from osis_internship_sdk.model.specialty_get import SpecialtyGet
from osis_internship_sdk.model.specialty_paging import SpecialtyPaging
from osis_internship_sdk.model.student_affectation_get import StudentAffectationGet
from osis_internship_sdk.model.student_affectation_paging import StudentAffectationPaging
from osis_internship_sdk.model.student_get import StudentGet
from osis_internship_sdk.model.student_paging import StudentPaging
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/internship
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_internship_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/internship"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'


# Enter a context with an instance of the API client
with osis_internship_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = internship_api.InternshipApi(api_client)
    
    try:
        api_response = api_instance.cohorts_get()
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->cohorts_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/internship*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InternshipApi* | [**cohorts_get**](docs/InternshipApi.md#cohorts_get) | **GET** /cohorts | 
*InternshipApi* | [**cohorts_uuid_get**](docs/InternshipApi.md#cohorts_uuid_get) | **GET** /cohorts/{uuid} | 
*InternshipApi* | [**internships_get**](docs/InternshipApi.md#internships_get) | **GET** /internships | 
*InternshipApi* | [**internships_uuid_get**](docs/InternshipApi.md#internships_uuid_get) | **GET** /internships/{uuid} | 
*InternshipApi* | [**masters_allocations_specialty_organization_get**](docs/InternshipApi.md#masters_allocations_specialty_organization_get) | **GET** /masters_allocations/{specialty}/{organization} | 
*InternshipApi* | [**masters_allocations_specialty_organization_post**](docs/InternshipApi.md#masters_allocations_specialty_organization_post) | **POST** /masters_allocations/{specialty}/{organization} | 
*InternshipApi* | [**masters_allocations_uuid_delete**](docs/InternshipApi.md#masters_allocations_uuid_delete) | **DELETE** /masters_allocations/{uuid} | 
*InternshipApi* | [**masters_allocations_uuid_get**](docs/InternshipApi.md#masters_allocations_uuid_get) | **GET** /masters_allocations/{uuid} | 
*InternshipApi* | [**masters_get**](docs/InternshipApi.md#masters_get) | **GET** /masters/ | 
*InternshipApi* | [**masters_post**](docs/InternshipApi.md#masters_post) | **POST** /masters/ | 
*InternshipApi* | [**masters_uuid_activate_account_put**](docs/InternshipApi.md#masters_uuid_activate_account_put) | **PUT** /masters/{uuid}/activate_account/ | 
*InternshipApi* | [**masters_uuid_allocations_get**](docs/InternshipApi.md#masters_uuid_allocations_get) | **GET** /masters/{uuid}/allocations/ | 
*InternshipApi* | [**masters_uuid_get**](docs/InternshipApi.md#masters_uuid_get) | **GET** /masters/{uuid} | 
*InternshipApi* | [**organizations_get**](docs/InternshipApi.md#organizations_get) | **GET** /organizations | 
*InternshipApi* | [**organizations_uuid_get**](docs/InternshipApi.md#organizations_uuid_get) | **GET** /organizations/{uuid} | 
*InternshipApi* | [**periods_get**](docs/InternshipApi.md#periods_get) | **GET** /periods | 
*InternshipApi* | [**periods_uuid_get**](docs/InternshipApi.md#periods_uuid_get) | **GET** /periods/{uuid} | 
*InternshipApi* | [**scores_affectation_uuid_validate_get**](docs/InternshipApi.md#scores_affectation_uuid_validate_get) | **GET** /scores/{affectation_uuid}/validate | 
*InternshipApi* | [**scores_student_uuid_period_uuid_get**](docs/InternshipApi.md#scores_student_uuid_period_uuid_get) | **GET** /scores/{student_uuid}/{period_uuid} | 
*InternshipApi* | [**scores_student_uuid_period_uuid_put**](docs/InternshipApi.md#scores_student_uuid_period_uuid_put) | **PUT** /scores/{student_uuid}/{period_uuid} | 
*InternshipApi* | [**specialties_get**](docs/InternshipApi.md#specialties_get) | **GET** /specialties | 
*InternshipApi* | [**specialties_uuid_get**](docs/InternshipApi.md#specialties_uuid_get) | **GET** /specialties/{uuid} | 
*InternshipApi* | [**students_affectations_specialty_organization_get**](docs/InternshipApi.md#students_affectations_specialty_organization_get) | **GET** /students_affectations/{specialty}/{organization} | 
*InternshipApi* | [**students_affectations_specialty_organization_stats_get**](docs/InternshipApi.md#students_affectations_specialty_organization_stats_get) | **GET** /students_affectations/{specialty}/{organization}/stats/ | 
*InternshipApi* | [**students_affectations_uuid_get**](docs/InternshipApi.md#students_affectations_uuid_get) | **GET** /students_affectations/{uuid} | 
*InternshipApi* | [**students_get**](docs/InternshipApi.md#students_get) | **GET** /students | 
*InternshipApi* | [**students_uuid_get**](docs/InternshipApi.md#students_uuid_get) | **GET** /students/{uuid} | 


## Documentation For Models

 - [AllocationGet](docs/AllocationGet.md)
 - [AllocationPaging](docs/AllocationPaging.md)
 - [CohortGet](docs/CohortGet.md)
 - [CohortPaging](docs/CohortPaging.md)
 - [Country](docs/Country.md)
 - [InlineResponse404](docs/InlineResponse404.md)
 - [InternshipGet](docs/InternshipGet.md)
 - [InternshipPaging](docs/InternshipPaging.md)
 - [MasterGet](docs/MasterGet.md)
 - [MasterPaging](docs/MasterPaging.md)
 - [OrganizationGet](docs/OrganizationGet.md)
 - [OrganizationPaging](docs/OrganizationPaging.md)
 - [PeriodGet](docs/PeriodGet.md)
 - [PeriodPaging](docs/PeriodPaging.md)
 - [Person](docs/Person.md)
 - [ScoreGet](docs/ScoreGet.md)
 - [SpecialtyGet](docs/SpecialtyGet.md)
 - [SpecialtyPaging](docs/SpecialtyPaging.md)
 - [Student](docs/Student.md)
 - [StudentAffectationGet](docs/StudentAffectationGet.md)
 - [StudentAffectationPaging](docs/StudentAffectationPaging.md)
 - [StudentGet](docs/StudentGet.md)
 - [StudentPaging](docs/StudentPaging.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in osis_internship_sdk.apis and osis_internship_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from osis_internship_sdk.api.default_api import DefaultApi`
- `from osis_internship_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import osis_internship_sdk
from osis_internship_sdk.apis import *
from osis_internship_sdk.models import *
```

