# python_client.UserApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_tokens**](UserApi.md#get_access_tokens) | **GET** /user/accessTokens | Get Access Tokens
[**get_user**](UserApi.md#get_user) | **GET** /user | Get User Details
[**register_user**](UserApi.md#register_user) | **POST** /user/register | Register User
[**saml_login**](UserApi.md#saml_login) | **POST** /user/samlLogin | Saml Login
[**unregister**](UserApi.md#unregister) | **DELETE** /user/unregister | Delete User
[**update_user**](UserApi.md#update_user) | **PUT** /user | Update User Details
[**user_logout**](UserApi.md#user_logout) | **POST** /user/logout | User Logout


# **get_access_tokens**
> UserAccessTokensResponse get_access_tokens(app_ids)

Get Access Tokens

The Get Access Tokens service is used to retrieve the access tokens for the application id(s) provided.<br>URL in the response can be used to launch the application for which token is requested.<br><b>Note:</b> This endpoint is deprecated for customers using the API Key-based authentication <br>and is applicable only to customers who use the SAML-based authentication.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.UserApi()
app_ids = 'app_ids_example' # str | appIds

try:
    # Get Access Tokens
    api_response = api_instance.get_access_tokens(app_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_access_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_ids** | **str**| appIds | 

### Return type

[**UserAccessTokensResponse**](UserAccessTokensResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserDetailResponse get_user()

Get User Details

The get user details service is used to get the user profile information and the application <br>preferences set at the time of user registration.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.UserApi()

try:
    # Get User Details
    api_response = api_instance.get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDetailResponse**](UserDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> UserResponse register_user(user_request)

Register User

The register user service is used to register a user in Yodlee.<br>The loginName cannot include spaces and must be between 3 and 150 characters.<br>locale passed must be one of the supported locales for the customer. <br>Currency provided in the input will be respected in the derived services and the amount fields in the response will be provided in the preferred currency.<br>userParam is accepted as a body parameter. <br><b>Note:</b> user.password is no longer supported.<br>The content type has to be passed as application/json for the body parameter.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.UserApi()
user_request = python_client.UserRequest() # UserRequest | userRequest

try:
    # Register User
    api_response = api_instance.register_user(user_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->register_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_request** | [**UserRequest**](UserRequest.md)| userRequest | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **saml_login**
> UserResponse saml_login(issuer, saml_response, source=source)

Saml Login

The SAML login service is used to authenticate system users with a SAML response.<br>A new user will be created with the input provided if that user isn't already in the system.<br>For existing users, the system will make updates based on changes or new information.<br>When authentication is successful, a user session token is returned.<br><b>Note:</b> The content type has to be passed as application/x-www-form-urlencoded. <br>issuer, source and samlResponse should be passed as body parameters.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.UserApi()
issuer = 'issuer_example' # str | issuer
saml_response = 'saml_response_example' # str | samlResponse
source = 'source_example' # str | source (optional)

try:
    # Saml Login
    api_response = api_instance.saml_login(issuer, saml_response, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->saml_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer** | **str**| issuer | 
 **saml_response** | **str**| samlResponse | 
 **source** | **str**| source | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister**
> unregister()

Delete User

The delete user service is used to delete or unregister a user from Yodlee. <br>Once deleted, the information related to the users cannot be retrieved. <br>The HTTP response code is 204 (Success without content)<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.UserApi()

try:
    # Delete User
    api_instance.unregister()
except ApiException as e:
    print("Exception when calling UserApi->unregister: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(user_request)

Update User Details

The update user details service is used to update user details like name, address, currency preference, etc.<br>Currency provided in the input will be respected in the <a href=\"https://developer.yodlee.com/apidocs/index.php#!/derived\">derived</a> services and the amount fields in the response will be provided in the preferred currency.<br>The HTTP response code is 204 (Success without content). <br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.UserApi()
user_request = python_client.UpdateUserRequest() # UpdateUserRequest | userRequest

try:
    # Update User Details
    api_instance.update_user(user_request)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)| userRequest | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_logout**
> user_logout()

User Logout

<b>Deprecated</b>: This endpoint is deprecated for API Key-based authentication. The user logout service allows the user to log out of the application.<br>The service does not return a response body. The HTTP response code is 204 (Success with no content).<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.UserApi()

try:
    # User Logout
    api_instance.user_logout()
except ApiException as e:
    print("Exception when calling UserApi->user_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

