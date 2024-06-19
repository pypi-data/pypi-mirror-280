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

class SubscriptionTaxationItem(object):
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
        'exempt_amount': 'float',
        'jurisdiction': 'str',
        'location_code': 'str',
        'name': 'str',
        'tax_amount': 'float',
        'tax_code': 'str',
        'tax_code_description': 'str',
        'tax_date': 'str',
        'tax_rate': 'float',
        'tax_rate_description': 'str',
        'tax_rate_type': 'TaxRateType'
    }

    attribute_map = {
        'exempt_amount': 'exemptAmount',
        'jurisdiction': 'jurisdiction',
        'location_code': 'locationCode',
        'name': 'name',
        'tax_amount': 'taxAmount',
        'tax_code': 'taxCode',
        'tax_code_description': 'taxCodeDescription',
        'tax_date': 'taxDate',
        'tax_rate': 'taxRate',
        'tax_rate_description': 'taxRateDescription',
        'tax_rate_type': 'taxRateType'
    }

    def __init__(self, exempt_amount=None, jurisdiction=None, location_code=None, name=None, tax_amount=None, tax_code=None, tax_code_description=None, tax_date=None, tax_rate=None, tax_rate_description=None, tax_rate_type=None):  # noqa: E501
        """SubscriptionTaxationItem - a model defined in Swagger"""  # noqa: E501
        self._exempt_amount = None
        self._jurisdiction = None
        self._location_code = None
        self._name = None
        self._tax_amount = None
        self._tax_code = None
        self._tax_code_description = None
        self._tax_date = None
        self._tax_rate = None
        self._tax_rate_description = None
        self._tax_rate_type = None
        self.discriminator = None
        if exempt_amount is not None:
            self.exempt_amount = exempt_amount
        if jurisdiction is not None:
            self.jurisdiction = jurisdiction
        if location_code is not None:
            self.location_code = location_code
        if name is not None:
            self.name = name
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if tax_code is not None:
            self.tax_code = tax_code
        if tax_code_description is not None:
            self.tax_code_description = tax_code_description
        if tax_date is not None:
            self.tax_date = tax_date
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if tax_rate_description is not None:
            self.tax_rate_description = tax_rate_description
        if tax_rate_type is not None:
            self.tax_rate_type = tax_rate_type

    @property
    def exempt_amount(self):
        """Gets the exempt_amount of this SubscriptionTaxationItem.  # noqa: E501

        The calculated tax amount excluded due to the exemption.   # noqa: E501

        :return: The exempt_amount of this SubscriptionTaxationItem.  # noqa: E501
        :rtype: float
        """
        return self._exempt_amount

    @exempt_amount.setter
    def exempt_amount(self, exempt_amount):
        """Sets the exempt_amount of this SubscriptionTaxationItem.

        The calculated tax amount excluded due to the exemption.   # noqa: E501

        :param exempt_amount: The exempt_amount of this SubscriptionTaxationItem.  # noqa: E501
        :type: float
        """

        self._exempt_amount = exempt_amount

    @property
    def jurisdiction(self):
        """Gets the jurisdiction of this SubscriptionTaxationItem.  # noqa: E501

        The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.   # noqa: E501

        :return: The jurisdiction of this SubscriptionTaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._jurisdiction

    @jurisdiction.setter
    def jurisdiction(self, jurisdiction):
        """Sets the jurisdiction of this SubscriptionTaxationItem.

        The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.   # noqa: E501

        :param jurisdiction: The jurisdiction of this SubscriptionTaxationItem.  # noqa: E501
        :type: str
        """

        self._jurisdiction = jurisdiction

    @property
    def location_code(self):
        """Gets the location_code of this SubscriptionTaxationItem.  # noqa: E501

        The identifier for the location based on the value of the taxCode field.   # noqa: E501

        :return: The location_code of this SubscriptionTaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._location_code

    @location_code.setter
    def location_code(self, location_code):
        """Sets the location_code of this SubscriptionTaxationItem.

        The identifier for the location based on the value of the taxCode field.   # noqa: E501

        :param location_code: The location_code of this SubscriptionTaxationItem.  # noqa: E501
        :type: str
        """

        self._location_code = location_code

    @property
    def name(self):
        """Gets the name of this SubscriptionTaxationItem.  # noqa: E501

        The name of the taxation item.   # noqa: E501

        :return: The name of this SubscriptionTaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionTaxationItem.

        The name of the taxation item.   # noqa: E501

        :param name: The name of this SubscriptionTaxationItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tax_amount(self):
        """Gets the tax_amount of this SubscriptionTaxationItem.  # noqa: E501

        The tax amount of the invoice item.   # noqa: E501

        :return: The tax_amount of this SubscriptionTaxationItem.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this SubscriptionTaxationItem.

        The tax amount of the invoice item.   # noqa: E501

        :param tax_amount: The tax_amount of this SubscriptionTaxationItem.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def tax_code(self):
        """Gets the tax_code of this SubscriptionTaxationItem.  # noqa: E501

        The tax code identifies which tax rules and tax rates to apply to a specific invoice.   # noqa: E501

        :return: The tax_code of this SubscriptionTaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._tax_code

    @tax_code.setter
    def tax_code(self, tax_code):
        """Sets the tax_code of this SubscriptionTaxationItem.

        The tax code identifies which tax rules and tax rates to apply to a specific invoice.   # noqa: E501

        :param tax_code: The tax_code of this SubscriptionTaxationItem.  # noqa: E501
        :type: str
        """

        self._tax_code = tax_code

    @property
    def tax_code_description(self):
        """Gets the tax_code_description of this SubscriptionTaxationItem.  # noqa: E501

        The description of the tax code.   # noqa: E501

        :return: The tax_code_description of this SubscriptionTaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._tax_code_description

    @tax_code_description.setter
    def tax_code_description(self, tax_code_description):
        """Sets the tax_code_description of this SubscriptionTaxationItem.

        The description of the tax code.   # noqa: E501

        :param tax_code_description: The tax_code_description of this SubscriptionTaxationItem.  # noqa: E501
        :type: str
        """

        self._tax_code_description = tax_code_description

    @property
    def tax_date(self):
        """Gets the tax_date of this SubscriptionTaxationItem.  # noqa: E501

        The date when the tax is applied to the invoice.   # noqa: E501

        :return: The tax_date of this SubscriptionTaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._tax_date

    @tax_date.setter
    def tax_date(self, tax_date):
        """Sets the tax_date of this SubscriptionTaxationItem.

        The date when the tax is applied to the invoice.   # noqa: E501

        :param tax_date: The tax_date of this SubscriptionTaxationItem.  # noqa: E501
        :type: str
        """

        self._tax_date = tax_date

    @property
    def tax_rate(self):
        """Gets the tax_rate of this SubscriptionTaxationItem.  # noqa: E501

        The tax rate applied to the invoice.   # noqa: E501

        :return: The tax_rate of this SubscriptionTaxationItem.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this SubscriptionTaxationItem.

        The tax rate applied to the invoice.   # noqa: E501

        :param tax_rate: The tax_rate of this SubscriptionTaxationItem.  # noqa: E501
        :type: float
        """

        self._tax_rate = tax_rate

    @property
    def tax_rate_description(self):
        """Gets the tax_rate_description of this SubscriptionTaxationItem.  # noqa: E501

        The description of the tax rate.   # noqa: E501

        :return: The tax_rate_description of this SubscriptionTaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._tax_rate_description

    @tax_rate_description.setter
    def tax_rate_description(self, tax_rate_description):
        """Sets the tax_rate_description of this SubscriptionTaxationItem.

        The description of the tax rate.   # noqa: E501

        :param tax_rate_description: The tax_rate_description of this SubscriptionTaxationItem.  # noqa: E501
        :type: str
        """

        self._tax_rate_description = tax_rate_description

    @property
    def tax_rate_type(self):
        """Gets the tax_rate_type of this SubscriptionTaxationItem.  # noqa: E501


        :return: The tax_rate_type of this SubscriptionTaxationItem.  # noqa: E501
        :rtype: TaxRateType
        """
        return self._tax_rate_type

    @tax_rate_type.setter
    def tax_rate_type(self, tax_rate_type):
        """Sets the tax_rate_type of this SubscriptionTaxationItem.


        :param tax_rate_type: The tax_rate_type of this SubscriptionTaxationItem.  # noqa: E501
        :type: TaxRateType
        """

        self._tax_rate_type = tax_rate_type

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
        if issubclass(SubscriptionTaxationItem, dict):
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
        if not isinstance(other, SubscriptionTaxationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
