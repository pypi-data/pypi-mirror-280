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

class PreviewStartDate(object):
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
        'preview_start_date_policy': 'PreviewStartDatePolicy',
        'specific_date': 'str'
    }

    attribute_map = {
        'preview_start_date_policy': 'previewStartDatePolicy',
        'specific_date': 'specificDate'
    }

    def __init__(self, preview_start_date_policy=None, specific_date=None):  # noqa: E501
        """PreviewStartDate - a model defined in Swagger"""  # noqa: E501
        self._preview_start_date_policy = None
        self._specific_date = None
        self.discriminator = None
        if preview_start_date_policy is not None:
            self.preview_start_date_policy = preview_start_date_policy
        if specific_date is not None:
            self.specific_date = specific_date

    @property
    def preview_start_date_policy(self):
        """Gets the preview_start_date_policy of this PreviewStartDate.  # noqa: E501


        :return: The preview_start_date_policy of this PreviewStartDate.  # noqa: E501
        :rtype: PreviewStartDatePolicy
        """
        return self._preview_start_date_policy

    @preview_start_date_policy.setter
    def preview_start_date_policy(self, preview_start_date_policy):
        """Sets the preview_start_date_policy of this PreviewStartDate.


        :param preview_start_date_policy: The preview_start_date_policy of this PreviewStartDate.  # noqa: E501
        :type: PreviewStartDatePolicy
        """

        self._preview_start_date_policy = preview_start_date_policy

    @property
    def specific_date(self):
        """Gets the specific_date of this PreviewStartDate.  # noqa: E501

        The specific date for the preview start date. Required if `previewStartDatePolicy` is `specificDate`.   # noqa: E501

        :return: The specific_date of this PreviewStartDate.  # noqa: E501
        :rtype: str
        """
        return self._specific_date

    @specific_date.setter
    def specific_date(self, specific_date):
        """Sets the specific_date of this PreviewStartDate.

        The specific date for the preview start date. Required if `previewStartDatePolicy` is `specificDate`.   # noqa: E501

        :param specific_date: The specific_date of this PreviewStartDate.  # noqa: E501
        :type: str
        """

        self._specific_date = specific_date

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
        if issubclass(PreviewStartDate, dict):
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
        if not isinstance(other, PreviewStartDate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
