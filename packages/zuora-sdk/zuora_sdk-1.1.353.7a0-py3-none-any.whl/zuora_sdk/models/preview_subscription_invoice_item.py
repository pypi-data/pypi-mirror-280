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

class PreviewSubscriptionInvoiceItem(object):
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
        'charge_amount': 'float',
        'charge_description': 'str',
        'charge_name': 'str',
        'product_name': 'str',
        'product_rate_plan_charge_id': 'str',
        'quantity': 'float',
        'service_end_date': 'date',
        'service_start_date': 'date',
        'tax_amount': 'float',
        'taxation_items': 'list[SubscriptionTaxationItem]',
        'unit_of_measure': 'str'
    }

    attribute_map = {
        'charge_amount': 'chargeAmount',
        'charge_description': 'chargeDescription',
        'charge_name': 'chargeName',
        'product_name': 'productName',
        'product_rate_plan_charge_id': 'productRatePlanChargeId',
        'quantity': 'quantity',
        'service_end_date': 'serviceEndDate',
        'service_start_date': 'serviceStartDate',
        'tax_amount': 'taxAmount',
        'taxation_items': 'taxationItems',
        'unit_of_measure': 'unitOfMeasure'
    }

    def __init__(self, charge_amount=None, charge_description=None, charge_name=None, product_name=None, product_rate_plan_charge_id=None, quantity=None, service_end_date=None, service_start_date=None, tax_amount=None, taxation_items=None, unit_of_measure=None):  # noqa: E501
        """PreviewSubscriptionInvoiceItem - a model defined in Swagger"""  # noqa: E501
        self._charge_amount = None
        self._charge_description = None
        self._charge_name = None
        self._product_name = None
        self._product_rate_plan_charge_id = None
        self._quantity = None
        self._service_end_date = None
        self._service_start_date = None
        self._tax_amount = None
        self._taxation_items = None
        self._unit_of_measure = None
        self.discriminator = None
        if charge_amount is not None:
            self.charge_amount = charge_amount
        if charge_description is not None:
            self.charge_description = charge_description
        if charge_name is not None:
            self.charge_name = charge_name
        if product_name is not None:
            self.product_name = product_name
        if product_rate_plan_charge_id is not None:
            self.product_rate_plan_charge_id = product_rate_plan_charge_id
        if quantity is not None:
            self.quantity = quantity
        if service_end_date is not None:
            self.service_end_date = service_end_date
        if service_start_date is not None:
            self.service_start_date = service_start_date
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if taxation_items is not None:
            self.taxation_items = taxation_items
        if unit_of_measure is not None:
            self.unit_of_measure = unit_of_measure

    @property
    def charge_amount(self):
        """Gets the charge_amount of this PreviewSubscriptionInvoiceItem.  # noqa: E501

        The amount of the charge. This amount doesn't include taxes unless the charge's tax mode is inclusive.   # noqa: E501

        :return: The charge_amount of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, charge_amount):
        """Sets the charge_amount of this PreviewSubscriptionInvoiceItem.

        The amount of the charge. This amount doesn't include taxes unless the charge's tax mode is inclusive.   # noqa: E501

        :param charge_amount: The charge_amount of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :type: float
        """

        self._charge_amount = charge_amount

    @property
    def charge_description(self):
        """Gets the charge_description of this PreviewSubscriptionInvoiceItem.  # noqa: E501

        Description of the charge.   # noqa: E501

        :return: The charge_description of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._charge_description

    @charge_description.setter
    def charge_description(self, charge_description):
        """Sets the charge_description of this PreviewSubscriptionInvoiceItem.

        Description of the charge.   # noqa: E501

        :param charge_description: The charge_description of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :type: str
        """

        self._charge_description = charge_description

    @property
    def charge_name(self):
        """Gets the charge_name of this PreviewSubscriptionInvoiceItem.  # noqa: E501

        Name of the charge.   # noqa: E501

        :return: The charge_name of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._charge_name

    @charge_name.setter
    def charge_name(self, charge_name):
        """Sets the charge_name of this PreviewSubscriptionInvoiceItem.

        Name of the charge.   # noqa: E501

        :param charge_name: The charge_name of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :type: str
        """

        self._charge_name = charge_name

    @property
    def product_name(self):
        """Gets the product_name of this PreviewSubscriptionInvoiceItem.  # noqa: E501

        Name of the product associated with this item.   # noqa: E501

        :return: The product_name of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this PreviewSubscriptionInvoiceItem.

        Name of the product associated with this item.   # noqa: E501

        :param product_name: The product_name of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def product_rate_plan_charge_id(self):
        """Gets the product_rate_plan_charge_id of this PreviewSubscriptionInvoiceItem.  # noqa: E501

        ID of the product rate plan charge.   # noqa: E501

        :return: The product_rate_plan_charge_id of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_charge_id

    @product_rate_plan_charge_id.setter
    def product_rate_plan_charge_id(self, product_rate_plan_charge_id):
        """Sets the product_rate_plan_charge_id of this PreviewSubscriptionInvoiceItem.

        ID of the product rate plan charge.   # noqa: E501

        :param product_rate_plan_charge_id: The product_rate_plan_charge_id of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_charge_id = product_rate_plan_charge_id

    @property
    def quantity(self):
        """Gets the quantity of this PreviewSubscriptionInvoiceItem.  # noqa: E501

        Quantity of this item.   # noqa: E501

        :return: The quantity of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PreviewSubscriptionInvoiceItem.

        Quantity of this item.   # noqa: E501

        :param quantity: The quantity of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def service_end_date(self):
        """Gets the service_end_date of this PreviewSubscriptionInvoiceItem.  # noqa: E501

        End date of the service period for this item, i.e., the last day of the period, as yyyy-mm-dd.   # noqa: E501

        :return: The service_end_date of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :rtype: date
        """
        return self._service_end_date

    @service_end_date.setter
    def service_end_date(self, service_end_date):
        """Sets the service_end_date of this PreviewSubscriptionInvoiceItem.

        End date of the service period for this item, i.e., the last day of the period, as yyyy-mm-dd.   # noqa: E501

        :param service_end_date: The service_end_date of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :type: date
        """

        self._service_end_date = service_end_date

    @property
    def service_start_date(self):
        """Gets the service_start_date of this PreviewSubscriptionInvoiceItem.  # noqa: E501

        Service start date as yyyy-mm-dd. If the charge is a one-time fee, this is the date of that charge.   # noqa: E501

        :return: The service_start_date of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :rtype: date
        """
        return self._service_start_date

    @service_start_date.setter
    def service_start_date(self, service_start_date):
        """Sets the service_start_date of this PreviewSubscriptionInvoiceItem.

        Service start date as yyyy-mm-dd. If the charge is a one-time fee, this is the date of that charge.   # noqa: E501

        :param service_start_date: The service_start_date of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :type: date
        """

        self._service_start_date = service_start_date

    @property
    def tax_amount(self):
        """Gets the tax_amount of this PreviewSubscriptionInvoiceItem.  # noqa: E501

        The tax amount of the invoice item.   # noqa: E501

        :return: The tax_amount of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this PreviewSubscriptionInvoiceItem.

        The tax amount of the invoice item.   # noqa: E501

        :param tax_amount: The tax_amount of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def taxation_items(self):
        """Gets the taxation_items of this PreviewSubscriptionInvoiceItem.  # noqa: E501

        List of taxation items. **Note**: This field is only available if you set the `zuora-version` request header to `315.0` or later.   # noqa: E501

        :return: The taxation_items of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :rtype: list[SubscriptionTaxationItem]
        """
        return self._taxation_items

    @taxation_items.setter
    def taxation_items(self, taxation_items):
        """Sets the taxation_items of this PreviewSubscriptionInvoiceItem.

        List of taxation items. **Note**: This field is only available if you set the `zuora-version` request header to `315.0` or later.   # noqa: E501

        :param taxation_items: The taxation_items of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :type: list[SubscriptionTaxationItem]
        """

        self._taxation_items = taxation_items

    @property
    def unit_of_measure(self):
        """Gets the unit_of_measure of this PreviewSubscriptionInvoiceItem.  # noqa: E501


        :return: The unit_of_measure of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """Sets the unit_of_measure of this PreviewSubscriptionInvoiceItem.


        :param unit_of_measure: The unit_of_measure of this PreviewSubscriptionInvoiceItem.  # noqa: E501
        :type: str
        """

        self._unit_of_measure = unit_of_measure

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
        if issubclass(PreviewSubscriptionInvoiceItem, dict):
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
        if not isinstance(other, PreviewSubscriptionInvoiceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
