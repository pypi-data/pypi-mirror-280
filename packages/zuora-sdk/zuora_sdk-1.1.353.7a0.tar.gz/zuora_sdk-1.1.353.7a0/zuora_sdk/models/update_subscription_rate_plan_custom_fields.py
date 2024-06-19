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

class UpdateSubscriptionRatePlanCustomFields(object):
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
        'charges': 'list[UpdateSubscriptionChargeCustomFields]',
        'custom_fields': 'dict(str, object)',
        'rate_plan_id': 'str'
    }

    attribute_map = {
        'charges': 'charges',
        'custom_fields': 'customFields',
        'rate_plan_id': 'ratePlanId'
    }

    def __init__(self, charges=None, custom_fields=None, rate_plan_id=None):  # noqa: E501
        """UpdateSubscriptionRatePlanCustomFields - a model defined in Swagger"""  # noqa: E501
        self._charges = None
        self._custom_fields = None
        self._rate_plan_id = None
        self.discriminator = None
        if charges is not None:
            self.charges = charges
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if rate_plan_id is not None:
            self.rate_plan_id = rate_plan_id

    @property
    def charges(self):
        """Gets the charges of this UpdateSubscriptionRatePlanCustomFields.  # noqa: E501


        :return: The charges of this UpdateSubscriptionRatePlanCustomFields.  # noqa: E501
        :rtype: list[UpdateSubscriptionChargeCustomFields]
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this UpdateSubscriptionRatePlanCustomFields.


        :param charges: The charges of this UpdateSubscriptionRatePlanCustomFields.  # noqa: E501
        :type: list[UpdateSubscriptionChargeCustomFields]
        """

        self._charges = charges

    @property
    def custom_fields(self):
        """Gets the custom_fields of this UpdateSubscriptionRatePlanCustomFields.  # noqa: E501

        Container for custom fields of the Rate Plan object. The custom fields of the Rate Plan object are used when rate plans are subscribed.   # noqa: E501

        :return: The custom_fields of this UpdateSubscriptionRatePlanCustomFields.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this UpdateSubscriptionRatePlanCustomFields.

        Container for custom fields of the Rate Plan object. The custom fields of the Rate Plan object are used when rate plans are subscribed.   # noqa: E501

        :param custom_fields: The custom_fields of this UpdateSubscriptionRatePlanCustomFields.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def rate_plan_id(self):
        """Gets the rate_plan_id of this UpdateSubscriptionRatePlanCustomFields.  # noqa: E501

        The rate plan id in any version of the subscription. This will be linked to the only one rate plan in the current version.  # noqa: E501

        :return: The rate_plan_id of this UpdateSubscriptionRatePlanCustomFields.  # noqa: E501
        :rtype: str
        """
        return self._rate_plan_id

    @rate_plan_id.setter
    def rate_plan_id(self, rate_plan_id):
        """Sets the rate_plan_id of this UpdateSubscriptionRatePlanCustomFields.

        The rate plan id in any version of the subscription. This will be linked to the only one rate plan in the current version.  # noqa: E501

        :param rate_plan_id: The rate_plan_id of this UpdateSubscriptionRatePlanCustomFields.  # noqa: E501
        :type: str
        """

        self._rate_plan_id = rate_plan_id

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
        if issubclass(UpdateSubscriptionRatePlanCustomFields, dict):
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
        if not isinstance(other, UpdateSubscriptionRatePlanCustomFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
