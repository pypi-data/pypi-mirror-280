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

class InvoiceSchedule(object):
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
        'account_id': 'str',
        'actual_amount': 'float',
        'additional_subscriptions_to_bill': 'list[str]',
        'billed_amount': 'float',
        'id': 'str',
        'invoice_separately': 'bool',
        'next_run_date': 'date',
        'notes': 'str',
        'number': 'str',
        'orders': 'list[str]',
        'schedule_items': 'list[InvoiceScheduleItem]',
        'specific_subscriptions': 'list[InvoiceScheduleSubscription]',
        'status': 'InvoiceScheduleStatus',
        'total_amount': 'float',
        'unbilled_amount': 'float'
    }

    attribute_map = {
        'account_id': 'accountId',
        'actual_amount': 'actualAmount',
        'additional_subscriptions_to_bill': 'additionalSubscriptionsToBill',
        'billed_amount': 'billedAmount',
        'id': 'id',
        'invoice_separately': 'invoiceSeparately',
        'next_run_date': 'nextRunDate',
        'notes': 'notes',
        'number': 'number',
        'orders': 'orders',
        'schedule_items': 'scheduleItems',
        'specific_subscriptions': 'specificSubscriptions',
        'status': 'status',
        'total_amount': 'totalAmount',
        'unbilled_amount': 'unbilledAmount'
    }

    def __init__(self, account_id=None, actual_amount=None, additional_subscriptions_to_bill=None, billed_amount=None, id=None, invoice_separately=None, next_run_date=None, notes=None, number=None, orders=None, schedule_items=None, specific_subscriptions=None, status=None, total_amount=None, unbilled_amount=None):  # noqa: E501
        """InvoiceSchedule - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._actual_amount = None
        self._additional_subscriptions_to_bill = None
        self._billed_amount = None
        self._id = None
        self._invoice_separately = None
        self._next_run_date = None
        self._notes = None
        self._number = None
        self._orders = None
        self._schedule_items = None
        self._specific_subscriptions = None
        self._status = None
        self._total_amount = None
        self._unbilled_amount = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if actual_amount is not None:
            self.actual_amount = actual_amount
        if additional_subscriptions_to_bill is not None:
            self.additional_subscriptions_to_bill = additional_subscriptions_to_bill
        if billed_amount is not None:
            self.billed_amount = billed_amount
        if id is not None:
            self.id = id
        if invoice_separately is not None:
            self.invoice_separately = invoice_separately
        if next_run_date is not None:
            self.next_run_date = next_run_date
        if notes is not None:
            self.notes = notes
        if number is not None:
            self.number = number
        if orders is not None:
            self.orders = orders
        if schedule_items is not None:
            self.schedule_items = schedule_items
        if specific_subscriptions is not None:
            self.specific_subscriptions = specific_subscriptions
        if status is not None:
            self.status = status
        if total_amount is not None:
            self.total_amount = total_amount
        if unbilled_amount is not None:
            self.unbilled_amount = unbilled_amount

    @property
    def account_id(self):
        """Gets the account_id of this InvoiceSchedule.  # noqa: E501

        The ID of the customer account that the invoice schedule belongs to.   # noqa: E501

        :return: The account_id of this InvoiceSchedule.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InvoiceSchedule.

        The ID of the customer account that the invoice schedule belongs to.   # noqa: E501

        :param account_id: The account_id of this InvoiceSchedule.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def actual_amount(self):
        """Gets the actual_amount of this InvoiceSchedule.  # noqa: E501

        The actual amount that needs to be billed during the processing of the invoice schedule.  By default, the actual amount is the same as the total amount. Even if order changes occur like Remove Product or Cancel Subscription, the value of the `totalAmount` field keeps unchanged. The value of the `actualAmount` field reflects the actual amount to be billed.   # noqa: E501

        :return: The actual_amount of this InvoiceSchedule.  # noqa: E501
        :rtype: float
        """
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, actual_amount):
        """Sets the actual_amount of this InvoiceSchedule.

        The actual amount that needs to be billed during the processing of the invoice schedule.  By default, the actual amount is the same as the total amount. Even if order changes occur like Remove Product or Cancel Subscription, the value of the `totalAmount` field keeps unchanged. The value of the `actualAmount` field reflects the actual amount to be billed.   # noqa: E501

        :param actual_amount: The actual_amount of this InvoiceSchedule.  # noqa: E501
        :type: float
        """

        self._actual_amount = actual_amount

    @property
    def additional_subscriptions_to_bill(self):
        """Gets the additional_subscriptions_to_bill of this InvoiceSchedule.  # noqa: E501

        A list of the numbers of the subscriptions that need to be billed together with the invoice schedule.   One invoice schedule can have at most 600 additional subscriptions.   # noqa: E501

        :return: The additional_subscriptions_to_bill of this InvoiceSchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_subscriptions_to_bill

    @additional_subscriptions_to_bill.setter
    def additional_subscriptions_to_bill(self, additional_subscriptions_to_bill):
        """Sets the additional_subscriptions_to_bill of this InvoiceSchedule.

        A list of the numbers of the subscriptions that need to be billed together with the invoice schedule.   One invoice schedule can have at most 600 additional subscriptions.   # noqa: E501

        :param additional_subscriptions_to_bill: The additional_subscriptions_to_bill of this InvoiceSchedule.  # noqa: E501
        :type: list[str]
        """

        self._additional_subscriptions_to_bill = additional_subscriptions_to_bill

    @property
    def billed_amount(self):
        """Gets the billed_amount of this InvoiceSchedule.  # noqa: E501

        The amount that has been billed during the processing of the invoice schedule.   # noqa: E501

        :return: The billed_amount of this InvoiceSchedule.  # noqa: E501
        :rtype: float
        """
        return self._billed_amount

    @billed_amount.setter
    def billed_amount(self, billed_amount):
        """Sets the billed_amount of this InvoiceSchedule.

        The amount that has been billed during the processing of the invoice schedule.   # noqa: E501

        :param billed_amount: The billed_amount of this InvoiceSchedule.  # noqa: E501
        :type: float
        """

        self._billed_amount = billed_amount

    @property
    def id(self):
        """Gets the id of this InvoiceSchedule.  # noqa: E501

        The unique ID of the invoice schedule.   # noqa: E501

        :return: The id of this InvoiceSchedule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceSchedule.

        The unique ID of the invoice schedule.   # noqa: E501

        :param id: The id of this InvoiceSchedule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_separately(self):
        """Gets the invoice_separately of this InvoiceSchedule.  # noqa: E501

        Whether the invoice items created from the invoice schedule appears on a separate invoice when Zuora generates invoices.   # noqa: E501

        :return: The invoice_separately of this InvoiceSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_separately

    @invoice_separately.setter
    def invoice_separately(self, invoice_separately):
        """Sets the invoice_separately of this InvoiceSchedule.

        Whether the invoice items created from the invoice schedule appears on a separate invoice when Zuora generates invoices.   # noqa: E501

        :param invoice_separately: The invoice_separately of this InvoiceSchedule.  # noqa: E501
        :type: bool
        """

        self._invoice_separately = invoice_separately

    @property
    def next_run_date(self):
        """Gets the next_run_date of this InvoiceSchedule.  # noqa: E501

        The run date of the next execution of invoice schedule. By default, the next run date is the same as run date of next pending invoice schedule item. It can be overwritten with a different date other than the default value. When the invoice schedule has completed the execution, the next run date is null.   # noqa: E501

        :return: The next_run_date of this InvoiceSchedule.  # noqa: E501
        :rtype: date
        """
        return self._next_run_date

    @next_run_date.setter
    def next_run_date(self, next_run_date):
        """Sets the next_run_date of this InvoiceSchedule.

        The run date of the next execution of invoice schedule. By default, the next run date is the same as run date of next pending invoice schedule item. It can be overwritten with a different date other than the default value. When the invoice schedule has completed the execution, the next run date is null.   # noqa: E501

        :param next_run_date: The next_run_date of this InvoiceSchedule.  # noqa: E501
        :type: date
        """

        self._next_run_date = next_run_date

    @property
    def notes(self):
        """Gets the notes of this InvoiceSchedule.  # noqa: E501

        Comments on the invoice schedule.   # noqa: E501

        :return: The notes of this InvoiceSchedule.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this InvoiceSchedule.

        Comments on the invoice schedule.   # noqa: E501

        :param notes: The notes of this InvoiceSchedule.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def number(self):
        """Gets the number of this InvoiceSchedule.  # noqa: E501

        The sequence number of the invoice schedule.   # noqa: E501

        :return: The number of this InvoiceSchedule.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InvoiceSchedule.

        The sequence number of the invoice schedule.   # noqa: E501

        :param number: The number of this InvoiceSchedule.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def orders(self):
        """Gets the orders of this InvoiceSchedule.  # noqa: E501

        A list of the IDs or numbers of the orders associated with the invoice schedule. One invoice schedule can be associated with at most 10 orders.   # noqa: E501

        :return: The orders of this InvoiceSchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this InvoiceSchedule.

        A list of the IDs or numbers of the orders associated with the invoice schedule. One invoice schedule can be associated with at most 10 orders.   # noqa: E501

        :param orders: The orders of this InvoiceSchedule.  # noqa: E501
        :type: list[str]
        """

        self._orders = orders

    @property
    def schedule_items(self):
        """Gets the schedule_items of this InvoiceSchedule.  # noqa: E501

        Container for schedule items. One invoice schedule can have at most 50 invoice schedule items.   # noqa: E501

        :return: The schedule_items of this InvoiceSchedule.  # noqa: E501
        :rtype: list[InvoiceScheduleItem]
        """
        return self._schedule_items

    @schedule_items.setter
    def schedule_items(self, schedule_items):
        """Sets the schedule_items of this InvoiceSchedule.

        Container for schedule items. One invoice schedule can have at most 50 invoice schedule items.   # noqa: E501

        :param schedule_items: The schedule_items of this InvoiceSchedule.  # noqa: E501
        :type: list[InvoiceScheduleItem]
        """

        self._schedule_items = schedule_items

    @property
    def specific_subscriptions(self):
        """Gets the specific_subscriptions of this InvoiceSchedule.  # noqa: E501

        A list of the numbers of specific subscriptions associated with the invoice schedule.   # noqa: E501

        :return: The specific_subscriptions of this InvoiceSchedule.  # noqa: E501
        :rtype: list[InvoiceScheduleSubscription]
        """
        return self._specific_subscriptions

    @specific_subscriptions.setter
    def specific_subscriptions(self, specific_subscriptions):
        """Sets the specific_subscriptions of this InvoiceSchedule.

        A list of the numbers of specific subscriptions associated with the invoice schedule.   # noqa: E501

        :param specific_subscriptions: The specific_subscriptions of this InvoiceSchedule.  # noqa: E501
        :type: list[InvoiceScheduleSubscription]
        """

        self._specific_subscriptions = specific_subscriptions

    @property
    def status(self):
        """Gets the status of this InvoiceSchedule.  # noqa: E501


        :return: The status of this InvoiceSchedule.  # noqa: E501
        :rtype: InvoiceScheduleStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InvoiceSchedule.


        :param status: The status of this InvoiceSchedule.  # noqa: E501
        :type: InvoiceScheduleStatus
        """

        self._status = status

    @property
    def total_amount(self):
        """Gets the total_amount of this InvoiceSchedule.  # noqa: E501

        The total amount that needs to be billed during the processing of the invoice schedule.   The value of this field keeps unchanged once invoice schedule items are created.   # noqa: E501

        :return: The total_amount of this InvoiceSchedule.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this InvoiceSchedule.

        The total amount that needs to be billed during the processing of the invoice schedule.   The value of this field keeps unchanged once invoice schedule items are created.   # noqa: E501

        :param total_amount: The total_amount of this InvoiceSchedule.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def unbilled_amount(self):
        """Gets the unbilled_amount of this InvoiceSchedule.  # noqa: E501

        The amount that is waiting to be billed during the processing of the invoice schedule.   # noqa: E501

        :return: The unbilled_amount of this InvoiceSchedule.  # noqa: E501
        :rtype: float
        """
        return self._unbilled_amount

    @unbilled_amount.setter
    def unbilled_amount(self, unbilled_amount):
        """Sets the unbilled_amount of this InvoiceSchedule.

        The amount that is waiting to be billed during the processing of the invoice schedule.   # noqa: E501

        :param unbilled_amount: The unbilled_amount of this InvoiceSchedule.  # noqa: E501
        :type: float
        """

        self._unbilled_amount = unbilled_amount

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
        if issubclass(InvoiceSchedule, dict):
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
        if not isinstance(other, InvoiceSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
