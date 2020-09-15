# CreateConsent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_access_frequency** | **str** | Data Access Frequency explains the number of times that this consent can be used.&lt;br&gt; Otherwise called as consent frequency type. | [optional] 
**title_body** | **str** | Description for the title. | 
**consent_id** | **int** | Consent Id generated through POST Consent. | 
**provider_id** | **int** | Provider Id for which the consent needs to be generated. | 
**consent_status** | **str** | Status of the consent. | 
**scope** | [**list[Scope]**](Scope.md) | Scope describes about the consent permissions and their purpose. | 
**title** | **str** | Title for the consent form. | 
**expiration_date** | **str** | Consent expiry date. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


