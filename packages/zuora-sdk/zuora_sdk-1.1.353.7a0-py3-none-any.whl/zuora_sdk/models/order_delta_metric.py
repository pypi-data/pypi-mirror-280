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

class OrderDeltaMetric(object):
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
        'charge_number': 'str',
        'currency': 'str',
        'end_date': 'date',
        'gross_amount': 'float',
        'net_amount': 'float',
        'order_action_id': 'str',
        'order_action_sequence': 'str',
        'order_action_type': 'str',
        'order_line_item_number': 'str',
        'product_rate_plan_charge_id': 'str',
        'rate_plan_charge_id': 'str',
        'start_date': 'date',
        'subscription_number': 'str'
    }

    attribute_map = {
        'charge_number': 'chargeNumber',
        'currency': 'currency',
        'end_date': 'endDate',
        'gross_amount': 'grossAmount',
        'net_amount': 'netAmount',
        'order_action_id': 'orderActionId',
        'order_action_sequence': 'orderActionSequence',
        'order_action_type': 'orderActionType',
        'order_line_item_number': 'orderLineItemNumber',
        'product_rate_plan_charge_id': 'productRatePlanChargeId',
        'rate_plan_charge_id': 'ratePlanChargeId',
        'start_date': 'startDate',
        'subscription_number': 'subscriptionNumber'
    }

    def __init__(self, charge_number=None, currency=None, end_date=None, gross_amount=None, net_amount=None, order_action_id=None, order_action_sequence=None, order_action_type=None, order_line_item_number=None, product_rate_plan_charge_id=None, rate_plan_charge_id=None, start_date=None, subscription_number=None):  # noqa: E501
        """OrderDeltaMetric - a model defined in Swagger"""  # noqa: E501
        self._charge_number = None
        self._currency = None
        self._end_date = None
        self._gross_amount = None
        self._net_amount = None
        self._order_action_id = None
        self._order_action_sequence = None
        self._order_action_type = None
        self._order_line_item_number = None
        self._product_rate_plan_charge_id = None
        self._rate_plan_charge_id = None
        self._start_date = None
        self._subscription_number = None
        self.discriminator = None
        if charge_number is not None:
            self.charge_number = charge_number
        if currency is not None:
            self.currency = currency
        if end_date is not None:
            self.end_date = end_date
        if gross_amount is not None:
            self.gross_amount = gross_amount
        if net_amount is not None:
            self.net_amount = net_amount
        if order_action_id is not None:
            self.order_action_id = order_action_id
        if order_action_sequence is not None:
            self.order_action_sequence = order_action_sequence
        if order_action_type is not None:
            self.order_action_type = order_action_type
        if order_line_item_number is not None:
            self.order_line_item_number = order_line_item_number
        if product_rate_plan_charge_id is not None:
            self.product_rate_plan_charge_id = product_rate_plan_charge_id
        if rate_plan_charge_id is not None:
            self.rate_plan_charge_id = rate_plan_charge_id
        if start_date is not None:
            self.start_date = start_date
        if subscription_number is not None:
            self.subscription_number = subscription_number

    @property
    def charge_number(self):
        """Gets the charge_number of this OrderDeltaMetric.  # noqa: E501

        The charge number for the associated Rate Plan Charge. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :return: The charge_number of this OrderDeltaMetric.  # noqa: E501
        :rtype: str
        """
        return self._charge_number

    @charge_number.setter
    def charge_number(self, charge_number):
        """Sets the charge_number of this OrderDeltaMetric.

        The charge number for the associated Rate Plan Charge. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :param charge_number: The charge_number of this OrderDeltaMetric.  # noqa: E501
        :type: str
        """

        self._charge_number = charge_number

    @property
    def currency(self):
        """Gets the currency of this OrderDeltaMetric.  # noqa: E501

        ISO 3-letter currency code (uppercase). For example, USD.   # noqa: E501

        :return: The currency of this OrderDeltaMetric.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this OrderDeltaMetric.

        ISO 3-letter currency code (uppercase). For example, USD.   # noqa: E501

        :param currency: The currency of this OrderDeltaMetric.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def end_date(self):
        """Gets the end_date of this OrderDeltaMetric.  # noqa: E501

        The end date for the order delta metric.   # noqa: E501

        :return: The end_date of this OrderDeltaMetric.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this OrderDeltaMetric.

        The end date for the order delta metric.   # noqa: E501

        :param end_date: The end_date of this OrderDeltaMetric.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def gross_amount(self):
        """Gets the gross_amount of this OrderDeltaMetric.  # noqa: E501

        The gross amount for the metric. The is the amount excluding applied discount.   # noqa: E501

        :return: The gross_amount of this OrderDeltaMetric.  # noqa: E501
        :rtype: float
        """
        return self._gross_amount

    @gross_amount.setter
    def gross_amount(self, gross_amount):
        """Sets the gross_amount of this OrderDeltaMetric.

        The gross amount for the metric. The is the amount excluding applied discount.   # noqa: E501

        :param gross_amount: The gross_amount of this OrderDeltaMetric.  # noqa: E501
        :type: float
        """

        self._gross_amount = gross_amount

    @property
    def net_amount(self):
        """Gets the net_amount of this OrderDeltaMetric.  # noqa: E501

        The net amount for the metric. The is the amount with discounts applied   # noqa: E501

        :return: The net_amount of this OrderDeltaMetric.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this OrderDeltaMetric.

        The net amount for the metric. The is the amount with discounts applied   # noqa: E501

        :param net_amount: The net_amount of this OrderDeltaMetric.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def order_action_id(self):
        """Gets the order_action_id of this OrderDeltaMetric.  # noqa: E501

        The Id for the related Order Action. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :return: The order_action_id of this OrderDeltaMetric.  # noqa: E501
        :rtype: str
        """
        return self._order_action_id

    @order_action_id.setter
    def order_action_id(self, order_action_id):
        """Sets the order_action_id of this OrderDeltaMetric.

        The Id for the related Order Action. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :param order_action_id: The order_action_id of this OrderDeltaMetric.  # noqa: E501
        :type: str
        """

        self._order_action_id = order_action_id

    @property
    def order_action_sequence(self):
        """Gets the order_action_sequence of this OrderDeltaMetric.  # noqa: E501

        The sequence for the related Order Action. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :return: The order_action_sequence of this OrderDeltaMetric.  # noqa: E501
        :rtype: str
        """
        return self._order_action_sequence

    @order_action_sequence.setter
    def order_action_sequence(self, order_action_sequence):
        """Sets the order_action_sequence of this OrderDeltaMetric.

        The sequence for the related Order Action. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :param order_action_sequence: The order_action_sequence of this OrderDeltaMetric.  # noqa: E501
        :type: str
        """

        self._order_action_sequence = order_action_sequence

    @property
    def order_action_type(self):
        """Gets the order_action_type of this OrderDeltaMetric.  # noqa: E501

        The type for the related Order Action. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :return: The order_action_type of this OrderDeltaMetric.  # noqa: E501
        :rtype: str
        """
        return self._order_action_type

    @order_action_type.setter
    def order_action_type(self, order_action_type):
        """Sets the order_action_type of this OrderDeltaMetric.

        The type for the related Order Action. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :param order_action_type: The order_action_type of this OrderDeltaMetric.  # noqa: E501
        :type: str
        """

        self._order_action_type = order_action_type

    @property
    def order_line_item_number(self):
        """Gets the order_line_item_number of this OrderDeltaMetric.  # noqa: E501

        A sequential number auto-assigned for each of order line items in a order, used as an index, for example, \"1\".   # noqa: E501

        :return: The order_line_item_number of this OrderDeltaMetric.  # noqa: E501
        :rtype: str
        """
        return self._order_line_item_number

    @order_line_item_number.setter
    def order_line_item_number(self, order_line_item_number):
        """Sets the order_line_item_number of this OrderDeltaMetric.

        A sequential number auto-assigned for each of order line items in a order, used as an index, for example, \"1\".   # noqa: E501

        :param order_line_item_number: The order_line_item_number of this OrderDeltaMetric.  # noqa: E501
        :type: str
        """

        self._order_line_item_number = order_line_item_number

    @property
    def product_rate_plan_charge_id(self):
        """Gets the product_rate_plan_charge_id of this OrderDeltaMetric.  # noqa: E501

        The Id for the associated Product Rate Plan Charge. This field can be null if the Order Line Item is not associated with a Product Rate Plan Charge.  # noqa: E501

        :return: The product_rate_plan_charge_id of this OrderDeltaMetric.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_charge_id

    @product_rate_plan_charge_id.setter
    def product_rate_plan_charge_id(self, product_rate_plan_charge_id):
        """Sets the product_rate_plan_charge_id of this OrderDeltaMetric.

        The Id for the associated Product Rate Plan Charge. This field can be null if the Order Line Item is not associated with a Product Rate Plan Charge.  # noqa: E501

        :param product_rate_plan_charge_id: The product_rate_plan_charge_id of this OrderDeltaMetric.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_charge_id = product_rate_plan_charge_id

    @property
    def rate_plan_charge_id(self):
        """Gets the rate_plan_charge_id of this OrderDeltaMetric.  # noqa: E501

        The id for the associated Rate Plan Charge. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :return: The rate_plan_charge_id of this OrderDeltaMetric.  # noqa: E501
        :rtype: str
        """
        return self._rate_plan_charge_id

    @rate_plan_charge_id.setter
    def rate_plan_charge_id(self, rate_plan_charge_id):
        """Sets the rate_plan_charge_id of this OrderDeltaMetric.

        The id for the associated Rate Plan Charge. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :param rate_plan_charge_id: The rate_plan_charge_id of this OrderDeltaMetric.  # noqa: E501
        :type: str
        """

        self._rate_plan_charge_id = rate_plan_charge_id

    @property
    def start_date(self):
        """Gets the start_date of this OrderDeltaMetric.  # noqa: E501

        The start date for the order delta metric.   # noqa: E501

        :return: The start_date of this OrderDeltaMetric.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this OrderDeltaMetric.

        The start date for the order delta metric.   # noqa: E501

        :param start_date: The start_date of this OrderDeltaMetric.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def subscription_number(self):
        """Gets the subscription_number of this OrderDeltaMetric.  # noqa: E501

        The number of the subscription. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :return: The subscription_number of this OrderDeltaMetric.  # noqa: E501
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this OrderDeltaMetric.

        The number of the subscription. This field can be null if the metric is generated for an Order Line Item.   # noqa: E501

        :param subscription_number: The subscription_number of this OrderDeltaMetric.  # noqa: E501
        :type: str
        """

        self._subscription_number = subscription_number

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
        if issubclass(OrderDeltaMetric, dict):
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
        if not isinstance(other, OrderDeltaMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
