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

class RatePlanChargeOverridePricing(object):
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
        'charge_model_data': 'OrderActionRatePlanChargeModelDataOverride',
        'discount': 'DiscountPricingOverride',
        'one_time_flat_fee': 'OneTimeFlatFeePricingOverride',
        'one_time_per_unit': 'OneTimePerUnitPricingOverride',
        'one_time_tiered': 'OneTimeTieredPricingOverride',
        'one_time_volume': 'OneTimeVolumePricingOverride',
        'recurring_delivery': 'OrderActionRatePlanRecurringDeliveryPricingOverride',
        'recurring_flat_fee': 'OrderActionRatePlanRecurringFlatFeePricingOverride',
        'recurring_per_unit': 'OrderActionRatePlanRecurringPerUnitPricingOverride',
        'recurring_tiered': 'OrderActionRatePlanRecurringTieredPricingOverride',
        'recurring_volume': 'OrderActionRatePlanRecurringVolumePricingOverride',
        'usage_flat_fee': 'UsageFlatFeePricingOverride',
        'usage_overage': 'UsageOveragePricingOverride',
        'usage_per_unit': 'UsagePerUnitPricingOverride',
        'usage_tiered': 'UsageTieredPricingOverride',
        'usage_tiered_with_overage': 'UsageTieredWithOveragePricingOverride',
        'usage_volume': 'UsageVolumePricingOverride'
    }

    attribute_map = {
        'charge_model_data': 'chargeModelData',
        'discount': 'discount',
        'one_time_flat_fee': 'oneTimeFlatFee',
        'one_time_per_unit': 'oneTimePerUnit',
        'one_time_tiered': 'oneTimeTiered',
        'one_time_volume': 'oneTimeVolume',
        'recurring_delivery': 'recurringDelivery',
        'recurring_flat_fee': 'recurringFlatFee',
        'recurring_per_unit': 'recurringPerUnit',
        'recurring_tiered': 'recurringTiered',
        'recurring_volume': 'recurringVolume',
        'usage_flat_fee': 'usageFlatFee',
        'usage_overage': 'usageOverage',
        'usage_per_unit': 'usagePerUnit',
        'usage_tiered': 'usageTiered',
        'usage_tiered_with_overage': 'usageTieredWithOverage',
        'usage_volume': 'usageVolume'
    }

    def __init__(self, charge_model_data=None, discount=None, one_time_flat_fee=None, one_time_per_unit=None, one_time_tiered=None, one_time_volume=None, recurring_delivery=None, recurring_flat_fee=None, recurring_per_unit=None, recurring_tiered=None, recurring_volume=None, usage_flat_fee=None, usage_overage=None, usage_per_unit=None, usage_tiered=None, usage_tiered_with_overage=None, usage_volume=None):  # noqa: E501
        """RatePlanChargeOverridePricing - a model defined in Swagger"""  # noqa: E501
        self._charge_model_data = None
        self._discount = None
        self._one_time_flat_fee = None
        self._one_time_per_unit = None
        self._one_time_tiered = None
        self._one_time_volume = None
        self._recurring_delivery = None
        self._recurring_flat_fee = None
        self._recurring_per_unit = None
        self._recurring_tiered = None
        self._recurring_volume = None
        self._usage_flat_fee = None
        self._usage_overage = None
        self._usage_per_unit = None
        self._usage_tiered = None
        self._usage_tiered_with_overage = None
        self._usage_volume = None
        self.discriminator = None
        if charge_model_data is not None:
            self.charge_model_data = charge_model_data
        if discount is not None:
            self.discount = discount
        if one_time_flat_fee is not None:
            self.one_time_flat_fee = one_time_flat_fee
        if one_time_per_unit is not None:
            self.one_time_per_unit = one_time_per_unit
        if one_time_tiered is not None:
            self.one_time_tiered = one_time_tiered
        if one_time_volume is not None:
            self.one_time_volume = one_time_volume
        if recurring_delivery is not None:
            self.recurring_delivery = recurring_delivery
        if recurring_flat_fee is not None:
            self.recurring_flat_fee = recurring_flat_fee
        if recurring_per_unit is not None:
            self.recurring_per_unit = recurring_per_unit
        if recurring_tiered is not None:
            self.recurring_tiered = recurring_tiered
        if recurring_volume is not None:
            self.recurring_volume = recurring_volume
        if usage_flat_fee is not None:
            self.usage_flat_fee = usage_flat_fee
        if usage_overage is not None:
            self.usage_overage = usage_overage
        if usage_per_unit is not None:
            self.usage_per_unit = usage_per_unit
        if usage_tiered is not None:
            self.usage_tiered = usage_tiered
        if usage_tiered_with_overage is not None:
            self.usage_tiered_with_overage = usage_tiered_with_overage
        if usage_volume is not None:
            self.usage_volume = usage_volume

    @property
    def charge_model_data(self):
        """Gets the charge_model_data of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The charge_model_data of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: OrderActionRatePlanChargeModelDataOverride
        """
        return self._charge_model_data

    @charge_model_data.setter
    def charge_model_data(self, charge_model_data):
        """Sets the charge_model_data of this RatePlanChargeOverridePricing.


        :param charge_model_data: The charge_model_data of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: OrderActionRatePlanChargeModelDataOverride
        """

        self._charge_model_data = charge_model_data

    @property
    def discount(self):
        """Gets the discount of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The discount of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: DiscountPricingOverride
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this RatePlanChargeOverridePricing.


        :param discount: The discount of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: DiscountPricingOverride
        """

        self._discount = discount

    @property
    def one_time_flat_fee(self):
        """Gets the one_time_flat_fee of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The one_time_flat_fee of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: OneTimeFlatFeePricingOverride
        """
        return self._one_time_flat_fee

    @one_time_flat_fee.setter
    def one_time_flat_fee(self, one_time_flat_fee):
        """Sets the one_time_flat_fee of this RatePlanChargeOverridePricing.


        :param one_time_flat_fee: The one_time_flat_fee of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: OneTimeFlatFeePricingOverride
        """

        self._one_time_flat_fee = one_time_flat_fee

    @property
    def one_time_per_unit(self):
        """Gets the one_time_per_unit of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The one_time_per_unit of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: OneTimePerUnitPricingOverride
        """
        return self._one_time_per_unit

    @one_time_per_unit.setter
    def one_time_per_unit(self, one_time_per_unit):
        """Sets the one_time_per_unit of this RatePlanChargeOverridePricing.


        :param one_time_per_unit: The one_time_per_unit of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: OneTimePerUnitPricingOverride
        """

        self._one_time_per_unit = one_time_per_unit

    @property
    def one_time_tiered(self):
        """Gets the one_time_tiered of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The one_time_tiered of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: OneTimeTieredPricingOverride
        """
        return self._one_time_tiered

    @one_time_tiered.setter
    def one_time_tiered(self, one_time_tiered):
        """Sets the one_time_tiered of this RatePlanChargeOverridePricing.


        :param one_time_tiered: The one_time_tiered of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: OneTimeTieredPricingOverride
        """

        self._one_time_tiered = one_time_tiered

    @property
    def one_time_volume(self):
        """Gets the one_time_volume of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The one_time_volume of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: OneTimeVolumePricingOverride
        """
        return self._one_time_volume

    @one_time_volume.setter
    def one_time_volume(self, one_time_volume):
        """Sets the one_time_volume of this RatePlanChargeOverridePricing.


        :param one_time_volume: The one_time_volume of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: OneTimeVolumePricingOverride
        """

        self._one_time_volume = one_time_volume

    @property
    def recurring_delivery(self):
        """Gets the recurring_delivery of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The recurring_delivery of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: OrderActionRatePlanRecurringDeliveryPricingOverride
        """
        return self._recurring_delivery

    @recurring_delivery.setter
    def recurring_delivery(self, recurring_delivery):
        """Sets the recurring_delivery of this RatePlanChargeOverridePricing.


        :param recurring_delivery: The recurring_delivery of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: OrderActionRatePlanRecurringDeliveryPricingOverride
        """

        self._recurring_delivery = recurring_delivery

    @property
    def recurring_flat_fee(self):
        """Gets the recurring_flat_fee of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The recurring_flat_fee of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: OrderActionRatePlanRecurringFlatFeePricingOverride
        """
        return self._recurring_flat_fee

    @recurring_flat_fee.setter
    def recurring_flat_fee(self, recurring_flat_fee):
        """Sets the recurring_flat_fee of this RatePlanChargeOverridePricing.


        :param recurring_flat_fee: The recurring_flat_fee of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: OrderActionRatePlanRecurringFlatFeePricingOverride
        """

        self._recurring_flat_fee = recurring_flat_fee

    @property
    def recurring_per_unit(self):
        """Gets the recurring_per_unit of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The recurring_per_unit of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: OrderActionRatePlanRecurringPerUnitPricingOverride
        """
        return self._recurring_per_unit

    @recurring_per_unit.setter
    def recurring_per_unit(self, recurring_per_unit):
        """Sets the recurring_per_unit of this RatePlanChargeOverridePricing.


        :param recurring_per_unit: The recurring_per_unit of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: OrderActionRatePlanRecurringPerUnitPricingOverride
        """

        self._recurring_per_unit = recurring_per_unit

    @property
    def recurring_tiered(self):
        """Gets the recurring_tiered of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The recurring_tiered of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: OrderActionRatePlanRecurringTieredPricingOverride
        """
        return self._recurring_tiered

    @recurring_tiered.setter
    def recurring_tiered(self, recurring_tiered):
        """Sets the recurring_tiered of this RatePlanChargeOverridePricing.


        :param recurring_tiered: The recurring_tiered of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: OrderActionRatePlanRecurringTieredPricingOverride
        """

        self._recurring_tiered = recurring_tiered

    @property
    def recurring_volume(self):
        """Gets the recurring_volume of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The recurring_volume of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: OrderActionRatePlanRecurringVolumePricingOverride
        """
        return self._recurring_volume

    @recurring_volume.setter
    def recurring_volume(self, recurring_volume):
        """Sets the recurring_volume of this RatePlanChargeOverridePricing.


        :param recurring_volume: The recurring_volume of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: OrderActionRatePlanRecurringVolumePricingOverride
        """

        self._recurring_volume = recurring_volume

    @property
    def usage_flat_fee(self):
        """Gets the usage_flat_fee of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The usage_flat_fee of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: UsageFlatFeePricingOverride
        """
        return self._usage_flat_fee

    @usage_flat_fee.setter
    def usage_flat_fee(self, usage_flat_fee):
        """Sets the usage_flat_fee of this RatePlanChargeOverridePricing.


        :param usage_flat_fee: The usage_flat_fee of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: UsageFlatFeePricingOverride
        """

        self._usage_flat_fee = usage_flat_fee

    @property
    def usage_overage(self):
        """Gets the usage_overage of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The usage_overage of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: UsageOveragePricingOverride
        """
        return self._usage_overage

    @usage_overage.setter
    def usage_overage(self, usage_overage):
        """Sets the usage_overage of this RatePlanChargeOverridePricing.


        :param usage_overage: The usage_overage of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: UsageOveragePricingOverride
        """

        self._usage_overage = usage_overage

    @property
    def usage_per_unit(self):
        """Gets the usage_per_unit of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The usage_per_unit of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: UsagePerUnitPricingOverride
        """
        return self._usage_per_unit

    @usage_per_unit.setter
    def usage_per_unit(self, usage_per_unit):
        """Sets the usage_per_unit of this RatePlanChargeOverridePricing.


        :param usage_per_unit: The usage_per_unit of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: UsagePerUnitPricingOverride
        """

        self._usage_per_unit = usage_per_unit

    @property
    def usage_tiered(self):
        """Gets the usage_tiered of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The usage_tiered of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: UsageTieredPricingOverride
        """
        return self._usage_tiered

    @usage_tiered.setter
    def usage_tiered(self, usage_tiered):
        """Sets the usage_tiered of this RatePlanChargeOverridePricing.


        :param usage_tiered: The usage_tiered of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: UsageTieredPricingOverride
        """

        self._usage_tiered = usage_tiered

    @property
    def usage_tiered_with_overage(self):
        """Gets the usage_tiered_with_overage of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The usage_tiered_with_overage of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: UsageTieredWithOveragePricingOverride
        """
        return self._usage_tiered_with_overage

    @usage_tiered_with_overage.setter
    def usage_tiered_with_overage(self, usage_tiered_with_overage):
        """Sets the usage_tiered_with_overage of this RatePlanChargeOverridePricing.


        :param usage_tiered_with_overage: The usage_tiered_with_overage of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: UsageTieredWithOveragePricingOverride
        """

        self._usage_tiered_with_overage = usage_tiered_with_overage

    @property
    def usage_volume(self):
        """Gets the usage_volume of this RatePlanChargeOverridePricing.  # noqa: E501


        :return: The usage_volume of this RatePlanChargeOverridePricing.  # noqa: E501
        :rtype: UsageVolumePricingOverride
        """
        return self._usage_volume

    @usage_volume.setter
    def usage_volume(self, usage_volume):
        """Sets the usage_volume of this RatePlanChargeOverridePricing.


        :param usage_volume: The usage_volume of this RatePlanChargeOverridePricing.  # noqa: E501
        :type: UsageVolumePricingOverride
        """

        self._usage_volume = usage_volume

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
        if issubclass(RatePlanChargeOverridePricing, dict):
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
        if not isinstance(other, RatePlanChargeOverridePricing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
