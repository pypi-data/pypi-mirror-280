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

class GetScheduledEvents200Response(object):
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
        'data': 'list[GetScheduledEventResponse]',
        'next': 'str'
    }

    attribute_map = {
        'data': 'data',
        'next': 'next'
    }

    def __init__(self, data=None, next=None):  # noqa: E501
        """GetScheduledEvents200Response - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._next = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if next is not None:
            self.next = next

    @property
    def data(self):
        """Gets the data of this GetScheduledEvents200Response.  # noqa: E501


        :return: The data of this GetScheduledEvents200Response.  # noqa: E501
        :rtype: list[GetScheduledEventResponse]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetScheduledEvents200Response.


        :param data: The data of this GetScheduledEvents200Response.  # noqa: E501
        :type: list[GetScheduledEventResponse]
        """

        self._data = data

    @property
    def next(self):
        """Gets the next of this GetScheduledEvents200Response.  # noqa: E501

        The link to the next page. No value if it is last page.  # noqa: E501

        :return: The next of this GetScheduledEvents200Response.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this GetScheduledEvents200Response.

        The link to the next page. No value if it is last page.  # noqa: E501

        :param next: The next of this GetScheduledEvents200Response.  # noqa: E501
        :type: str
        """

        self._next = next

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
        if issubclass(GetScheduledEvents200Response, dict):
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
        if not isinstance(other, GetScheduledEvents200Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
