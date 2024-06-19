# coding: utf-8

"""
    Zuora API Reference

    REST API reference for the Zuora Billing, Payments, and Central Platform! Check out the [REST API Overview](https://www.zuora.com/developer/api-references/api/overview/).  # noqa: E501

    OpenAPI spec version: 2024-05-20
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from zuora_sdk.api_client import ApiClient


class AuthenticationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def integration_v1_authenticate_post(self, role, clientname, **kwargs):  # noqa: E501
        """integration_v1_authenticate_post  # noqa: E501

        Use this API to Authenticate and get JWToken to push and pull data from your RevPro instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.integration_v1_authenticate_post(role, clientname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role: (required)
        :param str clientname: (required)
        :return: ExpandedAuthentication
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.integration_v1_authenticate_post_with_http_info(role, clientname, **kwargs)  # noqa: E501
        else:
            (data) = self.integration_v1_authenticate_post_with_http_info(role, clientname, **kwargs)  # noqa: E501
            return data

    def integration_v1_authenticate_post_with_http_info(self, role, clientname, **kwargs):  # noqa: E501
        """integration_v1_authenticate_post  # noqa: E501

        Use this API to Authenticate and get JWToken to push and pull data from your RevPro instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.integration_v1_authenticate_post_with_http_info(role, clientname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role: (required)
        :param str clientname: (required)
        :return: ExpandedAuthentication
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role', 'clientname']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method integration_v1_authenticate_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role' is set
        if ('role' not in params or
                params['role'] is None):
            raise ValueError("Missing the required parameter `role` when calling `integration_v1_authenticate_post`")  # noqa: E501
        # verify the required parameter 'clientname' is set
        if ('clientname' not in params or
                params['clientname'] is None):
            raise ValueError("Missing the required parameter `clientname` when calling `integration_v1_authenticate_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'role' in params:
            header_params['role'] = params['role']  # noqa: E501
        if 'clientname' in params:
            header_params['clientname'] = params['clientname']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/integration/v1/authenticate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExpandedAuthentication',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oauth2_token_post(self, client_id, client_secret, grant_type, **kwargs):  # noqa: E501
        """oauth2_token_post  # noqa: E501

        Use this API to Authenticate and get OAUTH token to push and pull data from your RevPro instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth2_token_post(client_id, client_secret, grant_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: (required)
        :param str client_secret: (required)
        :param str grant_type: (required)
        :return: ExpandedOAuth
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oauth2_token_post_with_http_info(client_id, client_secret, grant_type, **kwargs)  # noqa: E501
        else:
            (data) = self.oauth2_token_post_with_http_info(client_id, client_secret, grant_type, **kwargs)  # noqa: E501
            return data

    def oauth2_token_post_with_http_info(self, client_id, client_secret, grant_type, **kwargs):  # noqa: E501
        """oauth2_token_post  # noqa: E501

        Use this API to Authenticate and get OAUTH token to push and pull data from your RevPro instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth2_token_post_with_http_info(client_id, client_secret, grant_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: (required)
        :param str client_secret: (required)
        :param str grant_type: (required)
        :return: ExpandedOAuth
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'client_secret', 'grant_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth2_token_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `oauth2_token_post`")  # noqa: E501
        # verify the required parameter 'client_secret' is set
        if ('client_secret' not in params or
                params['client_secret'] is None):
            raise ValueError("Missing the required parameter `client_secret` when calling `oauth2_token_post`")  # noqa: E501
        # verify the required parameter 'grant_type' is set
        if ('grant_type' not in params or
                params['grant_type'] is None):
            raise ValueError("Missing the required parameter `grant_type` when calling `oauth2_token_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'client_id' in params:
            query_params.append(('client_id', params['client_id']))  # noqa: E501
        if 'client_secret' in params:
            query_params.append(('client_secret', params['client_secret']))  # noqa: E501
        if 'grant_type' in params:
            query_params.append(('grant_type', params['grant_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/oauth2/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExpandedOAuth',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
