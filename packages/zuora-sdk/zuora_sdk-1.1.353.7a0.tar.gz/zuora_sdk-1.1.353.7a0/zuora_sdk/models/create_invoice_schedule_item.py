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

class CreateInvoiceScheduleItem(object):
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
        'amount': 'float',
        'name': 'str',
        'percentage': 'float',
        'run_date': 'date',
        'target_date_for_additional_subscriptions': 'date'
    }

    attribute_map = {
        'amount': 'amount',
        'name': 'name',
        'percentage': 'percentage',
        'run_date': 'runDate',
        'target_date_for_additional_subscriptions': 'targetDateForAdditionalSubscriptions'
    }

    def __init__(self, amount=None, name=None, percentage=None, run_date=None, target_date_for_additional_subscriptions=None):  # noqa: E501
        """CreateInvoiceScheduleItem - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._name = None
        self._percentage = None
        self._run_date = None
        self._target_date_for_additional_subscriptions = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if name is not None:
            self.name = name
        if percentage is not None:
            self.percentage = percentage
        if run_date is not None:
            self.run_date = run_date
        if target_date_for_additional_subscriptions is not None:
            self.target_date_for_additional_subscriptions = target_date_for_additional_subscriptions

    @property
    def amount(self):
        """Gets the amount of this CreateInvoiceScheduleItem.  # noqa: E501

        The amount of the invoice to be generated during the processing of the invoice schedule item. You can only specify one of the `amount` and `percentage` fields.   # noqa: E501

        :return: The amount of this CreateInvoiceScheduleItem.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateInvoiceScheduleItem.

        The amount of the invoice to be generated during the processing of the invoice schedule item. You can only specify one of the `amount` and `percentage` fields.   # noqa: E501

        :param amount: The amount of this CreateInvoiceScheduleItem.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def name(self):
        """Gets the name of this CreateInvoiceScheduleItem.  # noqa: E501

        The name of the invoice schedule item.   # noqa: E501

        :return: The name of this CreateInvoiceScheduleItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInvoiceScheduleItem.

        The name of the invoice schedule item.   # noqa: E501

        :param name: The name of this CreateInvoiceScheduleItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def percentage(self):
        """Gets the percentage of this CreateInvoiceScheduleItem.  # noqa: E501

        The percentage of the total amount to be generated during the processing of the invoice schedule item. The field value must be greater than 0. You can only specify one of the `amount` and `percentage` fields.  # noqa: E501

        :return: The percentage of this CreateInvoiceScheduleItem.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this CreateInvoiceScheduleItem.

        The percentage of the total amount to be generated during the processing of the invoice schedule item. The field value must be greater than 0. You can only specify one of the `amount` and `percentage` fields.  # noqa: E501

        :param percentage: The percentage of this CreateInvoiceScheduleItem.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def run_date(self):
        """Gets the run_date of this CreateInvoiceScheduleItem.  # noqa: E501

        The date in the tenant’s time zone when the invoice schedule item is planned to be processed to generate an invoice.   When specifying run dates for invoice schedule items, consider that: - An invoice schedule item with a blank run date will not be executed. - You can only update the run date for an invoice schedule item in Pending status. - If the run date of an invoice schedule item is left empty, the dates of all subsequent invoice schedule items must also be blank. - You must specify run dates in chronological order for invoice schedule items.                     # noqa: E501

        :return: The run_date of this CreateInvoiceScheduleItem.  # noqa: E501
        :rtype: date
        """
        return self._run_date

    @run_date.setter
    def run_date(self, run_date):
        """Sets the run_date of this CreateInvoiceScheduleItem.

        The date in the tenant’s time zone when the invoice schedule item is planned to be processed to generate an invoice.   When specifying run dates for invoice schedule items, consider that: - An invoice schedule item with a blank run date will not be executed. - You can only update the run date for an invoice schedule item in Pending status. - If the run date of an invoice schedule item is left empty, the dates of all subsequent invoice schedule items must also be blank. - You must specify run dates in chronological order for invoice schedule items.                     # noqa: E501

        :param run_date: The run_date of this CreateInvoiceScheduleItem.  # noqa: E501
        :type: date
        """

        self._run_date = run_date

    @property
    def target_date_for_additional_subscriptions(self):
        """Gets the target_date_for_additional_subscriptions of this CreateInvoiceScheduleItem.  # noqa: E501

        The date in the tenant's time zone used by the invoice schedule to determine which fixed-period regular charges to be billed together with the invoice schedule item.   The regular charges must come from the subscriptions specified in the `additionalSubscriptionsToBill` field.   # noqa: E501

        :return: The target_date_for_additional_subscriptions of this CreateInvoiceScheduleItem.  # noqa: E501
        :rtype: date
        """
        return self._target_date_for_additional_subscriptions

    @target_date_for_additional_subscriptions.setter
    def target_date_for_additional_subscriptions(self, target_date_for_additional_subscriptions):
        """Sets the target_date_for_additional_subscriptions of this CreateInvoiceScheduleItem.

        The date in the tenant's time zone used by the invoice schedule to determine which fixed-period regular charges to be billed together with the invoice schedule item.   The regular charges must come from the subscriptions specified in the `additionalSubscriptionsToBill` field.   # noqa: E501

        :param target_date_for_additional_subscriptions: The target_date_for_additional_subscriptions of this CreateInvoiceScheduleItem.  # noqa: E501
        :type: date
        """

        self._target_date_for_additional_subscriptions = target_date_for_additional_subscriptions

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
        if issubclass(CreateInvoiceScheduleItem, dict):
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
        if not isinstance(other, CreateInvoiceScheduleItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
