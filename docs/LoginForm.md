# LoginForm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa_info_title** | **str** | The title for the MFA information demanded from the user.This is the title displayed in the provider site.This field is applicable for MFA form types only. &lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**help** | **str** | The help that can be displayed to the customer in the login form.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**forget_password_url** | **str** | The forget password URL of the provider site.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**form_type** | **str** | The type of the forms for which the user information is required.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**mfa_info_text** | **str** | The text displayed in the provider site while requesting the user&#39;s MFA information. This field is applicable for MFA form types only. &lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**login_help** | **str** | The help that can be displayed to the customer in the login form.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**mfa_timeout** | **int** | The amount of time before which the user is expected to provide MFA information. This field is applicable for MFA form types only. This would be an useful information that could be displayed to the users. &lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**id** | **int** | The identifier of the login form.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**row** | [**list[Row]**](Row.md) | This indicates one row in the form. The row will have one label. But it may have single or multiple fields.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


