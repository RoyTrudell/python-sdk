# python_client.EnrichDataApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**push_user_data**](EnrichDataApi.md#push_user_data) | **POST** /enrichData/userData | Push UserData


# **push_user_data**
> EnrichedTransactionResponse push_user_data(user_data=user_data)

Push UserData

<b>Push User Data </b><br>The data enrich API v1.1 allows customers to get the transactions enriched in real-time by feeding the data into the Yodlee Platform. To get the transactions enriched, it is necessary that users, accounts, and transactions are updated to the Yodlee Platform.<br>The following features are supported through the data enrich API:<ul><li>Add user</li><li>Add account</li><li>Update account</li><li>Add transactions</li><li>Update transactions</li></ul>Yodlee will enrich the transactions with the following information:<ul><li>Category</li><li>High Level Category</li><li>Detail Category</li><li>Simple description</li><li>Merchant details<ul><li>Name</li><li>Address</li></ul></li><li>Transaction type</li><li>Transaction subtype</li></ul>The data feed through the enrich APIs will be updated to the Yodlee Platform in real time. The updated accounts and transactions information can then be retrieved from the system using the respective Yodlee 1.1 APIs.<br><b> Implementation Notes </b><ul><li>Supported only through credential-based authentication mechanisms.</li><li>Customer must be TLS 1.2 compliant to integrate with the data enrich API.</li><li>Supported account types are savings, checking, and credit.</li><li>A maximum of 128 transactions can be passed to the API.</li><li>As the data enrich API is a premium offering and is priced per API call, Yodlee recommends not to call the API to update accounts and transactions.</li><li>The minimum required parameters to create account and transaction is accepted. The Yodlee data model supports more parameters than what is accepted in this API. Customers can make the rest of the parameters available during the auto-refresh process of the accounts.</li><li>Though few input parameters are optional, Yodlee recommends passing them as the account information will make complete sense to the consumers when it is displayed in the Yodlee applications or widgets.</li></ul>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.EnrichDataApi()
user_data = python_client.EnrichDataRequest() # EnrichDataRequest | Input for User Data (optional)

try:
    # Push UserData
    api_response = api_instance.push_user_data(user_data=user_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichDataApi->push_user_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_data** | [**EnrichDataRequest**](EnrichDataRequest.md)| Input for User Data | [optional] 

### Return type

[**EnrichedTransactionResponse**](EnrichedTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

