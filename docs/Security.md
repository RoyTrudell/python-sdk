# Security

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_exchange_details** | [**list[StockExchangeDetail]**](StockExchangeDetail.md) | Securities exchange provide the securities information at the corresponding exchanges. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**issue_type_multiplier** | **float** | Price units corresponding to the security style. This is used to derive actual price of the security from market value.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**state_taxable** | **bool** | The state in which the security is taxed.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**call_date** | **str** | Next call date of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**cdsc_fund_flag** | **bool** | cdsc fund flag of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**cusip** | **str** | A CUSIP is a nine-character alphanumeric code that identifies a North American financial security for the purposes of facilitating clearing and settlement of trades.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**federal_taxable** | **bool** | Flag indicating federal taxable.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**s_and_p_rating** | **str** | Unique identifier for S&amp;P rating on Envestnet platform.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**share_class** | **str** | Share class of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**is_envestnet_dummy_security** | **bool** | Flag indicating a dummy security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**description** | **str** | The description (name) of the security. For example, Cisco Systems.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**minimum_purchase** | **int** | Minimum purchase of security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**type** | **str** | Indicates the type of security like stocks, mutual fund, etc. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**first_coupon_date** | **str** | First coupon date of security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**frequency** | **int** | Coupon Frequency.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**accrual_method** | **str** | The method in which interest is accrued or earned.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**income_currency** | **str** | ISO 4217 currency code indicating income currency of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**maturity_date** | **str** | Maturity date of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**call_price** | **float** | Next call price of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**id** | **int** | The unique identifier of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**issue_date** | **str** | Issue date of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**sector** | **str** | Identifier of the sector to which the security belongs to.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**agency_factor** | **float** | Agency factor of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**interest_rate** | **float** | The rate of interest paid annually, expressed as a percentage of the bond&#39;s par or face value.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**last_modified_date** | **str** | The last updated date of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**gics_sector** | **str** | GICS Sector is a categorization the S&amp;P assigns to all publically traded companies. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**closed_flag** | **bool** | &lt;b&gt;true&lt;/b&gt;:Closed for all investors , &lt;b&gt;false&lt;/b&gt;: Open to all investors.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**sedol** | **str** | The Stock Exchange Daily Official List (SEDOL) is a set of security identifiers used in the United Kingdom and Ireland for clearing purposes.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The SEDOL field is only applicable to the trade related transactions.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**sub_sector** | **str** | GICS sector ID to which the security belongs to.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**last_coupon_date** | **str** | Last coupon date of security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**is_synthetic_security** | **bool** | Indicates whether the security is a simulated security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**trade_currency_code** | **str** | ISO 4217 currency code indicating trading currency of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**is_dummy_security** | **bool** | Indicates whether the security is a dummy security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**moody_rating** | **str** | Unique identifier for Moody rating on Envestnet platform.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**style** | **str** | Classification of the style for the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**firm_eligible** | **str** | &lt;b&gt;1&lt;/b&gt;- indicates Eligible,&lt;b&gt;0&lt;/b&gt;- indicates firm is not eligible.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**fund_family** | **str** | Mutual Fund Family Name.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 
**isin** | **str** | The International Securities Identification Number (ISIN) is used worldwide to identify specific securities. It is equivalent to CUSIP for international markets.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


