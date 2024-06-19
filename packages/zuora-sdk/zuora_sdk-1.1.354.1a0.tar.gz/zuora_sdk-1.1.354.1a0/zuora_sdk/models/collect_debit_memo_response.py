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

class CollectDebitMemoResponse(object):
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
        'applied_credit_memos': 'list[CollectDebitMemoResponseAppliedCreditMemos]',
        'applied_payments': 'list[CollectDebitMemoResponseAppliedPayments]',
        'debit_memo': 'CollectDebitMemoResponseDebitMemo',
        'processed_payment': 'CollectDebitMemoResponseProcessedPayment',
        'success': 'bool'
    }

    attribute_map = {
        'applied_credit_memos': 'appliedCreditMemos',
        'applied_payments': 'appliedPayments',
        'debit_memo': 'debitMemo',
        'processed_payment': 'processedPayment',
        'success': 'success'
    }

    def __init__(self, applied_credit_memos=None, applied_payments=None, debit_memo=None, processed_payment=None, success=None):  # noqa: E501
        """CollectDebitMemoResponse - a model defined in Swagger"""  # noqa: E501
        self._applied_credit_memos = None
        self._applied_payments = None
        self._debit_memo = None
        self._processed_payment = None
        self._success = None
        self.discriminator = None
        if applied_credit_memos is not None:
            self.applied_credit_memos = applied_credit_memos
        if applied_payments is not None:
            self.applied_payments = applied_payments
        if debit_memo is not None:
            self.debit_memo = debit_memo
        if processed_payment is not None:
            self.processed_payment = processed_payment
        if success is not None:
            self.success = success

    @property
    def applied_credit_memos(self):
        """Gets the applied_credit_memos of this CollectDebitMemoResponse.  # noqa: E501

        The information about which credit memo applied to the specific debit memo.   # noqa: E501

        :return: The applied_credit_memos of this CollectDebitMemoResponse.  # noqa: E501
        :rtype: list[CollectDebitMemoResponseAppliedCreditMemos]
        """
        return self._applied_credit_memos

    @applied_credit_memos.setter
    def applied_credit_memos(self, applied_credit_memos):
        """Sets the applied_credit_memos of this CollectDebitMemoResponse.

        The information about which credit memo applied to the specific debit memo.   # noqa: E501

        :param applied_credit_memos: The applied_credit_memos of this CollectDebitMemoResponse.  # noqa: E501
        :type: list[CollectDebitMemoResponseAppliedCreditMemos]
        """

        self._applied_credit_memos = applied_credit_memos

    @property
    def applied_payments(self):
        """Gets the applied_payments of this CollectDebitMemoResponse.  # noqa: E501

        The information about which payment applied to the specific debit memo.   # noqa: E501

        :return: The applied_payments of this CollectDebitMemoResponse.  # noqa: E501
        :rtype: list[CollectDebitMemoResponseAppliedPayments]
        """
        return self._applied_payments

    @applied_payments.setter
    def applied_payments(self, applied_payments):
        """Sets the applied_payments of this CollectDebitMemoResponse.

        The information about which payment applied to the specific debit memo.   # noqa: E501

        :param applied_payments: The applied_payments of this CollectDebitMemoResponse.  # noqa: E501
        :type: list[CollectDebitMemoResponseAppliedPayments]
        """

        self._applied_payments = applied_payments

    @property
    def debit_memo(self):
        """Gets the debit_memo of this CollectDebitMemoResponse.  # noqa: E501


        :return: The debit_memo of this CollectDebitMemoResponse.  # noqa: E501
        :rtype: CollectDebitMemoResponseDebitMemo
        """
        return self._debit_memo

    @debit_memo.setter
    def debit_memo(self, debit_memo):
        """Sets the debit_memo of this CollectDebitMemoResponse.


        :param debit_memo: The debit_memo of this CollectDebitMemoResponse.  # noqa: E501
        :type: CollectDebitMemoResponseDebitMemo
        """

        self._debit_memo = debit_memo

    @property
    def processed_payment(self):
        """Gets the processed_payment of this CollectDebitMemoResponse.  # noqa: E501


        :return: The processed_payment of this CollectDebitMemoResponse.  # noqa: E501
        :rtype: CollectDebitMemoResponseProcessedPayment
        """
        return self._processed_payment

    @processed_payment.setter
    def processed_payment(self, processed_payment):
        """Sets the processed_payment of this CollectDebitMemoResponse.


        :param processed_payment: The processed_payment of this CollectDebitMemoResponse.  # noqa: E501
        :type: CollectDebitMemoResponseProcessedPayment
        """

        self._processed_payment = processed_payment

    @property
    def success(self):
        """Gets the success of this CollectDebitMemoResponse.  # noqa: E501

        Returns `true` if the request was processed successfully.  # noqa: E501

        :return: The success of this CollectDebitMemoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CollectDebitMemoResponse.

        Returns `true` if the request was processed successfully.  # noqa: E501

        :param success: The success of this CollectDebitMemoResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(CollectDebitMemoResponse, dict):
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
        if not isinstance(other, CollectDebitMemoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
