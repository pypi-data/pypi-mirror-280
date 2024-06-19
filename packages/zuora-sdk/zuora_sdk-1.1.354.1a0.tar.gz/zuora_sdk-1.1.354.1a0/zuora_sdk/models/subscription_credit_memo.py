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

class SubscriptionCreditMemo(object):
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
        'amount_without_tax': 'float',
        'credit_memo_items': 'list[SubscriptionCreditMemoItem]',
        'tax_amount': 'float'
    }

    attribute_map = {
        'amount': 'amount',
        'amount_without_tax': 'amountWithoutTax',
        'credit_memo_items': 'creditMemoItems',
        'tax_amount': 'taxAmount'
    }

    def __init__(self, amount=None, amount_without_tax=None, credit_memo_items=None, tax_amount=None):  # noqa: E501
        """SubscriptionCreditMemo - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._amount_without_tax = None
        self._credit_memo_items = None
        self._tax_amount = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if amount_without_tax is not None:
            self.amount_without_tax = amount_without_tax
        if credit_memo_items is not None:
            self.credit_memo_items = credit_memo_items
        if tax_amount is not None:
            self.tax_amount = tax_amount

    @property
    def amount(self):
        """Gets the amount of this SubscriptionCreditMemo.  # noqa: E501

        Credit memo amount.  # noqa: E501

        :return: The amount of this SubscriptionCreditMemo.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SubscriptionCreditMemo.

        Credit memo amount.  # noqa: E501

        :param amount: The amount of this SubscriptionCreditMemo.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def amount_without_tax(self):
        """Gets the amount_without_tax of this SubscriptionCreditMemo.  # noqa: E501

        Credit memo amount minus tax.  # noqa: E501

        :return: The amount_without_tax of this SubscriptionCreditMemo.  # noqa: E501
        :rtype: float
        """
        return self._amount_without_tax

    @amount_without_tax.setter
    def amount_without_tax(self, amount_without_tax):
        """Sets the amount_without_tax of this SubscriptionCreditMemo.

        Credit memo amount minus tax.  # noqa: E501

        :param amount_without_tax: The amount_without_tax of this SubscriptionCreditMemo.  # noqa: E501
        :type: float
        """

        self._amount_without_tax = amount_without_tax

    @property
    def credit_memo_items(self):
        """Gets the credit_memo_items of this SubscriptionCreditMemo.  # noqa: E501


        :return: The credit_memo_items of this SubscriptionCreditMemo.  # noqa: E501
        :rtype: list[SubscriptionCreditMemoItem]
        """
        return self._credit_memo_items

    @credit_memo_items.setter
    def credit_memo_items(self, credit_memo_items):
        """Sets the credit_memo_items of this SubscriptionCreditMemo.


        :param credit_memo_items: The credit_memo_items of this SubscriptionCreditMemo.  # noqa: E501
        :type: list[SubscriptionCreditMemoItem]
        """

        self._credit_memo_items = credit_memo_items

    @property
    def tax_amount(self):
        """Gets the tax_amount of this SubscriptionCreditMemo.  # noqa: E501

        Tax amount on the credit memo.  # noqa: E501

        :return: The tax_amount of this SubscriptionCreditMemo.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this SubscriptionCreditMemo.

        Tax amount on the credit memo.  # noqa: E501

        :param tax_amount: The tax_amount of this SubscriptionCreditMemo.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

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
        if issubclass(SubscriptionCreditMemo, dict):
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
        if not isinstance(other, SubscriptionCreditMemo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
