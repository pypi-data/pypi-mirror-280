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

class PreviewOrderResultChargeMetrics(object):
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
        'charges': 'list[PreviewChargeMetrics]',
        'subscription_number': 'str'
    }

    attribute_map = {
        'charges': 'charges',
        'subscription_number': 'subscriptionNumber'
    }

    def __init__(self, charges=None, subscription_number=None):  # noqa: E501
        """PreviewOrderResultChargeMetrics - a model defined in Swagger"""  # noqa: E501
        self._charges = None
        self._subscription_number = None
        self.discriminator = None
        if charges is not None:
            self.charges = charges
        if subscription_number is not None:
            self.subscription_number = subscription_number

    @property
    def charges(self):
        """Gets the charges of this PreviewOrderResultChargeMetrics.  # noqa: E501


        :return: The charges of this PreviewOrderResultChargeMetrics.  # noqa: E501
        :rtype: list[PreviewChargeMetrics]
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this PreviewOrderResultChargeMetrics.


        :param charges: The charges of this PreviewOrderResultChargeMetrics.  # noqa: E501
        :type: list[PreviewChargeMetrics]
        """

        self._charges = charges

    @property
    def subscription_number(self):
        """Gets the subscription_number of this PreviewOrderResultChargeMetrics.  # noqa: E501

        The number of the subscription that has been affected by this order. When creating a subscription, this value will not show if the subscription number was not specified in the request.  # noqa: E501

        :return: The subscription_number of this PreviewOrderResultChargeMetrics.  # noqa: E501
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this PreviewOrderResultChargeMetrics.

        The number of the subscription that has been affected by this order. When creating a subscription, this value will not show if the subscription number was not specified in the request.  # noqa: E501

        :param subscription_number: The subscription_number of this PreviewOrderResultChargeMetrics.  # noqa: E501
        :type: str
        """

        self._subscription_number = subscription_number

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
        if issubclass(PreviewOrderResultChargeMetrics, dict):
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
        if not isinstance(other, PreviewOrderResultChargeMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
