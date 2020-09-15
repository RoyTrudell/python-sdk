# EnrichedTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** | The account&#39;s container.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**source_id** | **int** | A unique ID that the provider site has assigned to the transaction. The source ID is only available for the pre-populated accounts.&lt;br&gt;Pre-populated accounts are the accounts that the FI customers shares with Yodlee, so that the user does not have to add or aggregate those accounts. | [optional] 
**merchant_city** | **str** | City of the merchant.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] 
**high_level_category_id** | **int** | The high level category assigned to the transaction. The supported values are provided by the GET transactions/categories. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] 
**detail_category_id** | **int** | The id of the detail category that is assigned to the transaction. The supported values are provided by GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt; | [optional] 
**type** | **str** | The nature of the transaction, i.e., deposit, refund, payment, etc.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The transaction type field is available only for the United States, Canada, United Kingdom, and India based provider sites. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment&lt;br&gt; | [optional] 
**merchant_state** | **str** | State of the merchant.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] 
**transaction_id** | **int** | An unique identifier for the transaction. The combination of the id and account container are unique in the system. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] 
**merchant_name** | **str** | The name of the merchant.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] 
**merchant_id** | **str** | Identifier of the merchant.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt; | [optional] 
**simple_description** | **str** | The transaction description that appears at the FI site may not be self-explanatory, i.e., the source, purpose of the transaction may not be evident. Yodlee attempts to simplify and make the transaction meaningful to the consumer, and this simplified transaction description is provided in the simple description field.Note: The simple description field is available only in the United States, Canada, United Kingdom, and India.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, insurance, loan&lt;br&gt; | [optional] 
**sub_type** | **str** | The transaction subtype field provides a detailed transaction type. For example, purchase is a transaction type and the transaction subtype field indicates if the purchase was made using a debit or credit card.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The transaction subtype field is available only in the United States, Canada, United Kingdom, and India.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] 
**merchant_country** | **str** | Country of the merchant.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] 
**category_id** | **int** | The id of the category assigned to the transaction. This is the id field of the transaction category resource. The supported values are provided by the GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


