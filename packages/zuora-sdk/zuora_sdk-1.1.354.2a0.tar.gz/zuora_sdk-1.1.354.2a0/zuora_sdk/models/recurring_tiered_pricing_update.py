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
from zuora_sdk.models.price_change_params import PriceChangeParams  # noqa: F401,E501

class RecurringTieredPricingUpdate(PriceChangeParams):
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
        'quantity': 'float',
        'tiers': 'list[ChargeTier]'
    }
    if hasattr(PriceChangeParams, "swagger_types"):
        swagger_types.update(PriceChangeParams.swagger_types)

    attribute_map = {
        'quantity': 'quantity',
        'tiers': 'tiers'
    }
    if hasattr(PriceChangeParams, "attribute_map"):
        attribute_map.update(PriceChangeParams.attribute_map)

    def __init__(self, quantity=None, tiers=None, *args, **kwargs):  # noqa: E501
        """RecurringTieredPricingUpdate - a model defined in Swagger"""  # noqa: E501
        self._quantity = None
        self._tiers = None
        self.discriminator = None
        if quantity is not None:
            self.quantity = quantity
        if tiers is not None:
            self.tiers = tiers
        PriceChangeParams.__init__(self, *args, **kwargs)

    @property
    def quantity(self):
        """Gets the quantity of this RecurringTieredPricingUpdate.  # noqa: E501


        :return: The quantity of this RecurringTieredPricingUpdate.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this RecurringTieredPricingUpdate.


        :param quantity: The quantity of this RecurringTieredPricingUpdate.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def tiers(self):
        """Gets the tiers of this RecurringTieredPricingUpdate.  # noqa: E501


        :return: The tiers of this RecurringTieredPricingUpdate.  # noqa: E501
        :rtype: list[ChargeTier]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this RecurringTieredPricingUpdate.


        :param tiers: The tiers of this RecurringTieredPricingUpdate.  # noqa: E501
        :type: list[ChargeTier]
        """

        self._tiers = tiers

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
        if issubclass(RecurringTieredPricingUpdate, dict):
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
        if not isinstance(other, RecurringTieredPricingUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
