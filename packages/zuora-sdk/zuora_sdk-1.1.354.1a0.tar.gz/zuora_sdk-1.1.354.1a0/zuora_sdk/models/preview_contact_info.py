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

class PreviewContactInfo(object):
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
        'city': 'str',
        'country': 'str',
        'county': 'str',
        'postal_code': 'str',
        'state': 'str',
        'tax_region': 'str'
    }

    attribute_map = {
        'city': 'city',
        'country': 'country',
        'county': 'county',
        'postal_code': 'postalCode',
        'state': 'state',
        'tax_region': 'taxRegion'
    }

    def __init__(self, city=None, country=None, county=None, postal_code=None, state=None, tax_region=None):  # noqa: E501
        """PreviewContactInfo - a model defined in Swagger"""  # noqa: E501
        self._city = None
        self._country = None
        self._county = None
        self._postal_code = None
        self._state = None
        self._tax_region = None
        self.discriminator = None
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if county is not None:
            self.county = county
        if postal_code is not None:
            self.postal_code = postal_code
        if state is not None:
            self.state = state
        if tax_region is not None:
            self.tax_region = tax_region

    @property
    def city(self):
        """Gets the city of this PreviewContactInfo.  # noqa: E501


        :return: The city of this PreviewContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PreviewContactInfo.


        :param city: The city of this PreviewContactInfo.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this PreviewContactInfo.  # noqa: E501

        Country; must be a valid country name or abbreviation. If using Zuora Tax, you must specify a country to calculate tax.  # noqa: E501

        :return: The country of this PreviewContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PreviewContactInfo.

        Country; must be a valid country name or abbreviation. If using Zuora Tax, you must specify a country to calculate tax.  # noqa: E501

        :param country: The country of this PreviewContactInfo.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def county(self):
        """Gets the county of this PreviewContactInfo.  # noqa: E501


        :return: The county of this PreviewContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this PreviewContactInfo.


        :param county: The county of this PreviewContactInfo.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def postal_code(self):
        """Gets the postal_code of this PreviewContactInfo.  # noqa: E501


        :return: The postal_code of this PreviewContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this PreviewContactInfo.


        :param postal_code: The postal_code of this PreviewContactInfo.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """Gets the state of this PreviewContactInfo.  # noqa: E501


        :return: The state of this PreviewContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PreviewContactInfo.


        :param state: The state of this PreviewContactInfo.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def tax_region(self):
        """Gets the tax_region of this PreviewContactInfo.  # noqa: E501


        :return: The tax_region of this PreviewContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._tax_region

    @tax_region.setter
    def tax_region(self, tax_region):
        """Sets the tax_region of this PreviewContactInfo.


        :param tax_region: The tax_region of this PreviewContactInfo.  # noqa: E501
        :type: str
        """

        self._tax_region = tax_region

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
        if issubclass(PreviewContactInfo, dict):
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
        if not isinstance(other, PreviewContactInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
