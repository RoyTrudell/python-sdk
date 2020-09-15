# TransactionCategory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**high_level_category_name** | **str** | The name of the high level category. A group of similar transaction categories are clubbed together to form a high-level category.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt; | [optional] 
**high_level_category_id** | **int** | The unique identifier of the high level category.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt; | [optional] 
**detail_category** | [**list[DetailCategory]**](DetailCategory.md) | Entity that provides detail category attributes&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt; | [optional] 
**id** | **int** | Unique identifier of the category.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt; | [optional] 
**source** | **str** | Source used to identify whether the transaction category is user defined category or system created category.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**category** | **str** | The name of the category.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: Transaction categorization is one of the core features offered by Yodlee and the categories are assigned to the transactions by the system. Transactions can be clubbed together by the category that is assigned to them.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt; | [optional] 
**classification** | **str** | Category Classification.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**type** | **str** | Transaction categories and high-level categories are further mapped to five transaction category types. Customers, based on their needs can either use the transaction categories, the high-level categories, or the transaction category types. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


