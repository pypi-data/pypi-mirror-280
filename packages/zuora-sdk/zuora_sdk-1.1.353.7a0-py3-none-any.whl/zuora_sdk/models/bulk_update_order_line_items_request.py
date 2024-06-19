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

class BulkUpdateOrderLineItemsRequest(object):
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
        'order_line_items': 'list[BulkUpdateOrderLineItem]',
        'processing_options': 'ProcessingOptions'
    }

    attribute_map = {
        'order_line_items': 'orderLineItems',
        'processing_options': 'processingOptions'
    }

    def __init__(self, order_line_items=None, processing_options=None):  # noqa: E501
        """BulkUpdateOrderLineItemsRequest - a model defined in Swagger"""  # noqa: E501
        self._order_line_items = None
        self._processing_options = None
        self.discriminator = None
        if order_line_items is not None:
            self.order_line_items = order_line_items
        if processing_options is not None:
            self.processing_options = processing_options

    @property
    def order_line_items(self):
        """Gets the order_line_items of this BulkUpdateOrderLineItemsRequest.  # noqa: E501


        :return: The order_line_items of this BulkUpdateOrderLineItemsRequest.  # noqa: E501
        :rtype: list[BulkUpdateOrderLineItem]
        """
        return self._order_line_items

    @order_line_items.setter
    def order_line_items(self, order_line_items):
        """Sets the order_line_items of this BulkUpdateOrderLineItemsRequest.


        :param order_line_items: The order_line_items of this BulkUpdateOrderLineItemsRequest.  # noqa: E501
        :type: list[BulkUpdateOrderLineItem]
        """

        self._order_line_items = order_line_items

    @property
    def processing_options(self):
        """Gets the processing_options of this BulkUpdateOrderLineItemsRequest.  # noqa: E501


        :return: The processing_options of this BulkUpdateOrderLineItemsRequest.  # noqa: E501
        :rtype: ProcessingOptions
        """
        return self._processing_options

    @processing_options.setter
    def processing_options(self, processing_options):
        """Sets the processing_options of this BulkUpdateOrderLineItemsRequest.


        :param processing_options: The processing_options of this BulkUpdateOrderLineItemsRequest.  # noqa: E501
        :type: ProcessingOptions
        """

        self._processing_options = processing_options

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
        if issubclass(BulkUpdateOrderLineItemsRequest, dict):
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
        if not isinstance(other, BulkUpdateOrderLineItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
