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

class GetDebitMemoApplicationPart(object):
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
        'applied_amount': 'float',
        'created_by_id': 'str',
        'created_date': 'datetime',
        'credit_memo_id': 'str',
        'payment_id': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'applied_amount': 'appliedAmount',
        'created_by_id': 'createdById',
        'created_date': 'createdDate',
        'credit_memo_id': 'creditMemoId',
        'payment_id': 'paymentId',
        'updated_by_id': 'updatedById',
        'updated_date': 'updatedDate'
    }

    def __init__(self, applied_amount=None, created_by_id=None, created_date=None, credit_memo_id=None, payment_id=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """GetDebitMemoApplicationPart - a model defined in Swagger"""  # noqa: E501
        self._applied_amount = None
        self._created_by_id = None
        self._created_date = None
        self._credit_memo_id = None
        self._payment_id = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None
        if applied_amount is not None:
            self.applied_amount = applied_amount
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if credit_memo_id is not None:
            self.credit_memo_id = credit_memo_id
        if payment_id is not None:
            self.payment_id = payment_id
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def applied_amount(self):
        """Gets the applied_amount of this GetDebitMemoApplicationPart.  # noqa: E501

        The amount that is applied to the debit memo.   # noqa: E501

        :return: The applied_amount of this GetDebitMemoApplicationPart.  # noqa: E501
        :rtype: float
        """
        return self._applied_amount

    @applied_amount.setter
    def applied_amount(self, applied_amount):
        """Sets the applied_amount of this GetDebitMemoApplicationPart.

        The amount that is applied to the debit memo.   # noqa: E501

        :param applied_amount: The applied_amount of this GetDebitMemoApplicationPart.  # noqa: E501
        :type: float
        """

        self._applied_amount = applied_amount

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetDebitMemoApplicationPart.  # noqa: E501

        The ID of the Zuora user who created the payment or credit memo.   # noqa: E501

        :return: The created_by_id of this GetDebitMemoApplicationPart.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetDebitMemoApplicationPart.

        The ID of the Zuora user who created the payment or credit memo.   # noqa: E501

        :param created_by_id: The created_by_id of this GetDebitMemoApplicationPart.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this GetDebitMemoApplicationPart.  # noqa: E501

        The date and time when the payment or credit memo was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-12-01 15:31:10.   # noqa: E501

        :return: The created_date of this GetDebitMemoApplicationPart.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this GetDebitMemoApplicationPart.

        The date and time when the payment or credit memo was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-12-01 15:31:10.   # noqa: E501

        :param created_date: The created_date of this GetDebitMemoApplicationPart.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def credit_memo_id(self):
        """Gets the credit_memo_id of this GetDebitMemoApplicationPart.  # noqa: E501

        The ID of credit memo that is applied to the specified debit memo.   # noqa: E501

        :return: The credit_memo_id of this GetDebitMemoApplicationPart.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_id

    @credit_memo_id.setter
    def credit_memo_id(self, credit_memo_id):
        """Sets the credit_memo_id of this GetDebitMemoApplicationPart.

        The ID of credit memo that is applied to the specified debit memo.   # noqa: E501

        :param credit_memo_id: The credit_memo_id of this GetDebitMemoApplicationPart.  # noqa: E501
        :type: str
        """

        self._credit_memo_id = credit_memo_id

    @property
    def payment_id(self):
        """Gets the payment_id of this GetDebitMemoApplicationPart.  # noqa: E501

        The ID of the payment that is applied to the specified debit memo.   # noqa: E501

        :return: The payment_id of this GetDebitMemoApplicationPart.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this GetDebitMemoApplicationPart.

        The ID of the payment that is applied to the specified debit memo.   # noqa: E501

        :param payment_id: The payment_id of this GetDebitMemoApplicationPart.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this GetDebitMemoApplicationPart.  # noqa: E501

        The ID of the Zuora user who last updated the payment or credit memo.   # noqa: E501

        :return: The updated_by_id of this GetDebitMemoApplicationPart.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this GetDebitMemoApplicationPart.

        The ID of the Zuora user who last updated the payment or credit memo.   # noqa: E501

        :param updated_by_id: The updated_by_id of this GetDebitMemoApplicationPart.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this GetDebitMemoApplicationPart.  # noqa: E501

        The date and time when the payment or credit memo was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2018-01-02 11:42:16.   # noqa: E501

        :return: The updated_date of this GetDebitMemoApplicationPart.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this GetDebitMemoApplicationPart.

        The date and time when the payment or credit memo was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2018-01-02 11:42:16.   # noqa: E501

        :param updated_date: The updated_date of this GetDebitMemoApplicationPart.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

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
        if issubclass(GetDebitMemoApplicationPart, dict):
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
        if not isinstance(other, GetDebitMemoApplicationPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
