# python_client.ConsentsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_consent**](ConsentsApi.md#create_consent) | **POST** /consents | Post Consent
[**get_consent_details**](ConsentsApi.md#get_consent_details) | **GET** /consents/{consentId} | Get Consent Details
[**get_consents**](ConsentsApi.md#get_consents) | **GET** /consents | Get Consents
[**update_consent**](ConsentsApi.md#update_consent) | **PUT** /consents/{consentId} | Put Consent


# **create_consent**
> CreatedConsentResponse create_consent(consent_request)

Post Consent

The generate consent service is used to generate all the consent information and permissions associated to a provider. <br/>The scope provided in the response is based on the providerId and the datasets provided in the input. <br/>If no dataset value is provided, the datasets that are configured for the customer will be considered. <br/>The configured dataset can be overridden by providing the dataset as an input. <br/>If no applicationName is provided in the input, the default applicationName will be considered. <b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.ConsentsApi()
consent_request = python_client.CreateConsentRequest() # CreateConsentRequest | Unique identifier for the provider site(mandatory), the name of the application,  <br/>the flag responsible to include html content in the response, <br/>when passed as true and the name of the dataset attribute supported by the provider.

try:
    # Post Consent
    api_response = api_instance.create_consent(consent_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->create_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_request** | [**CreateConsentRequest**](CreateConsentRequest.md)| Unique identifier for the provider site(mandatory), the name of the application,  &lt;br/&gt;the flag responsible to include html content in the response, &lt;br/&gt;when passed as true and the name of the dataset attribute supported by the provider. | 

### Return type

[**CreatedConsentResponse**](CreatedConsentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_details**
> UpdatedConsentResponse get_consent_details(consent_id)

Get Consent Details

The get authorization URL for consent service provides the authorization URL for the renew consent flow, within the consent dashboard.<b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.ConsentsApi()
consent_id = 789 # int | Consent Id generated through POST Consent.

try:
    # Get Consent Details
    api_response = api_instance.get_consent_details(consent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->get_consent_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **int**| Consent Id generated through POST Consent. | 

### Return type

[**UpdatedConsentResponse**](UpdatedConsentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consents**
> ConsentResponse get_consents(consent_ids=consent_ids, provider_account_ids=provider_account_ids)

Get Consents

The get consent service is used to retrieve all the consents submitted to Yodlee. <br>The service can be used to build a manage consent interface or a consent dashboard to implement the renew and revoke consent flows.<br><b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.ConsentsApi()
consent_ids = 'consent_ids_example' # str | Consent Id generated through POST Consent. (optional)
provider_account_ids = 'provider_account_ids_example' # str | Unique identifier for the provider account resource. This is created during account addition. (optional)

try:
    # Get Consents
    api_response = api_instance.get_consents(consent_ids=consent_ids, provider_account_ids=provider_account_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->get_consents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_ids** | **str**| Consent Id generated through POST Consent. | [optional] 
 **provider_account_ids** | **str**| Unique identifier for the provider account resource. This is created during account addition. | [optional] 

### Return type

[**ConsentResponse**](ConsentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_consent**
> UpdatedConsentResponse update_consent(consent_id, consent_request)

Put Consent

The update consent service is used to capture the user acceptance of the consent presented to him or her. <br/>This service returns the authorization-redirect URL that should be used to display to the user, the bank's authentication interface.<b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.ConsentsApi()
consent_id = 789 # int | Consent Id generated through POST Consent.
consent_request = python_client.UpdateConsentRequest() # UpdateConsentRequest | Applicable Open Banking data cluster values.

try:
    # Put Consent
    api_response = api_instance.update_consent(consent_id, consent_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->update_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **int**| Consent Id generated through POST Consent. | 
 **consent_request** | [**UpdateConsentRequest**](UpdateConsentRequest.md)| Applicable Open Banking data cluster values. | 

### Return type

[**UpdatedConsentResponse**](UpdatedConsentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

