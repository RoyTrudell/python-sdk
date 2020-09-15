# python_client.DerivedApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_holding_summary**](DerivedApi.md#get_holding_summary) | **GET** /derived/holdingSummary | Get Holding Summary
[**get_networth**](DerivedApi.md#get_networth) | **GET** /derived/networth | Get Networth Summary
[**get_transaction_summary**](DerivedApi.md#get_transaction_summary) | **GET** /derived/transactionSummary | Get Transaction Summary


# **get_holding_summary**
> DerivedHoldingSummaryResponse get_holding_summary(account_ids=account_ids, classification_type=classification_type, include=include)

Get Holding Summary

The get holding summary service is used to get the summary of asset classifications for the user.<br>By default, accounts with status as ACTIVE and TO BE CLOSED will be considered.<br>If the include parameter value is passed as details then a summary with holdings and account information is returned.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.DerivedApi()
account_ids = 'account_ids_example' # str | Comma separated accountIds (optional)
classification_type = 'classification_type_example' # str | e.g. Country, Sector, etc. (optional)
include = 'include_example' # str | details (optional)

try:
    # Get Holding Summary
    api_response = api_instance.get_holding_summary(account_ids=account_ids, classification_type=classification_type, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedApi->get_holding_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | **str**| Comma separated accountIds | [optional] 
 **classification_type** | **str**| e.g. Country, Sector, etc. | [optional] 
 **include** | **str**| details | [optional] 

### Return type

[**DerivedHoldingSummaryResponse**](DerivedHoldingSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_networth**
> DerivedNetworthResponse get_networth(account_ids=account_ids, from_date=from_date, include=include, interval=interval, skip=skip, to_date=to_date, top=top)

Get Networth Summary

The get networth service is used to get the networth for the user.<br>If the include parameter value is passed as details then networth with historical balances is returned. <br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.DerivedApi()
account_ids = 'account_ids_example' # str | comma separated accountIds (optional)
from_date = 'from_date_example' # str | from date for balance retrieval (YYYY-MM-DD) (optional)
include = 'include_example' # str | details (optional)
interval = 'interval_example' # str | D-daily, W-weekly or M-monthly (optional)
skip = 56 # int | skip (Min 0) (optional)
to_date = 'to_date_example' # str | toDate for balance retrieval (YYYY-MM-DD) (optional)
top = 56 # int | top (Max 500) (optional)

try:
    # Get Networth Summary
    api_response = api_instance.get_networth(account_ids=account_ids, from_date=from_date, include=include, interval=interval, skip=skip, to_date=to_date, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedApi->get_networth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | **str**| comma separated accountIds | [optional] 
 **from_date** | **str**| from date for balance retrieval (YYYY-MM-DD) | [optional] 
 **include** | **str**| details | [optional] 
 **interval** | **str**| D-daily, W-weekly or M-monthly | [optional] 
 **skip** | **int**| skip (Min 0) | [optional] 
 **to_date** | **str**| toDate for balance retrieval (YYYY-MM-DD) | [optional] 
 **top** | **int**| top (Max 500) | [optional] 

### Return type

[**DerivedNetworthResponse**](DerivedNetworthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_summary**
> DerivedTransactionSummaryResponse get_transaction_summary(group_by, account_id=account_id, category_id=category_id, category_type=category_type, from_date=from_date, include=include, include_user_category=include_user_category, interval=interval, to_date=to_date)

Get Transaction Summary

The transaction summary service provides the summary values of transactions for the given date range by category type, high-level categories, or system-defined categories.<br><br>Yodlee has the transaction data stored for a day, month, year and week per category as per the availability of user's data. If the include parameter value is passed as details, then summary details will be returned depending on the interval passed-monthly is the default.<br><br><b>Notes:</b><br>1.Details can be requested for only one system-defined category<br>2.Passing categoryType is mandatory except when the groupBy value is CATEGORY_TYPE<br>3.Dates will not be respected for monthly, yearly, and weekly details<br>4.When monthly details are requested, only the fromDate and toDate month will be respected<br>5.When yearly details are requested, only the fromDate and toDate year will be respected<br>6.For weekly data points, details will be provided for every Sunday date available within the fromDate and toDate<br>7.This service supports the localization feature and accepts locale as a header parameter<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.DerivedApi()
group_by = 'group_by_example' # str | CATEGORY_TYPE, HIGH_LEVEL_CATEGORY or CATEGORY
account_id = 'account_id_example' # str | comma separated account Ids (optional)
category_id = 'category_id_example' # str | comma separated categoryIds (optional)
category_type = 'category_type_example' # str | INCOME, EXPENSE, TRANSFER, UNCATEGORIZE or DEFERRED_COMPENSATION (optional)
from_date = 'from_date_example' # str | YYYY-MM-DD format (optional)
include = 'include_example' # str | details (optional)
include_user_category = true # bool | TRUE/FALSE (optional)
interval = 'interval_example' # str | D-daily, W-weekly, M-mothly or Y-yearly (optional)
to_date = 'to_date_example' # str | YYYY-MM-DD format (optional)

try:
    # Get Transaction Summary
    api_response = api_instance.get_transaction_summary(group_by, account_id=account_id, category_id=category_id, category_type=category_type, from_date=from_date, include=include, include_user_category=include_user_category, interval=interval, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedApi->get_transaction_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_by** | **str**| CATEGORY_TYPE, HIGH_LEVEL_CATEGORY or CATEGORY | 
 **account_id** | **str**| comma separated account Ids | [optional] 
 **category_id** | **str**| comma separated categoryIds | [optional] 
 **category_type** | **str**| INCOME, EXPENSE, TRANSFER, UNCATEGORIZE or DEFERRED_COMPENSATION | [optional] 
 **from_date** | **str**| YYYY-MM-DD format | [optional] 
 **include** | **str**| details | [optional] 
 **include_user_category** | **bool**| TRUE/FALSE | [optional] 
 **interval** | **str**| D-daily, W-weekly, M-mothly or Y-yearly | [optional] 
 **to_date** | **str**| YYYY-MM-DD format | [optional] 

### Return type

[**DerivedTransactionSummaryResponse**](DerivedTransactionSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

