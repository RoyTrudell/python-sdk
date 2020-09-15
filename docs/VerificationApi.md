# python_client.VerificationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_verification_status**](VerificationApi.md#get_verification_status) | **GET** /verification | Get Verification Status
[**initiate_matching_or_challenge_deposite_verification**](VerificationApi.md#initiate_matching_or_challenge_deposite_verification) | **POST** /verification | Initiaite Matching Service and Challenge Deposit
[**verify_challenge_deposit**](VerificationApi.md#verify_challenge_deposit) | **PUT** /verification | Verify Challenge Deposit


# **get_verification_status**
> VerificationStatusResponse get_verification_status(account_id=account_id, provider_account_id=provider_account_id, verification_type=verification_type)

Get Verification Status

The get verification status service is used to retrieve the verification status of all accounts<br>for which the MS or CDV process has been initiated.<br>For the MS process, the account details object returns the aggregated information of the<br>verified accounts. For the CDV process, the account details object returns the user<br>provided account information.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.VerificationApi()
account_id = 'account_id_example' # str | Comma separated accountId (optional)
provider_account_id = 'provider_account_id_example' # str | Comma separated providerAccountId (optional)
verification_type = 'verification_type_example' # str | verificationType (optional)

try:
    # Get Verification Status
    api_response = api_instance.get_verification_status(account_id=account_id, provider_account_id=provider_account_id, verification_type=verification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->get_verification_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Comma separated accountId | [optional] 
 **provider_account_id** | **str**| Comma separated providerAccountId | [optional] 
 **verification_type** | **str**| verificationType | [optional] 

### Return type

[**VerificationStatusResponse**](VerificationStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_matching_or_challenge_deposite_verification**
> VerificationResponse initiate_matching_or_challenge_deposite_verification(verification_param)

Initiaite Matching Service and Challenge Deposit

The post verification service is used to initiate the matching service (MS) and the challenge deposit account verification (CDV) process to verify account ownership. The MS and CDV process can verify ownership of only bank accounts (i.e., checking and savings). <ul><li>MS verification - The MS verification can be initiated only for an already aggregated account or a providerAccount. The prerequisite for the MS verification process is to request the following ACCT_PROFILE dataset attributes:</li><ul><li>FULL_ACCT_NUMBER</li><li>BANK_TRANSFER_CODE (optional based on the configuration done for the customer)</li><li>HOLDER_NAME</li></ul>In the MS verification process, a string-match of the account holder name with the registered user name is performed instantaneously. Contact the Yodlee CustomerCare team to configure the full name or only the last name match.</li></ul><ul><li>Challenge deposit account verification - Once the CDV process is initiated, Yodlee will post the microtransaction (i.e., credit and debit) in the user's account. The CDV process takes 2 to 3 days to complete as it requires the user to provide the microtransaction details. The CDV process is currently supported only in the United States.</li></ul>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.VerificationApi()
verification_param = python_client.VerificationRequest() # VerificationRequest | verification information

try:
    # Initiaite Matching Service and Challenge Deposit
    api_response = api_instance.initiate_matching_or_challenge_deposite_verification(verification_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->initiate_matching_or_challenge_deposite_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verification_param** | [**VerificationRequest**](VerificationRequest.md)| verification information | 

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_challenge_deposit**
> VerificationResponse verify_challenge_deposit(verification_param)

Verify Challenge Deposit

The put verification service is used to complete the CDV process.<br> In the CDV process, the user-provided microtransaction details (i.e., credit and debit) is matched against the microtransactions posted by Yodlee.<br> For a successful verification of the account's ownership both microtransaction details should match.<br>The CDV process is currently supported only in the United States.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.VerificationApi()
verification_param = python_client.UpdateVerificationRequest() # UpdateVerificationRequest | verification information

try:
    # Verify Challenge Deposit
    api_response = api_instance.verify_challenge_deposit(verification_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->verify_challenge_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verification_param** | [**UpdateVerificationRequest**](UpdateVerificationRequest.md)| verification information | 

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

