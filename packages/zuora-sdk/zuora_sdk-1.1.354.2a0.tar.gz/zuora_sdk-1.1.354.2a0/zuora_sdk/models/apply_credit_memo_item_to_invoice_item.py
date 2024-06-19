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

class ApplyCreditMemoItemToInvoiceItem(object):
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
        'credit_memo_item_id': 'str',
        'credit_tax_item_id': 'str',
        'invoice_item_id': 'str',
        'tax_item_id': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'credit_memo_item_id': 'creditMemoItemId',
        'credit_tax_item_id': 'creditTaxItemId',
        'invoice_item_id': 'invoiceItemId',
        'tax_item_id': 'taxItemId'
    }

    def __init__(self, amount=None, credit_memo_item_id=None, credit_tax_item_id=None, invoice_item_id=None, tax_item_id=None):  # noqa: E501
        """ApplyCreditMemoItemToInvoiceItem - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._credit_memo_item_id = None
        self._credit_tax_item_id = None
        self._invoice_item_id = None
        self._tax_item_id = None
        self.discriminator = None
        self.amount = amount
        if credit_memo_item_id is not None:
            self.credit_memo_item_id = credit_memo_item_id
        if credit_tax_item_id is not None:
            self.credit_tax_item_id = credit_tax_item_id
        if invoice_item_id is not None:
            self.invoice_item_id = invoice_item_id
        if tax_item_id is not None:
            self.tax_item_id = tax_item_id

    @property
    def amount(self):
        """Gets the amount of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501

        The amount that is applied to the specific item.    # noqa: E501

        :return: The amount of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ApplyCreditMemoItemToInvoiceItem.

        The amount that is applied to the specific item.    # noqa: E501

        :param amount: The amount of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def credit_memo_item_id(self):
        """Gets the credit_memo_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501

        The ID of the credit memo item.   # noqa: E501

        :return: The credit_memo_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_item_id

    @credit_memo_item_id.setter
    def credit_memo_item_id(self, credit_memo_item_id):
        """Sets the credit_memo_item_id of this ApplyCreditMemoItemToInvoiceItem.

        The ID of the credit memo item.   # noqa: E501

        :param credit_memo_item_id: The credit_memo_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501
        :type: str
        """

        self._credit_memo_item_id = credit_memo_item_id

    @property
    def credit_tax_item_id(self):
        """Gets the credit_tax_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501

        The ID of the credit memo taxation item.   # noqa: E501

        :return: The credit_tax_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._credit_tax_item_id

    @credit_tax_item_id.setter
    def credit_tax_item_id(self, credit_tax_item_id):
        """Sets the credit_tax_item_id of this ApplyCreditMemoItemToInvoiceItem.

        The ID of the credit memo taxation item.   # noqa: E501

        :param credit_tax_item_id: The credit_tax_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501
        :type: str
        """

        self._credit_tax_item_id = credit_tax_item_id

    @property
    def invoice_item_id(self):
        """Gets the invoice_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501

        The ID of the invoice item that the credit memo item is applied to.   # noqa: E501

        :return: The invoice_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._invoice_item_id

    @invoice_item_id.setter
    def invoice_item_id(self, invoice_item_id):
        """Sets the invoice_item_id of this ApplyCreditMemoItemToInvoiceItem.

        The ID of the invoice item that the credit memo item is applied to.   # noqa: E501

        :param invoice_item_id: The invoice_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501
        :type: str
        """

        self._invoice_item_id = invoice_item_id

    @property
    def tax_item_id(self):
        """Gets the tax_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501

        The ID of the invoice taxation item that the credit memo taxation item is applied to.   # noqa: E501

        :return: The tax_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._tax_item_id

    @tax_item_id.setter
    def tax_item_id(self, tax_item_id):
        """Sets the tax_item_id of this ApplyCreditMemoItemToInvoiceItem.

        The ID of the invoice taxation item that the credit memo taxation item is applied to.   # noqa: E501

        :param tax_item_id: The tax_item_id of this ApplyCreditMemoItemToInvoiceItem.  # noqa: E501
        :type: str
        """

        self._tax_item_id = tax_item_id

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
        if issubclass(ApplyCreditMemoItemToInvoiceItem, dict):
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
        if not isinstance(other, ApplyCreditMemoItemToInvoiceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
