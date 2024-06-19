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

class PutScheduledEventRequest(object):
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
        'active': 'bool',
        'condition': 'str',
        'description': 'str',
        'display_name': 'str',
        'hours': 'int',
        'minutes': 'int',
        'parameters': 'dict(str, PostScheduledEventRequestParametersValue)'
    }

    attribute_map = {
        'active': 'active',
        'condition': 'condition',
        'description': 'description',
        'display_name': 'displayName',
        'hours': 'hours',
        'minutes': 'minutes',
        'parameters': 'parameters'
    }

    def __init__(self, active=None, condition=None, description=None, display_name=None, hours=None, minutes=None, parameters=None):  # noqa: E501
        """PutScheduledEventRequest - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._condition = None
        self._description = None
        self._display_name = None
        self._hours = None
        self._minutes = None
        self._parameters = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if condition is not None:
            self.condition = condition
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if hours is not None:
            self.hours = hours
        if minutes is not None:
            self.minutes = minutes
        if parameters is not None:
            self.parameters = parameters

    @property
    def active(self):
        """Gets the active of this PutScheduledEventRequest.  # noqa: E501

        Indicate whether the scheduled event is active or inactive  # noqa: E501

        :return: The active of this PutScheduledEventRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PutScheduledEventRequest.

        Indicate whether the scheduled event is active or inactive  # noqa: E501

        :param active: The active of this PutScheduledEventRequest.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def condition(self):
        """Gets the condition of this PutScheduledEventRequest.  # noqa: E501

        The filter rule conditions, written in [JEXL](http://commons.apache.org/proper/commons-jexl/). The scheduled event is triggered only if the condition is evaluated as true. The rule might contain event context merge fields and data source merge fields. Data source merge fields must be from [the base object of the event or from the joined objects of the base object](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL#Data_Sources_and_Objects). Scheduled events with invalid merge fields will fail to evaluate, thus will not be triggered. For example, to trigger an invoice due date scheduled event to only invoices with an amount over 1000, you would define the following condition:  ```Invoice.Amount > 1000```  `Invoice.Amount` refers to the `Amount` field of the Zuora object `Invoice`.   # noqa: E501

        :return: The condition of this PutScheduledEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this PutScheduledEventRequest.

        The filter rule conditions, written in [JEXL](http://commons.apache.org/proper/commons-jexl/). The scheduled event is triggered only if the condition is evaluated as true. The rule might contain event context merge fields and data source merge fields. Data source merge fields must be from [the base object of the event or from the joined objects of the base object](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL#Data_Sources_and_Objects). Scheduled events with invalid merge fields will fail to evaluate, thus will not be triggered. For example, to trigger an invoice due date scheduled event to only invoices with an amount over 1000, you would define the following condition:  ```Invoice.Amount > 1000```  `Invoice.Amount` refers to the `Amount` field of the Zuora object `Invoice`.   # noqa: E501

        :param condition: The condition of this PutScheduledEventRequest.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def description(self):
        """Gets the description of this PutScheduledEventRequest.  # noqa: E501

        The description of the scheduled event.  # noqa: E501

        :return: The description of this PutScheduledEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutScheduledEventRequest.

        The description of the scheduled event.  # noqa: E501

        :param description: The description of this PutScheduledEventRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this PutScheduledEventRequest.  # noqa: E501

        The display name of the scheduled event.  # noqa: E501

        :return: The display_name of this PutScheduledEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PutScheduledEventRequest.

        The display name of the scheduled event.  # noqa: E501

        :param display_name: The display_name of this PutScheduledEventRequest.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def hours(self):
        """Gets the hours of this PutScheduledEventRequest.  # noqa: E501

        The scheduled time (hour) that the scheduled event notifications are sent. This time is based on the localized timezone of your tenant.  # noqa: E501

        :return: The hours of this PutScheduledEventRequest.  # noqa: E501
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this PutScheduledEventRequest.

        The scheduled time (hour) that the scheduled event notifications are sent. This time is based on the localized timezone of your tenant.  # noqa: E501

        :param hours: The hours of this PutScheduledEventRequest.  # noqa: E501
        :type: int
        """

        self._hours = hours

    @property
    def minutes(self):
        """Gets the minutes of this PutScheduledEventRequest.  # noqa: E501

        The scheduled time (minute) that the scheduled event notifications are sent. This time is based on the localized timezone of your tenant.  # noqa: E501

        :return: The minutes of this PutScheduledEventRequest.  # noqa: E501
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this PutScheduledEventRequest.

        The scheduled time (minute) that the scheduled event notifications are sent. This time is based on the localized timezone of your tenant.  # noqa: E501

        :param minutes: The minutes of this PutScheduledEventRequest.  # noqa: E501
        :type: int
        """

        self._minutes = minutes

    @property
    def parameters(self):
        """Gets the parameters of this PutScheduledEventRequest.  # noqa: E501

        The parameters of the filter rule. The names of the parameters must match with the filter rule and can't be duplicated.  # noqa: E501

        :return: The parameters of this PutScheduledEventRequest.  # noqa: E501
        :rtype: dict(str, PostScheduledEventRequestParametersValue)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this PutScheduledEventRequest.

        The parameters of the filter rule. The names of the parameters must match with the filter rule and can't be duplicated.  # noqa: E501

        :param parameters: The parameters of this PutScheduledEventRequest.  # noqa: E501
        :type: dict(str, PostScheduledEventRequestParametersValue)
        """

        self._parameters = parameters

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
        if issubclass(PutScheduledEventRequest, dict):
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
        if not isinstance(other, PutScheduledEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
