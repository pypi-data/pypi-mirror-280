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

class ValidationErrors(object):
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
        'reasons': 'list[ValidationReasons]',
        'success': 'bool'
    }

    attribute_map = {
        'reasons': 'reasons',
        'success': 'success'
    }

    def __init__(self, reasons=None, success=None):  # noqa: E501
        """ValidationErrors - a model defined in Swagger"""  # noqa: E501
        self._reasons = None
        self._success = None
        self.discriminator = None
        if reasons is not None:
            self.reasons = reasons
        if success is not None:
            self.success = success

    @property
    def reasons(self):
        """Gets the reasons of this ValidationErrors.  # noqa: E501

        The list of reasons that the request was unsuccessful  # noqa: E501

        :return: The reasons of this ValidationErrors.  # noqa: E501
        :rtype: list[ValidationReasons]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this ValidationErrors.

        The list of reasons that the request was unsuccessful  # noqa: E501

        :param reasons: The reasons of this ValidationErrors.  # noqa: E501
        :type: list[ValidationReasons]
        """

        self._reasons = reasons

    @property
    def success(self):
        """Gets the success of this ValidationErrors.  # noqa: E501

        Returns `false` if the request was not successful.  # noqa: E501

        :return: The success of this ValidationErrors.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ValidationErrors.

        Returns `false` if the request was not successful.  # noqa: E501

        :param success: The success of this ValidationErrors.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(ValidationErrors, dict):
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
        if not isinstance(other, ValidationErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
