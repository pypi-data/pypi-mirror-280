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

class QuantityForUsageCharges(object):
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
        'charge_id': 'str',
        'quantity': 'float'
    }

    attribute_map = {
        'charge_id': 'chargeId',
        'quantity': 'quantity'
    }

    def __init__(self, charge_id=None, quantity=None):  # noqa: E501
        """QuantityForUsageCharges - a model defined in Swagger"""  # noqa: E501
        self._charge_id = None
        self._quantity = None
        self.discriminator = None
        if charge_id is not None:
            self.charge_id = charge_id
        if quantity is not None:
            self.quantity = quantity

    @property
    def charge_id(self):
        """Gets the charge_id of this QuantityForUsageCharges.  # noqa: E501

        The ID of the subscription charge.   # noqa: E501

        :return: The charge_id of this QuantityForUsageCharges.  # noqa: E501
        :rtype: str
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this QuantityForUsageCharges.

        The ID of the subscription charge.   # noqa: E501

        :param charge_id: The charge_id of this QuantityForUsageCharges.  # noqa: E501
        :type: str
        """

        self._charge_id = charge_id

    @property
    def quantity(self):
        """Gets the quantity of this QuantityForUsageCharges.  # noqa: E501

        The quantity of the subscription charge.   # noqa: E501

        :return: The quantity of this QuantityForUsageCharges.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this QuantityForUsageCharges.

        The quantity of the subscription charge.   # noqa: E501

        :param quantity: The quantity of this QuantityForUsageCharges.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

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
        if issubclass(QuantityForUsageCharges, dict):
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
        if not isinstance(other, QuantityForUsageCharges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
