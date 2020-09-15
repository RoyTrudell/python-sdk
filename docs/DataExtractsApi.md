# python_client.DataExtractsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_extracts_events**](DataExtractsApi.md#get_data_extracts_events) | **GET** /dataExtracts/events | Get Events
[**get_data_extracts_user_data**](DataExtractsApi.md#get_data_extracts_user_data) | **GET** /dataExtracts/userData | Get userData


# **get_data_extracts_events**
> DataExtractsEventResponse get_data_extracts_events(event_name, from_date, to_date)

Get Events

The get extracts events service is used to learn about occurrences of data extract related events. This service currently supports only the DATA_UPDATES event.<br>Passing the event name as DATA_UPDATES provides information about users for whom data has been modified in the system for the specified time range. To learn more, please refer to the <a href=\"https://developer.yodlee.com/docs/api/1.1/DataExtracts\">dataExtracts</a> page.<br>You can retrieve data in increments of no more than 60 minutes over the period of the last 7 days from today's date.<br>This service is only invoked with either admin access token or a cobrand session.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.DataExtractsApi()
event_name = 'event_name_example' # str | Event Name
from_date = 'from_date_example' # str | From DateTime (YYYY-MM-DDThh:mm:ssZ)
to_date = 'to_date_example' # str | To DateTime (YYYY-MM-DDThh:mm:ssZ)

try:
    # Get Events
    api_response = api_instance.get_data_extracts_events(event_name, from_date, to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExtractsApi->get_data_extracts_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| Event Name | 
 **from_date** | **str**| From DateTime (YYYY-MM-DDThh:mm:ssZ) | 
 **to_date** | **str**| To DateTime (YYYY-MM-DDThh:mm:ssZ) | 

### Return type

[**DataExtractsEventResponse**](DataExtractsEventResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_extracts_user_data**
> DataExtractsUserDataResponse get_data_extracts_user_data(from_date, login_name, to_date)

Get userData

The get user data service is used to get a user's modified data for a particular period of time for accounts, transactions, holdings, and provider account information.<br>The time difference between fromDate and toDate fields cannot be more than 60 minutes.<br>By default, pagination is available in this API. If there are more transactions left to be retrieved, the response header provides a link to retrieve the next set of transactions.<br>For example, in the first response, along with the dataset, 500 transactions will be retrieved. The next set of 500 transactions can be retrieved by using the link in the response header.<br>This service is only invoked with either admin access token or a cobrand session.<br/>Refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/DataExtracts\">dataExtracts</a> page for more information.<b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.DataExtractsApi()
from_date = 'from_date_example' # str | From DateTime (YYYY-MM-DDThh:mm:ssZ)
login_name = 'login_name_example' # str | Login Name
to_date = 'to_date_example' # str | To DateTime (YYYY-MM-DDThh:mm:ssZ)

try:
    # Get userData
    api_response = api_instance.get_data_extracts_user_data(from_date, login_name, to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExtractsApi->get_data_extracts_user_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_date** | **str**| From DateTime (YYYY-MM-DDThh:mm:ssZ) | 
 **login_name** | **str**| Login Name | 
 **to_date** | **str**| To DateTime (YYYY-MM-DDThh:mm:ssZ) | 

### Return type

[**DataExtractsUserDataResponse**](DataExtractsUserDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

