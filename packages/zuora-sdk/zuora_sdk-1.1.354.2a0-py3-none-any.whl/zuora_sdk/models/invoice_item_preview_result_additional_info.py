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

class InvoiceItemPreviewResultAdditionalInfo(object):
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
        'unit_of_measure': 'str',
        'number_of_deliveries': 'float'
    }

    attribute_map = {
        'quantity': 'quantity',
        'unit_of_measure': 'unitOfMeasure',
        'number_of_deliveries': 'numberOfDeliveries'
    }

    def __init__(self, quantity=None, unit_of_measure=None, number_of_deliveries=None):  # noqa: E501
        """InvoiceItemPreviewResultAdditionalInfo - a model defined in Swagger"""  # noqa: E501
        self._quantity = None
        self._unit_of_measure = None
        self._number_of_deliveries = None
        self.discriminator = None
        if quantity is not None:
            self.quantity = quantity
        if unit_of_measure is not None:
            self.unit_of_measure = unit_of_measure
        if number_of_deliveries is not None:
            self.number_of_deliveries = number_of_deliveries

    @property
    def quantity(self):
        """Gets the quantity of this InvoiceItemPreviewResultAdditionalInfo.  # noqa: E501


        :return: The quantity of this InvoiceItemPreviewResultAdditionalInfo.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InvoiceItemPreviewResultAdditionalInfo.


        :param quantity: The quantity of this InvoiceItemPreviewResultAdditionalInfo.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def unit_of_measure(self):
        """Gets the unit_of_measure of this InvoiceItemPreviewResultAdditionalInfo.  # noqa: E501


        :return: The unit_of_measure of this InvoiceItemPreviewResultAdditionalInfo.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """Sets the unit_of_measure of this InvoiceItemPreviewResultAdditionalInfo.


        :param unit_of_measure: The unit_of_measure of this InvoiceItemPreviewResultAdditionalInfo.  # noqa: E501
        :type: str
        """

        self._unit_of_measure = unit_of_measure

    @property
    def number_of_deliveries(self):
        """Gets the number_of_deliveries of this InvoiceItemPreviewResultAdditionalInfo.  # noqa: E501

        The number of delivery for charge.  **Note**: This field is available only if you have the Delivery Pricing feature enabled.   # noqa: E501

        :return: The number_of_deliveries of this InvoiceItemPreviewResultAdditionalInfo.  # noqa: E501
        :rtype: float
        """
        return self._number_of_deliveries

    @number_of_deliveries.setter
    def number_of_deliveries(self, number_of_deliveries):
        """Sets the number_of_deliveries of this InvoiceItemPreviewResultAdditionalInfo.

        The number of delivery for charge.  **Note**: This field is available only if you have the Delivery Pricing feature enabled.   # noqa: E501

        :param number_of_deliveries: The number_of_deliveries of this InvoiceItemPreviewResultAdditionalInfo.  # noqa: E501
        :type: float
        """

        self._number_of_deliveries = number_of_deliveries

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
        if issubclass(InvoiceItemPreviewResultAdditionalInfo, dict):
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
        if not isinstance(other, InvoiceItemPreviewResultAdditionalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
