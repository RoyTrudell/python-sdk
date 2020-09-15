# DerivedTransactionsSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_type** | **str** | Type of categories provided by transactions/categories service.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**category_summary** | [**list[DerivedCategorySummary]**](DerivedCategorySummary.md) | Summary of transaction amouts at category level.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] 
**credit_total** | [**Money**](Money.md) | The total of credit transactions for the category type.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] 
**links** | [**DerivedTransactionsLinks**](DerivedTransactionsLinks.md) | Link of the API services that corresponds to the value derivation.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] 
**debit_total** | [**Money**](Money.md) | The total of debit transactions for the category type.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


