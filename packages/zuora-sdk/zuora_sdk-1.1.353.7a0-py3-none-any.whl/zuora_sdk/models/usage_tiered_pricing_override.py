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
from zuora_sdk.models.price_change_params import PriceChangeParams  # noqa: F401,E501

class UsageTieredPricingOverride(PriceChangeParams):
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
        'rating_group': 'str',
        'tiers': 'list[ChargeTier]',
        'uom': 'str'
    }
    if hasattr(PriceChangeParams, "swagger_types"):
        swagger_types.update(PriceChangeParams.swagger_types)

    attribute_map = {
        'rating_group': 'ratingGroup',
        'tiers': 'tiers',
        'uom': 'uom'
    }
    if hasattr(PriceChangeParams, "attribute_map"):
        attribute_map.update(PriceChangeParams.attribute_map)

    def __init__(self, rating_group=None, tiers=None, uom=None, *args, **kwargs):  # noqa: E501
        """UsageTieredPricingOverride - a model defined in Swagger"""  # noqa: E501
        self._rating_group = None
        self._tiers = None
        self._uom = None
        self.discriminator = None
        if rating_group is not None:
            self.rating_group = rating_group
        if tiers is not None:
            self.tiers = tiers
        if uom is not None:
            self.uom = uom
        PriceChangeParams.__init__(self, *args, **kwargs)

    @property
    def rating_group(self):
        """Gets the rating_group of this UsageTieredPricingOverride.  # noqa: E501

        Specifies how Zuora groups usage records when rating usage. See [Usage Rating by Group](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Usage/Usage_Rating_by_Group) for more information.   * ByBillingPeriod (default): The rating is based on all the usages in a billing period.   * ByUsageStartDate: The rating is based on all the usages on the same usage start date.    * ByUsageRecord: The rating is based on each usage record.   * ByUsageUpload: The rating is based on all the usages in a uploaded usage file (.xls or .csv). If you import a mass usage in a single upload, which contains multiple usage files in .xls or .csv format, usage records are grouped for each usage file.   # noqa: E501

        :return: The rating_group of this UsageTieredPricingOverride.  # noqa: E501
        :rtype: str
        """
        return self._rating_group

    @rating_group.setter
    def rating_group(self, rating_group):
        """Sets the rating_group of this UsageTieredPricingOverride.

        Specifies how Zuora groups usage records when rating usage. See [Usage Rating by Group](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Usage/Usage_Rating_by_Group) for more information.   * ByBillingPeriod (default): The rating is based on all the usages in a billing period.   * ByUsageStartDate: The rating is based on all the usages on the same usage start date.    * ByUsageRecord: The rating is based on each usage record.   * ByUsageUpload: The rating is based on all the usages in a uploaded usage file (.xls or .csv). If you import a mass usage in a single upload, which contains multiple usage files in .xls or .csv format, usage records are grouped for each usage file.   # noqa: E501

        :param rating_group: The rating_group of this UsageTieredPricingOverride.  # noqa: E501
        :type: str
        """
        allowed_values = ["ByBillingPeriod", "ByUsageStartDate", "ByUsageRecord", "ByUsageUpload"]  # noqa: E501
        if rating_group not in allowed_values:
            raise ValueError(
                "Invalid value for `rating_group` ({0}), must be one of {1}"  # noqa: E501
                .format(rating_group, allowed_values)
            )

        self._rating_group = rating_group

    @property
    def tiers(self):
        """Gets the tiers of this UsageTieredPricingOverride.  # noqa: E501

        List of cumulative pricing tiers in the charge.   # noqa: E501

        :return: The tiers of this UsageTieredPricingOverride.  # noqa: E501
        :rtype: list[ChargeTier]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this UsageTieredPricingOverride.

        List of cumulative pricing tiers in the charge.   # noqa: E501

        :param tiers: The tiers of this UsageTieredPricingOverride.  # noqa: E501
        :type: list[ChargeTier]
        """

        self._tiers = tiers

    @property
    def uom(self):
        """Gets the uom of this UsageTieredPricingOverride.  # noqa: E501

        Unit of measure of the standalone charge.  **Note:** This field is available when the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Manage_subscription_transactions/Orders/Standalone_Orders/AA_Overview_of_Standalone_Orders\" target=\"_blank\">Standalone Orders</a> feature is enabled.   # noqa: E501

        :return: The uom of this UsageTieredPricingOverride.  # noqa: E501
        :rtype: str
        """
        return self._uom

    @uom.setter
    def uom(self, uom):
        """Sets the uom of this UsageTieredPricingOverride.

        Unit of measure of the standalone charge.  **Note:** This field is available when the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Manage_subscription_transactions/Orders/Standalone_Orders/AA_Overview_of_Standalone_Orders\" target=\"_blank\">Standalone Orders</a> feature is enabled.   # noqa: E501

        :param uom: The uom of this UsageTieredPricingOverride.  # noqa: E501
        :type: str
        """

        self._uom = uom

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
        if issubclass(UsageTieredPricingOverride, dict):
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
        if not isinstance(other, UsageTieredPricingOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
