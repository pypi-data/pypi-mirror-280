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

class GetPaymentMethodResponseApplePayForAccount(object):
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
        'apple_bin': 'str',
        'apple_card_number': 'str',
        'apple_card_type': 'str',
        'apple_expiry_date': 'str',
        'apple_gateway_token': 'str'
    }

    attribute_map = {
        'apple_bin': 'appleBIN',
        'apple_card_number': 'appleCardNumber',
        'apple_card_type': 'appleCardType',
        'apple_expiry_date': 'appleExpiryDate',
        'apple_gateway_token': 'appleGatewayToken'
    }

    def __init__(self, apple_bin=None, apple_card_number=None, apple_card_type=None, apple_expiry_date=None, apple_gateway_token=None):  # noqa: E501
        """GetPaymentMethodResponseApplePayForAccount - a model defined in Swagger"""  # noqa: E501
        self._apple_bin = None
        self._apple_card_number = None
        self._apple_card_type = None
        self._apple_expiry_date = None
        self._apple_gateway_token = None
        self.discriminator = None
        if apple_bin is not None:
            self.apple_bin = apple_bin
        if apple_card_number is not None:
            self.apple_card_number = apple_card_number
        if apple_card_type is not None:
            self.apple_card_type = apple_card_type
        if apple_expiry_date is not None:
            self.apple_expiry_date = apple_expiry_date
        if apple_gateway_token is not None:
            self.apple_gateway_token = apple_gateway_token

    @property
    def apple_bin(self):
        """Gets the apple_bin of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501

        This field is only available for Apple Pay payment methods.   # noqa: E501

        :return: The apple_bin of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501
        :rtype: str
        """
        return self._apple_bin

    @apple_bin.setter
    def apple_bin(self, apple_bin):
        """Sets the apple_bin of this GetPaymentMethodResponseApplePayForAccount.

        This field is only available for Apple Pay payment methods.   # noqa: E501

        :param apple_bin: The apple_bin of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501
        :type: str
        """

        self._apple_bin = apple_bin

    @property
    def apple_card_number(self):
        """Gets the apple_card_number of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501

        This field is only available for Apple Pay payment methods.   # noqa: E501

        :return: The apple_card_number of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501
        :rtype: str
        """
        return self._apple_card_number

    @apple_card_number.setter
    def apple_card_number(self, apple_card_number):
        """Sets the apple_card_number of this GetPaymentMethodResponseApplePayForAccount.

        This field is only available for Apple Pay payment methods.   # noqa: E501

        :param apple_card_number: The apple_card_number of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501
        :type: str
        """

        self._apple_card_number = apple_card_number

    @property
    def apple_card_type(self):
        """Gets the apple_card_type of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501

        This field is only available for Apple Pay payment methods.  For Apple Pay payment methods on Adyen, the first 100 characters of [paymentMethodVariant](https://docs.adyen.com/development-resources/paymentmethodvariant) returned from Adyen are stored in this field.   # noqa: E501

        :return: The apple_card_type of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501
        :rtype: str
        """
        return self._apple_card_type

    @apple_card_type.setter
    def apple_card_type(self, apple_card_type):
        """Sets the apple_card_type of this GetPaymentMethodResponseApplePayForAccount.

        This field is only available for Apple Pay payment methods.  For Apple Pay payment methods on Adyen, the first 100 characters of [paymentMethodVariant](https://docs.adyen.com/development-resources/paymentmethodvariant) returned from Adyen are stored in this field.   # noqa: E501

        :param apple_card_type: The apple_card_type of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501
        :type: str
        """

        self._apple_card_type = apple_card_type

    @property
    def apple_expiry_date(self):
        """Gets the apple_expiry_date of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501

        This field is only available for Apple Pay payment methods.   # noqa: E501

        :return: The apple_expiry_date of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501
        :rtype: str
        """
        return self._apple_expiry_date

    @apple_expiry_date.setter
    def apple_expiry_date(self, apple_expiry_date):
        """Sets the apple_expiry_date of this GetPaymentMethodResponseApplePayForAccount.

        This field is only available for Apple Pay payment methods.   # noqa: E501

        :param apple_expiry_date: The apple_expiry_date of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501
        :type: str
        """

        self._apple_expiry_date = apple_expiry_date

    @property
    def apple_gateway_token(self):
        """Gets the apple_gateway_token of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501

        This field is only available for Apple Pay payment methods.   # noqa: E501

        :return: The apple_gateway_token of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501
        :rtype: str
        """
        return self._apple_gateway_token

    @apple_gateway_token.setter
    def apple_gateway_token(self, apple_gateway_token):
        """Sets the apple_gateway_token of this GetPaymentMethodResponseApplePayForAccount.

        This field is only available for Apple Pay payment methods.   # noqa: E501

        :param apple_gateway_token: The apple_gateway_token of this GetPaymentMethodResponseApplePayForAccount.  # noqa: E501
        :type: str
        """

        self._apple_gateway_token = apple_gateway_token

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
        if issubclass(GetPaymentMethodResponseApplePayForAccount, dict):
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
        if not isinstance(other, GetPaymentMethodResponseApplePayForAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
