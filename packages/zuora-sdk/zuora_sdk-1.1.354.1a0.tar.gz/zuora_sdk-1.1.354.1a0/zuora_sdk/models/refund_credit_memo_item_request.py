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

class RefundCreditMemoItemRequest(object):
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
        'credit_tax_item_id': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'credit_memo_item_id': 'creditMemoItemId',
        'credit_tax_item_id': 'creditTaxItemId'
    }

    def __init__(self, amount=None, credit_memo_item_id=None, credit_tax_item_id=None):  # noqa: E501
        """RefundCreditMemoItemRequest - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._credit_memo_item_id = None
        self._credit_tax_item_id = None
        self.discriminator = None
        self.amount = amount
        if credit_memo_item_id is not None:
            self.credit_memo_item_id = credit_memo_item_id
        if credit_tax_item_id is not None:
            self.credit_tax_item_id = credit_tax_item_id

    @property
    def amount(self):
        """Gets the amount of this RefundCreditMemoItemRequest.  # noqa: E501

        The amount of the refund on the specific item.   # noqa: E501

        :return: The amount of this RefundCreditMemoItemRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RefundCreditMemoItemRequest.

        The amount of the refund on the specific item.   # noqa: E501

        :param amount: The amount of this RefundCreditMemoItemRequest.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def credit_memo_item_id(self):
        """Gets the credit_memo_item_id of this RefundCreditMemoItemRequest.  # noqa: E501

        The ID of the credit memo item that is refunded.   # noqa: E501

        :return: The credit_memo_item_id of this RefundCreditMemoItemRequest.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_item_id

    @credit_memo_item_id.setter
    def credit_memo_item_id(self, credit_memo_item_id):
        """Sets the credit_memo_item_id of this RefundCreditMemoItemRequest.

        The ID of the credit memo item that is refunded.   # noqa: E501

        :param credit_memo_item_id: The credit_memo_item_id of this RefundCreditMemoItemRequest.  # noqa: E501
        :type: str
        """

        self._credit_memo_item_id = credit_memo_item_id

    @property
    def credit_tax_item_id(self):
        """Gets the credit_tax_item_id of this RefundCreditMemoItemRequest.  # noqa: E501

        The ID of the credit memo taxation item that is refunded.   # noqa: E501

        :return: The credit_tax_item_id of this RefundCreditMemoItemRequest.  # noqa: E501
        :rtype: str
        """
        return self._credit_tax_item_id

    @credit_tax_item_id.setter
    def credit_tax_item_id(self, credit_tax_item_id):
        """Sets the credit_tax_item_id of this RefundCreditMemoItemRequest.

        The ID of the credit memo taxation item that is refunded.   # noqa: E501

        :param credit_tax_item_id: The credit_tax_item_id of this RefundCreditMemoItemRequest.  # noqa: E501
        :type: str
        """

        self._credit_tax_item_id = credit_tax_item_id

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
        if issubclass(RefundCreditMemoItemRequest, dict):
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
        if not isinstance(other, RefundCreditMemoItemRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
