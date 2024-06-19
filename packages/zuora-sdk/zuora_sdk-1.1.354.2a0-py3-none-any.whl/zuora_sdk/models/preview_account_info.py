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

class PreviewAccountInfo(object):
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
        'bill_cycle_day': 'int',
        'currency': 'str',
        'custom_fields': 'dict(str, object)',
        'sold_to_contact': 'PreviewContactInfo',
        'tax_info': 'TaxInfo'
    }

    attribute_map = {
        'bill_cycle_day': 'billCycleDay',
        'currency': 'currency',
        'custom_fields': 'customFields',
        'sold_to_contact': 'soldToContact',
        'tax_info': 'taxInfo'
    }

    def __init__(self, bill_cycle_day=None, currency=None, custom_fields=None, sold_to_contact=None, tax_info=None):  # noqa: E501
        """PreviewAccountInfo - a model defined in Swagger"""  # noqa: E501
        self._bill_cycle_day = None
        self._currency = None
        self._custom_fields = None
        self._sold_to_contact = None
        self._tax_info = None
        self.discriminator = None
        self.bill_cycle_day = bill_cycle_day
        self.currency = currency
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if sold_to_contact is not None:
            self.sold_to_contact = sold_to_contact
        if tax_info is not None:
            self.tax_info = tax_info

    @property
    def bill_cycle_day(self):
        """Gets the bill_cycle_day of this PreviewAccountInfo.  # noqa: E501

        Day of the month that the account prefers billing periods to begin on. If set to 0, the bill cycle day will be set as \"AutoSet\".  # noqa: E501

        :return: The bill_cycle_day of this PreviewAccountInfo.  # noqa: E501
        :rtype: int
        """
        return self._bill_cycle_day

    @bill_cycle_day.setter
    def bill_cycle_day(self, bill_cycle_day):
        """Sets the bill_cycle_day of this PreviewAccountInfo.

        Day of the month that the account prefers billing periods to begin on. If set to 0, the bill cycle day will be set as \"AutoSet\".  # noqa: E501

        :param bill_cycle_day: The bill_cycle_day of this PreviewAccountInfo.  # noqa: E501
        :type: int
        """
        if bill_cycle_day is None:
            raise ValueError("Invalid value for `bill_cycle_day`, must not be `None`")  # noqa: E501

        self._bill_cycle_day = bill_cycle_day

    @property
    def currency(self):
        """Gets the currency of this PreviewAccountInfo.  # noqa: E501

        ISO 3-letter currency code (uppercase). For example, USD.   # noqa: E501

        :return: The currency of this PreviewAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PreviewAccountInfo.

        ISO 3-letter currency code (uppercase). For example, USD.   # noqa: E501

        :param currency: The currency of this PreviewAccountInfo.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def custom_fields(self):
        """Gets the custom_fields of this PreviewAccountInfo.  # noqa: E501

        Container for custom fields of an Account object.   # noqa: E501

        :return: The custom_fields of this PreviewAccountInfo.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this PreviewAccountInfo.

        Container for custom fields of an Account object.   # noqa: E501

        :param custom_fields: The custom_fields of this PreviewAccountInfo.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def sold_to_contact(self):
        """Gets the sold_to_contact of this PreviewAccountInfo.  # noqa: E501


        :return: The sold_to_contact of this PreviewAccountInfo.  # noqa: E501
        :rtype: PreviewContactInfo
        """
        return self._sold_to_contact

    @sold_to_contact.setter
    def sold_to_contact(self, sold_to_contact):
        """Sets the sold_to_contact of this PreviewAccountInfo.


        :param sold_to_contact: The sold_to_contact of this PreviewAccountInfo.  # noqa: E501
        :type: PreviewContactInfo
        """

        self._sold_to_contact = sold_to_contact

    @property
    def tax_info(self):
        """Gets the tax_info of this PreviewAccountInfo.  # noqa: E501


        :return: The tax_info of this PreviewAccountInfo.  # noqa: E501
        :rtype: TaxInfo
        """
        return self._tax_info

    @tax_info.setter
    def tax_info(self, tax_info):
        """Sets the tax_info of this PreviewAccountInfo.


        :param tax_info: The tax_info of this PreviewAccountInfo.  # noqa: E501
        :type: TaxInfo
        """

        self._tax_info = tax_info

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
        if issubclass(PreviewAccountInfo, dict):
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
        if not isinstance(other, PreviewAccountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
