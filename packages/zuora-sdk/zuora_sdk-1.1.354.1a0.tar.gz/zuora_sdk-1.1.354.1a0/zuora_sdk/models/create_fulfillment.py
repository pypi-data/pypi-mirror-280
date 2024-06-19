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

class CreateFulfillment(object):
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
        'order_line_item_id': 'str',
        'bill_target_date': 'date',
        'carrier': 'str',
        'custom_fields': 'dict(str, object)',
        'description': 'str',
        'exclude_item_billing_from_revenue_accounting': 'bool',
        'exclude_item_booking_from_revenue_accounting': 'bool',
        'external_id': 'str',
        'fulfillment_date': 'date',
        'fulfillment_location': 'str',
        'fulfillment_system': 'str',
        'fulfillment_type': 'FulfillmentType',
        'quantity': 'float',
        'state': 'FulfillmentState',
        'tracking_number': 'str',
        'fulfillment_items': 'list[FulfillmentItem]'
    }

    attribute_map = {
        'order_line_item_id': 'orderLineItemId',
        'bill_target_date': 'billTargetDate',
        'carrier': 'carrier',
        'custom_fields': 'customFields',
        'description': 'description',
        'exclude_item_billing_from_revenue_accounting': 'excludeItemBillingFromRevenueAccounting',
        'exclude_item_booking_from_revenue_accounting': 'excludeItemBookingFromRevenueAccounting',
        'external_id': 'externalId',
        'fulfillment_date': 'fulfillmentDate',
        'fulfillment_location': 'fulfillmentLocation',
        'fulfillment_system': 'fulfillmentSystem',
        'fulfillment_type': 'fulfillmentType',
        'quantity': 'quantity',
        'state': 'state',
        'tracking_number': 'trackingNumber',
        'fulfillment_items': 'fulfillmentItems'
    }

    def __init__(self, order_line_item_id=None, bill_target_date=None, carrier=None, custom_fields=None, description=None, exclude_item_billing_from_revenue_accounting=None, exclude_item_booking_from_revenue_accounting=None, external_id=None, fulfillment_date=None, fulfillment_location=None, fulfillment_system=None, fulfillment_type=None, quantity=None, state=None, tracking_number=None, fulfillment_items=None):  # noqa: E501
        """CreateFulfillment - a model defined in Swagger"""  # noqa: E501
        self._order_line_item_id = None
        self._bill_target_date = None
        self._carrier = None
        self._custom_fields = None
        self._description = None
        self._exclude_item_billing_from_revenue_accounting = None
        self._exclude_item_booking_from_revenue_accounting = None
        self._external_id = None
        self._fulfillment_date = None
        self._fulfillment_location = None
        self._fulfillment_system = None
        self._fulfillment_type = None
        self._quantity = None
        self._state = None
        self._tracking_number = None
        self._fulfillment_items = None
        self.discriminator = None
        if order_line_item_id is not None:
            self.order_line_item_id = order_line_item_id
        if bill_target_date is not None:
            self.bill_target_date = bill_target_date
        if carrier is not None:
            self.carrier = carrier
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if description is not None:
            self.description = description
        if exclude_item_billing_from_revenue_accounting is not None:
            self.exclude_item_billing_from_revenue_accounting = exclude_item_billing_from_revenue_accounting
        if exclude_item_booking_from_revenue_accounting is not None:
            self.exclude_item_booking_from_revenue_accounting = exclude_item_booking_from_revenue_accounting
        if external_id is not None:
            self.external_id = external_id
        if fulfillment_date is not None:
            self.fulfillment_date = fulfillment_date
        if fulfillment_location is not None:
            self.fulfillment_location = fulfillment_location
        if fulfillment_system is not None:
            self.fulfillment_system = fulfillment_system
        if fulfillment_type is not None:
            self.fulfillment_type = fulfillment_type
        if quantity is not None:
            self.quantity = quantity
        if state is not None:
            self.state = state
        if tracking_number is not None:
            self.tracking_number = tracking_number
        if fulfillment_items is not None:
            self.fulfillment_items = fulfillment_items

    @property
    def order_line_item_id(self):
        """Gets the order_line_item_id of this CreateFulfillment.  # noqa: E501

        The reference id of the related Order Line Item.   # noqa: E501

        :return: The order_line_item_id of this CreateFulfillment.  # noqa: E501
        :rtype: str
        """
        return self._order_line_item_id

    @order_line_item_id.setter
    def order_line_item_id(self, order_line_item_id):
        """Sets the order_line_item_id of this CreateFulfillment.

        The reference id of the related Order Line Item.   # noqa: E501

        :param order_line_item_id: The order_line_item_id of this CreateFulfillment.  # noqa: E501
        :type: str
        """

        self._order_line_item_id = order_line_item_id

    @property
    def bill_target_date(self):
        """Gets the bill_target_date of this CreateFulfillment.  # noqa: E501

        The target date for the Fulfillment to be picked up by bill run for billing.   # noqa: E501

        :return: The bill_target_date of this CreateFulfillment.  # noqa: E501
        :rtype: date
        """
        return self._bill_target_date

    @bill_target_date.setter
    def bill_target_date(self, bill_target_date):
        """Sets the bill_target_date of this CreateFulfillment.

        The target date for the Fulfillment to be picked up by bill run for billing.   # noqa: E501

        :param bill_target_date: The bill_target_date of this CreateFulfillment.  # noqa: E501
        :type: date
        """

        self._bill_target_date = bill_target_date

    @property
    def carrier(self):
        """Gets the carrier of this CreateFulfillment.  # noqa: E501

        The carrier of the Fulfillment. The available values can be configured in **Billing Settings** > **Fulfillment Settings** through Zuora UI.   # noqa: E501

        :return: The carrier of this CreateFulfillment.  # noqa: E501
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this CreateFulfillment.

        The carrier of the Fulfillment. The available values can be configured in **Billing Settings** > **Fulfillment Settings** through Zuora UI.   # noqa: E501

        :param carrier: The carrier of this CreateFulfillment.  # noqa: E501
        :type: str
        """

        self._carrier = carrier

    @property
    def custom_fields(self):
        """Gets the custom_fields of this CreateFulfillment.  # noqa: E501

        Container for custom fields of a Fulfillment object.   # noqa: E501

        :return: The custom_fields of this CreateFulfillment.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this CreateFulfillment.

        Container for custom fields of a Fulfillment object.   # noqa: E501

        :param custom_fields: The custom_fields of this CreateFulfillment.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def description(self):
        """Gets the description of this CreateFulfillment.  # noqa: E501

        The description of the Fulfillment.   # noqa: E501

        :return: The description of this CreateFulfillment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateFulfillment.

        The description of the Fulfillment.   # noqa: E501

        :param description: The description of this CreateFulfillment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def exclude_item_billing_from_revenue_accounting(self):
        """Gets the exclude_item_billing_from_revenue_accounting of this CreateFulfillment.  # noqa: E501

        The flag to exclude Fulfillment related invoice items, invoice item adjustments, credit memo items, and debit memo items from revenue accounting.  **Note**: This field is only available if you have the [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration) feature enabled.    # noqa: E501

        :return: The exclude_item_billing_from_revenue_accounting of this CreateFulfillment.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_item_billing_from_revenue_accounting

    @exclude_item_billing_from_revenue_accounting.setter
    def exclude_item_billing_from_revenue_accounting(self, exclude_item_billing_from_revenue_accounting):
        """Sets the exclude_item_billing_from_revenue_accounting of this CreateFulfillment.

        The flag to exclude Fulfillment related invoice items, invoice item adjustments, credit memo items, and debit memo items from revenue accounting.  **Note**: This field is only available if you have the [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration) feature enabled.    # noqa: E501

        :param exclude_item_billing_from_revenue_accounting: The exclude_item_billing_from_revenue_accounting of this CreateFulfillment.  # noqa: E501
        :type: bool
        """

        self._exclude_item_billing_from_revenue_accounting = exclude_item_billing_from_revenue_accounting

    @property
    def exclude_item_booking_from_revenue_accounting(self):
        """Gets the exclude_item_booking_from_revenue_accounting of this CreateFulfillment.  # noqa: E501

        The flag to exclude Fulfillment from revenue accounting.  **Note**: This field is only available if you have the [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration) feature enabled.    # noqa: E501

        :return: The exclude_item_booking_from_revenue_accounting of this CreateFulfillment.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_item_booking_from_revenue_accounting

    @exclude_item_booking_from_revenue_accounting.setter
    def exclude_item_booking_from_revenue_accounting(self, exclude_item_booking_from_revenue_accounting):
        """Sets the exclude_item_booking_from_revenue_accounting of this CreateFulfillment.

        The flag to exclude Fulfillment from revenue accounting.  **Note**: This field is only available if you have the [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration) feature enabled.    # noqa: E501

        :param exclude_item_booking_from_revenue_accounting: The exclude_item_booking_from_revenue_accounting of this CreateFulfillment.  # noqa: E501
        :type: bool
        """

        self._exclude_item_booking_from_revenue_accounting = exclude_item_booking_from_revenue_accounting

    @property
    def external_id(self):
        """Gets the external_id of this CreateFulfillment.  # noqa: E501

        The external id of the Fulfillment.   # noqa: E501

        :return: The external_id of this CreateFulfillment.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CreateFulfillment.

        The external id of the Fulfillment.   # noqa: E501

        :param external_id: The external_id of this CreateFulfillment.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def fulfillment_date(self):
        """Gets the fulfillment_date of this CreateFulfillment.  # noqa: E501

        The date of the Fulfillment.   # noqa: E501

        :return: The fulfillment_date of this CreateFulfillment.  # noqa: E501
        :rtype: date
        """
        return self._fulfillment_date

    @fulfillment_date.setter
    def fulfillment_date(self, fulfillment_date):
        """Sets the fulfillment_date of this CreateFulfillment.

        The date of the Fulfillment.   # noqa: E501

        :param fulfillment_date: The fulfillment_date of this CreateFulfillment.  # noqa: E501
        :type: date
        """

        self._fulfillment_date = fulfillment_date

    @property
    def fulfillment_location(self):
        """Gets the fulfillment_location of this CreateFulfillment.  # noqa: E501

        The fulfillment location of the Fulfillment. The available values can be configured in **Billing Settings** > **Fulfillment Settings** through Zuora UI.   # noqa: E501

        :return: The fulfillment_location of this CreateFulfillment.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_location

    @fulfillment_location.setter
    def fulfillment_location(self, fulfillment_location):
        """Sets the fulfillment_location of this CreateFulfillment.

        The fulfillment location of the Fulfillment. The available values can be configured in **Billing Settings** > **Fulfillment Settings** through Zuora UI.   # noqa: E501

        :param fulfillment_location: The fulfillment_location of this CreateFulfillment.  # noqa: E501
        :type: str
        """

        self._fulfillment_location = fulfillment_location

    @property
    def fulfillment_system(self):
        """Gets the fulfillment_system of this CreateFulfillment.  # noqa: E501

        The fulfillment system of the Fulfillment. The available values can be configured in **Billing Settings** > **Fulfillment Settings** through Zuora UI.   # noqa: E501

        :return: The fulfillment_system of this CreateFulfillment.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_system

    @fulfillment_system.setter
    def fulfillment_system(self, fulfillment_system):
        """Sets the fulfillment_system of this CreateFulfillment.

        The fulfillment system of the Fulfillment. The available values can be configured in **Billing Settings** > **Fulfillment Settings** through Zuora UI.   # noqa: E501

        :param fulfillment_system: The fulfillment_system of this CreateFulfillment.  # noqa: E501
        :type: str
        """

        self._fulfillment_system = fulfillment_system

    @property
    def fulfillment_type(self):
        """Gets the fulfillment_type of this CreateFulfillment.  # noqa: E501


        :return: The fulfillment_type of this CreateFulfillment.  # noqa: E501
        :rtype: FulfillmentType
        """
        return self._fulfillment_type

    @fulfillment_type.setter
    def fulfillment_type(self, fulfillment_type):
        """Sets the fulfillment_type of this CreateFulfillment.


        :param fulfillment_type: The fulfillment_type of this CreateFulfillment.  # noqa: E501
        :type: FulfillmentType
        """

        self._fulfillment_type = fulfillment_type

    @property
    def quantity(self):
        """Gets the quantity of this CreateFulfillment.  # noqa: E501

        The quantity of the Fulfillment.   # noqa: E501

        :return: The quantity of this CreateFulfillment.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CreateFulfillment.

        The quantity of the Fulfillment.   # noqa: E501

        :param quantity: The quantity of this CreateFulfillment.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def state(self):
        """Gets the state of this CreateFulfillment.  # noqa: E501


        :return: The state of this CreateFulfillment.  # noqa: E501
        :rtype: FulfillmentState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreateFulfillment.


        :param state: The state of this CreateFulfillment.  # noqa: E501
        :type: FulfillmentState
        """

        self._state = state

    @property
    def tracking_number(self):
        """Gets the tracking_number of this CreateFulfillment.  # noqa: E501

        The tracking number of the Fulfillment.   # noqa: E501

        :return: The tracking_number of this CreateFulfillment.  # noqa: E501
        :rtype: str
        """
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        """Sets the tracking_number of this CreateFulfillment.

        The tracking number of the Fulfillment.   # noqa: E501

        :param tracking_number: The tracking_number of this CreateFulfillment.  # noqa: E501
        :type: str
        """

        self._tracking_number = tracking_number

    @property
    def fulfillment_items(self):
        """Gets the fulfillment_items of this CreateFulfillment.  # noqa: E501


        :return: The fulfillment_items of this CreateFulfillment.  # noqa: E501
        :rtype: list[FulfillmentItem]
        """
        return self._fulfillment_items

    @fulfillment_items.setter
    def fulfillment_items(self, fulfillment_items):
        """Sets the fulfillment_items of this CreateFulfillment.


        :param fulfillment_items: The fulfillment_items of this CreateFulfillment.  # noqa: E501
        :type: list[FulfillmentItem]
        """

        self._fulfillment_items = fulfillment_items

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
        if issubclass(CreateFulfillment, dict):
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
        if not isinstance(other, CreateFulfillment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
