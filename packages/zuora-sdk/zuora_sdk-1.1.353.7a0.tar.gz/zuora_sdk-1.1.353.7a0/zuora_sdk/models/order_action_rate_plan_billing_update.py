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

class OrderActionRatePlanBillingUpdate(object):
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
        'billing_period_alignment': 'BillingPeriodAlignment'
    }

    attribute_map = {
        'billing_period_alignment': 'billingPeriodAlignment'
    }

    def __init__(self, billing_period_alignment=None):  # noqa: E501
        """OrderActionRatePlanBillingUpdate - a model defined in Swagger"""  # noqa: E501
        self._billing_period_alignment = None
        self.discriminator = None
        if billing_period_alignment is not None:
            self.billing_period_alignment = billing_period_alignment

    @property
    def billing_period_alignment(self):
        """Gets the billing_period_alignment of this OrderActionRatePlanBillingUpdate.  # noqa: E501


        :return: The billing_period_alignment of this OrderActionRatePlanBillingUpdate.  # noqa: E501
        :rtype: BillingPeriodAlignment
        """
        return self._billing_period_alignment

    @billing_period_alignment.setter
    def billing_period_alignment(self, billing_period_alignment):
        """Sets the billing_period_alignment of this OrderActionRatePlanBillingUpdate.


        :param billing_period_alignment: The billing_period_alignment of this OrderActionRatePlanBillingUpdate.  # noqa: E501
        :type: BillingPeriodAlignment
        """

        self._billing_period_alignment = billing_period_alignment

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
        if issubclass(OrderActionRatePlanBillingUpdate, dict):
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
        if not isinstance(other, OrderActionRatePlanBillingUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
