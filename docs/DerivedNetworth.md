# DerivedNetworth

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_date** | **str** | The date as of when the networth information is provided.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, creditcard, investment, insurance, realEstate, loan&lt;br&gt; | [optional] 
**liability** | [**Money**](Money.md) | The liability amount that the user owes.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, creditcard, investment, insurance, realEstate, loan&lt;br&gt; | [optional] 
**historical_balances** | [**list[DerivedNetworthHistoricalBalance]**](DerivedNetworthHistoricalBalance.md) | Balances of the accounts over the period of time.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, creditcard, investment, insurance, realEstate, loan&lt;br&gt; | [optional] 
**networth** | [**Money**](Money.md) | Networth of the user.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, creditcard, investment, insurance, realEstate, loan&lt;br&gt; | [optional] 
**asset** | [**Money**](Money.md) | The asset value that the user owns.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, creditcard, investment, insurance, realEstate, loan&lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


