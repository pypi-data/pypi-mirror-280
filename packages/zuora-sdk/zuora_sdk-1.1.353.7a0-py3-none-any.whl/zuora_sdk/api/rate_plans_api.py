# coding: utf-8

"""
    Zuora API Reference

    REST API reference for the Zuora Billing, Payments, and Central Platform! Check out the [REST API Overview](https://www.zuora.com/developer/api-references/api/overview/).  # noqa: E501

    OpenAPI spec version: 2023-10-24
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from zuora_sdk.api_client import ApiClient


class RatePlansApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_rate_plan(self, rate_plan_id, **kwargs):  # noqa: E501
        """Retrieve a rate plan  # noqa: E501

         Retrieves the detailed information about a specific subscription rate plan.  * If you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled, this operation retrieves information about a subscription rate plan and the related order that has amended the rate plan.  * If you have the [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization) feature enabled, this operation retrieves information about a subscription rate plan and the related order and amendment that have amended the rate plan.  * If you are an existing Zuora Subscribe and Amend customer, this operation retrieves information about a subscription rate plan and the related amendment that has amended the rate plan.  **Note:** Orders is now generally available as of Zuora Billing Release 284 (August 2020). If you are an existing Zuora Subscribe and Amend customer and want to adopt Orders, see [What is Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization#What_is_Orders_Harmonization.3F) and join the [Orders Harmonization community group](https://community.zuora.com/t5/Orders-Harmonization/gp-p/Orders-Harmonization) for more information. If you want to enable Orders, submit a request at [Zuora Global Support](https://support.zuora.com/).  **Note:** You can only retrieve information about the following order actions:  * `addProduct` * `updateProduct` * `removeProduct` * `changePlan`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rate_plan(rate_plan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rate_plan_id: The ID of the subscription rate plan to be retrieved. (required)
        :param str accept_encoding: Include the `Accept-Encoding: gzip` header to compress responses as a gzipped file. It can significantly reduce the bandwidth required for a response.   If specified, Zuora automatically compresses responses that contain over 1000 bytes of data, and the response contains a `Content-Encoding` header with the compression algorithm so that your client can decompress it. 
        :param str content_encoding: Include the `Content-Encoding: gzip` header to compress a request. With this header specified, you should upload a gzipped file for the request payload instead of sending the JSON payload. 
        :param str authorization: The value is in the `Bearer {token}` format where {token} is a valid OAuth token generated by calling [Create an OAuth token](https://www.zuora.com/developer/api-references/api/operation/createToken). 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version: The minor version of the Zuora REST API.  
        :return: GetOrderActionRatePlanResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rate_plan_with_http_info(rate_plan_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_rate_plan_with_http_info(rate_plan_id, **kwargs)  # noqa: E501
            return data

    def get_rate_plan_with_http_info(self, rate_plan_id, **kwargs):  # noqa: E501
        """Retrieve a rate plan  # noqa: E501

         Retrieves the detailed information about a specific subscription rate plan.  * If you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled, this operation retrieves information about a subscription rate plan and the related order that has amended the rate plan.  * If you have the [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization) feature enabled, this operation retrieves information about a subscription rate plan and the related order and amendment that have amended the rate plan.  * If you are an existing Zuora Subscribe and Amend customer, this operation retrieves information about a subscription rate plan and the related amendment that has amended the rate plan.  **Note:** Orders is now generally available as of Zuora Billing Release 284 (August 2020). If you are an existing Zuora Subscribe and Amend customer and want to adopt Orders, see [What is Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization#What_is_Orders_Harmonization.3F) and join the [Orders Harmonization community group](https://community.zuora.com/t5/Orders-Harmonization/gp-p/Orders-Harmonization) for more information. If you want to enable Orders, submit a request at [Zuora Global Support](https://support.zuora.com/).  **Note:** You can only retrieve information about the following order actions:  * `addProduct` * `updateProduct` * `removeProduct` * `changePlan`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rate_plan_with_http_info(rate_plan_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rate_plan_id: The ID of the subscription rate plan to be retrieved. (required)
        :param str accept_encoding: Include the `Accept-Encoding: gzip` header to compress responses as a gzipped file. It can significantly reduce the bandwidth required for a response.   If specified, Zuora automatically compresses responses that contain over 1000 bytes of data, and the response contains a `Content-Encoding` header with the compression algorithm so that your client can decompress it. 
        :param str content_encoding: Include the `Content-Encoding: gzip` header to compress a request. With this header specified, you should upload a gzipped file for the request payload instead of sending the JSON payload. 
        :param str authorization: The value is in the `Bearer {token}` format where {token} is a valid OAuth token generated by calling [Create an OAuth token](https://www.zuora.com/developer/api-references/api/operation/createToken). 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version: The minor version of the Zuora REST API.  
        :return: GetOrderActionRatePlanResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rate_plan_id', 'accept_encoding', 'content_encoding', 'authorization', 'zuora_track_id', 'zuora_entity_ids', 'zuora_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rate_plan" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rate_plan_id' is set
        if ('rate_plan_id' not in params or
                params['rate_plan_id'] is None):
            raise ValueError("Missing the required parameter `rate_plan_id` when calling `get_rate_plan`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rate_plan_id' in params:
            path_params['ratePlanId'] = params['rate_plan_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'accept_encoding' in params:
            header_params['Accept-Encoding'] = params['accept_encoding']  # noqa: E501
        if 'content_encoding' in params:
            header_params['Content-Encoding'] = params['content_encoding']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'zuora_track_id' in params:
            header_params['Zuora-Track-Id'] = params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501
        if 'zuora_version' in params:
            header_params['Zuora-Version'] = params['zuora_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/rateplans/{ratePlanId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetOrderActionRatePlanResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
