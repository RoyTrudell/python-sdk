# ProviderAccountPreferences

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_data_extracts_enabled** | **bool** | Indicates if the updates to the provider account should be part of the data extracts event notification or the data extract data retrieval service.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts?include&#x3D;preferences&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}?include&#x3D;preferences&lt;/li&gt;&lt;/ul&gt; | [optional] 
**linked_provider_account_id** | **int** | LinkedproviderAccountd is a providerAccountId linked by the user to the primary provider account. &lt;br&gt;LinkedProviderAccountId and the providerAccountId belongs to the same institution.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST Provider Account&lt;/li&gt;&lt;li&gt;PUT Provider Account&lt;/li&gt;&lt;li&gt;GET Provider Accounts&lt;/li&gt;&lt;/ul&gt; | [optional] 
**is_auto_refresh_enabled** | **bool** | Indicates if auto-refreshes have to be triggered for the provider account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts?include&#x3D;preferences&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}?include&#x3D;preferences&lt;/li&gt;&lt;/ul&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


