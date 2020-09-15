# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferences** | [**UserResponsePreferences**](UserResponsePreferences.md) | Preferences of the user to be respected in the data provided through various API services.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST user/samlLogin&lt;/li&gt;&lt;li&gt;POST user/register&lt;/li&gt;&lt;li&gt;GET user&lt;/li&gt;&lt;/ul&gt; | [optional] 
**session** | [**UserSession**](UserSession.md) | Session token of the user using which other services are invoked in the system.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST user/samlLogin&lt;/li&gt;&lt;li&gt;POST user/register&lt;/li&gt;&lt;/ul&gt; | [optional] 
**login_name** | **str** | The login name of the user used for authentication.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST user/register&lt;/li&gt;&lt;li&gt;GET user&lt;/li&gt;&lt;/ul&gt; | [optional] 
**name** | [**Name**](Name.md) | First, middle and last names of the user.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST user/samlLogin&lt;/li&gt;&lt;li&gt;POST user/register&lt;/li&gt;&lt;li&gt;GET user&lt;/li&gt;&lt;/ul&gt; | [optional] 
**id** | **int** | The unique identifier of a consumer/user in Yodlee system for whom the API services would be accessed for.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST user/samlLogin&lt;/li&gt;&lt;li&gt;POST user/register&lt;/li&gt;&lt;li&gt;GET user&lt;/li&gt;&lt;/ul&gt; | [optional] 
**role_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


