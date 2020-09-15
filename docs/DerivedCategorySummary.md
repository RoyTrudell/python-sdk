# DerivedCategorySummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_total** | [**Money**](Money.md) | The total of credit transactions for the category.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] 
**details** | [**list[DerivedCategorySummaryDetails]**](DerivedCategorySummaryDetails.md) | Credit and debit summary per date.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] 
**links** | [**DerivedTransactionsLinks**](DerivedTransactionsLinks.md) | Link of the API services that corresponds to the value derivation.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] 
**category_name** | **str** | The name of the category.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] 
**category_id** | **int** | Id of the category. This information is provided by transactions/categories service.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] 
**debit_total** | [**Money**](Money.md) | The total of debit transactions for the category.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


