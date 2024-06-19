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

class ApplyCreditMemoToInvoice(object):
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
        'amount': 'float',
        'invoice_id': 'str',
        'items': 'list[ApplyCreditMemoItemToInvoiceItem]'
    }

    attribute_map = {
        'amount': 'amount',
        'invoice_id': 'invoiceId',
        'items': 'items'
    }

    def __init__(self, amount=None, invoice_id=None, items=None):  # noqa: E501
        """ApplyCreditMemoToInvoice - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._invoice_id = None
        self._items = None
        self.discriminator = None
        self.amount = amount
        self.invoice_id = invoice_id
        if items is not None:
            self.items = items

    @property
    def amount(self):
        """Gets the amount of this ApplyCreditMemoToInvoice.  # noqa: E501

        The credit memo amount to be applied to the invoice.   # noqa: E501

        :return: The amount of this ApplyCreditMemoToInvoice.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ApplyCreditMemoToInvoice.

        The credit memo amount to be applied to the invoice.   # noqa: E501

        :param amount: The amount of this ApplyCreditMemoToInvoice.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def invoice_id(self):
        """Gets the invoice_id of this ApplyCreditMemoToInvoice.  # noqa: E501

        The unique ID of the invoice that the credit memo is applied to.   # noqa: E501

        :return: The invoice_id of this ApplyCreditMemoToInvoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this ApplyCreditMemoToInvoice.

        The unique ID of the invoice that the credit memo is applied to.   # noqa: E501

        :param invoice_id: The invoice_id of this ApplyCreditMemoToInvoice.  # noqa: E501
        :type: str
        """
        if invoice_id is None:
            raise ValueError("Invalid value for `invoice_id`, must not be `None`")  # noqa: E501

        self._invoice_id = invoice_id

    @property
    def items(self):
        """Gets the items of this ApplyCreditMemoToInvoice.  # noqa: E501

        Container for items. The maximum number of items is 1,000.  If `creditMemoItemId` is the source, then it should be accompanied by a target `invoiceItemId`.  If `creditTaxItemId` is the source, then it should be accompanied by a target `taxItemId`.   # noqa: E501

        :return: The items of this ApplyCreditMemoToInvoice.  # noqa: E501
        :rtype: list[ApplyCreditMemoItemToInvoiceItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ApplyCreditMemoToInvoice.

        Container for items. The maximum number of items is 1,000.  If `creditMemoItemId` is the source, then it should be accompanied by a target `invoiceItemId`.  If `creditTaxItemId` is the source, then it should be accompanied by a target `taxItemId`.   # noqa: E501

        :param items: The items of this ApplyCreditMemoToInvoice.  # noqa: E501
        :type: list[ApplyCreditMemoItemToInvoiceItem]
        """

        self._items = items

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
        if issubclass(ApplyCreditMemoToInvoice, dict):
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
        if not isinstance(other, ApplyCreditMemoToInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
