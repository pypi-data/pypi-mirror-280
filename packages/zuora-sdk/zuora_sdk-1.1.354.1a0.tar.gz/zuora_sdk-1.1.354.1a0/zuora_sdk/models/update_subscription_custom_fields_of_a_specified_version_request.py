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

class UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest(object):
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
        'custom_fields': 'dict(str, object)',
        'rate_plans': 'list[UpdateSubscriptionRatePlanCustomFieldsOfASpecifiedVersion]'
    }

    attribute_map = {
        'custom_fields': 'customFields',
        'rate_plans': 'ratePlans'
    }

    def __init__(self, custom_fields=None, rate_plans=None):  # noqa: E501
        """UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest - a model defined in Swagger"""  # noqa: E501
        self._custom_fields = None
        self._rate_plans = None
        self.discriminator = None
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if rate_plans is not None:
            self.rate_plans = rate_plans

    @property
    def custom_fields(self):
        """Gets the custom_fields of this UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest.  # noqa: E501

        Container for custom fields of a Subscription object.   # noqa: E501

        :return: The custom_fields of this UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest.

        Container for custom fields of a Subscription object.   # noqa: E501

        :param custom_fields: The custom_fields of this UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def rate_plans(self):
        """Gets the rate_plans of this UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest.  # noqa: E501


        :return: The rate_plans of this UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest.  # noqa: E501
        :rtype: list[UpdateSubscriptionRatePlanCustomFieldsOfASpecifiedVersion]
        """
        return self._rate_plans

    @rate_plans.setter
    def rate_plans(self, rate_plans):
        """Sets the rate_plans of this UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest.


        :param rate_plans: The rate_plans of this UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest.  # noqa: E501
        :type: list[UpdateSubscriptionRatePlanCustomFieldsOfASpecifiedVersion]
        """

        self._rate_plans = rate_plans

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
        if issubclass(UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest, dict):
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
        if not isinstance(other, UpdateSubscriptionCustomFieldsOfASpecifiedVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
