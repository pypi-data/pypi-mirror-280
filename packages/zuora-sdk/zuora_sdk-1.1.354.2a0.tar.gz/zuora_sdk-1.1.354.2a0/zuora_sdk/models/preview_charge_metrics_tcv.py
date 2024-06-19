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

class PreviewChargeMetricsTcv(object):
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
        'discount': 'float',
        'discount_delta': 'float',
        'regular': 'float',
        'regular_delta': 'float'
    }

    attribute_map = {
        'discount': 'discount',
        'discount_delta': 'discountDelta',
        'regular': 'regular',
        'regular_delta': 'regularDelta'
    }

    def __init__(self, discount=None, discount_delta=None, regular=None, regular_delta=None):  # noqa: E501
        """PreviewChargeMetricsTcv - a model defined in Swagger"""  # noqa: E501
        self._discount = None
        self._discount_delta = None
        self._regular = None
        self._regular_delta = None
        self.discriminator = None
        if discount is not None:
            self.discount = discount
        if discount_delta is not None:
            self.discount_delta = discount_delta
        if regular is not None:
            self.regular = regular
        if regular_delta is not None:
            self.regular_delta = regular_delta

    @property
    def discount(self):
        """Gets the discount of this PreviewChargeMetricsTcv.  # noqa: E501

        Always equals to discountTcb.  # noqa: E501

        :return: The discount of this PreviewChargeMetricsTcv.  # noqa: E501
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this PreviewChargeMetricsTcv.

        Always equals to discountTcb.  # noqa: E501

        :param discount: The discount of this PreviewChargeMetricsTcv.  # noqa: E501
        :type: float
        """

        self._discount = discount

    @property
    def discount_delta(self):
        """Gets the discount_delta of this PreviewChargeMetricsTcv.  # noqa: E501

        Always equals to delta discountTcb.  # noqa: E501

        :return: The discount_delta of this PreviewChargeMetricsTcv.  # noqa: E501
        :rtype: float
        """
        return self._discount_delta

    @discount_delta.setter
    def discount_delta(self, discount_delta):
        """Sets the discount_delta of this PreviewChargeMetricsTcv.

        Always equals to delta discountTcb.  # noqa: E501

        :param discount_delta: The discount_delta of this PreviewChargeMetricsTcv.  # noqa: E501
        :type: float
        """

        self._discount_delta = discount_delta

    @property
    def regular(self):
        """Gets the regular of this PreviewChargeMetricsTcv.  # noqa: E501


        :return: The regular of this PreviewChargeMetricsTcv.  # noqa: E501
        :rtype: float
        """
        return self._regular

    @regular.setter
    def regular(self, regular):
        """Sets the regular of this PreviewChargeMetricsTcv.


        :param regular: The regular of this PreviewChargeMetricsTcv.  # noqa: E501
        :type: float
        """

        self._regular = regular

    @property
    def regular_delta(self):
        """Gets the regular_delta of this PreviewChargeMetricsTcv.  # noqa: E501


        :return: The regular_delta of this PreviewChargeMetricsTcv.  # noqa: E501
        :rtype: float
        """
        return self._regular_delta

    @regular_delta.setter
    def regular_delta(self, regular_delta):
        """Sets the regular_delta of this PreviewChargeMetricsTcv.


        :param regular_delta: The regular_delta of this PreviewChargeMetricsTcv.  # noqa: E501
        :type: float
        """

        self._regular_delta = regular_delta

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
        if issubclass(PreviewChargeMetricsTcv, dict):
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
        if not isinstance(other, PreviewChargeMetricsTcv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
