# python_client.AccountsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manual_account**](AccountsApi.md#create_manual_account) | **POST** /accounts | Add Manual Account
[**delete_account**](AccountsApi.md#delete_account) | **DELETE** /accounts/{accountId} | Delete Account
[**evaluate_address**](AccountsApi.md#evaluate_address) | **POST** /accounts/evaluateAddress | Evaluate Address
[**get_account**](AccountsApi.md#get_account) | **GET** /accounts/{accountId} | Get Account Details
[**get_all_accounts**](AccountsApi.md#get_all_accounts) | **GET** /accounts | Get Accounts
[**get_associated_accounts**](AccountsApi.md#get_associated_accounts) | **GET** /accounts/associatedAccounts/{providerAccountId} | Associated Accounts
[**get_historical_balances**](AccountsApi.md#get_historical_balances) | **GET** /accounts/historicalBalances | Get Historical Balances
[**migrate_accounts**](AccountsApi.md#migrate_accounts) | **PUT** /accounts/migrateAccounts/{providerAccountId} | Migrate Accounts
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

# **evaluate_address**
> EvaluateAddressResponse evaluate_address(address_param)

Evaluate Address

Use this service to validate the address before adding the real estate account.<br>If the address is valid, the service will return the complete address information.<br>The response will contain multiple addresses if the user-provided input matches with multiple entries in the vendor database.<br>In the case of multiple matches, the user can select the appropriate address from the list and then invoke the add account service with the complete address.<br><b>Note:</b> Yodlee recommends to use this service before adding the real estate account to avoid failures.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AccountsApi()
address_param = python_client.EvaluateAddressRequest() # EvaluateAddressRequest | addressParam

try:
    # Evaluate Address
    api_response = api_instance.evaluate_address(address_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->evaluate_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_param** | [**EvaluateAddressRequest**](EvaluateAddressRequest.md)| addressParam | 

### Return type

[**EvaluateAddressResponse**](EvaluateAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> AccountResponse get_account(account_id, container, include=include)

Get Account Details

The get account details service provides detailed information of an account.<br><b>Note:</b><br>fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response.

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
include = 'include_example' # str | profile, holder, fullAccountNumber, fullAccountNumberList, paymentProfile, autoRefresh<br><b>Note:</b>fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response. (optional)

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
 **include** | **str**| profile, holder, fullAccountNumber, fullAccountNumberList, paymentProfile, autoRefresh&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response. | [optional] 

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

The get accounts service provides information about accounts added by the user.<br>By default, this service returns information for active and to be closed accounts.<br>If requestId is provided, the accounts that are updated in the context of the requestId will be provided in the response.<br><b>Note:</b><br>fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response.

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
include = 'include_example' # str | profile, holder, fullAccountNumber, fullAccountNumberList, paymentProfile, autoRefresh<br><b>Note:</b>fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response. (optional)
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
 **include** | **str**| profile, holder, fullAccountNumber, fullAccountNumberList, paymentProfile, autoRefresh&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response. | [optional] 
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

# **get_associated_accounts**
> AssociatedAccountsResponse get_associated_accounts(provider_account_id)

Associated Accounts

Yodlee classifies providers into credential-based aggregation and Open Banking (OB) providers.<br>This service is associated with the OB aggregation flow. As part of the OB solution, financial institutions may merge their subsidiaries and provide data as a single OB provider.<br>Before the OB solution, this data was aggregated with different provider IDs.<br>This service accepts the providerAccountId and returns all accounts of the associated providerAccounts that belong to the subsidiary of the financial institution.<br>This data should be displayed to the user to let them select the accounts that they wish to provide consent to share account data.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AccountsApi()
provider_account_id = 789 # int | providerAccountId

try:
    # Associated Accounts
    api_response = api_instance.get_associated_accounts(provider_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_associated_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_account_id** | **int**| providerAccountId | 

### Return type

[**AssociatedAccountsResponse**](AssociatedAccountsResponse.md)

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

# **migrate_accounts**
> AccountMigrationResponse migrate_accounts(provider_account_id)

Migrate Accounts

This service is associated with the open banking (OB) flow.<br>Before invoking this service, display all the associated accounts to the user by calling the GET /associatedAccounts API.<br>The migrate accounts API treats the user's consent acceptance to initiate account migration. Invoking this service indicates that the user has given the consent to access the associated account information from the financial institution.<br>If an existing provider supports bank, card, and loan accounts, and chose only to provide bank and card through OB APIs, a new providerAccountId for OB will be created.<br>The bank and card account information will be moved to the new providerAccountId. The loan account will be retained in the existing provider account.<br>This service returns the OB providerId and the OB providerAccountId. Note that, as part of this process, there is a possibility of one or more providerAccounts getting merged.<br>The update or delete actions will not be allowed for the providerAccounts involved in the migration process until the user completes the authorization on the OB provider.<br>The oauthMigrationEligibilityStatus attribute in the GET /accounts API response indicates the accounts included in the migration process.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.AccountsApi()
provider_account_id = 789 # int | providerAccountId

try:
    # Migrate Accounts
    api_response = api_instance.migrate_accounts(provider_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->migrate_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_account_id** | **int**| providerAccountId | 

### Return type

[**AccountMigrationResponse**](AccountMigrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

