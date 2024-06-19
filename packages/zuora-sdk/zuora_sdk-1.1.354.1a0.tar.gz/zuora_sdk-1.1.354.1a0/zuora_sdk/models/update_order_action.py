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

class UpdateOrderAction(object):
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
        'change_reason': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'change_reason': 'changeReason',
        'custom_fields': 'customFields'
    }

    def __init__(self, change_reason=None, custom_fields=None):  # noqa: E501
        """UpdateOrderAction - a model defined in Swagger"""  # noqa: E501
        self._change_reason = None
        self._custom_fields = None
        self.discriminator = None
        if change_reason is not None:
            self.change_reason = change_reason
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def change_reason(self):
        """Gets the change_reason of this UpdateOrderAction.  # noqa: E501

        The change reason set for an order action when the order action is updated.   # noqa: E501

        :return: The change_reason of this UpdateOrderAction.  # noqa: E501
        :rtype: str
        """
        return self._change_reason

    @change_reason.setter
    def change_reason(self, change_reason):
        """Sets the change_reason of this UpdateOrderAction.

        The change reason set for an order action when the order action is updated.   # noqa: E501

        :param change_reason: The change_reason of this UpdateOrderAction.  # noqa: E501
        :type: str
        """

        self._change_reason = change_reason

    @property
    def custom_fields(self):
        """Gets the custom_fields of this UpdateOrderAction.  # noqa: E501

        Container for custom fields of an Order Action object.   # noqa: E501

        :return: The custom_fields of this UpdateOrderAction.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this UpdateOrderAction.

        Container for custom fields of an Order Action object.   # noqa: E501

        :param custom_fields: The custom_fields of this UpdateOrderAction.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

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
        if issubclass(UpdateOrderAction, dict):
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
        if not isinstance(other, UpdateOrderAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
