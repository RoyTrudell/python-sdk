# TransactionCategorizationRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_clauses** | [**list[RuleClause]**](RuleClause.md) | Details of rules. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt; | [optional] 
**user_defined_rule_id** | **int** | Unique identifier generated for every rule the user creates.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt; | [optional] 
**category_level_id** | **int** | The level of the category for which the rule is created.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, insurance, loan&lt;br&gt; | [optional] 
**transaction_categorisation_id** | **int** | Category id that is assigned to the transaction when the transaction matches the rule clause. This is the id field of the transaction category resource.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt; | [optional] 
**mem_id** | **int** | Unique identifier of the user.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt; | [optional] 
**rule_priority** | **int** | The order in which the rules get executed on transactions.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bill, creditCard, investment, insurance, loan&lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


