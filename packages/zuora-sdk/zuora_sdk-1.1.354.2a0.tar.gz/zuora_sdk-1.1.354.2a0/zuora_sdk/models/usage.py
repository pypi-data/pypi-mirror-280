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

class Usage(object):
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
        '_date': 'str',
        'values': 'UsageValues'
    }

    attribute_map = {
        '_date': 'date',
        'values': 'values'
    }

    def __init__(self, _date=None, values=None):  # noqa: E501
        """Usage - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._values = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if values is not None:
            self.values = values

    @property
    def _date(self):
        """Gets the _date of this Usage.  # noqa: E501

        The date when the usage record is created.   # noqa: E501

        :return: The _date of this Usage.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Usage.

        The date when the usage record is created.   # noqa: E501

        :param _date: The _date of this Usage.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def values(self):
        """Gets the values of this Usage.  # noqa: E501


        :return: The values of this Usage.  # noqa: E501
        :rtype: UsageValues
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Usage.


        :param values: The values of this Usage.  # noqa: E501
        :type: UsageValues
        """

        self._values = values

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
        if issubclass(Usage, dict):
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
        if not isinstance(other, Usage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
