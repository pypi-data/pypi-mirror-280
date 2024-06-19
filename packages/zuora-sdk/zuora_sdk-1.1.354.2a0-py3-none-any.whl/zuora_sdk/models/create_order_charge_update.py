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

class CreateOrderChargeUpdate(object):
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
        'billing': 'BillingUpdate',
        'charge_number': 'str',
        'product_rate_plan_charge_number': 'str',
        'product_rate_plan_charge_id': 'str',
        'custom_fields': 'dict(str, object)',
        'description': 'str',
        'effective_date': 'TriggerParams',
        'prepaid_quantity': 'float',
        'pricing': 'AllOfCreateOrderChargeUpdatePricing',
        'unique_token': 'str'
    }

    attribute_map = {
        'billing': 'billing',
        'charge_number': 'chargeNumber',
        'product_rate_plan_charge_number': 'productRatePlanChargeNumber',
        'product_rate_plan_charge_id': 'productRatePlanChargeId',
        'custom_fields': 'customFields',
        'description': 'description',
        'effective_date': 'effectiveDate',
        'prepaid_quantity': 'prepaidQuantity',
        'pricing': 'pricing',
        'unique_token': 'uniqueToken'
    }

    def __init__(self, billing=None, charge_number=None, product_rate_plan_charge_number=None, product_rate_plan_charge_id=None, custom_fields=None, description=None, effective_date=None, prepaid_quantity=None, pricing=None, unique_token=None):  # noqa: E501
        """CreateOrderChargeUpdate - a model defined in Swagger"""  # noqa: E501
        self._billing = None
        self._charge_number = None
        self._product_rate_plan_charge_number = None
        self._product_rate_plan_charge_id = None
        self._custom_fields = None
        self._description = None
        self._effective_date = None
        self._prepaid_quantity = None
        self._pricing = None
        self._unique_token = None
        self.discriminator = None
        if billing is not None:
            self.billing = billing
        if charge_number is not None:
            self.charge_number = charge_number
        if product_rate_plan_charge_number is not None:
            self.product_rate_plan_charge_number = product_rate_plan_charge_number
        if product_rate_plan_charge_id is not None:
            self.product_rate_plan_charge_id = product_rate_plan_charge_id
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if description is not None:
            self.description = description
        if effective_date is not None:
            self.effective_date = effective_date
        if prepaid_quantity is not None:
            self.prepaid_quantity = prepaid_quantity
        if pricing is not None:
            self.pricing = pricing
        if unique_token is not None:
            self.unique_token = unique_token

    @property
    def billing(self):
        """Gets the billing of this CreateOrderChargeUpdate.  # noqa: E501


        :return: The billing of this CreateOrderChargeUpdate.  # noqa: E501
        :rtype: BillingUpdate
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this CreateOrderChargeUpdate.


        :param billing: The billing of this CreateOrderChargeUpdate.  # noqa: E501
        :type: BillingUpdate
        """

        self._billing = billing

    @property
    def charge_number(self):
        """Gets the charge_number of this CreateOrderChargeUpdate.  # noqa: E501

        The number of the charge to be updated. The value of this field is inherited from the `subscriptions` > `orderActions` > `addProduct` > `chargeOverrides` > `chargeNumber` field.   # noqa: E501

        :return: The charge_number of this CreateOrderChargeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._charge_number

    @charge_number.setter
    def charge_number(self, charge_number):
        """Sets the charge_number of this CreateOrderChargeUpdate.

        The number of the charge to be updated. The value of this field is inherited from the `subscriptions` > `orderActions` > `addProduct` > `chargeOverrides` > `chargeNumber` field.   # noqa: E501

        :param charge_number: The charge_number of this CreateOrderChargeUpdate.  # noqa: E501
        :type: str
        """

        self._charge_number = charge_number

    @property
    def product_rate_plan_charge_number(self):
        """Gets the product_rate_plan_charge_number of this CreateOrderChargeUpdate.  # noqa: E501

        Number of a product rate-plan charge for this subscription.   # noqa: E501

        :return: The product_rate_plan_charge_number of this CreateOrderChargeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_charge_number

    @product_rate_plan_charge_number.setter
    def product_rate_plan_charge_number(self, product_rate_plan_charge_number):
        """Sets the product_rate_plan_charge_number of this CreateOrderChargeUpdate.

        Number of a product rate-plan charge for this subscription.   # noqa: E501

        :param product_rate_plan_charge_number: The product_rate_plan_charge_number of this CreateOrderChargeUpdate.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_charge_number = product_rate_plan_charge_number

    @property
    def product_rate_plan_charge_id(self):
        """Gets the product_rate_plan_charge_id of this CreateOrderChargeUpdate.  # noqa: E501

        ID of a product rate-plan charge for this subscription.   # noqa: E501

        :return: The product_rate_plan_charge_id of this CreateOrderChargeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_charge_id

    @product_rate_plan_charge_id.setter
    def product_rate_plan_charge_id(self, product_rate_plan_charge_id):
        """Sets the product_rate_plan_charge_id of this CreateOrderChargeUpdate.

        ID of a product rate-plan charge for this subscription.   # noqa: E501

        :param product_rate_plan_charge_id: The product_rate_plan_charge_id of this CreateOrderChargeUpdate.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_charge_id = product_rate_plan_charge_id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this CreateOrderChargeUpdate.  # noqa: E501

        Container for custom fields of a Rate Plan Charge object.   # noqa: E501

        :return: The custom_fields of this CreateOrderChargeUpdate.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this CreateOrderChargeUpdate.

        Container for custom fields of a Rate Plan Charge object.   # noqa: E501

        :param custom_fields: The custom_fields of this CreateOrderChargeUpdate.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def description(self):
        """Gets the description of this CreateOrderChargeUpdate.  # noqa: E501


        :return: The description of this CreateOrderChargeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateOrderChargeUpdate.


        :param description: The description of this CreateOrderChargeUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def effective_date(self):
        """Gets the effective_date of this CreateOrderChargeUpdate.  # noqa: E501


        :return: The effective_date of this CreateOrderChargeUpdate.  # noqa: E501
        :rtype: TriggerParams
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this CreateOrderChargeUpdate.


        :param effective_date: The effective_date of this CreateOrderChargeUpdate.  # noqa: E501
        :type: TriggerParams
        """

        self._effective_date = effective_date

    @property
    def prepaid_quantity(self):
        """Gets the prepaid_quantity of this CreateOrderChargeUpdate.  # noqa: E501

        **Note**: This field is only available if you have the [Prepaid with Drawdown](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown) feature enabled.  The number of units included in a [prepayment charge](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown/Create_prepayment_charge). Must be a positive number (>0).   # noqa: E501

        :return: The prepaid_quantity of this CreateOrderChargeUpdate.  # noqa: E501
        :rtype: float
        """
        return self._prepaid_quantity

    @prepaid_quantity.setter
    def prepaid_quantity(self, prepaid_quantity):
        """Sets the prepaid_quantity of this CreateOrderChargeUpdate.

        **Note**: This field is only available if you have the [Prepaid with Drawdown](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown) feature enabled.  The number of units included in a [prepayment charge](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown/Create_prepayment_charge). Must be a positive number (>0).   # noqa: E501

        :param prepaid_quantity: The prepaid_quantity of this CreateOrderChargeUpdate.  # noqa: E501
        :type: float
        """

        self._prepaid_quantity = prepaid_quantity

    @property
    def pricing(self):
        """Gets the pricing of this CreateOrderChargeUpdate.  # noqa: E501

        Pricing information about the charge.   # noqa: E501

        :return: The pricing of this CreateOrderChargeUpdate.  # noqa: E501
        :rtype: AllOfCreateOrderChargeUpdatePricing
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this CreateOrderChargeUpdate.

        Pricing information about the charge.   # noqa: E501

        :param pricing: The pricing of this CreateOrderChargeUpdate.  # noqa: E501
        :type: AllOfCreateOrderChargeUpdatePricing
        """

        self._pricing = pricing

    @property
    def unique_token(self):
        """Gets the unique_token of this CreateOrderChargeUpdate.  # noqa: E501

        A unique string to represent the rate plan charge in the order. The unique token is used to perform multiple actions against a newly added rate plan charge. For example, if you want to add and update a product in the same order, assign a unique token to the newly added rate plan charge and use that token in future order actions.   # noqa: E501

        :return: The unique_token of this CreateOrderChargeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._unique_token

    @unique_token.setter
    def unique_token(self, unique_token):
        """Sets the unique_token of this CreateOrderChargeUpdate.

        A unique string to represent the rate plan charge in the order. The unique token is used to perform multiple actions against a newly added rate plan charge. For example, if you want to add and update a product in the same order, assign a unique token to the newly added rate plan charge and use that token in future order actions.   # noqa: E501

        :param unique_token: The unique_token of this CreateOrderChargeUpdate.  # noqa: E501
        :type: str
        """

        self._unique_token = unique_token

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
        if issubclass(CreateOrderChargeUpdate, dict):
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
        if not isinstance(other, CreateOrderChargeUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
