# python_client.HoldingsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_classification_list**](HoldingsApi.md#get_asset_classification_list) | **GET** /holdings/assetClassificationList | Get Asset Classification List
[**get_holding_type_list**](HoldingsApi.md#get_holding_type_list) | **GET** /holdings/holdingTypeList | Get Holding Type List
[**get_holdings**](HoldingsApi.md#get_holdings) | **GET** /holdings | Get Holdings
[**get_securities**](HoldingsApi.md#get_securities) | **GET** /holdings/securities | Get Security Details


# **get_asset_classification_list**
> HoldingAssetClassificationListResponse get_asset_classification_list()

Get Asset Classification List

The get asset classifications list service is used to get the supported asset classifications. <br>The response includes different classification types like assetClass, country, sector, style, etc., <br>and the values corresponding to each type.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.HoldingsApi()

try:
    # Get Asset Classification List
    api_response = api_instance.get_asset_classification_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoldingsApi->get_asset_classification_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HoldingAssetClassificationListResponse**](HoldingAssetClassificationListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holding_type_list**
> HoldingTypeListResponse get_holding_type_list()

Get Holding Type List

The get holding types list service is used to get the supported holding types.<br>The response includes different holding types such as future, moneyMarketFund, stock, etc.<br>and it returns the supported holding types <br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.HoldingsApi()

try:
    # Get Holding Type List
    api_response = api_instance.get_holding_type_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoldingsApi->get_holding_type_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HoldingTypeListResponse**](HoldingTypeListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holdings**
> HoldingResponse get_holdings(account_id=account_id, asset_classification_classification_type=asset_classification_classification_type, classification_value=classification_value, include=include, provider_account_id=provider_account_id)

Get Holdings

The get holdings service is used to get the list of holdings of a user.<br>Supported holding types can be employeeStockOption, <br>moneyMarketFund, bond, etc. and is obtained using get holding type list service. <br>Asset classifications for the holdings need to be requested through the \"include\" parameter.<br>Asset classification information for holdings are not available by default, as it is a premium feature.<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.HoldingsApi()
account_id = 'account_id_example' # str | Comma separated accountId (optional)
asset_classification_classification_type = 'asset_classification_classification_type_example' # str | e.g. Country, Sector, etc. (optional)
classification_value = 'classification_value_example' # str | e.g. US (optional)
include = 'include_example' # str | assetClassification (optional)
provider_account_id = 'provider_account_id_example' # str | providerAccountId (optional)

try:
    # Get Holdings
    api_response = api_instance.get_holdings(account_id=account_id, asset_classification_classification_type=asset_classification_classification_type, classification_value=classification_value, include=include, provider_account_id=provider_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoldingsApi->get_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Comma separated accountId | [optional] 
 **asset_classification_classification_type** | **str**| e.g. Country, Sector, etc. | [optional] 
 **classification_value** | **str**| e.g. US | [optional] 
 **include** | **str**| assetClassification | [optional] 
 **provider_account_id** | **str**| providerAccountId | [optional] 

### Return type

[**HoldingResponse**](HoldingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_securities**
> HoldingSecuritiesResponse get_securities(holding_id=holding_id)

Get Security Details

The get security details service is used to get all the security information for the holdings<br>

### Example
```python
from __future__ import print_function
import time
import python_client
from python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_client.HoldingsApi()
holding_id = 'holding_id_example' # str | Comma separated holdingId (optional)

try:
    # Get Security Details
    api_response = api_instance.get_securities(holding_id=holding_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoldingsApi->get_securities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holding_id** | **str**| Comma separated holdingId | [optional] 

### Return type

[**HoldingSecuritiesResponse**](HoldingSecuritiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

