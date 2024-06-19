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
from zuora_sdk.models.order_delta_metric import OrderDeltaMetric  # noqa: F401,E501

class OrderDeltaTcb(OrderDeltaMetric):
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
        'order_line_item_id': 'str'
    }
    if hasattr(OrderDeltaMetric, "swagger_types"):
        swagger_types.update(OrderDeltaMetric.swagger_types)

    attribute_map = {
        'order_line_item_id': 'orderLineItemId'
    }
    if hasattr(OrderDeltaMetric, "attribute_map"):
        attribute_map.update(OrderDeltaMetric.attribute_map)

    def __init__(self, order_line_item_id=None, *args, **kwargs):  # noqa: E501
        """OrderDeltaTcb - a model defined in Swagger"""  # noqa: E501
        self._order_line_item_id = None
        self.discriminator = None
        if order_line_item_id is not None:
            self.order_line_item_id = order_line_item_id
        OrderDeltaMetric.__init__(self, *args, **kwargs)

    @property
    def order_line_item_id(self):
        """Gets the order_line_item_id of this OrderDeltaTcb.  # noqa: E501

        The sytem generated Id for the Order Line Item. This field can be null if the metric is generated for a Rate Plan Charge.   # noqa: E501

        :return: The order_line_item_id of this OrderDeltaTcb.  # noqa: E501
        :rtype: str
        """
        return self._order_line_item_id

    @order_line_item_id.setter
    def order_line_item_id(self, order_line_item_id):
        """Sets the order_line_item_id of this OrderDeltaTcb.

        The sytem generated Id for the Order Line Item. This field can be null if the metric is generated for a Rate Plan Charge.   # noqa: E501

        :param order_line_item_id: The order_line_item_id of this OrderDeltaTcb.  # noqa: E501
        :type: str
        """

        self._order_line_item_id = order_line_item_id

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
        if issubclass(OrderDeltaTcb, dict):
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
        if not isinstance(other, OrderDeltaTcb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
