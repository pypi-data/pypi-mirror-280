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


class FilesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_files(self, file_id, **kwargs):  # noqa: E501
        """Retrieve a file  # noqa: E501

        Retrieve files such as export results, invoices, and accounting period reports.  The response content type depends on the type of file that you retrieve. For example, if you retrieve an invoice PDF, the value of the `Content-Type` header in the response is `application/pdf;charset=UTF-8`.  Other content types include:  - `text/csv` for CSV files - `application/msword` for Microsoft Word files - `application/vnd.ms-excel` and `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`   for Microsoft Excel files (*.xls* and *.xlsx* respectively) - `application/zip` and `application/x-gzip` for ZIP and Gzip files respectively - `text/html` for HTML files - `text/plain` for text files  The response always contains character encoding information in the `Content-Type` header. For example, `Content-Type: application/zip;charset=UTF-8`.  **Note:** The maximum file size is 2,047 MB. If you have a data request that exceeds this limit, Zuora returns the following 403 response: `<security:max-object-size>2047MB</security:max-object-size>`. Submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to determine if large file optimization is an option for you.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_files(file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_id: The Zuora ID of the file to retrieve.  (required)
        :param str accept_encoding: Include the `Accept-Encoding: gzip` header to compress responses as a gzipped file. It can significantly reduce the bandwidth required for a response.   If specified, Zuora automatically compresses responses that contain over 1000 bytes of data, and the response contains a `Content-Encoding` header with the compression algorithm so that your client can decompress it. 
        :param str content_encoding: Include the `Content-Encoding: gzip` header to compress a request. With this header specified, you should upload a gzipped file for the request payload instead of sending the JSON payload. 
        :param str authorization: The value is in the `Bearer {token}` format where {token} is a valid OAuth token generated by calling [Create an OAuth token](https://www.zuora.com/developer/api-references/api/operation/createToken). 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version: The minor version of the Zuora REST API.  
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_files_with_http_info(file_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_files_with_http_info(file_id, **kwargs)  # noqa: E501
            return data

    def get_files_with_http_info(self, file_id, **kwargs):  # noqa: E501
        """Retrieve a file  # noqa: E501

        Retrieve files such as export results, invoices, and accounting period reports.  The response content type depends on the type of file that you retrieve. For example, if you retrieve an invoice PDF, the value of the `Content-Type` header in the response is `application/pdf;charset=UTF-8`.  Other content types include:  - `text/csv` for CSV files - `application/msword` for Microsoft Word files - `application/vnd.ms-excel` and `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`   for Microsoft Excel files (*.xls* and *.xlsx* respectively) - `application/zip` and `application/x-gzip` for ZIP and Gzip files respectively - `text/html` for HTML files - `text/plain` for text files  The response always contains character encoding information in the `Content-Type` header. For example, `Content-Type: application/zip;charset=UTF-8`.  **Note:** The maximum file size is 2,047 MB. If you have a data request that exceeds this limit, Zuora returns the following 403 response: `<security:max-object-size>2047MB</security:max-object-size>`. Submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to determine if large file optimization is an option for you.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_files_with_http_info(file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_id: The Zuora ID of the file to retrieve.  (required)
        :param str accept_encoding: Include the `Accept-Encoding: gzip` header to compress responses as a gzipped file. It can significantly reduce the bandwidth required for a response.   If specified, Zuora automatically compresses responses that contain over 1000 bytes of data, and the response contains a `Content-Encoding` header with the compression algorithm so that your client can decompress it. 
        :param str content_encoding: Include the `Content-Encoding: gzip` header to compress a request. With this header specified, you should upload a gzipped file for the request payload instead of sending the JSON payload. 
        :param str authorization: The value is in the `Bearer {token}` format where {token} is a valid OAuth token generated by calling [Create an OAuth token](https://www.zuora.com/developer/api-references/api/operation/createToken). 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version: The minor version of the Zuora REST API.  
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_id', 'accept_encoding', 'content_encoding', 'authorization', 'zuora_track_id', 'zuora_entity_ids', 'zuora_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_files" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_id' is set
        if ('file_id' not in params or
                params['file_id'] is None):
            raise ValueError("Missing the required parameter `file_id` when calling `get_files`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_id' in params:
            path_params['file-id'] = params['file_id']  # noqa: E501

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
            ['multipart/form-data', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/files/{file-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
