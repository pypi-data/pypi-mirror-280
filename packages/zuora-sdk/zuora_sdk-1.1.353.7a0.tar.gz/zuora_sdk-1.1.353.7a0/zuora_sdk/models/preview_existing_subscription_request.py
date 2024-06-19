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

class PreviewExistingSubscriptionRequest(object):
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
        'preview_start_date': 'PreviewStartDate',
        'preview_through_date': 'PreviewThroughDate',
        'quantity_for_usage_charges': 'list[QuantityForUsageCharges]'
    }

    attribute_map = {
        'preview_start_date': 'previewStartDate',
        'preview_through_date': 'previewThroughDate',
        'quantity_for_usage_charges': 'quantityForUsageCharges'
    }

    def __init__(self, preview_start_date=None, preview_through_date=None, quantity_for_usage_charges=None):  # noqa: E501
        """PreviewExistingSubscriptionRequest - a model defined in Swagger"""  # noqa: E501
        self._preview_start_date = None
        self._preview_through_date = None
        self._quantity_for_usage_charges = None
        self.discriminator = None
        if preview_start_date is not None:
            self.preview_start_date = preview_start_date
        if preview_through_date is not None:
            self.preview_through_date = preview_through_date
        if quantity_for_usage_charges is not None:
            self.quantity_for_usage_charges = quantity_for_usage_charges

    @property
    def preview_start_date(self):
        """Gets the preview_start_date of this PreviewExistingSubscriptionRequest.  # noqa: E501


        :return: The preview_start_date of this PreviewExistingSubscriptionRequest.  # noqa: E501
        :rtype: PreviewStartDate
        """
        return self._preview_start_date

    @preview_start_date.setter
    def preview_start_date(self, preview_start_date):
        """Sets the preview_start_date of this PreviewExistingSubscriptionRequest.


        :param preview_start_date: The preview_start_date of this PreviewExistingSubscriptionRequest.  # noqa: E501
        :type: PreviewStartDate
        """

        self._preview_start_date = preview_start_date

    @property
    def preview_through_date(self):
        """Gets the preview_through_date of this PreviewExistingSubscriptionRequest.  # noqa: E501


        :return: The preview_through_date of this PreviewExistingSubscriptionRequest.  # noqa: E501
        :rtype: PreviewThroughDate
        """
        return self._preview_through_date

    @preview_through_date.setter
    def preview_through_date(self, preview_through_date):
        """Sets the preview_through_date of this PreviewExistingSubscriptionRequest.


        :param preview_through_date: The preview_through_date of this PreviewExistingSubscriptionRequest.  # noqa: E501
        :type: PreviewThroughDate
        """

        self._preview_through_date = preview_through_date

    @property
    def quantity_for_usage_charges(self):
        """Gets the quantity_for_usage_charges of this PreviewExistingSubscriptionRequest.  # noqa: E501

        Container for usage charges.   # noqa: E501

        :return: The quantity_for_usage_charges of this PreviewExistingSubscriptionRequest.  # noqa: E501
        :rtype: list[QuantityForUsageCharges]
        """
        return self._quantity_for_usage_charges

    @quantity_for_usage_charges.setter
    def quantity_for_usage_charges(self, quantity_for_usage_charges):
        """Sets the quantity_for_usage_charges of this PreviewExistingSubscriptionRequest.

        Container for usage charges.   # noqa: E501

        :param quantity_for_usage_charges: The quantity_for_usage_charges of this PreviewExistingSubscriptionRequest.  # noqa: E501
        :type: list[QuantityForUsageCharges]
        """

        self._quantity_for_usage_charges = quantity_for_usage_charges

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
        if issubclass(PreviewExistingSubscriptionRequest, dict):
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
        if not isinstance(other, PreviewExistingSubscriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
