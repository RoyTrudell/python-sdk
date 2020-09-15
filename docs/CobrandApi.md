# python_client.CobrandApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cobrand_login**](CobrandApi.md#cobrand_login) | **POST** /cobrand/login | Cobrand Login
[**cobrand_logout**](CobrandApi.md#cobrand_logout) | **POST** /cobrand/logout | Cobrand Logout
[**create_subscription_event**](CobrandApi.md#create_subscription_event) | **POST** /cobrand/config/notifications/events/{eventName} | Subscribe Event
[**delete_subscribed_event**](CobrandApi.md#delete_subscribed_event) | **DELETE** /cobrand/config/notifications/events/{eventName} | Delete Subscription
[**get_public_key**](CobrandApi.md#get_public_key) | **GET** /cobrand/publicKey | Get Public Key
[**get_subscribed_events**](CobrandApi.md#get_subscribed_events) | **GET** /cobrand/config/notifications/events | Get Subscribed Events
[**update_subscribed_event**](CobrandApi.md#update_subscribed_event) | **PUT** /cobrand/config/notifications/events/{eventName} | Update Subscription


# **cobrand_login**
> CobrandLoginResponse cobrand_login(cobrand_login_request)

Cobrand Login

The cobrand login service authenticates a cobrand.<br>Cobrand session in the response includes the cobrand session token (cobSession) <br>which is used in subsequent API calls like registering or signing in the user. <br>The idle timeout for a cobrand session is 2 hours and the absolute timeout is 24 hours. This service can be <br>invoked to create a new cobrand session token. <br><b>Note:</b> This endpoint is deprecated for customers using the API Key-based authentication and is applicable only to customers who use the SAML-based authentication.<br>The content type has to be passed as application/json for the body parameter. <br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.CobrandApi()
cobrand_login_request = python_client.CobrandLoginRequest() # CobrandLoginRequest | cobrandLoginRequest

try:
    # Cobrand Login
    api_response = api_instance.cobrand_login(cobrand_login_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CobrandApi->cobrand_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cobrand_login_request** | [**CobrandLoginRequest**](CobrandLoginRequest.md)| cobrandLoginRequest | 

### Return type

[**CobrandLoginResponse**](CobrandLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cobrand_logout**
> cobrand_logout()

Cobrand Logout

The cobrand logout service is used to log out the cobrand.<br>This service does not return a response. The HTTP response code is 204 (Success with no content).<br><b>Note:</b> This endpoint is deprecated for customers using the API Key-based authentication and is applicable only to customers who use the SAML-based authentication.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.CobrandApi()

try:
    # Cobrand Logout
    api_instance.cobrand_logout()
except ApiException as e:
    print("Exception when calling CobrandApi->cobrand_logout: %s\n" % e)
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

# **create_subscription_event**
> create_subscription_event(event_name, event_request)

Subscribe Event

<b>Refer POST /configs/notifications/events/{eventName}.</b><br>The subscribe events service is used to subscribe to an event for receiving notifications.<br>The callback URL, where the notification will be posted should be provided to this service.<br>If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.<br>Customers can subscribe to REFRESH,DATA_UPDATES and AUTO_REFRESH_UPDATES event.<br><br><b>Notes</b>:<br>This service is not available in developer sandbox/test environment and will be made available for testing in your dedicated environment, once the contract is signed.<br>The content type has to be passed as application/json for the body parameter.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.CobrandApi()
event_name = 'event_name_example' # str | eventName
event_request = python_client.CreateCobrandNotificationEventRequest() # CreateCobrandNotificationEventRequest | eventRequest

try:
    # Subscribe Event
    api_instance.create_subscription_event(event_name, event_request)
except ApiException as e:
    print("Exception when calling CobrandApi->create_subscription_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| eventName | 
 **event_request** | [**CreateCobrandNotificationEventRequest**](CreateCobrandNotificationEventRequest.md)| eventRequest | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscribed_event**
> delete_subscribed_event(event_name)

Delete Subscription

<b>Refer DELETE /configs/notifications/events/{eventName}.</b><br>The delete events service is used to unsubscribe from an events service.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.CobrandApi()
event_name = 'event_name_example' # str | eventName

try:
    # Delete Subscription
    api_instance.delete_subscribed_event(event_name)
except ApiException as e:
    print("Exception when calling CobrandApi->delete_subscribed_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| eventName | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_key**
> CobrandPublicKeyResponse get_public_key()

Get Public Key

<b>Refer GET /configs/publicKey.</b><br>The get public key service provides the customer the public key that should be used to encrypt the user credentials before sending it to Yodlee.<br>This endpoint is useful only for PKI enabled.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.CobrandApi()

try:
    # Get Public Key
    api_response = api_instance.get_public_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CobrandApi->get_public_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CobrandPublicKeyResponse**](CobrandPublicKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscribed_events**
> CobrandNotificationResponse get_subscribed_events(event_name=event_name)

Get Subscribed Events

<b>Refer GET /configs/notifications/events.</b><br>The get events service provides the list of events for which consumers subscribed <br>to receive notifications. <br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.CobrandApi()
event_name = 'event_name_example' # str | eventName (optional)

try:
    # Get Subscribed Events
    api_response = api_instance.get_subscribed_events(event_name=event_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CobrandApi->get_subscribed_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| eventName | [optional] 

### Return type

[**CobrandNotificationResponse**](CobrandNotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscribed_event**
> update_subscribed_event(event_name, event_request)

Update Subscription

<b>Refer PUT /configs/notifications/events/{eventName}.</b><br>The update events service is used to update the callback URL.<br>If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.<br><b>Note:</b> The content type has to be passed as application/json for the body parameter. <br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.CobrandApi()
event_name = 'event_name_example' # str | eventName
event_request = python_client.UpdateCobrandNotificationEventRequest() # UpdateCobrandNotificationEventRequest | eventRequest

try:
    # Update Subscription
    api_instance.update_subscribed_event(event_name, event_request)
except ApiException as e:
    print("Exception when calling CobrandApi->update_subscribed_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| eventName | 
 **event_request** | [**UpdateCobrandNotificationEventRequest**](UpdateCobrandNotificationEventRequest.md)| eventRequest | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

