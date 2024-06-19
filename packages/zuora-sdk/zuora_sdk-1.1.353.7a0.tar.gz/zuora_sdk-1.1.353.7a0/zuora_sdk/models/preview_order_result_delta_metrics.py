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

class PreviewOrderResultDeltaMetrics(object):
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
        'order_delta_mrr': 'list[OrderDeltaMrr]',
        'order_delta_tcb': 'list[OrderDeltaTcb]',
        'order_delta_tcv': 'list[OrderDeltaTcv]'
    }

    attribute_map = {
        'order_delta_mrr': 'orderDeltaMrr',
        'order_delta_tcb': 'orderDeltaTcb',
        'order_delta_tcv': 'orderDeltaTcv'
    }

    def __init__(self, order_delta_mrr=None, order_delta_tcb=None, order_delta_tcv=None):  # noqa: E501
        """PreviewOrderResultDeltaMetrics - a model defined in Swagger"""  # noqa: E501
        self._order_delta_mrr = None
        self._order_delta_tcb = None
        self._order_delta_tcv = None
        self.discriminator = None
        if order_delta_mrr is not None:
            self.order_delta_mrr = order_delta_mrr
        if order_delta_tcb is not None:
            self.order_delta_tcb = order_delta_tcb
        if order_delta_tcv is not None:
            self.order_delta_tcv = order_delta_tcv

    @property
    def order_delta_mrr(self):
        """Gets the order_delta_mrr of this PreviewOrderResultDeltaMetrics.  # noqa: E501


        :return: The order_delta_mrr of this PreviewOrderResultDeltaMetrics.  # noqa: E501
        :rtype: list[OrderDeltaMrr]
        """
        return self._order_delta_mrr

    @order_delta_mrr.setter
    def order_delta_mrr(self, order_delta_mrr):
        """Sets the order_delta_mrr of this PreviewOrderResultDeltaMetrics.


        :param order_delta_mrr: The order_delta_mrr of this PreviewOrderResultDeltaMetrics.  # noqa: E501
        :type: list[OrderDeltaMrr]
        """

        self._order_delta_mrr = order_delta_mrr

    @property
    def order_delta_tcb(self):
        """Gets the order_delta_tcb of this PreviewOrderResultDeltaMetrics.  # noqa: E501


        :return: The order_delta_tcb of this PreviewOrderResultDeltaMetrics.  # noqa: E501
        :rtype: list[OrderDeltaTcb]
        """
        return self._order_delta_tcb

    @order_delta_tcb.setter
    def order_delta_tcb(self, order_delta_tcb):
        """Sets the order_delta_tcb of this PreviewOrderResultDeltaMetrics.


        :param order_delta_tcb: The order_delta_tcb of this PreviewOrderResultDeltaMetrics.  # noqa: E501
        :type: list[OrderDeltaTcb]
        """

        self._order_delta_tcb = order_delta_tcb

    @property
    def order_delta_tcv(self):
        """Gets the order_delta_tcv of this PreviewOrderResultDeltaMetrics.  # noqa: E501


        :return: The order_delta_tcv of this PreviewOrderResultDeltaMetrics.  # noqa: E501
        :rtype: list[OrderDeltaTcv]
        """
        return self._order_delta_tcv

    @order_delta_tcv.setter
    def order_delta_tcv(self, order_delta_tcv):
        """Sets the order_delta_tcv of this PreviewOrderResultDeltaMetrics.


        :param order_delta_tcv: The order_delta_tcv of this PreviewOrderResultDeltaMetrics.  # noqa: E501
        :type: list[OrderDeltaTcv]
        """

        self._order_delta_tcv = order_delta_tcv

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
        if issubclass(PreviewOrderResultDeltaMetrics, dict):
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
        if not isinstance(other, PreviewOrderResultDeltaMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
