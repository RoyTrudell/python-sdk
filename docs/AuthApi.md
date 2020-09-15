# python_client.AuthApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_key**](AuthApi.md#delete_api_key) | **DELETE** /auth/apiKey/{key} | Delete API Key
[**delete_token**](AuthApi.md#delete_token) | **DELETE** /auth/token | Delete Token
[**generate_access_token**](AuthApi.md#generate_access_token) | **POST** /auth/token | Generate Access Token
[**generate_api_key**](AuthApi.md#generate_api_key) | **POST** /auth/apiKey | Generate API Key
[**get_api_keys**](AuthApi.md#get_api_keys) | **GET** /auth/apiKey | Get API Keys


# **delete_api_key**
> delete_api_key(key)

Delete API Key

This endpoint allows an existing API key to be deleted.<br>You can use one of the following authorization methods to access this API:<br><ol><li>cobsession</li><li>JWT token</li></ol><b>Notes:</b><br>This service is not available in developer sandbox environment and will be made available<br>for testing in your dedicated environment. 

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AuthApi()
key = 'key_example' # str | key

try:
    # Delete API Key
    api_instance.delete_api_key(key)
except ApiException as e:
    print("Exception when calling AuthApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> delete_token()

Delete Token

This endpoint revokes the token passed in the Authorization header. This service is applicable for <br/>JWT-based (and all API key-based) authentication and also client credential (clientId and secret) <br/>based authentication. This service does not return a response body. The HTTP response code is 204 <br/>(success with no content). Tokens generally have limited lifetime of up to 30 minutes. You will <br/>call this service when you finish working with one user, and you want to delete the valid token <br/>rather than simply letting it expire.<br/><br/>Note: Revoking an access token (either type, admin or a user token) can take up to 2 minutes, <br/>as the tokens are stored on a distributed system.<br/>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AuthApi()

try:
    # Delete Token
    api_instance.delete_token()
except ApiException as e:
    print("Exception when calling AuthApi->delete_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_access_token**
> ClientCredentialTokenResponse generate_access_token()

Generate Access Token

<b>Generate Access Token using client credential authentication.</b><br/><br><br>This service returns access tokens required to access Yodlee 1.1 APIs. These tokens are the <br/>simplest and easiest of several alternatives for authenticating with Yodlee servers.<br/><br><br>The most commonly used services obtain data specific to an end user (your customer). <br/>For these services, you need a <b>user access token</b>. These are simply tokens created with <br/>the user name parameter (<b>loginName</b>) set to the id of your end user.  Note: you determine <br/>this id and you must ensure it's unique among all your customers.<br/><br><br>Each token issued has an associated user. The token passed in the http headers explicitly <br/>names the user referenced in that API call.<br/><br><br>Some of the APIs do administrative work, and don't reference an end user. <br/>One example of administrative work is key management. Another example is <br/>registering a new user explicitly, with <b>POST /user/register</b> call <br/>or subscribe to webhook, with <b>POST /config/notifications/events/{eventName}</b>. <br/>To invoke these, you need an <b>admin access token</b>. Create this by passing in <br/>your admin user login name in place of a regular user name.<br/><br><br>This service also allows for simplified registration of new users. Any time you pass in a user <br/>name not already in use, the system will automatically implicitly create a new user for you. <br/>This user will have naturally have very few associated details. You can later provide additional <br/>user information by calling the <b>PUT user/register service</b>.<br/><br><br><b>Notes:</b><br/>The content type has to be passed as application/x-www-form-urlencoded.<br/>//Upgrading to client credential authentication requires infrastructure reconfiguration. <br/>Customers wishing to switch from another authentication scheme to client credential authentication, <br/>please contact Yodlee Client Services.

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AuthApi()

try:
    # Generate Access Token
    api_response = api_instance.generate_access_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->generate_access_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientCredentialTokenResponse**](ClientCredentialTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_api_key**
> ApiKeyResponse generate_api_key(api_key_request)

Generate API Key

This endpoint is used to generate an API key. The RSA public key you provide should be in<br/>2048 bit PKCS#8 encoded format. A public key is a mandatory input for generating the API key.<br/>The public key should be a unique key. The apiKeyId you get in the response is what you should<br/>use to generate the JWT token.<br> You can use one of the following authorization methods to access<br/>this API:<br/><ol><li>cobsession</li><li>JWT token</li></ol>Alternatively, you can use base 64 encoded cobrandLogin and cobrandPassword in the Authorization header (Format: Authorization: Basic <encoded value of cobrandLogin: cobrandPassword>)<br><b>Note:</b><br>This service is not available in developer sandbox environment and will be made available for testing in your dedicated environment. The content type has to be passed as application/json for the body parameter.

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AuthApi()
api_key_request = python_client.ApiKeyRequest() # ApiKeyRequest | apiKeyRequest

try:
    # Generate API Key
    api_response = api_instance.generate_api_key(api_key_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->generate_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_request** | [**ApiKeyRequest**](ApiKeyRequest.md)| apiKeyRequest | 

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys**
> ApiKeyResponse get_api_keys()

Get API Keys

This endpoint provides the list of API keys that exist for a customer.<br>You can use one of the following authorization methods to access this API:<br><ol><li>cobsession</li><li>JWT token</li></ol><b>Notes:</b><br>This service is not available in developer sandbox environment and will be made available<br>for testing in your dedicated environment. 

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AuthApi()

try:
    # Get API Keys
    api_response = api_instance.get_api_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_api_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

