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

class ReverseCreditMemoRequest(object):
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
        'apply_effective_date': 'date',
        'memo_date': 'date'
    }

    attribute_map = {
        'apply_effective_date': 'applyEffectiveDate',
        'memo_date': 'memoDate'
    }

    def __init__(self, apply_effective_date=None, memo_date=None):  # noqa: E501
        """ReverseCreditMemoRequest - a model defined in Swagger"""  # noqa: E501
        self._apply_effective_date = None
        self._memo_date = None
        self.discriminator = None
        if apply_effective_date is not None:
            self.apply_effective_date = apply_effective_date
        if memo_date is not None:
            self.memo_date = memo_date

    @property
    def apply_effective_date(self):
        """Gets the apply_effective_date of this ReverseCreditMemoRequest.  # noqa: E501

        The date when the to-be-reversed credit memo is applied to the newly generated debit memo, in `yyyy-mm-dd` format. The effective date must be later than or equal to the memo date.  The default value is the date when you reverse the credit memo and create the debit memo.   # noqa: E501

        :return: The apply_effective_date of this ReverseCreditMemoRequest.  # noqa: E501
        :rtype: date
        """
        return self._apply_effective_date

    @apply_effective_date.setter
    def apply_effective_date(self, apply_effective_date):
        """Sets the apply_effective_date of this ReverseCreditMemoRequest.

        The date when the to-be-reversed credit memo is applied to the newly generated debit memo, in `yyyy-mm-dd` format. The effective date must be later than or equal to the memo date.  The default value is the date when you reverse the credit memo and create the debit memo.   # noqa: E501

        :param apply_effective_date: The apply_effective_date of this ReverseCreditMemoRequest.  # noqa: E501
        :type: date
        """

        self._apply_effective_date = apply_effective_date

    @property
    def memo_date(self):
        """Gets the memo_date of this ReverseCreditMemoRequest.  # noqa: E501

        The date when the debit memo is created, in `yyyy-mm-dd` format. The memo date must be later than or equal to the credit memo's memo date.  The default value is the date when you reverse the credit memo and create the debit memo.   # noqa: E501

        :return: The memo_date of this ReverseCreditMemoRequest.  # noqa: E501
        :rtype: date
        """
        return self._memo_date

    @memo_date.setter
    def memo_date(self, memo_date):
        """Sets the memo_date of this ReverseCreditMemoRequest.

        The date when the debit memo is created, in `yyyy-mm-dd` format. The memo date must be later than or equal to the credit memo's memo date.  The default value is the date when you reverse the credit memo and create the debit memo.   # noqa: E501

        :param memo_date: The memo_date of this ReverseCreditMemoRequest.  # noqa: E501
        :type: date
        """

        self._memo_date = memo_date

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
        if issubclass(ReverseCreditMemoRequest, dict):
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
        if not isinstance(other, ReverseCreditMemoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
