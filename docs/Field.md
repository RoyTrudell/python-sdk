# Field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | The prefix string that has to be displayed before the field value.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**min_length** | **int** | The minimum length of the login form field.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**value_editable** | **str** | Indicates whether the field is editable or not.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**is_optional** | **bool** | Indicates if a field is an optional field or a mandatory field.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**suffix** | **str** | The suffix string that has to be displayed next to the field value.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**type** | **str** | This indicates the display type of the field. For example, text box, image, etc. &lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**is_value_provided** | **bool** | Indicates that the answer to the security question already exists in the Yodlee system.Persuading the user to provide the answer to the security question again during the edit-credential flow can be avoided.&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts?include&#x3D;questions&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}? include&#x3D;questions&lt;/li&gt;&lt;/ul&gt; | [optional] 
**size** | **int** |  | [optional] 
**name** | **str** | Name of the field.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**id** | **str** | Identifier for the field.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**value** | **str** | Value expected from the user for the field. This will be blank and is expected to be filled and sent back when submitting the login or MFA information.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**max_length** | **int** | The maximum length of the login form field.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**option** | [**list[Option]**](Option.md) | Provides the different values that are available for the user to choose. This field is applicable for drop-down or radio field types.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


