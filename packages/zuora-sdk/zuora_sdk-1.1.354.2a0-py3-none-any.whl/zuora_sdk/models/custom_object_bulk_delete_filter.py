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

class CustomObjectBulkDeleteFilter(object):
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
        'conditions': 'list[CustomObjectBulkDeleteFilterCondition]'
    }

    attribute_map = {
        'conditions': 'conditions'
    }

    def __init__(self, conditions=None):  # noqa: E501
        """CustomObjectBulkDeleteFilter - a model defined in Swagger"""  # noqa: E501
        self._conditions = None
        self.discriminator = None
        self.conditions = conditions

    @property
    def conditions(self):
        """Gets the conditions of this CustomObjectBulkDeleteFilter.  # noqa: E501

        Group of field filter conditions that are evaluated in conjunction with each other using the AND operator. The minimum number of conditions is 1 and the maximum is 2.  # noqa: E501

        :return: The conditions of this CustomObjectBulkDeleteFilter.  # noqa: E501
        :rtype: list[CustomObjectBulkDeleteFilterCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this CustomObjectBulkDeleteFilter.

        Group of field filter conditions that are evaluated in conjunction with each other using the AND operator. The minimum number of conditions is 1 and the maximum is 2.  # noqa: E501

        :param conditions: The conditions of this CustomObjectBulkDeleteFilter.  # noqa: E501
        :type: list[CustomObjectBulkDeleteFilterCondition]
        """
        if conditions is None:
            raise ValueError("Invalid value for `conditions`, must not be `None`")  # noqa: E501

        self._conditions = conditions

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
        if issubclass(CustomObjectBulkDeleteFilter, dict):
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
        if not isinstance(other, CustomObjectBulkDeleteFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
