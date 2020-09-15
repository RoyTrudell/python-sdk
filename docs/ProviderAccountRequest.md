# ProviderAccountRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_id** | **int** | Consent Id generated for the request through POST Consent.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST Provider Account&lt;/li&gt;&lt;li&gt;PUT Provider Account&lt;/li&gt;&lt;/ul&gt; | [optional] 
**preferences** | [**ProviderAccountPreferences**](ProviderAccountPreferences.md) |  | [optional] 
**aggregation_source** | **str** |  | [optional] 
**field** | [**list[Field]**](Field.md) |  | 
**dataset_name** | **list[str]** |  | [optional] 
**dataset** | [**list[ProvidersDataset]**](ProvidersDataset.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


