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

class PostScheduledEventRequestParametersValue(object):
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
        'description': 'str',
        'display_name': 'str',
        'options': 'list[str]',
        'value_type': 'PostScheduledEventRequestParametersValueValueType'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'displayName',
        'options': 'options',
        'value_type': 'valueType'
    }

    def __init__(self, description=None, display_name=None, options=None, value_type=None):  # noqa: E501
        """PostScheduledEventRequestParametersValue - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._display_name = None
        self._options = None
        self._value_type = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if options is not None:
            self.options = options
        if value_type is not None:
            self.value_type = value_type

    @property
    def description(self):
        """Gets the description of this PostScheduledEventRequestParametersValue.  # noqa: E501

        The description of the parameter.  # noqa: E501

        :return: The description of this PostScheduledEventRequestParametersValue.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostScheduledEventRequestParametersValue.

        The description of the parameter.  # noqa: E501

        :param description: The description of this PostScheduledEventRequestParametersValue.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this PostScheduledEventRequestParametersValue.  # noqa: E501

        The display name of the parameter.  # noqa: E501

        :return: The display_name of this PostScheduledEventRequestParametersValue.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PostScheduledEventRequestParametersValue.

        The display name of the parameter.  # noqa: E501

        :param display_name: The display_name of this PostScheduledEventRequestParametersValue.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def options(self):
        """Gets the options of this PostScheduledEventRequestParametersValue.  # noqa: E501

        The option values of the parameter.  # noqa: E501

        :return: The options of this PostScheduledEventRequestParametersValue.  # noqa: E501
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PostScheduledEventRequestParametersValue.

        The option values of the parameter.  # noqa: E501

        :param options: The options of this PostScheduledEventRequestParametersValue.  # noqa: E501
        :type: list[str]
        """

        self._options = options

    @property
    def value_type(self):
        """Gets the value_type of this PostScheduledEventRequestParametersValue.  # noqa: E501


        :return: The value_type of this PostScheduledEventRequestParametersValue.  # noqa: E501
        :rtype: PostScheduledEventRequestParametersValueValueType
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this PostScheduledEventRequestParametersValue.


        :param value_type: The value_type of this PostScheduledEventRequestParametersValue.  # noqa: E501
        :type: PostScheduledEventRequestParametersValueValueType
        """

        self._value_type = value_type

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
        if issubclass(PostScheduledEventRequestParametersValue, dict):
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
        if not isinstance(other, PostScheduledEventRequestParametersValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
