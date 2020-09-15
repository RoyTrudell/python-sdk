# ProviderAccountDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated** | **str** | Indicate when the providerAccount is last updated successfully.&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET dataExtracts/userData&lt;/li&gt;&lt;/ul&gt; | [optional] 
**consent_id** | **int** | Consent Id generated through POST Consent.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; | 
**login_form** | [**list[LoginForm]**](LoginForm.md) | This entity gets returned in the response for only MFA based provider accounts during the add/update account polling process. This indicates that the MFA information is expected from the user to complete the process. This represents the structure of MFA form that is displayed to the user in the provider site.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**preferences** | [**ProviderAccountPreferences**](ProviderAccountPreferences.md) | User preference values for Auto-Refresh and DataExtracts Notification&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**created_date** | **str** | The date on when the provider account is created in the system.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**aggregation_source** | **str** | The source through which the providerAccount is added in the system.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET dataExtracts/userData&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**provider_id** | **int** | Unique identifier for the provider resource. This denotes the provider for which the provider account id is generated by the user.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET dataExtracts/userData&lt;/li&gt;&lt;/ul&gt; | [optional] 
**request_id** | **str** | Unique id generated to indicate the request.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**is_manual** | **bool** | Indicates whether account is a manual or aggregated provider account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET dataExtracts/userData&lt;/li&gt;&lt;/ul&gt; | [optional] 
**id** | **int** | Unique identifier for the provider account resource. This is created during account addition.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET dataExtracts/userData&lt;/li&gt;&lt;/ul&gt; | [optional] 
**dataset** | [**list[AccountDataset]**](AccountDataset.md) | Logical grouping of dataset attributes into datasets such as Basic Aggregation Data, Account Profile and Documents.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET dataExtracts/userData&lt;/li&gt;&lt;/ul&gt; | [optional] 
**status** | **str** | The status of last update attempted for the account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET dataExtracts/userData&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

