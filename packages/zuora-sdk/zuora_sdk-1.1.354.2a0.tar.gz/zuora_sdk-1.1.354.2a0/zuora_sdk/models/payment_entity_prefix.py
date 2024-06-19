# coding: utf-8

"""
    Zuora API Reference

    REST API reference for the Zuora Billing, Payments, and Central Platform! Check out the [REST API Overview](https://www.zuora.com/developer/api-references/api/overview/).  # noqa: E501

    OpenAPI spec version: 2024-05-20
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentEntityPrefix(object):
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
        'prefix': 'str',
        'start_number': 'int'
    }

    attribute_map = {
        'prefix': 'prefix',
        'start_number': 'startNumber'
    }

    def __init__(self, prefix=None, start_number=None):  # noqa: E501
        """PaymentEntityPrefix - a model defined in Swagger"""  # noqa: E501
        self._prefix = None
        self._start_number = None
        self.discriminator = None
        if prefix is not None:
            self.prefix = prefix
        if start_number is not None:
            self.start_number = start_number

    @property
    def prefix(self):
        """Gets the prefix of this PaymentEntityPrefix.  # noqa: E501

        The prefix of payments.   # noqa: E501

        :return: The prefix of this PaymentEntityPrefix.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this PaymentEntityPrefix.

        The prefix of payments.   # noqa: E501

        :param prefix: The prefix of this PaymentEntityPrefix.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def start_number(self):
        """Gets the start_number of this PaymentEntityPrefix.  # noqa: E501

        The starting number of payments.   # noqa: E501

        :return: The start_number of this PaymentEntityPrefix.  # noqa: E501
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this PaymentEntityPrefix.

        The starting number of payments.   # noqa: E501

        :param start_number: The start_number of this PaymentEntityPrefix.  # noqa: E501
        :type: int
        """

        self._start_number = start_number

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
        if issubclass(PaymentEntityPrefix, dict):
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
        if not isinstance(other, PaymentEntityPrefix):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
