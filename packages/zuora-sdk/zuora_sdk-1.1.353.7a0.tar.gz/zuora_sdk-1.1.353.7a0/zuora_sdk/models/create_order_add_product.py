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
from zuora_sdk.models.create_order_rate_plan_override import CreateOrderRatePlanOverride  # noqa: F401,E501

class CreateOrderAddProduct(CreateOrderRatePlanOverride):
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
        'rate_plan_overrides': 'list[CreateOrderProductRatePlanOverride]'
    }
    if hasattr(CreateOrderRatePlanOverride, "swagger_types"):
        swagger_types.update(CreateOrderRatePlanOverride.swagger_types)

    attribute_map = {
        'rate_plan_overrides': 'ratePlanOverrides'
    }
    if hasattr(CreateOrderRatePlanOverride, "attribute_map"):
        attribute_map.update(CreateOrderRatePlanOverride.attribute_map)

    def __init__(self, rate_plan_overrides=None, *args, **kwargs):  # noqa: E501
        """CreateOrderAddProduct - a model defined in Swagger"""  # noqa: E501
        self._rate_plan_overrides = None
        self.discriminator = None
        if rate_plan_overrides is not None:
            self.rate_plan_overrides = rate_plan_overrides
        CreateOrderRatePlanOverride.__init__(self, *args, **kwargs)

    @property
    def rate_plan_overrides(self):
        """Gets the rate_plan_overrides of this CreateOrderAddProduct.  # noqa: E501


        :return: The rate_plan_overrides of this CreateOrderAddProduct.  # noqa: E501
        :rtype: list[CreateOrderProductRatePlanOverride]
        """
        return self._rate_plan_overrides

    @rate_plan_overrides.setter
    def rate_plan_overrides(self, rate_plan_overrides):
        """Sets the rate_plan_overrides of this CreateOrderAddProduct.


        :param rate_plan_overrides: The rate_plan_overrides of this CreateOrderAddProduct.  # noqa: E501
        :type: list[CreateOrderProductRatePlanOverride]
        """

        self._rate_plan_overrides = rate_plan_overrides

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
        if issubclass(CreateOrderAddProduct, dict):
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
        if not isinstance(other, CreateOrderAddProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
