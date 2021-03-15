# osis_internship_sdk.InternshipApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/internship*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cohorts_get**](InternshipApi.md#cohorts_get) | **GET** /cohorts | 
[**cohorts_uuid_get**](InternshipApi.md#cohorts_uuid_get) | **GET** /cohorts/{uuid} | 
[**internships_get**](InternshipApi.md#internships_get) | **GET** /internships | 
[**internships_uuid_get**](InternshipApi.md#internships_uuid_get) | **GET** /internships/{uuid} | 
[**masters_allocations_specialty_organization_get**](InternshipApi.md#masters_allocations_specialty_organization_get) | **GET** /masters_allocations/{specialty}/{organization} | 
[**masters_allocations_specialty_organization_post**](InternshipApi.md#masters_allocations_specialty_organization_post) | **POST** /masters_allocations/{specialty}/{organization} | 
[**masters_allocations_uuid_delete**](InternshipApi.md#masters_allocations_uuid_delete) | **DELETE** /masters_allocations/{uuid} | 
[**masters_allocations_uuid_get**](InternshipApi.md#masters_allocations_uuid_get) | **GET** /masters_allocations/{uuid} | 
[**masters_get**](InternshipApi.md#masters_get) | **GET** /masters/ | 
[**masters_post**](InternshipApi.md#masters_post) | **POST** /masters/ | 
[**masters_uuid_activate_account_put**](InternshipApi.md#masters_uuid_activate_account_put) | **PUT** /masters/{uuid}/activate_account/ | 
[**masters_uuid_allocations_get**](InternshipApi.md#masters_uuid_allocations_get) | **GET** /masters/{uuid}/allocations/ | 
[**masters_uuid_get**](InternshipApi.md#masters_uuid_get) | **GET** /masters/{uuid} | 
[**organizations_get**](InternshipApi.md#organizations_get) | **GET** /organizations | 
[**organizations_uuid_get**](InternshipApi.md#organizations_uuid_get) | **GET** /organizations/{uuid} | 
[**periods_get**](InternshipApi.md#periods_get) | **GET** /periods | 
[**periods_uuid_get**](InternshipApi.md#periods_uuid_get) | **GET** /periods/{uuid} | 
[**scores_affectation_uuid_validate_get**](InternshipApi.md#scores_affectation_uuid_validate_get) | **GET** /scores/{affectation_uuid}/validate | 
[**scores_student_uuid_period_uuid_get**](InternshipApi.md#scores_student_uuid_period_uuid_get) | **GET** /scores/{student_uuid}/{period_uuid} | 
[**scores_student_uuid_period_uuid_put**](InternshipApi.md#scores_student_uuid_period_uuid_put) | **PUT** /scores/{student_uuid}/{period_uuid} | 
[**specialties_get**](InternshipApi.md#specialties_get) | **GET** /specialties | 
[**specialties_uuid_get**](InternshipApi.md#specialties_uuid_get) | **GET** /specialties/{uuid} | 
[**students_affectations_specialty_organization_get**](InternshipApi.md#students_affectations_specialty_organization_get) | **GET** /students_affectations/{specialty}/{organization} | 
[**students_affectations_uuid_get**](InternshipApi.md#students_affectations_uuid_get) | **GET** /students_affectations/{uuid} | 
[**students_get**](InternshipApi.md#students_get) | **GET** /students | 
[**students_uuid_get**](InternshipApi.md#students_uuid_get) | **GET** /students/{uuid} | 


# **cohorts_get**
> CohortPaging cohorts_get()



Obtain the list of cohorts

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.cohort_paging import CohortPaging
from pprint import pprint
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

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.cohorts_get()
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->cohorts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CohortPaging**](CohortPaging.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of the list of cohorts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cohorts_uuid_get**
> CohortGet cohorts_uuid_get(uuid)



Obtain information about a specific cohort

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.cohort_get import CohortGet
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the cohort

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cohorts_uuid_get(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->cohorts_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the cohort |

### Return type

[**CohortGet**](CohortGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of a cohort&#39;s data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internships_get**
> InternshipPaging internships_get()



Obtain the list of internships

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.internship_paging import InternshipPaging
from pprint import pprint
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

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.internships_get()
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->internships_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InternshipPaging**](InternshipPaging.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of the list of internships |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internships_uuid_get**
> InternshipGet internships_uuid_get(uuid)



Obtain information about a specific internship

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.internship_get import InternshipGet
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the internship

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.internships_uuid_get(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->internships_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the internship |

### Return type

[**InternshipGet**](InternshipGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of an internship&#39;s data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_allocations_specialty_organization_get**
> AllocationPaging masters_allocations_specialty_organization_get(organization, specialty)



Obtain the list of master allocations filtered by specialty and organization

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.allocation_paging import AllocationPaging
from pprint import pprint
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
    organization = "organization_example" # str | 
    specialty = "specialty_example" # str | 
    role = "all" # str |  (optional) if omitted the server will use the default value of "all"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.masters_allocations_specialty_organization_get(organization, specialty)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->masters_allocations_specialty_organization_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.masters_allocations_specialty_organization_get(organization, specialty, role=role)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->masters_allocations_specialty_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  |
 **specialty** | **str**|  |
 **role** | **str**|  | [optional] if omitted the server will use the default value of "all"

### Return type

[**AllocationPaging**](AllocationPaging.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of the list of masters allocations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_allocations_specialty_organization_post**
> AllocationGet masters_allocations_specialty_organization_post(organization, specialty, allocation_get)



Create new internship allocation

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.allocation_get import AllocationGet
from pprint import pprint
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
    organization = "organization_example" # str | 
    specialty = "specialty_example" # str | 
    allocation_get = AllocationGet(
        url="url_example",
        uuid="uuid_example",
        master=MasterGet(
            url="url_example",
            uuid="uuid_example",
            person=Person(
                uuid="uuid_example",
                first_name="Dupont",
                last_name="Jacques",
                email="jacques.dupont@mail.xyz",
                gender="M",
                birth_date=dateutil_parser('Sun Jan 01 01:00:00 CET 1989').date(),
            ),
            civility="DOCTOR",
            user_account_status="active",
        ),
        organization=OrganizationGet(
            url="url_example",
            uuid="uuid_example",
            name="CHU XYZ",
            acronym="XYZ",
            website="www.chuxyz.be",
            reference="01",
            phone="01/01.01.01",
            location="Rue de l'hôpital",
            postal_code="1000",
            city="Bruxelles",
            country=Country(
                url="url_example",
                uuid="uuid_example",
                iso_code="BE",
                name="Belgium",
                nationality="Belgian",
            ),
            cohort=CohortGet(
                url="url_example",
                uuid="uuid_example",
                name="R6-2021",
                description="Student cohort for academic year 2020-2021",
                publication_start_date="01/04/2020",
                subscription_start_date="01/02/2020",
                subscription_end_date="01/03/2020",
            ),
        ),
        specialty=SpecialtyGet(
            url="url_example",
            uuid="uuid_example",
            name="Xyzetologie",
            acronym="XYZ",
            mandatory=True,
            sequence=1,
            cohort=CohortGet(
                url="url_example",
                uuid="uuid_example",
                name="R6-2021",
                description="Student cohort for academic year 2020-2021",
                publication_start_date="01/04/2020",
                subscription_start_date="01/02/2020",
                subscription_end_date="01/03/2020",
            ),
            selectable=True,
        ),
        role="MASTER",
    ) # AllocationGet | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.masters_allocations_specialty_organization_post(organization, specialty, allocation_get)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->masters_allocations_specialty_organization_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  |
 **specialty** | **str**|  |
 **allocation_get** | [**AllocationGet**](AllocationGet.md)|  |

### Return type

[**AllocationGet**](AllocationGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created an internship master allocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_allocations_uuid_delete**
> AllocationGet masters_allocations_uuid_delete(uuid)



Delete a master allocation

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.allocation_get import AllocationGet
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the master allocation

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.masters_allocations_uuid_delete(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->masters_allocations_uuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the master allocation |

### Return type

[**AllocationGet**](AllocationGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful delete of a master allocation&#39;s data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_allocations_uuid_get**
> AllocationGet masters_allocations_uuid_get(uuid)



Obtain information about a specific master allocation

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.allocation_get import AllocationGet
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the master allocation

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.masters_allocations_uuid_get(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->masters_allocations_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the master allocation |

### Return type

[**AllocationGet**](AllocationGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of a master allocation&#39;s data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_get**
> MasterPaging masters_get()



Obtain the list of internship masters

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.master_paging import MasterPaging
from pprint import pprint
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
    search = "search_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.masters_get(search=search)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->masters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional]

### Return type

[**MasterPaging**](MasterPaging.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of the list of internship masters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_post**
> MasterGet masters_post(master_get)



Create new internship master

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.master_get import MasterGet
from pprint import pprint
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
    master_get = MasterGet(
        url="url_example",
        uuid="uuid_example",
        person=Person(
            uuid="uuid_example",
            first_name="Dupont",
            last_name="Jacques",
            email="jacques.dupont@mail.xyz",
            gender="M",
            birth_date=dateutil_parser('Sun Jan 01 01:00:00 CET 1989').date(),
        ),
        civility="DOCTOR",
        user_account_status="active",
    ) # MasterGet | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.masters_post(master_get)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->masters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_get** | [**MasterGet**](MasterGet.md)|  |

### Return type

[**MasterGet**](MasterGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created an internship master |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_uuid_activate_account_put**
> MasterGet masters_uuid_activate_account_put(uuid)



Set master account activation status to ACTIVE

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.master_get import MasterGet
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the master

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.masters_uuid_activate_account_put(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->masters_uuid_activate_account_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the master |

### Return type

[**MasterGet**](MasterGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful master&#39;s account status update. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_uuid_allocations_get**
> AllocationPaging masters_uuid_allocations_get(uuid)



Obtain the list of internship-master allocations

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.allocation_paging import AllocationPaging
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the master
    current = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.masters_uuid_allocations_get(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->masters_uuid_allocations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.masters_uuid_allocations_get(uuid, current=current)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->masters_uuid_allocations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the master |
 **current** | **bool**|  | [optional]

### Return type

[**AllocationPaging**](AllocationPaging.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of the list of allocations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_uuid_get**
> MasterGet masters_uuid_get(uuid)



Obtain information about a specific master

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.master_get import MasterGet
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the master

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.masters_uuid_get(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->masters_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the master |

### Return type

[**MasterGet**](MasterGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of a master&#39;s data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_get**
> OrganizationPaging organizations_get()



Obtain the list of organizations

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.organization_paging import OrganizationPaging
from pprint import pprint
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

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.organizations_get()
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->organizations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganizationPaging**](OrganizationPaging.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of the list of organizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_uuid_get**
> OrganizationGet organizations_uuid_get(uuid)



Obtain information about a specific organization

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.organization_get import OrganizationGet
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the organization

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.organizations_uuid_get(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->organizations_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the organization |

### Return type

[**OrganizationGet**](OrganizationGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of an organization&#39;s data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periods_get**
> PeriodPaging periods_get()



Obtain the list of periods

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.period_paging import PeriodPaging
from pprint import pprint
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
    active = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.periods_get(active=active)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->periods_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**|  | [optional]

### Return type

[**PeriodPaging**](PeriodPaging.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of the list of periods |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periods_uuid_get**
> PeriodGet periods_uuid_get(uuid)



Obtain information about a specific period

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.period_get import PeriodGet
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the period

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.periods_uuid_get(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->periods_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the period |

### Return type

[**PeriodGet**](PeriodGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of a period&#39;s data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scores_affectation_uuid_validate_get**
> scores_affectation_uuid_validate_get(affectation_uuid)



Validate a score

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.inline_response404 import InlineResponse404
from pprint import pprint
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
    affectation_uuid = "affectation_uuid_example" # str | The UUID of the period

    # example passing only required values which don't have defaults set
    try:
        api_instance.scores_affectation_uuid_validate_get(affectation_uuid)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->scores_affectation_uuid_validate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affectation_uuid** | **str**| The UUID of the period |

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully validated an internship score |  -  |
**404** | Affectation or score not found, validation aborted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scores_student_uuid_period_uuid_get**
> ScoreGet scores_student_uuid_period_uuid_get(student_uuid, period_uuid)



Get or create information about a specific student's score for a given period

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.score_get import ScoreGet
from pprint import pprint
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
    student_uuid = "student_uuid_example" # str | The UUID of the student
    period_uuid = "period_uuid_example" # str | The UUID of the period

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.scores_student_uuid_period_uuid_get(student_uuid, period_uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->scores_student_uuid_period_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student_uuid** | **str**| The UUID of the student |
 **period_uuid** | **str**| The UUID of the period |

### Return type

[**ScoreGet**](ScoreGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get or create of a student&#39;s score for a given period. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scores_student_uuid_period_uuid_put**
> scores_student_uuid_period_uuid_put(student_uuid, period_uuid, score_get)



Update a student's score for a given period

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.score_get import ScoreGet
from pprint import pprint
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
    student_uuid = "student_uuid_example" # str | The UUID of the student
    period_uuid = "period_uuid_example" # str | The UUID of the period
    score_get = ScoreGet(
        uuid="uuid_example",
        student=Student(
            uuid="uuid_example",
            registration_id="44444444444",
            person=Person(
                uuid="uuid_example",
                first_name="Dupont",
                last_name="Jacques",
                email="jacques.dupont@mail.xyz",
                gender="M",
                birth_date=dateutil_parser('Sun Jan 01 01:00:00 CET 1989').date(),
            ),
        ),
        period=PeriodGet(
            url="url_example",
            uuid="uuid_example",
            name="P1",
            date_start="01/02/2020",
            date_end="01/03/2020",
            cohort=CohortGet(
                url="url_example",
                uuid="uuid_example",
                name="R6-2021",
                description="Student cohort for academic year 2020-2021",
                publication_start_date="01/04/2020",
                subscription_start_date="01/02/2020",
                subscription_end_date="01/03/2020",
            ),
        ),
        cohort=CohortGet(
            url="url_example",
            uuid="uuid_example",
            name="R6-2021",
            description="Student cohort for academic year 2020-2021",
            publication_start_date="01/04/2020",
            subscription_start_date="01/02/2020",
            subscription_end_date="01/03/2020",
        ),
        excused=True,
        reason="reason_example",
        score=3.14,
        comments={},
        objectives={},
        validated=True,
        apd_1="apd_1_example",
        apd_2="apd_2_example",
        apd_3="apd_3_example",
        apd_4="apd_4_example",
        apd_5="apd_5_example",
        apd_6="apd_6_example",
        apd_7="apd_7_example",
        apd_8="apd_8_example",
        apd_9="apd_9_example",
        apd_10="apd_10_example",
        apd_11="apd_11_example",
        apd_12="apd_12_example",
        apd_13="apd_13_example",
        apd_14="apd_14_example",
        apd_15="apd_15_example",
    ) # ScoreGet | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.scores_student_uuid_period_uuid_put(student_uuid, period_uuid, score_get)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->scores_student_uuid_period_uuid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student_uuid** | **str**| The UUID of the student |
 **period_uuid** | **str**| The UUID of the period |
 **score_get** | [**ScoreGet**](ScoreGet.md)|  |

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful update of a score for a given period |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specialties_get**
> SpecialtyPaging specialties_get()



Obtain the list of specialties

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.specialty_paging import SpecialtyPaging
from pprint import pprint
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

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.specialties_get()
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->specialties_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SpecialtyPaging**](SpecialtyPaging.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of the list of specialties |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specialties_uuid_get**
> SpecialtyGet specialties_uuid_get(uuid)



Obtain information about a specific specialty

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.specialty_get import SpecialtyGet
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the specialty

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.specialties_uuid_get(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->specialties_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the specialty |

### Return type

[**SpecialtyGet**](SpecialtyGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of a specialty&#39;s data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **students_affectations_specialty_organization_get**
> StudentAffectationPaging students_affectations_specialty_organization_get(organization, specialty)



Obtain the list of students affectations

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.student_affectation_paging import StudentAffectationPaging
from pprint import pprint
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
    organization = "organization_example" # str | 
    specialty = "specialty_example" # str | 
    period = "all" # str |  (optional) if omitted the server will use the default value of "all"
    with_score = False # bool |  (optional) if omitted the server will use the default value of False
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.students_affectations_specialty_organization_get(organization, specialty)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->students_affectations_specialty_organization_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.students_affectations_specialty_organization_get(organization, specialty, period=period, with_score=with_score, limit=limit, offset=offset)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->students_affectations_specialty_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  |
 **specialty** | **str**|  |
 **period** | **str**|  | [optional] if omitted the server will use the default value of "all"
 **with_score** | **bool**|  | [optional] if omitted the server will use the default value of False
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]

### Return type

[**StudentAffectationPaging**](StudentAffectationPaging.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of the list of students affectations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **students_affectations_uuid_get**
> StudentAffectationGet students_affectations_uuid_get(uuid)



Obtain information about a specific student's affectation

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.student_affectation_get import StudentAffectationGet
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the student's affectation

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.students_affectations_uuid_get(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->students_affectations_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the student&#39;s affectation |

### Return type

[**StudentAffectationGet**](StudentAffectationGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of a student&#39;s affectation&#39;s data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **students_get**
> StudentPaging students_get()



Obtain the list of students

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.student_paging import StudentPaging
from pprint import pprint
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

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.students_get()
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->students_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StudentPaging**](StudentPaging.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of the list of students |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **students_uuid_get**
> StudentGet students_uuid_get(uuid)



Obtain information about a specific internship student

### Example

* Api Key Authentication (Token):
```python
import time
import osis_internship_sdk
from osis_internship_sdk.api import internship_api
from osis_internship_sdk.model.student_get import StudentGet
from pprint import pprint
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
    uuid = "uuid_example" # str | The UUID of the internship student

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.students_uuid_get(uuid)
        pprint(api_response)
    except osis_internship_sdk.ApiException as e:
        print("Exception when calling InternshipApi->students_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the internship student |

### Return type

[**StudentGet**](StudentGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get of a internship student&#39;s data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

