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


class StageErrorApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def integration_v1_stage_error_errortype_get(self, token, errortype, **kwargs):  # noqa: E501
        """integration_v1_stage_error_errortype_get  # noqa: E501

        Use this API to get the staging error data for transaction or event type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.integration_v1_stage_error_errortype_get(token, errortype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Authorization token issued by the authentication API (required)
        :param str errortype: error type (required)
        :return: ExpandedStageError
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.integration_v1_stage_error_errortype_get_with_http_info(token, errortype, **kwargs)  # noqa: E501
        else:
            (data) = self.integration_v1_stage_error_errortype_get_with_http_info(token, errortype, **kwargs)  # noqa: E501
            return data

    def integration_v1_stage_error_errortype_get_with_http_info(self, token, errortype, **kwargs):  # noqa: E501
        """integration_v1_stage_error_errortype_get  # noqa: E501

        Use this API to get the staging error data for transaction or event type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.integration_v1_stage_error_errortype_get_with_http_info(token, errortype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Authorization token issued by the authentication API (required)
        :param str errortype: error type (required)
        :return: ExpandedStageError
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'errortype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method integration_v1_stage_error_errortype_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `integration_v1_stage_error_errortype_get`")  # noqa: E501
        # verify the required parameter 'errortype' is set
        if ('errortype' not in params or
                params['errortype'] is None):
            raise ValueError("Missing the required parameter `errortype` when calling `integration_v1_stage_error_errortype_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'errortype' in params:
            path_params['errortype'] = params['errortype']  # noqa: E501

        query_params = []

        header_params = {}
        if 'token' in params:
            header_params['token'] = params['token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/integration/v1/stage/error/{errortype}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExpandedStageError',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
