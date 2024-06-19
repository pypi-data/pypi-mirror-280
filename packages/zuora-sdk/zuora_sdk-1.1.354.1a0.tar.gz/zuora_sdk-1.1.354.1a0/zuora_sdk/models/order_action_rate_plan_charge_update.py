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

class OrderActionRatePlanChargeUpdate(object):
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
        'billing': 'AllOfOrderActionRatePlanChargeUpdateBilling',
        'charge_number': 'str',
        'custom_fields': 'dict(str, object)',
        'description': 'str',
        'effective_date': 'TriggerParams',
        'pricing': 'AllOfOrderActionRatePlanChargeUpdatePricing',
        'unique_token': 'str'
    }

    attribute_map = {
        'billing': 'billing',
        'charge_number': 'chargeNumber',
        'custom_fields': 'customFields',
        'description': 'description',
        'effective_date': 'effectiveDate',
        'pricing': 'pricing',
        'unique_token': 'uniqueToken'
    }

    def __init__(self, billing=None, charge_number=None, custom_fields=None, description=None, effective_date=None, pricing=None, unique_token=None):  # noqa: E501
        """OrderActionRatePlanChargeUpdate - a model defined in Swagger"""  # noqa: E501
        self._billing = None
        self._charge_number = None
        self._custom_fields = None
        self._description = None
        self._effective_date = None
        self._pricing = None
        self._unique_token = None
        self.discriminator = None
        if billing is not None:
            self.billing = billing
        if charge_number is not None:
            self.charge_number = charge_number
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if description is not None:
            self.description = description
        if effective_date is not None:
            self.effective_date = effective_date
        if pricing is not None:
            self.pricing = pricing
        if unique_token is not None:
            self.unique_token = unique_token

    @property
    def billing(self):
        """Gets the billing of this OrderActionRatePlanChargeUpdate.  # noqa: E501

        Billing information about the charge.   # noqa: E501

        :return: The billing of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :rtype: AllOfOrderActionRatePlanChargeUpdateBilling
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this OrderActionRatePlanChargeUpdate.

        Billing information about the charge.   # noqa: E501

        :param billing: The billing of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :type: AllOfOrderActionRatePlanChargeUpdateBilling
        """

        self._billing = billing

    @property
    def charge_number(self):
        """Gets the charge_number of this OrderActionRatePlanChargeUpdate.  # noqa: E501

        Read only. Identifies the charge to be updated.   # noqa: E501

        :return: The charge_number of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._charge_number

    @charge_number.setter
    def charge_number(self, charge_number):
        """Sets the charge_number of this OrderActionRatePlanChargeUpdate.

        Read only. Identifies the charge to be updated.   # noqa: E501

        :param charge_number: The charge_number of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :type: str
        """

        self._charge_number = charge_number

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderActionRatePlanChargeUpdate.  # noqa: E501

        Container for custom fields of a Rate Plan Charge object.   # noqa: E501

        :return: The custom_fields of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderActionRatePlanChargeUpdate.

        Container for custom fields of a Rate Plan Charge object.   # noqa: E501

        :param custom_fields: The custom_fields of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def description(self):
        """Gets the description of this OrderActionRatePlanChargeUpdate.  # noqa: E501

        Description of the charge.   # noqa: E501

        :return: The description of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrderActionRatePlanChargeUpdate.

        Description of the charge.   # noqa: E501

        :param description: The description of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def effective_date(self):
        """Gets the effective_date of this OrderActionRatePlanChargeUpdate.  # noqa: E501


        :return: The effective_date of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :rtype: TriggerParams
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this OrderActionRatePlanChargeUpdate.


        :param effective_date: The effective_date of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :type: TriggerParams
        """

        self._effective_date = effective_date

    @property
    def pricing(self):
        """Gets the pricing of this OrderActionRatePlanChargeUpdate.  # noqa: E501

        Pricing information about the charge.   # noqa: E501

        :return: The pricing of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :rtype: AllOfOrderActionRatePlanChargeUpdatePricing
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this OrderActionRatePlanChargeUpdate.

        Pricing information about the charge.   # noqa: E501

        :param pricing: The pricing of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :type: AllOfOrderActionRatePlanChargeUpdatePricing
        """

        self._pricing = pricing

    @property
    def unique_token(self):
        """Gets the unique_token of this OrderActionRatePlanChargeUpdate.  # noqa: E501

        A unique string to represent the rate plan charge in the order. The unique token is used to perform multiple actions against a newly added rate plan. For example, if you want to add and update a product in the same order, you would assign a unique token to the product rate plan when added and use that token in future order actions.   # noqa: E501

        :return: The unique_token of this OrderActionRatePlanChargeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._unique_token

    @unique_token.setter
    def unique_token(self, unique_token):
        """Sets the unique_token of this OrderActionRatePlanChargeUpdate.

        A unique string to represent the rate plan charge in the order. The unique token is used to perform multiple actions against a newly added rate plan. For example, if you want to add and update a product in the same order, you would assign a unique token to the product rate plan when added and use that token in future order actions.   # noqa: E501

        :param unique_token: The unique_token of this OrderActionRatePlanChargeUpdate.  # noqa: E501
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
        if issubclass(OrderActionRatePlanChargeUpdate, dict):
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
        if not isinstance(other, OrderActionRatePlanChargeUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
