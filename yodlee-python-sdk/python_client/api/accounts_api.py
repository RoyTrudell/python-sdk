# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs, using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. You can generate a client SDK for Python, Java, javascript, PHP or other languages according to your development needs. For more details about our APIs themselves, please refer to https://developer.yodlee.com/Yodlee_API/.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from python_client.api_client import ApiClient


class AccountsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_manual_account(self, account_param, **kwargs):  # noqa: E501
        """Add Manual Account  # noqa: E501

        The add account service is used to add manual accounts.<br>The response of add account service includes the account name , account number and Yodlee generated account id.<br>All manual accounts added will be included as part of networth calculation by default.<br>Add manual account support is available for bank, card, investment, insurance, loan and bills container only.<br><b>Note:</b> A real estate account addition is only supported for SYSTEM and MANUAL valuation type.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_manual_account(account_param, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateAccountRequest account_param: accountParam (required)
        :return: CreatedAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_manual_account_with_http_info(account_param, **kwargs)  # noqa: E501
        else:
            (data) = self.create_manual_account_with_http_info(account_param, **kwargs)  # noqa: E501
            return data

    def create_manual_account_with_http_info(self, account_param, **kwargs):  # noqa: E501
        """Add Manual Account  # noqa: E501

        The add account service is used to add manual accounts.<br>The response of add account service includes the account name , account number and Yodlee generated account id.<br>All manual accounts added will be included as part of networth calculation by default.<br>Add manual account support is available for bank, card, investment, insurance, loan and bills container only.<br><b>Note:</b> A real estate account addition is only supported for SYSTEM and MANUAL valuation type.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_manual_account_with_http_info(account_param, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateAccountRequest account_param: accountParam (required)
        :return: CreatedAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_param']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_manual_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_param' is set
        if ('account_param' not in params or
                params['account_param'] is None):
            raise ValueError("Missing the required parameter `account_param` when calling `create_manual_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account_param' in params:
            body_params = params['account_param']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/accounts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreatedAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_account(self, account_id, **kwargs):  # noqa: E501
        """Delete Account  # noqa: E501

        The delete account service allows an account to be deleted.<br>This service does not return a response. The HTTP response code is 204 (Success with no content).<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_account(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: accountId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_account_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_account_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def delete_account_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """Delete Account  # noqa: E501

        The delete account service allows an account to be deleted.<br>This service does not return a response. The HTTP response code is 204 (Success with no content).<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_account_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: accountId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_account(self, account_id, container, **kwargs):  # noqa: E501
        """Get Account Details  # noqa: E501

        The get account details service provides detailed information of an account.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account(account_id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: accountId (required)
        :param str container: bank/creditCard/investment/insurance/loan/reward/bill/realEstate/otherAssets/otherLiabilities (required)
        :param str include: profile, holder, fullAccountNumber, paymentProfile, autoRefresh
        :return: AccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_account_with_http_info(account_id, container, **kwargs)  # noqa: E501
        else:
            (data) = self.get_account_with_http_info(account_id, container, **kwargs)  # noqa: E501
            return data

    def get_account_with_http_info(self, account_id, container, **kwargs):  # noqa: E501
        """Get Account Details  # noqa: E501

        The get account details service provides detailed information of an account.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_with_http_info(account_id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: accountId (required)
        :param str container: bank/creditCard/investment/insurance/loan/reward/bill/realEstate/otherAssets/otherLiabilities (required)
        :param str include: profile, holder, fullAccountNumber, paymentProfile, autoRefresh
        :return: AccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'container', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_account`")  # noqa: E501
        # verify the required parameter 'container' is set
        if ('container' not in params or
                params['container'] is None):
            raise ValueError("Missing the required parameter `container` when calling `get_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []
        if 'container' in params:
            query_params.append(('container', params['container']))  # noqa: E501
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_accounts(self, **kwargs):  # noqa: E501
        """Get Accounts  # noqa: E501

        The get accounts service provides information about accounts added by the user.<br>By default, this service returns information for active and to be closed accounts.<br>If requestId is provided, the accounts that are updated in the context of the requestId will be provided in the response.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_accounts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Comma separated accountIds.
        :param str container: bank/creditCard/investment/insurance/loan/reward/bill/realEstate/otherAssets/otherLiabilities
        :param str include: profile, holder, fullAccountNumber, paymentProfile, autoRefresh
        :param str provider_account_id: Comma separated providerAccountIds.
        :param str request_id: The unique identifier that returns contextual data
        :param str status: ACTIVE,INACTIVE,TO_BE_CLOSED,CLOSED
        :return: AccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_accounts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_accounts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_accounts_with_http_info(self, **kwargs):  # noqa: E501
        """Get Accounts  # noqa: E501

        The get accounts service provides information about accounts added by the user.<br>By default, this service returns information for active and to be closed accounts.<br>If requestId is provided, the accounts that are updated in the context of the requestId will be provided in the response.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_accounts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Comma separated accountIds.
        :param str container: bank/creditCard/investment/insurance/loan/reward/bill/realEstate/otherAssets/otherLiabilities
        :param str include: profile, holder, fullAccountNumber, paymentProfile, autoRefresh
        :param str provider_account_id: Comma separated providerAccountIds.
        :param str request_id: The unique identifier that returns contextual data
        :param str status: ACTIVE,INACTIVE,TO_BE_CLOSED,CLOSED
        :return: AccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'container', 'include', 'provider_account_id', 'request_id', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_accounts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'container' in params:
            query_params.append(('container', params['container']))  # noqa: E501
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
        if 'provider_account_id' in params:
            query_params.append(('providerAccountId', params['provider_account_id']))  # noqa: E501
        if 'request_id' in params:
            query_params.append(('requestId', params['request_id']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_historical_balances(self, **kwargs):  # noqa: E501
        """Get Historical Balances  # noqa: E501

        The historical balances service is used to retrieve the historical balances for an account or a user.<br>Historical balances are daily (D), weekly (W), and monthly (M). <br>The interval input should be passed as D, W, and M to retrieve the desired historical balances. The default interval is daily (D). <br>When no account id is provided, historical balances of the accounts that are active, to be closed, and closed are provided in the response. <br>If the fromDate and toDate are not passed, the last 90 days of data will be provided. <br>The fromDate and toDate should be passed in the YYYY-MM-DD format. <br>The date field in the response denotes the date for which the balance is requested.<br>includeCF needs to be sent as true if the customer wants to return carried forward balances <br>for a date when the data is not available. <br>asofDate field in the response denotes the date as of which the balance was updated for that account.<br>When there is no balance available for a requested date and if includeCF is sent as true, the previous <br>date for which the balance is available is provided in the response. When there is no previous <br>balance available, no data will be sent. <br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_historical_balances(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: accountId
        :param str from_date: from date for balance retrieval (YYYY-MM-DD)
        :param bool include_cf: Consider carry forward logic for missing balances
        :param str interval: D-daily, W-weekly or M-monthly
        :param int skip: skip (Min 0)
        :param str to_date: toDate for balance retrieval (YYYY-MM-DD)
        :param int top: top (Max 500)
        :return: AccountHistoricalBalancesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_historical_balances_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_historical_balances_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_historical_balances_with_http_info(self, **kwargs):  # noqa: E501
        """Get Historical Balances  # noqa: E501

        The historical balances service is used to retrieve the historical balances for an account or a user.<br>Historical balances are daily (D), weekly (W), and monthly (M). <br>The interval input should be passed as D, W, and M to retrieve the desired historical balances. The default interval is daily (D). <br>When no account id is provided, historical balances of the accounts that are active, to be closed, and closed are provided in the response. <br>If the fromDate and toDate are not passed, the last 90 days of data will be provided. <br>The fromDate and toDate should be passed in the YYYY-MM-DD format. <br>The date field in the response denotes the date for which the balance is requested.<br>includeCF needs to be sent as true if the customer wants to return carried forward balances <br>for a date when the data is not available. <br>asofDate field in the response denotes the date as of which the balance was updated for that account.<br>When there is no balance available for a requested date and if includeCF is sent as true, the previous <br>date for which the balance is available is provided in the response. When there is no previous <br>balance available, no data will be sent. <br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_historical_balances_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: accountId
        :param str from_date: from date for balance retrieval (YYYY-MM-DD)
        :param bool include_cf: Consider carry forward logic for missing balances
        :param str interval: D-daily, W-weekly or M-monthly
        :param int skip: skip (Min 0)
        :param str to_date: toDate for balance retrieval (YYYY-MM-DD)
        :param int top: top (Max 500)
        :return: AccountHistoricalBalancesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'from_date', 'include_cf', 'interval', 'skip', 'to_date', 'top']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_historical_balances" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'include_cf' in params:
            query_params.append(('includeCF', params['include_cf']))  # noqa: E501
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501
        if 'top' in params:
            query_params.append(('top', params['top']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/accounts/historicalBalances', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountHistoricalBalancesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_account(self, account_id, account_request, **kwargs):  # noqa: E501
        """Update Account  # noqa: E501

        The update account service is used to update manual and aggregated accounts.<br>The HTTP response code is 204 (Success without content).<br>Update manual account support is available for bank, card, investment, insurance, loan, bills, otherAssets, otherLiabilities and realEstate containers only.<br><b>Note:</b> A real estate account update is only supported for SYSTEM and MANUAL valuation type.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_account(account_id, account_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: accountId (required)
        :param UpdateAccountRequest account_request: accountRequest (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_account_with_http_info(account_id, account_request, **kwargs)  # noqa: E501
        else:
            (data) = self.update_account_with_http_info(account_id, account_request, **kwargs)  # noqa: E501
            return data

    def update_account_with_http_info(self, account_id, account_request, **kwargs):  # noqa: E501
        """Update Account  # noqa: E501

        The update account service is used to update manual and aggregated accounts.<br>The HTTP response code is 204 (Success without content).<br>Update manual account support is available for bank, card, investment, insurance, loan, bills, otherAssets, otherLiabilities and realEstate containers only.<br><b>Note:</b> A real estate account update is only supported for SYSTEM and MANUAL valuation type.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_account_with_http_info(account_id, account_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: accountId (required)
        :param UpdateAccountRequest account_request: accountRequest (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'account_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update_account`")  # noqa: E501
        # verify the required parameter 'account_request' is set
        if ('account_request' not in params or
                params['account_request'] is None):
            raise ValueError("Missing the required parameter `account_request` when calling `update_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account_request' in params:
            body_params = params['account_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
