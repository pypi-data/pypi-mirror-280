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

class CreatePaymentSessionRequest(object):
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
        'account_id': 'str',
        'amount': 'float',
        'auth_amount': 'float',
        'currency': 'str',
        'payment_gateway': 'str',
        'process_payment': 'bool'
    }

    attribute_map = {
        'account_id': 'accountId',
        'amount': 'amount',
        'auth_amount': 'authAmount',
        'currency': 'currency',
        'payment_gateway': 'paymentGateway',
        'process_payment': 'processPayment'
    }

    def __init__(self, account_id=None, amount=None, auth_amount=None, currency=None, payment_gateway=None, process_payment=None):  # noqa: E501
        """CreatePaymentSessionRequest - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._amount = None
        self._auth_amount = None
        self._currency = None
        self._payment_gateway = None
        self._process_payment = None
        self.discriminator = None
        self.account_id = account_id
        if amount is not None:
            self.amount = amount
        if auth_amount is not None:
            self.auth_amount = auth_amount
        self.currency = currency
        self.payment_gateway = payment_gateway
        self.process_payment = process_payment

    @property
    def account_id(self):
        """Gets the account_id of this CreatePaymentSessionRequest.  # noqa: E501

        The ID of the customer account in Zuora that is associated with this payment method.   # noqa: E501

        :return: The account_id of this CreatePaymentSessionRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CreatePaymentSessionRequest.

        The ID of the customer account in Zuora that is associated with this payment method.   # noqa: E501

        :param account_id: The account_id of this CreatePaymentSessionRequest.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def amount(self):
        """Gets the amount of this CreatePaymentSessionRequest.  # noqa: E501

        The amount of the payment.  This field is required if `processPayment` is `true`.   # noqa: E501

        :return: The amount of this CreatePaymentSessionRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreatePaymentSessionRequest.

        The amount of the payment.  This field is required if `processPayment` is `true`.   # noqa: E501

        :param amount: The amount of this CreatePaymentSessionRequest.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def auth_amount(self):
        """Gets the auth_amount of this CreatePaymentSessionRequest.  # noqa: E501

        The authorization amount for the payment method. Specify a value greater than 0.  This field is required if `processPayment` is false.   # noqa: E501

        :return: The auth_amount of this CreatePaymentSessionRequest.  # noqa: E501
        :rtype: float
        """
        return self._auth_amount

    @auth_amount.setter
    def auth_amount(self, auth_amount):
        """Sets the auth_amount of this CreatePaymentSessionRequest.

        The authorization amount for the payment method. Specify a value greater than 0.  This field is required if `processPayment` is false.   # noqa: E501

        :param auth_amount: The auth_amount of this CreatePaymentSessionRequest.  # noqa: E501
        :type: float
        """

        self._auth_amount = auth_amount

    @property
    def currency(self):
        """Gets the currency of this CreatePaymentSessionRequest.  # noqa: E501

        The currency of the payment in the format of the three-character ISO currency code.   # noqa: E501

        :return: The currency of this CreatePaymentSessionRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreatePaymentSessionRequest.

        The currency of the payment in the format of the three-character ISO currency code.   # noqa: E501

        :param currency: The currency of this CreatePaymentSessionRequest.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def payment_gateway(self):
        """Gets the payment_gateway of this CreatePaymentSessionRequest.  # noqa: E501

        The ID of the payment gateway instance configured in Zuora that will process the payment, such as `e884322ab8c711edab030242ac120004`.   # noqa: E501

        :return: The payment_gateway of this CreatePaymentSessionRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_gateway

    @payment_gateway.setter
    def payment_gateway(self, payment_gateway):
        """Sets the payment_gateway of this CreatePaymentSessionRequest.

        The ID of the payment gateway instance configured in Zuora that will process the payment, such as `e884322ab8c711edab030242ac120004`.   # noqa: E501

        :param payment_gateway: The payment_gateway of this CreatePaymentSessionRequest.  # noqa: E501
        :type: str
        """
        if payment_gateway is None:
            raise ValueError("Invalid value for `payment_gateway`, must not be `None`")  # noqa: E501

        self._payment_gateway = payment_gateway

    @property
    def process_payment(self):
        """Gets the process_payment of this CreatePaymentSessionRequest.  # noqa: E501

        Indicate whether a payment should be processed after creating the payment method.  If this field is set to `true`, you must specify the `amount` field.  If this field is set to `false`, you must specify the `authAmount` field. The payment method will be verified through the payment gateway instance specified in the `paymentGateway` field.   # noqa: E501

        :return: The process_payment of this CreatePaymentSessionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._process_payment

    @process_payment.setter
    def process_payment(self, process_payment):
        """Sets the process_payment of this CreatePaymentSessionRequest.

        Indicate whether a payment should be processed after creating the payment method.  If this field is set to `true`, you must specify the `amount` field.  If this field is set to `false`, you must specify the `authAmount` field. The payment method will be verified through the payment gateway instance specified in the `paymentGateway` field.   # noqa: E501

        :param process_payment: The process_payment of this CreatePaymentSessionRequest.  # noqa: E501
        :type: bool
        """
        if process_payment is None:
            raise ValueError("Invalid value for `process_payment`, must not be `None`")  # noqa: E501

        self._process_payment = process_payment

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
        if issubclass(CreatePaymentSessionRequest, dict):
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
        if not isinstance(other, CreatePaymentSessionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
