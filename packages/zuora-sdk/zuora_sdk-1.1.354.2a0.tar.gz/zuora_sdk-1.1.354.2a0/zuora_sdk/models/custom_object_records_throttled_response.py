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

class CustomObjectRecordsThrottledResponse(object):
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
        'code': 'int',
        'details': 'list[CustomObjectRecordsWithError]',
        'message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'details': 'details',
        'message': 'message'
    }

    def __init__(self, code=None, details=None, message=None):  # noqa: E501
        """CustomObjectRecordsThrottledResponse - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._details = None
        self._message = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if details is not None:
            self.details = details
        if message is not None:
            self.message = message

    @property
    def code(self):
        """Gets the code of this CustomObjectRecordsThrottledResponse.  # noqa: E501


        :return: The code of this CustomObjectRecordsThrottledResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CustomObjectRecordsThrottledResponse.


        :param code: The code of this CustomObjectRecordsThrottledResponse.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def details(self):
        """Gets the details of this CustomObjectRecordsThrottledResponse.  # noqa: E501


        :return: The details of this CustomObjectRecordsThrottledResponse.  # noqa: E501
        :rtype: list[CustomObjectRecordsWithError]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this CustomObjectRecordsThrottledResponse.


        :param details: The details of this CustomObjectRecordsThrottledResponse.  # noqa: E501
        :type: list[CustomObjectRecordsWithError]
        """

        self._details = details

    @property
    def message(self):
        """Gets the message of this CustomObjectRecordsThrottledResponse.  # noqa: E501


        :return: The message of this CustomObjectRecordsThrottledResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CustomObjectRecordsThrottledResponse.


        :param message: The message of this CustomObjectRecordsThrottledResponse.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(CustomObjectRecordsThrottledResponse, dict):
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
        if not isinstance(other, CustomObjectRecordsThrottledResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
