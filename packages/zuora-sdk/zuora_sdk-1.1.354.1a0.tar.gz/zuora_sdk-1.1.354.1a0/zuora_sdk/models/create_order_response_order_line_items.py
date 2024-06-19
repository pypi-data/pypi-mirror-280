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

class CreateOrderResponseOrderLineItems(object):
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
        'id': 'str',
        'item_number': 'str'
    }

    attribute_map = {
        'id': 'id',
        'item_number': 'itemNumber'
    }

    def __init__(self, id=None, item_number=None):  # noqa: E501
        """CreateOrderResponseOrderLineItems - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._item_number = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if item_number is not None:
            self.item_number = item_number

    @property
    def id(self):
        """Gets the id of this CreateOrderResponseOrderLineItems.  # noqa: E501

        The sytem generated Id for the Order Line Item.  # noqa: E501

        :return: The id of this CreateOrderResponseOrderLineItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateOrderResponseOrderLineItems.

        The sytem generated Id for the Order Line Item.  # noqa: E501

        :param id: The id of this CreateOrderResponseOrderLineItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def item_number(self):
        """Gets the item_number of this CreateOrderResponseOrderLineItems.  # noqa: E501

        The number for the Order Line Item.  # noqa: E501

        :return: The item_number of this CreateOrderResponseOrderLineItems.  # noqa: E501
        :rtype: str
        """
        return self._item_number

    @item_number.setter
    def item_number(self, item_number):
        """Sets the item_number of this CreateOrderResponseOrderLineItems.

        The number for the Order Line Item.  # noqa: E501

        :param item_number: The item_number of this CreateOrderResponseOrderLineItems.  # noqa: E501
        :type: str
        """

        self._item_number = item_number

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
        if issubclass(CreateOrderResponseOrderLineItems, dict):
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
        if not isinstance(other, CreateOrderResponseOrderLineItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
