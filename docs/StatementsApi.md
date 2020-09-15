# python_client.StatementsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statements**](StatementsApi.md#get_statements) | **GET** /statements | Get Statements


# **get_statements**
> StatementResponse get_statements(account_id=account_id, container=container, from_date=from_date, is_latest=is_latest, status=status)

Get Statements

The statements service is used to get the list of statement related information. <br>By default, all the latest statements of active and to be closed accounts are retrieved for the user. <br>Certain sites do not have both a statement date and a due date. When a fromDate is passed as an <br>input, all the statements that have the due date on or after the passed date are retrieved. <br>For sites that do not have the due date, statements that have the statement date <br>on or after the passed date are retrieved. <br>The default value of \"isLatest\" is true. To retrieve historical statements isLatest needs to be set to false.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.StatementsApi()
account_id = 'account_id_example' # str | accountId (optional)
container = 'container_example' # str | creditCard/loan/bill/insurance (optional)
from_date = 'from_date_example' # str | from date for statement retrieval (YYYY-MM-DD) (optional)
is_latest = 'is_latest_example' # str | isLatest (true/false) (optional)
status = 'status_example' # str | ACTIVE,TO_BE_CLOSED,CLOSED (optional)

try:
    # Get Statements
    api_response = api_instance.get_statements(account_id=account_id, container=container, from_date=from_date, is_latest=is_latest, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->get_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | [optional] 
 **container** | **str**| creditCard/loan/bill/insurance | [optional] 
 **from_date** | **str**| from date for statement retrieval (YYYY-MM-DD) | [optional] 
 **is_latest** | **str**| isLatest (true/false) | [optional] 
 **status** | **str**| ACTIVE,TO_BE_CLOSED,CLOSED | [optional] 

### Return type

[**StatementResponse**](StatementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

