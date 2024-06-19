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

class OrderActionRatePlanChargeOverride(object):
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
        'billing': 'ChargeOverrideBilling',
        'charge_number': 'str',
        'custom_fields': 'dict(str, object)',
        'description': 'str',
        'end_date': 'EndConditions',
        'pricing': 'RatePlanChargeOverridePricing',
        'product_rate_plan_charge_id': 'str',
        'rev_rec_code': 'str',
        'rev_rec_trigger_condition': 'RevRecTriggerCondition',
        'revenue_recognition_rule_name': 'RevenueRecognitionRuleName',
        'start_date': 'TriggerParams',
        'unique_token': 'str'
    }

    attribute_map = {
        'billing': 'billing',
        'charge_number': 'chargeNumber',
        'custom_fields': 'customFields',
        'description': 'description',
        'end_date': 'endDate',
        'pricing': 'pricing',
        'product_rate_plan_charge_id': 'productRatePlanChargeId',
        'rev_rec_code': 'revRecCode',
        'rev_rec_trigger_condition': 'revRecTriggerCondition',
        'revenue_recognition_rule_name': 'revenueRecognitionRuleName',
        'start_date': 'startDate',
        'unique_token': 'uniqueToken'
    }

    def __init__(self, billing=None, charge_number=None, custom_fields=None, description=None, end_date=None, pricing=None, product_rate_plan_charge_id=None, rev_rec_code=None, rev_rec_trigger_condition=None, revenue_recognition_rule_name=None, start_date=None, unique_token=None):  # noqa: E501
        """OrderActionRatePlanChargeOverride - a model defined in Swagger"""  # noqa: E501
        self._billing = None
        self._charge_number = None
        self._custom_fields = None
        self._description = None
        self._end_date = None
        self._pricing = None
        self._product_rate_plan_charge_id = None
        self._rev_rec_code = None
        self._rev_rec_trigger_condition = None
        self._revenue_recognition_rule_name = None
        self._start_date = None
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
        if end_date is not None:
            self.end_date = end_date
        if pricing is not None:
            self.pricing = pricing
        self.product_rate_plan_charge_id = product_rate_plan_charge_id
        if rev_rec_code is not None:
            self.rev_rec_code = rev_rec_code
        if rev_rec_trigger_condition is not None:
            self.rev_rec_trigger_condition = rev_rec_trigger_condition
        if revenue_recognition_rule_name is not None:
            self.revenue_recognition_rule_name = revenue_recognition_rule_name
        if start_date is not None:
            self.start_date = start_date
        if unique_token is not None:
            self.unique_token = unique_token

    @property
    def billing(self):
        """Gets the billing of this OrderActionRatePlanChargeOverride.  # noqa: E501


        :return: The billing of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: ChargeOverrideBilling
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this OrderActionRatePlanChargeOverride.


        :param billing: The billing of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :type: ChargeOverrideBilling
        """

        self._billing = billing

    @property
    def charge_number(self):
        """Gets the charge_number of this OrderActionRatePlanChargeOverride.  # noqa: E501

        Charge number of the charge. For example, C-00000307.  If you do not set this field, Zuora will generate the charge number.   # noqa: E501

        :return: The charge_number of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._charge_number

    @charge_number.setter
    def charge_number(self, charge_number):
        """Sets the charge_number of this OrderActionRatePlanChargeOverride.

        Charge number of the charge. For example, C-00000307.  If you do not set this field, Zuora will generate the charge number.   # noqa: E501

        :param charge_number: The charge_number of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :type: str
        """

        self._charge_number = charge_number

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderActionRatePlanChargeOverride.  # noqa: E501

        Container for custom fields of a Rate Plan Charge object.   # noqa: E501

        :return: The custom_fields of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderActionRatePlanChargeOverride.

        Container for custom fields of a Rate Plan Charge object.   # noqa: E501

        :param custom_fields: The custom_fields of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def description(self):
        """Gets the description of this OrderActionRatePlanChargeOverride.  # noqa: E501

        Description of the charge.   # noqa: E501

        :return: The description of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrderActionRatePlanChargeOverride.

        Description of the charge.   # noqa: E501

        :param description: The description of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_date(self):
        """Gets the end_date of this OrderActionRatePlanChargeOverride.  # noqa: E501


        :return: The end_date of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: EndConditions
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this OrderActionRatePlanChargeOverride.


        :param end_date: The end_date of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :type: EndConditions
        """

        self._end_date = end_date

    @property
    def pricing(self):
        """Gets the pricing of this OrderActionRatePlanChargeOverride.  # noqa: E501


        :return: The pricing of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: RatePlanChargeOverridePricing
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this OrderActionRatePlanChargeOverride.


        :param pricing: The pricing of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :type: RatePlanChargeOverridePricing
        """

        self._pricing = pricing

    @property
    def product_rate_plan_charge_id(self):
        """Gets the product_rate_plan_charge_id of this OrderActionRatePlanChargeOverride.  # noqa: E501

        Internal identifier of the product rate plan charge that the charge is based on.   # noqa: E501

        :return: The product_rate_plan_charge_id of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_charge_id

    @product_rate_plan_charge_id.setter
    def product_rate_plan_charge_id(self, product_rate_plan_charge_id):
        """Sets the product_rate_plan_charge_id of this OrderActionRatePlanChargeOverride.

        Internal identifier of the product rate plan charge that the charge is based on.   # noqa: E501

        :param product_rate_plan_charge_id: The product_rate_plan_charge_id of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :type: str
        """
        if product_rate_plan_charge_id is None:
            raise ValueError("Invalid value for `product_rate_plan_charge_id`, must not be `None`")  # noqa: E501

        self._product_rate_plan_charge_id = product_rate_plan_charge_id

    @property
    def rev_rec_code(self):
        """Gets the rev_rec_code of this OrderActionRatePlanChargeOverride.  # noqa: E501

        Revenue Recognition Code   # noqa: E501

        :return: The rev_rec_code of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._rev_rec_code

    @rev_rec_code.setter
    def rev_rec_code(self, rev_rec_code):
        """Sets the rev_rec_code of this OrderActionRatePlanChargeOverride.

        Revenue Recognition Code   # noqa: E501

        :param rev_rec_code: The rev_rec_code of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :type: str
        """

        self._rev_rec_code = rev_rec_code

    @property
    def rev_rec_trigger_condition(self):
        """Gets the rev_rec_trigger_condition of this OrderActionRatePlanChargeOverride.  # noqa: E501


        :return: The rev_rec_trigger_condition of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: RevRecTriggerCondition
        """
        return self._rev_rec_trigger_condition

    @rev_rec_trigger_condition.setter
    def rev_rec_trigger_condition(self, rev_rec_trigger_condition):
        """Sets the rev_rec_trigger_condition of this OrderActionRatePlanChargeOverride.


        :param rev_rec_trigger_condition: The rev_rec_trigger_condition of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :type: RevRecTriggerCondition
        """

        self._rev_rec_trigger_condition = rev_rec_trigger_condition

    @property
    def revenue_recognition_rule_name(self):
        """Gets the revenue_recognition_rule_name of this OrderActionRatePlanChargeOverride.  # noqa: E501


        :return: The revenue_recognition_rule_name of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: RevenueRecognitionRuleName
        """
        return self._revenue_recognition_rule_name

    @revenue_recognition_rule_name.setter
    def revenue_recognition_rule_name(self, revenue_recognition_rule_name):
        """Sets the revenue_recognition_rule_name of this OrderActionRatePlanChargeOverride.


        :param revenue_recognition_rule_name: The revenue_recognition_rule_name of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :type: RevenueRecognitionRuleName
        """

        self._revenue_recognition_rule_name = revenue_recognition_rule_name

    @property
    def start_date(self):
        """Gets the start_date of this OrderActionRatePlanChargeOverride.  # noqa: E501


        :return: The start_date of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: TriggerParams
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this OrderActionRatePlanChargeOverride.


        :param start_date: The start_date of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :type: TriggerParams
        """

        self._start_date = start_date

    @property
    def unique_token(self):
        """Gets the unique_token of this OrderActionRatePlanChargeOverride.  # noqa: E501

        Unique identifier for the charge. This identifier enables you to refer to the charge before the charge has an internal identifier in Zuora.  For instance, suppose that you want to use a single order to add a product to a subscription and later update the same product. When you add the product, you can set a unique identifier for the charge. Then when you update the product, you can use the same unique identifier to specify which charge to modify.   # noqa: E501

        :return: The unique_token of this OrderActionRatePlanChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._unique_token

    @unique_token.setter
    def unique_token(self, unique_token):
        """Sets the unique_token of this OrderActionRatePlanChargeOverride.

        Unique identifier for the charge. This identifier enables you to refer to the charge before the charge has an internal identifier in Zuora.  For instance, suppose that you want to use a single order to add a product to a subscription and later update the same product. When you add the product, you can set a unique identifier for the charge. Then when you update the product, you can use the same unique identifier to specify which charge to modify.   # noqa: E501

        :param unique_token: The unique_token of this OrderActionRatePlanChargeOverride.  # noqa: E501
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
        if issubclass(OrderActionRatePlanChargeOverride, dict):
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
        if not isinstance(other, OrderActionRatePlanChargeOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
