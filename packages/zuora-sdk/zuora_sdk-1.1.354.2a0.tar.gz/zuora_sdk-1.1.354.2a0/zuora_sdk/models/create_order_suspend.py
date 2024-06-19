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

class CreateOrderSuspend(object):
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
        'suspend_periods': 'int',
        'suspend_periods_type': 'SuspendPeriodsType',
        'suspend_policy': 'SuspendPolicy',
        'suspend_specific_date': 'date'
    }

    attribute_map = {
        'suspend_periods': 'suspendPeriods',
        'suspend_periods_type': 'suspendPeriodsType',
        'suspend_policy': 'suspendPolicy',
        'suspend_specific_date': 'suspendSpecificDate'
    }

    def __init__(self, suspend_periods=None, suspend_periods_type=None, suspend_policy=None, suspend_specific_date=None):  # noqa: E501
        """CreateOrderSuspend - a model defined in Swagger"""  # noqa: E501
        self._suspend_periods = None
        self._suspend_periods_type = None
        self._suspend_policy = None
        self._suspend_specific_date = None
        self.discriminator = None
        if suspend_periods is not None:
            self.suspend_periods = suspend_periods
        if suspend_periods_type is not None:
            self.suspend_periods_type = suspend_periods_type
        self.suspend_policy = suspend_policy
        if suspend_specific_date is not None:
            self.suspend_specific_date = suspend_specific_date

    @property
    def suspend_periods(self):
        """Gets the suspend_periods of this CreateOrderSuspend.  # noqa: E501

        This field is applicable only when the `suspendPolicy` field is set to `FixedPeriodsFromToday`. It must be used together with the `suspendPeriodsType` field.   The total number of the periods used to specify when a subscription suspension takes effect. The subscription suspension will take place after the specified time frame (`suspendPeriods` multiplied by `suspendPeriodsType`) from today's date.    # noqa: E501

        :return: The suspend_periods of this CreateOrderSuspend.  # noqa: E501
        :rtype: int
        """
        return self._suspend_periods

    @suspend_periods.setter
    def suspend_periods(self, suspend_periods):
        """Sets the suspend_periods of this CreateOrderSuspend.

        This field is applicable only when the `suspendPolicy` field is set to `FixedPeriodsFromToday`. It must be used together with the `suspendPeriodsType` field.   The total number of the periods used to specify when a subscription suspension takes effect. The subscription suspension will take place after the specified time frame (`suspendPeriods` multiplied by `suspendPeriodsType`) from today's date.    # noqa: E501

        :param suspend_periods: The suspend_periods of this CreateOrderSuspend.  # noqa: E501
        :type: int
        """

        self._suspend_periods = suspend_periods

    @property
    def suspend_periods_type(self):
        """Gets the suspend_periods_type of this CreateOrderSuspend.  # noqa: E501


        :return: The suspend_periods_type of this CreateOrderSuspend.  # noqa: E501
        :rtype: SuspendPeriodsType
        """
        return self._suspend_periods_type

    @suspend_periods_type.setter
    def suspend_periods_type(self, suspend_periods_type):
        """Sets the suspend_periods_type of this CreateOrderSuspend.


        :param suspend_periods_type: The suspend_periods_type of this CreateOrderSuspend.  # noqa: E501
        :type: SuspendPeriodsType
        """

        self._suspend_periods_type = suspend_periods_type

    @property
    def suspend_policy(self):
        """Gets the suspend_policy of this CreateOrderSuspend.  # noqa: E501


        :return: The suspend_policy of this CreateOrderSuspend.  # noqa: E501
        :rtype: SuspendPolicy
        """
        return self._suspend_policy

    @suspend_policy.setter
    def suspend_policy(self, suspend_policy):
        """Sets the suspend_policy of this CreateOrderSuspend.


        :param suspend_policy: The suspend_policy of this CreateOrderSuspend.  # noqa: E501
        :type: SuspendPolicy
        """
        if suspend_policy is None:
            raise ValueError("Invalid value for `suspend_policy`, must not be `None`")  # noqa: E501

        self._suspend_policy = suspend_policy

    @property
    def suspend_specific_date(self):
        """Gets the suspend_specific_date of this CreateOrderSuspend.  # noqa: E501

        This field is applicable only when the `suspendPolicy` field is set to `SpecificDate`.  A specific date when the subscription suspension takes effect, in YYYY-MM-DD format. The value should not be earlier than the subscription's contract effective date or later than the subscription's term end date.   # noqa: E501

        :return: The suspend_specific_date of this CreateOrderSuspend.  # noqa: E501
        :rtype: date
        """
        return self._suspend_specific_date

    @suspend_specific_date.setter
    def suspend_specific_date(self, suspend_specific_date):
        """Sets the suspend_specific_date of this CreateOrderSuspend.

        This field is applicable only when the `suspendPolicy` field is set to `SpecificDate`.  A specific date when the subscription suspension takes effect, in YYYY-MM-DD format. The value should not be earlier than the subscription's contract effective date or later than the subscription's term end date.   # noqa: E501

        :param suspend_specific_date: The suspend_specific_date of this CreateOrderSuspend.  # noqa: E501
        :type: date
        """

        self._suspend_specific_date = suspend_specific_date

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
        if issubclass(CreateOrderSuspend, dict):
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
        if not isinstance(other, CreateOrderSuspend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
