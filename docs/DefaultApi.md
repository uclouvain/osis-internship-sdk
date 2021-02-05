# osis_internship_sdk.DefaultApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/internship*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cohorts_get**](DefaultApi.md#cohorts_get) | **GET** /cohorts | 
[**cohorts_uuid_get**](DefaultApi.md#cohorts_uuid_get) | **GET** /cohorts/{uuid} | 
[**internships_get**](DefaultApi.md#internships_get) | **GET** /internships | 
[**internships_uuid_get**](DefaultApi.md#internships_uuid_get) | **GET** /internships/{uuid} | 
[**masters_allocations_specialty_organization_get**](DefaultApi.md#masters_allocations_specialty_organization_get) | **GET** /masters_allocations/{specialty}/{organization} | 
[**masters_allocations_specialty_organization_post**](DefaultApi.md#masters_allocations_specialty_organization_post) | **POST** /masters_allocations/{specialty}/{organization} | 
[**masters_allocations_uuid_get**](DefaultApi.md#masters_allocations_uuid_get) | **GET** /masters_allocations/{uuid} | 
[**masters_get**](DefaultApi.md#masters_get) | **GET** /masters/ | 
[**masters_post**](DefaultApi.md#masters_post) | **POST** /masters/ | 
[**masters_uuid_activate_account_put**](DefaultApi.md#masters_uuid_activate_account_put) | **PUT** /masters/{uuid}/activate_account/ | 
[**masters_uuid_allocations_get**](DefaultApi.md#masters_uuid_allocations_get) | **GET** /masters/{uuid}/allocations/ | 
[**masters_uuid_get**](DefaultApi.md#masters_uuid_get) | **GET** /masters/{uuid} | 
[**organizations_get**](DefaultApi.md#organizations_get) | **GET** /organizations | 
[**organizations_uuid_get**](DefaultApi.md#organizations_uuid_get) | **GET** /organizations/{uuid} | 
[**periods_get**](DefaultApi.md#periods_get) | **GET** /periods | 
[**periods_uuid_get**](DefaultApi.md#periods_uuid_get) | **GET** /periods/{uuid} | 
[**scores_student_uuid_period_uuid_get**](DefaultApi.md#scores_student_uuid_period_uuid_get) | **GET** /scores/{student_uuid}/{period_uuid} | 
[**scores_student_uuid_period_uuid_put**](DefaultApi.md#scores_student_uuid_period_uuid_put) | **PUT** /scores/{student_uuid}/{period_uuid} | 
[**specialties_get**](DefaultApi.md#specialties_get) | **GET** /specialties | 
[**specialties_uuid_get**](DefaultApi.md#specialties_uuid_get) | **GET** /specialties/{uuid} | 
[**students_affectations_specialty_organization_get**](DefaultApi.md#students_affectations_specialty_organization_get) | **GET** /students_affectations/{specialty}/{organization} | 
[**students_affectations_uuid_get**](DefaultApi.md#students_affectations_uuid_get) | **GET** /students_affectations/{uuid} | 
[**students_get**](DefaultApi.md#students_get) | **GET** /students | 
[**students_uuid_get**](DefaultApi.md#students_uuid_get) | **GET** /students/{uuid} | 


# **cohorts_get**
> object cohorts_get()



Obtain the list of cohorts

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))

try:
    api_response = api_instance.cohorts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cohorts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cohorts_uuid_get**
> CohortGet cohorts_uuid_get(uuid)



Obtain information about a specific cohort

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the cohort

try:
    api_response = api_instance.cohorts_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cohorts_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the cohort | 

### Return type

[**CohortGet**](CohortGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internships_get**
> object internships_get()



Obtain the list of internships

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))

try:
    api_response = api_instance.internships_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->internships_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internships_uuid_get**
> InternshipGet internships_uuid_get(uuid)



Obtain information about a specific internship

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the internship

try:
    api_response = api_instance.internships_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->internships_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the internship | 

### Return type

[**InternshipGet**](InternshipGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_allocations_specialty_organization_get**
> object masters_allocations_specialty_organization_get(organization, specialty, role=role)



Obtain the list of master allocations filtered by specialty and organization

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
organization = 'organization_example' # str | 
specialty = 'specialty_example' # str | 
role = 'all' # str |  (optional) (default to 'all')

try:
    api_response = api_instance.masters_allocations_specialty_organization_get(organization, specialty, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->masters_allocations_specialty_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **specialty** | **str**|  | 
 **role** | **str**|  | [optional] [default to &#39;all&#39;]

### Return type

**object**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_allocations_specialty_organization_post**
> AllocationGet masters_allocations_specialty_organization_post(organization, specialty, allocation_get)



Create new internship allocation

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
organization = 'organization_example' # str | 
specialty = 'specialty_example' # str | 
allocation_get = osis_internship_sdk.AllocationGet() # AllocationGet | 

try:
    api_response = api_instance.masters_allocations_specialty_organization_post(organization, specialty, allocation_get)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->masters_allocations_specialty_organization_post: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_allocations_uuid_get**
> AllocationGet masters_allocations_uuid_get(uuid)



Obtain information about a specific master allocation

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the master allocation

try:
    api_response = api_instance.masters_allocations_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->masters_allocations_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the master allocation | 

### Return type

[**AllocationGet**](AllocationGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_get**
> object masters_get(search=search)



Obtain the list of internship masters

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
search = 'search_example' # str |  (optional)

try:
    api_response = api_instance.masters_get(search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->masters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_post**
> MasterGet masters_post(master_get)



Create new internship master

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
master_get = osis_internship_sdk.MasterGet() # MasterGet | 

try:
    api_response = api_instance.masters_post(master_get)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->masters_post: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_uuid_activate_account_put**
> MasterGet masters_uuid_activate_account_put(uuid)



Set master account activation status to ACTIVE

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the master

try:
    api_response = api_instance.masters_uuid_activate_account_put(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->masters_uuid_activate_account_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the master | 

### Return type

[**MasterGet**](MasterGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_uuid_allocations_get**
> object masters_uuid_allocations_get(uuid, current=current)



Obtain the list of internship-master allocations

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the master
current = True # bool |  (optional)

try:
    api_response = api_instance.masters_uuid_allocations_get(uuid, current=current)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->masters_uuid_allocations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the master | 
 **current** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masters_uuid_get**
> MasterGet masters_uuid_get(uuid)



Obtain information about a specific master

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the master

try:
    api_response = api_instance.masters_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->masters_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the master | 

### Return type

[**MasterGet**](MasterGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_get**
> object organizations_get()



Obtain the list of organizations

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))

try:
    api_response = api_instance.organizations_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_uuid_get**
> OrganizationGet organizations_uuid_get(uuid)



Obtain information about a specific organization

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the organization

try:
    api_response = api_instance.organizations_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the organization | 

### Return type

[**OrganizationGet**](OrganizationGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periods_get**
> object periods_get(active=active)



Obtain the list of periods

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
active = True # bool |  (optional)

try:
    api_response = api_instance.periods_get(active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->periods_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periods_uuid_get**
> PeriodGet periods_uuid_get(uuid)



Obtain information about a specific period

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the period

try:
    api_response = api_instance.periods_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->periods_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the period | 

### Return type

[**PeriodGet**](PeriodGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scores_student_uuid_period_uuid_get**
> ScoreGet scores_student_uuid_period_uuid_get(student_uuid, period_uuid)



Get or create information about a specific student's score for a given period

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
student_uuid = 'student_uuid_example' # str | The UUID of the student
period_uuid = 'period_uuid_example' # str | The UUID of the period

try:
    api_response = api_instance.scores_student_uuid_period_uuid_get(student_uuid, period_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->scores_student_uuid_period_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student_uuid** | [**str**](.md)| The UUID of the student | 
 **period_uuid** | [**str**](.md)| The UUID of the period | 

### Return type

[**ScoreGet**](ScoreGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scores_student_uuid_period_uuid_put**
> scores_student_uuid_period_uuid_put(student_uuid, period_uuid, score_get)



Update a student's score for a given period

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
student_uuid = 'student_uuid_example' # str | The UUID of the student
period_uuid = 'period_uuid_example' # str | The UUID of the period
score_get = osis_internship_sdk.ScoreGet() # ScoreGet | 

try:
    api_instance.scores_student_uuid_period_uuid_put(student_uuid, period_uuid, score_get)
except ApiException as e:
    print("Exception when calling DefaultApi->scores_student_uuid_period_uuid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student_uuid** | [**str**](.md)| The UUID of the student | 
 **period_uuid** | [**str**](.md)| The UUID of the period | 
 **score_get** | [**ScoreGet**](ScoreGet.md)|  | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specialties_get**
> object specialties_get()



Obtain the list of specialties

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))

try:
    api_response = api_instance.specialties_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->specialties_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specialties_uuid_get**
> SpecialtyGet specialties_uuid_get(uuid)



Obtain information about a specific specialty

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the specialty

try:
    api_response = api_instance.specialties_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->specialties_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the specialty | 

### Return type

[**SpecialtyGet**](SpecialtyGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **students_affectations_specialty_organization_get**
> object students_affectations_specialty_organization_get(organization, specialty, period=period, with_score=with_score, limit=limit, offset=offset)



Obtain the list of students affectations

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
organization = 'organization_example' # str | 
specialty = 'specialty_example' # str | 
period = 'all' # str |  (optional) (default to 'all')
with_score = False # bool |  (optional) (default to False)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)

try:
    api_response = api_instance.students_affectations_specialty_organization_get(organization, specialty, period=period, with_score=with_score, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->students_affectations_specialty_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **specialty** | **str**|  | 
 **period** | **str**|  | [optional] [default to &#39;all&#39;]
 **with_score** | **bool**|  | [optional] [default to False]
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

**object**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **students_affectations_uuid_get**
> StudentAffectationGet students_affectations_uuid_get(uuid)



Obtain information about a specific student's affectation

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the student's affectation

try:
    api_response = api_instance.students_affectations_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->students_affectations_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the student&#39;s affectation | 

### Return type

[**StudentAffectationGet**](StudentAffectationGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **students_get**
> object students_get()



Obtain the list of students

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))

try:
    api_response = api_instance.students_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->students_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **students_uuid_get**
> StudentGet students_uuid_get(uuid)



Obtain information about a specific internship student

### Example

* Api Key Authentication (Token): 
```python
from __future__ import print_function
import time
import osis_internship_sdk
from osis_internship_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = osis_internship_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = osis_internship_sdk.DefaultApi(osis_internship_sdk.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the internship student

try:
    api_response = api_instance.students_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->students_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| The UUID of the internship student | 

### Return type

[**StudentGet**](StudentGet.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

