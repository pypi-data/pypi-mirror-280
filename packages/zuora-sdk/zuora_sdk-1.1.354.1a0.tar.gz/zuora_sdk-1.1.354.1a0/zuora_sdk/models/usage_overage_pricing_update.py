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

class UsageOveragePricingUpdate(PriceChangeParams):
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
        'included_units': 'float',
        'overage_price': 'float'
    }
    if hasattr(PriceChangeParams, "swagger_types"):
        swagger_types.update(PriceChangeParams.swagger_types)

    attribute_map = {
        'included_units': 'includedUnits',
        'overage_price': 'overagePrice'
    }
    if hasattr(PriceChangeParams, "attribute_map"):
        attribute_map.update(PriceChangeParams.attribute_map)

    def __init__(self, included_units=None, overage_price=None, *args, **kwargs):  # noqa: E501
        """UsageOveragePricingUpdate - a model defined in Swagger"""  # noqa: E501
        self._included_units = None
        self._overage_price = None
        self.discriminator = None
        if included_units is not None:
            self.included_units = included_units
        if overage_price is not None:
            self.overage_price = overage_price
        PriceChangeParams.__init__(self, *args, **kwargs)

    @property
    def included_units(self):
        """Gets the included_units of this UsageOveragePricingUpdate.  # noqa: E501

        A certain quantity of units for free in the overage charge model. It cannot be negative. It must be 0 and above. Decimals are allowed.   # noqa: E501

        :return: The included_units of this UsageOveragePricingUpdate.  # noqa: E501
        :rtype: float
        """
        return self._included_units

    @included_units.setter
    def included_units(self, included_units):
        """Sets the included_units of this UsageOveragePricingUpdate.

        A certain quantity of units for free in the overage charge model. It cannot be negative. It must be 0 and above. Decimals are allowed.   # noqa: E501

        :param included_units: The included_units of this UsageOveragePricingUpdate.  # noqa: E501
        :type: float
        """

        self._included_units = included_units

    @property
    def overage_price(self):
        """Gets the overage_price of this UsageOveragePricingUpdate.  # noqa: E501


        :return: The overage_price of this UsageOveragePricingUpdate.  # noqa: E501
        :rtype: float
        """
        return self._overage_price

    @overage_price.setter
    def overage_price(self, overage_price):
        """Sets the overage_price of this UsageOveragePricingUpdate.


        :param overage_price: The overage_price of this UsageOveragePricingUpdate.  # noqa: E501
        :type: float
        """

        self._overage_price = overage_price

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
        if issubclass(UsageOveragePricingUpdate, dict):
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
        if not isinstance(other, UsageOveragePricingUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
