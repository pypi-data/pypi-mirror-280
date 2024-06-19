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

class GetQueryNotificationDefinitions200Response(object):
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
        'next': 'str',
        'data': 'list[GetPublicNotificationDefinitionResponse]'
    }

    attribute_map = {
        'next': 'next',
        'data': 'data'
    }

    def __init__(self, next=None, data=None):  # noqa: E501
        """GetQueryNotificationDefinitions200Response - a model defined in Swagger"""  # noqa: E501
        self._next = None
        self._data = None
        self.discriminator = None
        if next is not None:
            self.next = next
        if data is not None:
            self.data = data

    @property
    def next(self):
        """Gets the next of this GetQueryNotificationDefinitions200Response.  # noqa: E501

        The URI to query the next page of data, e.g. '/notification-definitions?start=1&limit=10'. The start equals request's start+limit, and the limit equals the request's limit. If the current page is the last page, this value is null.  # noqa: E501

        :return: The next of this GetQueryNotificationDefinitions200Response.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this GetQueryNotificationDefinitions200Response.

        The URI to query the next page of data, e.g. '/notification-definitions?start=1&limit=10'. The start equals request's start+limit, and the limit equals the request's limit. If the current page is the last page, this value is null.  # noqa: E501

        :param next: The next of this GetQueryNotificationDefinitions200Response.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def data(self):
        """Gets the data of this GetQueryNotificationDefinitions200Response.  # noqa: E501


        :return: The data of this GetQueryNotificationDefinitions200Response.  # noqa: E501
        :rtype: list[GetPublicNotificationDefinitionResponse]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetQueryNotificationDefinitions200Response.


        :param data: The data of this GetQueryNotificationDefinitions200Response.  # noqa: E501
        :type: list[GetPublicNotificationDefinitionResponse]
        """

        self._data = data

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
        if issubclass(GetQueryNotificationDefinitions200Response, dict):
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
        if not isinstance(other, GetQueryNotificationDefinitions200Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
