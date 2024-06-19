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

class PreviewExistingSubscriptionResultInvoices(object):
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
        'invoice_number': 'str',
        'amount': 'float',
        'amount_without_tax': 'float',
        'tax_amount': 'float',
        'target_date': 'date',
        'invoice_items': 'list[PreviewExistingSubscriptionInvoiceItemResult]',
        'status': 'str',
        'is_from_existing_invoice': 'bool'
    }

    attribute_map = {
        'invoice_number': 'invoiceNumber',
        'amount': 'amount',
        'amount_without_tax': 'amountWithoutTax',
        'tax_amount': 'taxAmount',
        'target_date': 'targetDate',
        'invoice_items': 'invoiceItems',
        'status': 'status',
        'is_from_existing_invoice': 'isFromExistingInvoice'
    }

    def __init__(self, invoice_number=None, amount=None, amount_without_tax=None, tax_amount=None, target_date=None, invoice_items=None, status=None, is_from_existing_invoice=None):  # noqa: E501
        """PreviewExistingSubscriptionResultInvoices - a model defined in Swagger"""  # noqa: E501
        self._invoice_number = None
        self._amount = None
        self._amount_without_tax = None
        self._tax_amount = None
        self._target_date = None
        self._invoice_items = None
        self._status = None
        self._is_from_existing_invoice = None
        self.discriminator = None
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if amount is not None:
            self.amount = amount
        if amount_without_tax is not None:
            self.amount_without_tax = amount_without_tax
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if target_date is not None:
            self.target_date = target_date
        if invoice_items is not None:
            self.invoice_items = invoice_items
        if status is not None:
            self.status = status
        if is_from_existing_invoice is not None:
            self.is_from_existing_invoice = is_from_existing_invoice

    @property
    def invoice_number(self):
        """Gets the invoice_number of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501

        The invoice number.  # noqa: E501

        :return: The invoice_number of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this PreviewExistingSubscriptionResultInvoices.

        The invoice number.  # noqa: E501

        :param invoice_number: The invoice_number of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def amount(self):
        """Gets the amount of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501

        Invoice amount.  # noqa: E501

        :return: The amount of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PreviewExistingSubscriptionResultInvoices.

        Invoice amount.  # noqa: E501

        :param amount: The amount of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def amount_without_tax(self):
        """Gets the amount_without_tax of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501

        Invoice amount minus tax.  # noqa: E501

        :return: The amount_without_tax of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :rtype: float
        """
        return self._amount_without_tax

    @amount_without_tax.setter
    def amount_without_tax(self, amount_without_tax):
        """Sets the amount_without_tax of this PreviewExistingSubscriptionResultInvoices.

        Invoice amount minus tax.  # noqa: E501

        :param amount_without_tax: The amount_without_tax of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :type: float
        """

        self._amount_without_tax = amount_without_tax

    @property
    def tax_amount(self):
        """Gets the tax_amount of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501

        The tax amount of the invoice.  # noqa: E501

        :return: The tax_amount of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this PreviewExistingSubscriptionResultInvoices.

        The tax amount of the invoice.  # noqa: E501

        :param tax_amount: The tax_amount of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def target_date(self):
        """Gets the target_date of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501

        Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd.  # noqa: E501

        :return: The target_date of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this PreviewExistingSubscriptionResultInvoices.

        Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd.  # noqa: E501

        :param target_date: The target_date of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :type: date
        """

        self._target_date = target_date

    @property
    def invoice_items(self):
        """Gets the invoice_items of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501

        Container for invoice items.  # noqa: E501

        :return: The invoice_items of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :rtype: list[PreviewExistingSubscriptionInvoiceItemResult]
        """
        return self._invoice_items

    @invoice_items.setter
    def invoice_items(self, invoice_items):
        """Sets the invoice_items of this PreviewExistingSubscriptionResultInvoices.

        Container for invoice items.  # noqa: E501

        :param invoice_items: The invoice_items of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :type: list[PreviewExistingSubscriptionInvoiceItemResult]
        """

        self._invoice_items = invoice_items

    @property
    def status(self):
        """Gets the status of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501

        The status of the invoice.  # noqa: E501

        :return: The status of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PreviewExistingSubscriptionResultInvoices.

        The status of the invoice.  # noqa: E501

        :param status: The status of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def is_from_existing_invoice(self):
        """Gets the is_from_existing_invoice of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501

        Indicates whether the invoice information is from an existing invoice.  # noqa: E501

        :return: The is_from_existing_invoice of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :rtype: bool
        """
        return self._is_from_existing_invoice

    @is_from_existing_invoice.setter
    def is_from_existing_invoice(self, is_from_existing_invoice):
        """Sets the is_from_existing_invoice of this PreviewExistingSubscriptionResultInvoices.

        Indicates whether the invoice information is from an existing invoice.  # noqa: E501

        :param is_from_existing_invoice: The is_from_existing_invoice of this PreviewExistingSubscriptionResultInvoices.  # noqa: E501
        :type: bool
        """

        self._is_from_existing_invoice = is_from_existing_invoice

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
        if issubclass(PreviewExistingSubscriptionResultInvoices, dict):
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
        if not isinstance(other, PreviewExistingSubscriptionResultInvoices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
