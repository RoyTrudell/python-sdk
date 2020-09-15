# Merchant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website** | **str** | The website of the merchant.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,loan&lt;br&gt; | [optional] 
**address** | [**AccountAddress**](AccountAddress.md) | The address of the merchant associated with the transaction is populated in the merchant address field.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The merchant address field is not available by default and customers will have to specifically request the merchant&#39;s address (that includes city, state, and ZIP of the merchant). The merchant address field is available only for merchants in the United States.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt; | [optional] 
**contact** | [**Contact**](Contact.md) | The merchant contact information like phone and email.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,loan&lt;br&gt; | [optional] 
**category_label** | **list[str]** | The business categories of the merchant.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) | The merchant geolocation coordinates like latitude and longitude.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,loan&lt;br&gt; | [optional] 
**name** | **str** | The name of the merchant.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] 
**id** | **str** | Identifier of the merchant.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] 
**source** | **str** | The source through which merchant information is retrieved.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


