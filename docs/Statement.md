# Statement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apr** | **float** | The APR applied to the balance on the credit card account, as available in the statement.&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; In case of variable APR, the APR available on the statement might differ from the APR available at the account-level.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**cash_apr** | **float** | The APR applicable to cash withdrawals on the credit card account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**billing_period_start** | **str** | The start date of the statement period.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**due_date** | **str** | The date by when the minimum payment is due to be paid.&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; The due date that appears in the statement may differ from the due date at the account-level.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**interest_amount** | [**Money**](Money.md) | The interest amount that is part of the amount due or the payment amount.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**statement_date** | **str** | The date on which the statement is generated.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**cash_advance** | [**Money**](Money.md) | Cash Advance is the amount that is withdrawn from credit card over the counter or from an ATM up to the available credit/cash limit.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**billing_period_end** | **str** | The end date of the statement period.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**principal_amount** | [**Money**](Money.md) | The principal amount that is part of the amount due or the payment amount.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**loan_balance** | [**Money**](Money.md) | The outstanding principal balance on the loan account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**amount_due** | [**Money**](Money.md) | The total amount owed at the end of the billing period.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**account_id** | **int** | Account to which the statement belongs to.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**last_updated** | **str** | The date when the account was last updated by Yodlee.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**is_latest** | **bool** | The field is set to true if the statement is the latest generated statement.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**minimum_payment** | [**Money**](Money.md) | &lt;b&gt;Credit Card:&lt;/b&gt; The minimum amount that the consumer has to pay every month on the credit card account. Data provides an up-to-date information to the consumer.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**last_payment_date** | **str** | The date on which the last payment was done during the billing cycle.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**last_payment_amount** | [**Money**](Money.md) | The last payment done for the previous billing cycle in the current statement period.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**id** | **int** | Unique identifier for the statement.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 
**new_charges** | [**Money**](Money.md) | New charges on the statement (i.e., charges since last statement to end of the billing period). Applicable to line of credit loan type.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bill, loan, insurance&lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


