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

class GetChargeOverride(object):
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
        'drawdown_rate': 'float',
        'end_date': 'EndConditions',
        'exclude_item_billing_from_revenue_accounting': 'bool',
        'exclude_item_booking_from_revenue_accounting': 'bool',
        'is_allocation_eligible': 'bool',
        'is_rollover': 'bool',
        'is_unbilled': 'bool',
        'prepaid_quantity': 'float',
        'proration_option': 'str',
        'pricing': 'ChargeOverridePricing',
        'product_rate_plan_charge_number': 'str',
        'product_rateplan_charge_id': 'str',
        'rev_rec_code': 'str',
        'rev_rec_trigger_condition': 'RevRecTriggerCondition',
        'revenue_recognition_rule_name': 'str',
        'rollover_apply': 'RolloverApply',
        'rollover_periods': 'float',
        'start_date': 'TriggerParams',
        'unique_token': 'str',
        'upsell_origin_charge_number': 'str',
        'validity_period_type': 'ValidityPeriodType'
    }

    attribute_map = {
        'billing': 'billing',
        'charge_number': 'chargeNumber',
        'custom_fields': 'customFields',
        'description': 'description',
        'drawdown_rate': 'drawdownRate',
        'end_date': 'endDate',
        'exclude_item_billing_from_revenue_accounting': 'excludeItemBillingFromRevenueAccounting',
        'exclude_item_booking_from_revenue_accounting': 'excludeItemBookingFromRevenueAccounting',
        'is_allocation_eligible': 'isAllocationEligible',
        'is_rollover': 'isRollover',
        'is_unbilled': 'isUnbilled',
        'prepaid_quantity': 'prepaidQuantity',
        'proration_option': 'prorationOption',
        'pricing': 'pricing',
        'product_rate_plan_charge_number': 'productRatePlanChargeNumber',
        'product_rateplan_charge_id': 'productRateplanChargeId',
        'rev_rec_code': 'revRecCode',
        'rev_rec_trigger_condition': 'revRecTriggerCondition',
        'revenue_recognition_rule_name': 'revenueRecognitionRuleName',
        'rollover_apply': 'rolloverApply',
        'rollover_periods': 'rolloverPeriods',
        'start_date': 'startDate',
        'unique_token': 'uniqueToken',
        'upsell_origin_charge_number': 'upsellOriginChargeNumber',
        'validity_period_type': 'validityPeriodType'
    }

    def __init__(self, billing=None, charge_number=None, custom_fields=None, description=None, drawdown_rate=None, end_date=None, exclude_item_billing_from_revenue_accounting=None, exclude_item_booking_from_revenue_accounting=None, is_allocation_eligible=None, is_rollover=None, is_unbilled=None, prepaid_quantity=None, proration_option=None, pricing=None, product_rate_plan_charge_number=None, product_rateplan_charge_id=None, rev_rec_code=None, rev_rec_trigger_condition=None, revenue_recognition_rule_name=None, rollover_apply=None, rollover_periods=None, start_date=None, unique_token=None, upsell_origin_charge_number=None, validity_period_type=None):  # noqa: E501
        """GetChargeOverride - a model defined in Swagger"""  # noqa: E501
        self._billing = None
        self._charge_number = None
        self._custom_fields = None
        self._description = None
        self._drawdown_rate = None
        self._end_date = None
        self._exclude_item_billing_from_revenue_accounting = None
        self._exclude_item_booking_from_revenue_accounting = None
        self._is_allocation_eligible = None
        self._is_rollover = None
        self._is_unbilled = None
        self._prepaid_quantity = None
        self._proration_option = None
        self._pricing = None
        self._product_rate_plan_charge_number = None
        self._product_rateplan_charge_id = None
        self._rev_rec_code = None
        self._rev_rec_trigger_condition = None
        self._revenue_recognition_rule_name = None
        self._rollover_apply = None
        self._rollover_periods = None
        self._start_date = None
        self._unique_token = None
        self._upsell_origin_charge_number = None
        self._validity_period_type = None
        self.discriminator = None
        if billing is not None:
            self.billing = billing
        if charge_number is not None:
            self.charge_number = charge_number
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if description is not None:
            self.description = description
        if drawdown_rate is not None:
            self.drawdown_rate = drawdown_rate
        if end_date is not None:
            self.end_date = end_date
        if exclude_item_billing_from_revenue_accounting is not None:
            self.exclude_item_billing_from_revenue_accounting = exclude_item_billing_from_revenue_accounting
        if exclude_item_booking_from_revenue_accounting is not None:
            self.exclude_item_booking_from_revenue_accounting = exclude_item_booking_from_revenue_accounting
        if is_allocation_eligible is not None:
            self.is_allocation_eligible = is_allocation_eligible
        if is_rollover is not None:
            self.is_rollover = is_rollover
        if is_unbilled is not None:
            self.is_unbilled = is_unbilled
        if prepaid_quantity is not None:
            self.prepaid_quantity = prepaid_quantity
        if proration_option is not None:
            self.proration_option = proration_option
        if pricing is not None:
            self.pricing = pricing
        if product_rate_plan_charge_number is not None:
            self.product_rate_plan_charge_number = product_rate_plan_charge_number
        self.product_rateplan_charge_id = product_rateplan_charge_id
        if rev_rec_code is not None:
            self.rev_rec_code = rev_rec_code
        if rev_rec_trigger_condition is not None:
            self.rev_rec_trigger_condition = rev_rec_trigger_condition
        if revenue_recognition_rule_name is not None:
            self.revenue_recognition_rule_name = revenue_recognition_rule_name
        if rollover_apply is not None:
            self.rollover_apply = rollover_apply
        if rollover_periods is not None:
            self.rollover_periods = rollover_periods
        if start_date is not None:
            self.start_date = start_date
        if unique_token is not None:
            self.unique_token = unique_token
        if upsell_origin_charge_number is not None:
            self.upsell_origin_charge_number = upsell_origin_charge_number
        if validity_period_type is not None:
            self.validity_period_type = validity_period_type

    @property
    def billing(self):
        """Gets the billing of this GetChargeOverride.  # noqa: E501


        :return: The billing of this GetChargeOverride.  # noqa: E501
        :rtype: ChargeOverrideBilling
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this GetChargeOverride.


        :param billing: The billing of this GetChargeOverride.  # noqa: E501
        :type: ChargeOverrideBilling
        """

        self._billing = billing

    @property
    def charge_number(self):
        """Gets the charge_number of this GetChargeOverride.  # noqa: E501

        Charge number of the charge. For example, C-00000307.  If you do not set this field, Zuora will generate the charge number.   # noqa: E501

        :return: The charge_number of this GetChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._charge_number

    @charge_number.setter
    def charge_number(self, charge_number):
        """Sets the charge_number of this GetChargeOverride.

        Charge number of the charge. For example, C-00000307.  If you do not set this field, Zuora will generate the charge number.   # noqa: E501

        :param charge_number: The charge_number of this GetChargeOverride.  # noqa: E501
        :type: str
        """

        self._charge_number = charge_number

    @property
    def custom_fields(self):
        """Gets the custom_fields of this GetChargeOverride.  # noqa: E501

        Container for custom fields of a Rate Plan Charge object.   # noqa: E501

        :return: The custom_fields of this GetChargeOverride.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this GetChargeOverride.

        Container for custom fields of a Rate Plan Charge object.   # noqa: E501

        :param custom_fields: The custom_fields of this GetChargeOverride.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def description(self):
        """Gets the description of this GetChargeOverride.  # noqa: E501

        Description of the charge.   # noqa: E501

        :return: The description of this GetChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetChargeOverride.

        Description of the charge.   # noqa: E501

        :param description: The description of this GetChargeOverride.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def drawdown_rate(self):
        """Gets the drawdown_rate of this GetChargeOverride.  # noqa: E501

        **Note**: This field is only available if you have the [Prepaid with Drawdown](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown) feature enabled.  The [conversion rate](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown/Create_drawdown_charge#UOM_Conversion) between Usage UOM and Drawdown UOM for a [drawdown charge](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown/Create_drawdown_charge). Must be a positive number (>0).   # noqa: E501

        :return: The drawdown_rate of this GetChargeOverride.  # noqa: E501
        :rtype: float
        """
        return self._drawdown_rate

    @drawdown_rate.setter
    def drawdown_rate(self, drawdown_rate):
        """Sets the drawdown_rate of this GetChargeOverride.

        **Note**: This field is only available if you have the [Prepaid with Drawdown](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown) feature enabled.  The [conversion rate](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown/Create_drawdown_charge#UOM_Conversion) between Usage UOM and Drawdown UOM for a [drawdown charge](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown/Create_drawdown_charge). Must be a positive number (>0).   # noqa: E501

        :param drawdown_rate: The drawdown_rate of this GetChargeOverride.  # noqa: E501
        :type: float
        """

        self._drawdown_rate = drawdown_rate

    @property
    def end_date(self):
        """Gets the end_date of this GetChargeOverride.  # noqa: E501


        :return: The end_date of this GetChargeOverride.  # noqa: E501
        :rtype: EndConditions
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GetChargeOverride.


        :param end_date: The end_date of this GetChargeOverride.  # noqa: E501
        :type: EndConditions
        """

        self._end_date = end_date

    @property
    def exclude_item_billing_from_revenue_accounting(self):
        """Gets the exclude_item_billing_from_revenue_accounting of this GetChargeOverride.  # noqa: E501

        The flag to exclude rate plan charge related invoice items, invoice item adjustments, credit memo items, and debit memo items from revenue accounting.  **Note**: This field is only available if you have the [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration) feature enabled.    # noqa: E501

        :return: The exclude_item_billing_from_revenue_accounting of this GetChargeOverride.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_item_billing_from_revenue_accounting

    @exclude_item_billing_from_revenue_accounting.setter
    def exclude_item_billing_from_revenue_accounting(self, exclude_item_billing_from_revenue_accounting):
        """Sets the exclude_item_billing_from_revenue_accounting of this GetChargeOverride.

        The flag to exclude rate plan charge related invoice items, invoice item adjustments, credit memo items, and debit memo items from revenue accounting.  **Note**: This field is only available if you have the [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration) feature enabled.    # noqa: E501

        :param exclude_item_billing_from_revenue_accounting: The exclude_item_billing_from_revenue_accounting of this GetChargeOverride.  # noqa: E501
        :type: bool
        """

        self._exclude_item_billing_from_revenue_accounting = exclude_item_billing_from_revenue_accounting

    @property
    def exclude_item_booking_from_revenue_accounting(self):
        """Gets the exclude_item_booking_from_revenue_accounting of this GetChargeOverride.  # noqa: E501

        The flag to exclude rate plan charges from revenue accounting.  **Note**: This field is only available if you have the [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration) feature enabled.    # noqa: E501

        :return: The exclude_item_booking_from_revenue_accounting of this GetChargeOverride.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_item_booking_from_revenue_accounting

    @exclude_item_booking_from_revenue_accounting.setter
    def exclude_item_booking_from_revenue_accounting(self, exclude_item_booking_from_revenue_accounting):
        """Sets the exclude_item_booking_from_revenue_accounting of this GetChargeOverride.

        The flag to exclude rate plan charges from revenue accounting.  **Note**: This field is only available if you have the [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration) feature enabled.    # noqa: E501

        :param exclude_item_booking_from_revenue_accounting: The exclude_item_booking_from_revenue_accounting of this GetChargeOverride.  # noqa: E501
        :type: bool
        """

        self._exclude_item_booking_from_revenue_accounting = exclude_item_booking_from_revenue_accounting

    @property
    def is_allocation_eligible(self):
        """Gets the is_allocation_eligible of this GetChargeOverride.  # noqa: E501

        This field is used to identify if the charge segment is allocation eligible in revenue recognition.  **Note**: This feature is in the **Early Adopter** phase. If you want to use the feature, submit a request at <a href=\"https://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a>, and we will evaluate whether the feature is suitable for your use cases.   # noqa: E501

        :return: The is_allocation_eligible of this GetChargeOverride.  # noqa: E501
        :rtype: bool
        """
        return self._is_allocation_eligible

    @is_allocation_eligible.setter
    def is_allocation_eligible(self, is_allocation_eligible):
        """Sets the is_allocation_eligible of this GetChargeOverride.

        This field is used to identify if the charge segment is allocation eligible in revenue recognition.  **Note**: This feature is in the **Early Adopter** phase. If you want to use the feature, submit a request at <a href=\"https://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a>, and we will evaluate whether the feature is suitable for your use cases.   # noqa: E501

        :param is_allocation_eligible: The is_allocation_eligible of this GetChargeOverride.  # noqa: E501
        :type: bool
        """

        self._is_allocation_eligible = is_allocation_eligible

    @property
    def is_rollover(self):
        """Gets the is_rollover of this GetChargeOverride.  # noqa: E501

        **Note**: This field is only available if you have the [Prepaid with Drawdown](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown) feature enabled.  To use this field, you must set the `X-Zuora-WSDL-Version` request header to 114 or higher. Otherwise, an error occurs.  The value is either \"True\" or \"False\". It determines whether the rollover fields are needed.   # noqa: E501

        :return: The is_rollover of this GetChargeOverride.  # noqa: E501
        :rtype: bool
        """
        return self._is_rollover

    @is_rollover.setter
    def is_rollover(self, is_rollover):
        """Sets the is_rollover of this GetChargeOverride.

        **Note**: This field is only available if you have the [Prepaid with Drawdown](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown) feature enabled.  To use this field, you must set the `X-Zuora-WSDL-Version` request header to 114 or higher. Otherwise, an error occurs.  The value is either \"True\" or \"False\". It determines whether the rollover fields are needed.   # noqa: E501

        :param is_rollover: The is_rollover of this GetChargeOverride.  # noqa: E501
        :type: bool
        """

        self._is_rollover = is_rollover

    @property
    def is_unbilled(self):
        """Gets the is_unbilled of this GetChargeOverride.  # noqa: E501

        This field is used to dictate how to perform the accounting during revenue recognition.  **Note**: This feature is in the **Early Adopter** phase. If you want to use the feature, submit a request at <a href=\"https://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a>, and we will evaluate whether the feature is suitable for your use cases.   # noqa: E501

        :return: The is_unbilled of this GetChargeOverride.  # noqa: E501
        :rtype: bool
        """
        return self._is_unbilled

    @is_unbilled.setter
    def is_unbilled(self, is_unbilled):
        """Sets the is_unbilled of this GetChargeOverride.

        This field is used to dictate how to perform the accounting during revenue recognition.  **Note**: This feature is in the **Early Adopter** phase. If you want to use the feature, submit a request at <a href=\"https://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a>, and we will evaluate whether the feature is suitable for your use cases.   # noqa: E501

        :param is_unbilled: The is_unbilled of this GetChargeOverride.  # noqa: E501
        :type: bool
        """

        self._is_unbilled = is_unbilled

    @property
    def prepaid_quantity(self):
        """Gets the prepaid_quantity of this GetChargeOverride.  # noqa: E501

        **Note**: This field is only available if you have the [Prepaid with Drawdown](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown) feature enabled.  The number of units included in a [prepayment charge](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown/Create_prepayment_charge). Must be a positive number (>0).   # noqa: E501

        :return: The prepaid_quantity of this GetChargeOverride.  # noqa: E501
        :rtype: float
        """
        return self._prepaid_quantity

    @prepaid_quantity.setter
    def prepaid_quantity(self, prepaid_quantity):
        """Sets the prepaid_quantity of this GetChargeOverride.

        **Note**: This field is only available if you have the [Prepaid with Drawdown](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown) feature enabled.  The number of units included in a [prepayment charge](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown/Create_prepayment_charge). Must be a positive number (>0).   # noqa: E501

        :param prepaid_quantity: The prepaid_quantity of this GetChargeOverride.  # noqa: E501
        :type: float
        """

        self._prepaid_quantity = prepaid_quantity

    @property
    def proration_option(self):
        """Gets the proration_option of this GetChargeOverride.  # noqa: E501


        :return: The proration_option of this GetChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._proration_option

    @proration_option.setter
    def proration_option(self, proration_option):
        """Sets the proration_option of this GetChargeOverride.


        :param proration_option: The proration_option of this GetChargeOverride.  # noqa: E501
        :type: str
        """

        self._proration_option = proration_option

    @property
    def pricing(self):
        """Gets the pricing of this GetChargeOverride.  # noqa: E501


        :return: The pricing of this GetChargeOverride.  # noqa: E501
        :rtype: ChargeOverridePricing
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this GetChargeOverride.


        :param pricing: The pricing of this GetChargeOverride.  # noqa: E501
        :type: ChargeOverridePricing
        """

        self._pricing = pricing

    @property
    def product_rate_plan_charge_number(self):
        """Gets the product_rate_plan_charge_number of this GetChargeOverride.  # noqa: E501

        Number of a product rate-plan charge for this subscription.   # noqa: E501

        :return: The product_rate_plan_charge_number of this GetChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_charge_number

    @product_rate_plan_charge_number.setter
    def product_rate_plan_charge_number(self, product_rate_plan_charge_number):
        """Sets the product_rate_plan_charge_number of this GetChargeOverride.

        Number of a product rate-plan charge for this subscription.   # noqa: E501

        :param product_rate_plan_charge_number: The product_rate_plan_charge_number of this GetChargeOverride.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_charge_number = product_rate_plan_charge_number

    @property
    def product_rateplan_charge_id(self):
        """Gets the product_rateplan_charge_id of this GetChargeOverride.  # noqa: E501

        Internal identifier of the product rate plan charge that the charge is based on.   # noqa: E501

        :return: The product_rateplan_charge_id of this GetChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._product_rateplan_charge_id

    @product_rateplan_charge_id.setter
    def product_rateplan_charge_id(self, product_rateplan_charge_id):
        """Sets the product_rateplan_charge_id of this GetChargeOverride.

        Internal identifier of the product rate plan charge that the charge is based on.   # noqa: E501

        :param product_rateplan_charge_id: The product_rateplan_charge_id of this GetChargeOverride.  # noqa: E501
        :type: str
        """
        if product_rateplan_charge_id is None:
            raise ValueError("Invalid value for `product_rateplan_charge_id`, must not be `None`")  # noqa: E501

        self._product_rateplan_charge_id = product_rateplan_charge_id

    @property
    def rev_rec_code(self):
        """Gets the rev_rec_code of this GetChargeOverride.  # noqa: E501

        Revenue Recognition Code   # noqa: E501

        :return: The rev_rec_code of this GetChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._rev_rec_code

    @rev_rec_code.setter
    def rev_rec_code(self, rev_rec_code):
        """Sets the rev_rec_code of this GetChargeOverride.

        Revenue Recognition Code   # noqa: E501

        :param rev_rec_code: The rev_rec_code of this GetChargeOverride.  # noqa: E501
        :type: str
        """

        self._rev_rec_code = rev_rec_code

    @property
    def rev_rec_trigger_condition(self):
        """Gets the rev_rec_trigger_condition of this GetChargeOverride.  # noqa: E501


        :return: The rev_rec_trigger_condition of this GetChargeOverride.  # noqa: E501
        :rtype: RevRecTriggerCondition
        """
        return self._rev_rec_trigger_condition

    @rev_rec_trigger_condition.setter
    def rev_rec_trigger_condition(self, rev_rec_trigger_condition):
        """Sets the rev_rec_trigger_condition of this GetChargeOverride.


        :param rev_rec_trigger_condition: The rev_rec_trigger_condition of this GetChargeOverride.  # noqa: E501
        :type: RevRecTriggerCondition
        """

        self._rev_rec_trigger_condition = rev_rec_trigger_condition

    @property
    def revenue_recognition_rule_name(self):
        """Gets the revenue_recognition_rule_name of this GetChargeOverride.  # noqa: E501

        Specifies the revenue recognition rule, such as `Recognize upon invoicing` or `Recognize daily over time`.   # noqa: E501

        :return: The revenue_recognition_rule_name of this GetChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._revenue_recognition_rule_name

    @revenue_recognition_rule_name.setter
    def revenue_recognition_rule_name(self, revenue_recognition_rule_name):
        """Sets the revenue_recognition_rule_name of this GetChargeOverride.

        Specifies the revenue recognition rule, such as `Recognize upon invoicing` or `Recognize daily over time`.   # noqa: E501

        :param revenue_recognition_rule_name: The revenue_recognition_rule_name of this GetChargeOverride.  # noqa: E501
        :type: str
        """

        self._revenue_recognition_rule_name = revenue_recognition_rule_name

    @property
    def rollover_apply(self):
        """Gets the rollover_apply of this GetChargeOverride.  # noqa: E501


        :return: The rollover_apply of this GetChargeOverride.  # noqa: E501
        :rtype: RolloverApply
        """
        return self._rollover_apply

    @rollover_apply.setter
    def rollover_apply(self, rollover_apply):
        """Sets the rollover_apply of this GetChargeOverride.


        :param rollover_apply: The rollover_apply of this GetChargeOverride.  # noqa: E501
        :type: RolloverApply
        """

        self._rollover_apply = rollover_apply

    @property
    def rollover_periods(self):
        """Gets the rollover_periods of this GetChargeOverride.  # noqa: E501

        **Note**: This field is only available if you have the [Prepaid with Drawdown](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown) feature enabled.  To use this field, you must set the `X-Zuora-WSDL-Version` request header to 114 or higher. Otherwise, an error occurs.  This field defines the number of rollover periods, it is restricted to 3.   # noqa: E501

        :return: The rollover_periods of this GetChargeOverride.  # noqa: E501
        :rtype: float
        """
        return self._rollover_periods

    @rollover_periods.setter
    def rollover_periods(self, rollover_periods):
        """Sets the rollover_periods of this GetChargeOverride.

        **Note**: This field is only available if you have the [Prepaid with Drawdown](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Prepaid_with_Drawdown) feature enabled.  To use this field, you must set the `X-Zuora-WSDL-Version` request header to 114 or higher. Otherwise, an error occurs.  This field defines the number of rollover periods, it is restricted to 3.   # noqa: E501

        :param rollover_periods: The rollover_periods of this GetChargeOverride.  # noqa: E501
        :type: float
        """

        self._rollover_periods = rollover_periods

    @property
    def start_date(self):
        """Gets the start_date of this GetChargeOverride.  # noqa: E501


        :return: The start_date of this GetChargeOverride.  # noqa: E501
        :rtype: TriggerParams
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GetChargeOverride.


        :param start_date: The start_date of this GetChargeOverride.  # noqa: E501
        :type: TriggerParams
        """

        self._start_date = start_date

    @property
    def unique_token(self):
        """Gets the unique_token of this GetChargeOverride.  # noqa: E501

        Unique identifier for the charge. This identifier enables you to refer to the charge before the charge has an internal identifier in Zuora.  For instance, suppose that you want to use a single order to add a product to a subscription and later update the same product. When you add the product, you can set a unique identifier for the charge. Then when you update the product, you can use the same unique identifier to specify which charge to modify.   # noqa: E501

        :return: The unique_token of this GetChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._unique_token

    @unique_token.setter
    def unique_token(self, unique_token):
        """Sets the unique_token of this GetChargeOverride.

        Unique identifier for the charge. This identifier enables you to refer to the charge before the charge has an internal identifier in Zuora.  For instance, suppose that you want to use a single order to add a product to a subscription and later update the same product. When you add the product, you can set a unique identifier for the charge. Then when you update the product, you can use the same unique identifier to specify which charge to modify.   # noqa: E501

        :param unique_token: The unique_token of this GetChargeOverride.  # noqa: E501
        :type: str
        """

        self._unique_token = unique_token

    @property
    def upsell_origin_charge_number(self):
        """Gets the upsell_origin_charge_number of this GetChargeOverride.  # noqa: E501

        **Note**: The Quantity Upsell feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](https://support.zuora.com).  The identifier of the original upselling charge associated with the current charge.   # noqa: E501

        :return: The upsell_origin_charge_number of this GetChargeOverride.  # noqa: E501
        :rtype: str
        """
        return self._upsell_origin_charge_number

    @upsell_origin_charge_number.setter
    def upsell_origin_charge_number(self, upsell_origin_charge_number):
        """Sets the upsell_origin_charge_number of this GetChargeOverride.

        **Note**: The Quantity Upsell feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](https://support.zuora.com).  The identifier of the original upselling charge associated with the current charge.   # noqa: E501

        :param upsell_origin_charge_number: The upsell_origin_charge_number of this GetChargeOverride.  # noqa: E501
        :type: str
        """

        self._upsell_origin_charge_number = upsell_origin_charge_number

    @property
    def validity_period_type(self):
        """Gets the validity_period_type of this GetChargeOverride.  # noqa: E501


        :return: The validity_period_type of this GetChargeOverride.  # noqa: E501
        :rtype: ValidityPeriodType
        """
        return self._validity_period_type

    @validity_period_type.setter
    def validity_period_type(self, validity_period_type):
        """Sets the validity_period_type of this GetChargeOverride.


        :param validity_period_type: The validity_period_type of this GetChargeOverride.  # noqa: E501
        :type: ValidityPeriodType
        """

        self._validity_period_type = validity_period_type

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
        if issubclass(GetChargeOverride, dict):
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
        if not isinstance(other, GetChargeOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
