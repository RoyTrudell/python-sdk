# EnrichDataTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** | The account&#39;s container.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**source_id** | **str** | A unique ID that the provider site has assigned to the transaction. The source ID is only available for the pre-populated accounts.&lt;br&gt;Pre-populated accounts are the accounts that the FI customers shares with Yodlee, so that the user does not have to add or aggregate those accounts. | [optional] 
**amount** | [**Money**](Money.md) | The amount of the transaction as it appears at the FI site. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt; | [optional] 
**description** | [**Description**](Description.md) | Description details&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt; | [optional] 
**post_date** | **str** | The date on which the transaction is posted to the account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt; | [optional] 
**user_login_name** | **str** | The loginName of the User.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt; | [optional] 
**account_number** | **str** | The account number as it appears on the site. (The POST accounts service response return this field as number)&lt;br&gt;&lt;b&gt;Additional Details&lt;/b&gt;:&lt;b&gt; Bank/ Loan/ Insurance/ Investment/Bill&lt;/b&gt;:&lt;br&gt; The account number for the bank account as it appears at the site.&lt;br&gt;&lt;b&gt;Credit Card&lt;/b&gt;: The account number of the card account as it appears at the site,&lt;br&gt;i.e., the card number.The account number can be full or partial based on how it is displayed in the account summary page of the site.In most cases, the site does not display the full account number in the account summary page and additional navigation is required to aggregate it.&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: All Containers&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Both &lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;br&gt;&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;POST accounts&lt;/li&gt;&lt;li&gt;POST dataExtracts/userData&lt;/li&gt;&lt;li&gt;POST dataEnrich/userData&lt;/li&gt;&lt;/ul&gt; | [optional] 
**transaction_date** | **str** | The date the transaction happens in the account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt; | [optional] 
**base_type** | **str** | Indicates if the transaction appears as a debit or a credit transaction in the account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**status** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


