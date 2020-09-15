# python_client.AccountsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manual_account**](AccountsApi.md#create_manual_account) | **POST** /accounts | Add Manual Account
[**delete_account**](AccountsApi.md#delete_account) | **DELETE** /accounts/{accountId} | Delete Account
[**get_account**](AccountsApi.md#get_account) | **GET** /accounts/{accountId} | Get Account Details
[**get_all_accounts**](AccountsApi.md#get_all_accounts) | **GET** /accounts | Get Accounts
[**get_historical_balances**](AccountsApi.md#get_historical_balances) | **GET** /accounts/historicalBalances | Get Historical Balances
[**update_account**](AccountsApi.md#update_account) | **PUT** /accounts/{accountId} | Update Account


# **create_manual_account**
> CreatedAccountResponse create_manual_account(account_param)

Add Manual Account

The add account service is used to add manual accounts.<br>The response of add account service includes the account name , account number and Yodlee generated account id.<br>All manual accounts added will be included as part of networth calculation by default.<br>Add manual account support is available for bank, card, investment, insurance, loan and bills container only.<br><b>Note:</b> A real estate account addition is only supported for SYSTEM and MANUAL valuation type.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AccountsApi()
account_param = python_client.CreateAccountRequest() # CreateAccountRequest | accountParam

try:
    # Add Manual Account
    api_response = api_instance.create_manual_account(account_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_manual_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_param** | [**CreateAccountRequest**](CreateAccountRequest.md)| accountParam | 

### Return type

[**CreatedAccountResponse**](CreatedAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> delete_account(account_id)

Delete Account

The delete account service allows an account to be deleted.<br>This service does not return a response. The HTTP response code is 204 (Success with no content).<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AccountsApi()
account_id = 789 # int | accountId

try:
    # Delete Account
    api_instance.delete_account(account_id)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> AccountResponse get_account(account_id, container, include=include)

Get Account Details

The get account details service provides detailed information of an account.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AccountsApi()
account_id = 789 # int | accountId
container = 'container_example' # str | bank/creditCard/investment/insurance/loan/reward/bill/realEstate/otherAssets/otherLiabilities
include = 'include_example' # str | profile, holder, fullAccountNumber, paymentProfile, autoRefresh (optional)

try:
    # Get Account Details
    api_response = api_instance.get_account(account_id, container, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **container** | **str**| bank/creditCard/investment/insurance/loan/reward/bill/realEstate/otherAssets/otherLiabilities | 
 **include** | **str**| profile, holder, fullAccountNumber, paymentProfile, autoRefresh | [optional] 

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accounts**
> AccountResponse get_all_accounts(account_id=account_id, container=container, include=include, provider_account_id=provider_account_id, request_id=request_id, status=status)

Get Accounts

The get accounts service provides information about accounts added by the user.<br>By default, this service returns information for active and to be closed accounts.<br>If requestId is provided, the accounts that are updated in the context of the requestId will be provided in the response.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AccountsApi()
account_id = 'account_id_example' # str | Comma separated accountIds. (optional)
container = 'container_example' # str | bank/creditCard/investment/insurance/loan/reward/bill/realEstate/otherAssets/otherLiabilities (optional)
include = 'include_example' # str | profile, holder, fullAccountNumber, paymentProfile, autoRefresh (optional)
provider_account_id = 'provider_account_id_example' # str | Comma separated providerAccountIds. (optional)
request_id = 'request_id_example' # str | The unique identifier that returns contextual data (optional)
status = 'status_example' # str | ACTIVE,INACTIVE,TO_BE_CLOSED,CLOSED (optional)

try:
    # Get Accounts
    api_response = api_instance.get_all_accounts(account_id=account_id, container=container, include=include, provider_account_id=provider_account_id, request_id=request_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_all_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Comma separated accountIds. | [optional] 
 **container** | **str**| bank/creditCard/investment/insurance/loan/reward/bill/realEstate/otherAssets/otherLiabilities | [optional] 
 **include** | **str**| profile, holder, fullAccountNumber, paymentProfile, autoRefresh | [optional] 
 **provider_account_id** | **str**| Comma separated providerAccountIds. | [optional] 
 **request_id** | **str**| The unique identifier that returns contextual data | [optional] 
 **status** | **str**| ACTIVE,INACTIVE,TO_BE_CLOSED,CLOSED | [optional] 

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_balances**
> AccountHistoricalBalancesResponse get_historical_balances(account_id=account_id, from_date=from_date, include_cf=include_cf, interval=interval, skip=skip, to_date=to_date, top=top)

Get Historical Balances

The historical balances service is used to retrieve the historical balances for an account or a user.<br>Historical balances are daily (D), weekly (W), and monthly (M). <br>The interval input should be passed as D, W, and M to retrieve the desired historical balances. The default interval is daily (D). <br>When no account id is provided, historical balances of the accounts that are active, to be closed, and closed are provided in the response. <br>If the fromDate and toDate are not passed, the last 90 days of data will be provided. <br>The fromDate and toDate should be passed in the YYYY-MM-DD format. <br>The date field in the response denotes the date for which the balance is requested.<br>includeCF needs to be sent as true if the customer wants to return carried forward balances <br>for a date when the data is not available. <br>asofDate field in the response denotes the date as of which the balance was updated for that account.<br>When there is no balance available for a requested date and if includeCF is sent as true, the previous <br>date for which the balance is available is provided in the response. When there is no previous <br>balance available, no data will be sent. <br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AccountsApi()
account_id = 'account_id_example' # str | accountId (optional)
from_date = 'from_date_example' # str | from date for balance retrieval (YYYY-MM-DD) (optional)
include_cf = true # bool | Consider carry forward logic for missing balances (optional)
interval = 'interval_example' # str | D-daily, W-weekly or M-monthly (optional)
skip = 56 # int | skip (Min 0) (optional)
to_date = 'to_date_example' # str | toDate for balance retrieval (YYYY-MM-DD) (optional)
top = 56 # int | top (Max 500) (optional)

try:
    # Get Historical Balances
    api_response = api_instance.get_historical_balances(account_id=account_id, from_date=from_date, include_cf=include_cf, interval=interval, skip=skip, to_date=to_date, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_historical_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | [optional] 
 **from_date** | **str**| from date for balance retrieval (YYYY-MM-DD) | [optional] 
 **include_cf** | **bool**| Consider carry forward logic for missing balances | [optional] 
 **interval** | **str**| D-daily, W-weekly or M-monthly | [optional] 
 **skip** | **int**| skip (Min 0) | [optional] 
 **to_date** | **str**| toDate for balance retrieval (YYYY-MM-DD) | [optional] 
 **top** | **int**| top (Max 500) | [optional] 

### Return type

[**AccountHistoricalBalancesResponse**](AccountHistoricalBalancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> update_account(account_id, account_request)

Update Account

The update account service is used to update manual and aggregated accounts.<br>The HTTP response code is 204 (Success without content).<br>Update manual account support is available for bank, card, investment, insurance, loan, bills, otherAssets, otherLiabilities and realEstate containers only.<br><b>Note:</b> A real estate account update is only supported for SYSTEM and MANUAL valuation type.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AccountsApi()
account_id = 789 # int | accountId
account_request = python_client.UpdateAccountRequest() # UpdateAccountRequest | accountRequest

try:
    # Update Account
    api_instance.update_account(account_id, account_request)
except ApiException as e:
    print("Exception when calling AccountsApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **account_request** | [**UpdateAccountRequest**](UpdateAccountRequest.md)| accountRequest | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

