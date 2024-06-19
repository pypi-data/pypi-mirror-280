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

class TimeSlicedMetrics(object):
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
        'end_date': 'date',
        'generated_reason': 'TimeSlicedMetricsGeneratedReason',
        'invoice_owner': 'str',
        'order_item_id': 'str',
        'start_date': 'date',
        'subscription_owner': 'str',
        'term_number': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'end_date': 'endDate',
        'generated_reason': 'generatedReason',
        'invoice_owner': 'invoiceOwner',
        'order_item_id': 'orderItemId',
        'start_date': 'startDate',
        'subscription_owner': 'subscriptionOwner',
        'term_number': 'termNumber'
    }

    def __init__(self, amount=None, end_date=None, generated_reason=None, invoice_owner=None, order_item_id=None, start_date=None, subscription_owner=None, term_number=None):  # noqa: E501
        """TimeSlicedMetrics - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._end_date = None
        self._generated_reason = None
        self._invoice_owner = None
        self._order_item_id = None
        self._start_date = None
        self._subscription_owner = None
        self._term_number = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if end_date is not None:
            self.end_date = end_date
        if generated_reason is not None:
            self.generated_reason = generated_reason
        if invoice_owner is not None:
            self.invoice_owner = invoice_owner
        if order_item_id is not None:
            self.order_item_id = order_item_id
        if start_date is not None:
            self.start_date = start_date
        if subscription_owner is not None:
            self.subscription_owner = subscription_owner
        if term_number is not None:
            self.term_number = term_number

    @property
    def amount(self):
        """Gets the amount of this TimeSlicedMetrics.  # noqa: E501


        :return: The amount of this TimeSlicedMetrics.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TimeSlicedMetrics.


        :param amount: The amount of this TimeSlicedMetrics.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def end_date(self):
        """Gets the end_date of this TimeSlicedMetrics.  # noqa: E501


        :return: The end_date of this TimeSlicedMetrics.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TimeSlicedMetrics.


        :param end_date: The end_date of this TimeSlicedMetrics.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def generated_reason(self):
        """Gets the generated_reason of this TimeSlicedMetrics.  # noqa: E501


        :return: The generated_reason of this TimeSlicedMetrics.  # noqa: E501
        :rtype: TimeSlicedMetricsGeneratedReason
        """
        return self._generated_reason

    @generated_reason.setter
    def generated_reason(self, generated_reason):
        """Sets the generated_reason of this TimeSlicedMetrics.


        :param generated_reason: The generated_reason of this TimeSlicedMetrics.  # noqa: E501
        :type: TimeSlicedMetricsGeneratedReason
        """

        self._generated_reason = generated_reason

    @property
    def invoice_owner(self):
        """Gets the invoice_owner of this TimeSlicedMetrics.  # noqa: E501

        The acount number of the billing account that is billed for the subscription.  # noqa: E501

        :return: The invoice_owner of this TimeSlicedMetrics.  # noqa: E501
        :rtype: str
        """
        return self._invoice_owner

    @invoice_owner.setter
    def invoice_owner(self, invoice_owner):
        """Sets the invoice_owner of this TimeSlicedMetrics.

        The acount number of the billing account that is billed for the subscription.  # noqa: E501

        :param invoice_owner: The invoice_owner of this TimeSlicedMetrics.  # noqa: E501
        :type: str
        """

        self._invoice_owner = invoice_owner

    @property
    def order_item_id(self):
        """Gets the order_item_id of this TimeSlicedMetrics.  # noqa: E501

        The ID of the order item referenced by the order metrics.  This field is only available to existing Orders customers who already have access to the field.  **Note:** The following Order Metrics have been deprecated. Any new customers who onboard on [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) or [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization) will not get these metrics. * The Order ELP and Order Item objects  * The \"Generated Reason\" and \"Order Item ID\" fields in the Order MRR, Order TCB, Order TCV, and Order Quantity objects  Existing Orders customers who have these metrics will continue to be supported.   # noqa: E501

        :return: The order_item_id of this TimeSlicedMetrics.  # noqa: E501
        :rtype: str
        """
        return self._order_item_id

    @order_item_id.setter
    def order_item_id(self, order_item_id):
        """Sets the order_item_id of this TimeSlicedMetrics.

        The ID of the order item referenced by the order metrics.  This field is only available to existing Orders customers who already have access to the field.  **Note:** The following Order Metrics have been deprecated. Any new customers who onboard on [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) or [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization) will not get these metrics. * The Order ELP and Order Item objects  * The \"Generated Reason\" and \"Order Item ID\" fields in the Order MRR, Order TCB, Order TCV, and Order Quantity objects  Existing Orders customers who have these metrics will continue to be supported.   # noqa: E501

        :param order_item_id: The order_item_id of this TimeSlicedMetrics.  # noqa: E501
        :type: str
        """

        self._order_item_id = order_item_id

    @property
    def start_date(self):
        """Gets the start_date of this TimeSlicedMetrics.  # noqa: E501


        :return: The start_date of this TimeSlicedMetrics.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TimeSlicedMetrics.


        :param start_date: The start_date of this TimeSlicedMetrics.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def subscription_owner(self):
        """Gets the subscription_owner of this TimeSlicedMetrics.  # noqa: E501

        The acount number of the billing account that owns the subscription.  # noqa: E501

        :return: The subscription_owner of this TimeSlicedMetrics.  # noqa: E501
        :rtype: str
        """
        return self._subscription_owner

    @subscription_owner.setter
    def subscription_owner(self, subscription_owner):
        """Sets the subscription_owner of this TimeSlicedMetrics.

        The acount number of the billing account that owns the subscription.  # noqa: E501

        :param subscription_owner: The subscription_owner of this TimeSlicedMetrics.  # noqa: E501
        :type: str
        """

        self._subscription_owner = subscription_owner

    @property
    def term_number(self):
        """Gets the term_number of this TimeSlicedMetrics.  # noqa: E501


        :return: The term_number of this TimeSlicedMetrics.  # noqa: E501
        :rtype: int
        """
        return self._term_number

    @term_number.setter
    def term_number(self, term_number):
        """Sets the term_number of this TimeSlicedMetrics.


        :param term_number: The term_number of this TimeSlicedMetrics.  # noqa: E501
        :type: int
        """

        self._term_number = term_number

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
        if issubclass(TimeSlicedMetrics, dict):
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
        if not isinstance(other, TimeSlicedMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
