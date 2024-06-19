# coding: utf-8

"""
    Zuora API Reference

    REST API reference for the Zuora Billing, Payments, and Central Platform! Check out the [REST API Overview](https://www.zuora.com/developer/api-references/api/overview/).  # noqa: E501

    OpenAPI spec version: 2023-10-24
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SettingItemHttpOperation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'method': 'SettingItemHttpOperationMethod',
        'parameters': 'list[SettingItemHttpRequestParameter]',
        'request_type': 'object',
        'response_type': 'object',
        'url': 'str'
    }

    attribute_map = {
        'method': 'method',
        'parameters': 'parameters',
        'request_type': 'requestType',
        'response_type': 'responseType',
        'url': 'url'
    }

    def __init__(self, method=None, parameters=None, request_type=None, response_type=None, url=None):  # noqa: E501
        """SettingItemHttpOperation - a model defined in Swagger"""  # noqa: E501
        self._method = None
        self._parameters = None
        self._request_type = None
        self._response_type = None
        self._url = None
        self.discriminator = None
        if method is not None:
            self.method = method
        if parameters is not None:
            self.parameters = parameters
        if request_type is not None:
            self.request_type = request_type
        if response_type is not None:
            self.response_type = response_type
        if url is not None:
            self.url = url

    @property
    def method(self):
        """Gets the method of this SettingItemHttpOperation.  # noqa: E501


        :return: The method of this SettingItemHttpOperation.  # noqa: E501
        :rtype: SettingItemHttpOperationMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this SettingItemHttpOperation.


        :param method: The method of this SettingItemHttpOperation.  # noqa: E501
        :type: SettingItemHttpOperationMethod
        """

        self._method = method

    @property
    def parameters(self):
        """Gets the parameters of this SettingItemHttpOperation.  # noqa: E501

        An array of paramters required by this operation.  # noqa: E501

        :return: The parameters of this SettingItemHttpOperation.  # noqa: E501
        :rtype: list[SettingItemHttpRequestParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this SettingItemHttpOperation.

        An array of paramters required by this operation.  # noqa: E501

        :param parameters: The parameters of this SettingItemHttpOperation.  # noqa: E501
        :type: list[SettingItemHttpRequestParameter]
        """

        self._parameters = parameters

    @property
    def request_type(self):
        """Gets the request_type of this SettingItemHttpOperation.  # noqa: E501

        JSON Schema for the request body of this operation.  # noqa: E501

        :return: The request_type of this SettingItemHttpOperation.  # noqa: E501
        :rtype: object
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this SettingItemHttpOperation.

        JSON Schema for the request body of this operation.  # noqa: E501

        :param request_type: The request_type of this SettingItemHttpOperation.  # noqa: E501
        :type: object
        """

        self._request_type = request_type

    @property
    def response_type(self):
        """Gets the response_type of this SettingItemHttpOperation.  # noqa: E501

        JSON Schema for the response body of this operation.  # noqa: E501

        :return: The response_type of this SettingItemHttpOperation.  # noqa: E501
        :rtype: object
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this SettingItemHttpOperation.

        JSON Schema for the response body of this operation.  # noqa: E501

        :param response_type: The response_type of this SettingItemHttpOperation.  # noqa: E501
        :type: object
        """

        self._response_type = response_type

    @property
    def url(self):
        """Gets the url of this SettingItemHttpOperation.  # noqa: E501

        The endpoint url of the operation method. For example, `/settings/billing-rules`.  # noqa: E501

        :return: The url of this SettingItemHttpOperation.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SettingItemHttpOperation.

        The endpoint url of the operation method. For example, `/settings/billing-rules`.  # noqa: E501

        :param url: The url of this SettingItemHttpOperation.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SettingItemHttpOperation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SettingItemHttpOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
