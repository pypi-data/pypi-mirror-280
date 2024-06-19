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

class UpdatePaymentMethodRequest(object):
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
        'account_holder_info': 'UpdaterPaymentMethodRequestAccountHolderInfo',
        'account_key': 'str',
        'auth_gateway': 'str',
        'currency_code': 'str',
        'gateway_options': 'GatewayOptions',
        'ip_address': 'str',
        'mandate_info': 'PaymentMethodRequestMandateInfo',
        'processing_options': 'PaymentMethodRequestProcessingOptions',
        'expiration_month': 'int',
        'expiration_year': 'int',
        'security_code': 'str'
    }

    attribute_map = {
        'account_holder_info': 'accountHolderInfo',
        'account_key': 'accountKey',
        'auth_gateway': 'authGateway',
        'currency_code': 'currencyCode',
        'gateway_options': 'gatewayOptions',
        'ip_address': 'ipAddress',
        'mandate_info': 'mandateInfo',
        'processing_options': 'processingOptions',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'security_code': 'securityCode'
    }

    def __init__(self, account_holder_info=None, account_key=None, auth_gateway=None, currency_code=None, gateway_options=None, ip_address=None, mandate_info=None, processing_options=None, expiration_month=None, expiration_year=None, security_code=None):  # noqa: E501
        """UpdatePaymentMethodRequest - a model defined in Swagger"""  # noqa: E501
        self._account_holder_info = None
        self._account_key = None
        self._auth_gateway = None
        self._currency_code = None
        self._gateway_options = None
        self._ip_address = None
        self._mandate_info = None
        self._processing_options = None
        self._expiration_month = None
        self._expiration_year = None
        self._security_code = None
        self.discriminator = None
        if account_holder_info is not None:
            self.account_holder_info = account_holder_info
        if account_key is not None:
            self.account_key = account_key
        if auth_gateway is not None:
            self.auth_gateway = auth_gateway
        if currency_code is not None:
            self.currency_code = currency_code
        if gateway_options is not None:
            self.gateway_options = gateway_options
        if ip_address is not None:
            self.ip_address = ip_address
        if mandate_info is not None:
            self.mandate_info = mandate_info
        if processing_options is not None:
            self.processing_options = processing_options
        if expiration_month is not None:
            self.expiration_month = expiration_month
        if expiration_year is not None:
            self.expiration_year = expiration_year
        if security_code is not None:
            self.security_code = security_code

    @property
    def account_holder_info(self):
        """Gets the account_holder_info of this UpdatePaymentMethodRequest.  # noqa: E501


        :return: The account_holder_info of this UpdatePaymentMethodRequest.  # noqa: E501
        :rtype: UpdaterPaymentMethodRequestAccountHolderInfo
        """
        return self._account_holder_info

    @account_holder_info.setter
    def account_holder_info(self, account_holder_info):
        """Sets the account_holder_info of this UpdatePaymentMethodRequest.


        :param account_holder_info: The account_holder_info of this UpdatePaymentMethodRequest.  # noqa: E501
        :type: UpdaterPaymentMethodRequestAccountHolderInfo
        """

        self._account_holder_info = account_holder_info

    @property
    def account_key(self):
        """Gets the account_key of this UpdatePaymentMethodRequest.  # noqa: E501

        The ID of the customer account associated with this payment method, such as `2x92c0f859b0480f0159d3a4a6ee5bb6`.  **Note:** You can use this field to associate an orphan payment method with a customer account. If a payment method is already associated with a customer account, you cannot change the associated payment method through this operation. You cannot remove the previous account ID and leave this field empty, either.   # noqa: E501

        :return: The account_key of this UpdatePaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_key

    @account_key.setter
    def account_key(self, account_key):
        """Sets the account_key of this UpdatePaymentMethodRequest.

        The ID of the customer account associated with this payment method, such as `2x92c0f859b0480f0159d3a4a6ee5bb6`.  **Note:** You can use this field to associate an orphan payment method with a customer account. If a payment method is already associated with a customer account, you cannot change the associated payment method through this operation. You cannot remove the previous account ID and leave this field empty, either.   # noqa: E501

        :param account_key: The account_key of this UpdatePaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._account_key = account_key

    @property
    def auth_gateway(self):
        """Gets the auth_gateway of this UpdatePaymentMethodRequest.  # noqa: E501

        Specifies the ID of the payment gateway that Zuora will use to authorize the payments that are made with the payment method.   This field is not supported in updating Credit Card Reference Transaction payment methods.   # noqa: E501

        :return: The auth_gateway of this UpdatePaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._auth_gateway

    @auth_gateway.setter
    def auth_gateway(self, auth_gateway):
        """Sets the auth_gateway of this UpdatePaymentMethodRequest.

        Specifies the ID of the payment gateway that Zuora will use to authorize the payments that are made with the payment method.   This field is not supported in updating Credit Card Reference Transaction payment methods.   # noqa: E501

        :param auth_gateway: The auth_gateway of this UpdatePaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._auth_gateway = auth_gateway

    @property
    def currency_code(self):
        """Gets the currency_code of this UpdatePaymentMethodRequest.  # noqa: E501

        The currency used for payment method authorization.   # noqa: E501

        :return: The currency_code of this UpdatePaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this UpdatePaymentMethodRequest.

        The currency used for payment method authorization.   # noqa: E501

        :param currency_code: The currency_code of this UpdatePaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def gateway_options(self):
        """Gets the gateway_options of this UpdatePaymentMethodRequest.  # noqa: E501


        :return: The gateway_options of this UpdatePaymentMethodRequest.  # noqa: E501
        :rtype: GatewayOptions
        """
        return self._gateway_options

    @gateway_options.setter
    def gateway_options(self, gateway_options):
        """Sets the gateway_options of this UpdatePaymentMethodRequest.


        :param gateway_options: The gateway_options of this UpdatePaymentMethodRequest.  # noqa: E501
        :type: GatewayOptions
        """

        self._gateway_options = gateway_options

    @property
    def ip_address(self):
        """Gets the ip_address of this UpdatePaymentMethodRequest.  # noqa: E501

        The IPv4 or IPv6 information of the user when the payment method is created or updated. Some gateways use this field for fraud prevention. If this field is passed to Zuora, Zuora directly passes it to gateways.   If the IP address length is beyond 45 characters, a validation error occurs.  For validating SEPA payment methods on Stripe v2, this field is required.   # noqa: E501

        :return: The ip_address of this UpdatePaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this UpdatePaymentMethodRequest.

        The IPv4 or IPv6 information of the user when the payment method is created or updated. Some gateways use this field for fraud prevention. If this field is passed to Zuora, Zuora directly passes it to gateways.   If the IP address length is beyond 45 characters, a validation error occurs.  For validating SEPA payment methods on Stripe v2, this field is required.   # noqa: E501

        :param ip_address: The ip_address of this UpdatePaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def mandate_info(self):
        """Gets the mandate_info of this UpdatePaymentMethodRequest.  # noqa: E501


        :return: The mandate_info of this UpdatePaymentMethodRequest.  # noqa: E501
        :rtype: PaymentMethodRequestMandateInfo
        """
        return self._mandate_info

    @mandate_info.setter
    def mandate_info(self, mandate_info):
        """Sets the mandate_info of this UpdatePaymentMethodRequest.


        :param mandate_info: The mandate_info of this UpdatePaymentMethodRequest.  # noqa: E501
        :type: PaymentMethodRequestMandateInfo
        """

        self._mandate_info = mandate_info

    @property
    def processing_options(self):
        """Gets the processing_options of this UpdatePaymentMethodRequest.  # noqa: E501


        :return: The processing_options of this UpdatePaymentMethodRequest.  # noqa: E501
        :rtype: PaymentMethodRequestProcessingOptions
        """
        return self._processing_options

    @processing_options.setter
    def processing_options(self, processing_options):
        """Sets the processing_options of this UpdatePaymentMethodRequest.


        :param processing_options: The processing_options of this UpdatePaymentMethodRequest.  # noqa: E501
        :type: PaymentMethodRequestProcessingOptions
        """

        self._processing_options = processing_options

    @property
    def expiration_month(self):
        """Gets the expiration_month of this UpdatePaymentMethodRequest.  # noqa: E501

        One or two digits expiration month (1-12).            # noqa: E501

        :return: The expiration_month of this UpdatePaymentMethodRequest.  # noqa: E501
        :rtype: int
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """Sets the expiration_month of this UpdatePaymentMethodRequest.

        One or two digits expiration month (1-12).            # noqa: E501

        :param expiration_month: The expiration_month of this UpdatePaymentMethodRequest.  # noqa: E501
        :type: int
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """Gets the expiration_year of this UpdatePaymentMethodRequest.  # noqa: E501

        Four-digit expiration year.   # noqa: E501

        :return: The expiration_year of this UpdatePaymentMethodRequest.  # noqa: E501
        :rtype: int
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """Sets the expiration_year of this UpdatePaymentMethodRequest.

        Four-digit expiration year.   # noqa: E501

        :param expiration_year: The expiration_year of this UpdatePaymentMethodRequest.  # noqa: E501
        :type: int
        """

        self._expiration_year = expiration_year

    @property
    def security_code(self):
        """Gets the security_code of this UpdatePaymentMethodRequest.  # noqa: E501

        Optional. It is the CVV or CVV2 security code specific for the credit card or debit card. To ensure PCI compliance, this value is not stored and cannot be queried.   If securityCode code is not passed in the request payload, this operation only updates related fields in the payload. It does not validate the payment method through the gateway.  If securityCode is passed in the request payload, this operation retrieves the credit card information from payload and validates them through the gateway.   # noqa: E501

        :return: The security_code of this UpdatePaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this UpdatePaymentMethodRequest.

        Optional. It is the CVV or CVV2 security code specific for the credit card or debit card. To ensure PCI compliance, this value is not stored and cannot be queried.   If securityCode code is not passed in the request payload, this operation only updates related fields in the payload. It does not validate the payment method through the gateway.  If securityCode is passed in the request payload, this operation retrieves the credit card information from payload and validates them through the gateway.   # noqa: E501

        :param security_code: The security_code of this UpdatePaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._security_code = security_code

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
        if issubclass(UpdatePaymentMethodRequest, dict):
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
        if not isinstance(other, UpdatePaymentMethodRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
