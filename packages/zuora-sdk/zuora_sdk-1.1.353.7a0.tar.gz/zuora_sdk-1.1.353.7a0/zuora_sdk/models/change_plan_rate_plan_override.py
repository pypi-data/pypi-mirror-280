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

class ChangePlanRatePlanOverride(object):
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
        'charge_overrides': 'list[GetChargeOverride]',
        'clearing_existing_features': 'bool',
        'custom_fields': 'dict(str, object)',
        'externally_managed_plan_id': 'str',
        'product_rate_plan_id': 'str',
        'product_rate_plan_number': 'str',
        'subscription_product_features': 'list[RatePlanFeatureOverride]',
        'unique_token': 'str'
    }

    attribute_map = {
        'charge_overrides': 'chargeOverrides',
        'clearing_existing_features': 'clearingExistingFeatures',
        'custom_fields': 'customFields',
        'externally_managed_plan_id': 'externallyManagedPlanId',
        'product_rate_plan_id': 'productRatePlanId',
        'product_rate_plan_number': 'productRatePlanNumber',
        'subscription_product_features': 'subscriptionProductFeatures',
        'unique_token': 'uniqueToken'
    }

    def __init__(self, charge_overrides=None, clearing_existing_features=None, custom_fields=None, externally_managed_plan_id=None, product_rate_plan_id=None, product_rate_plan_number=None, subscription_product_features=None, unique_token=None):  # noqa: E501
        """ChangePlanRatePlanOverride - a model defined in Swagger"""  # noqa: E501
        self._charge_overrides = None
        self._clearing_existing_features = None
        self._custom_fields = None
        self._externally_managed_plan_id = None
        self._product_rate_plan_id = None
        self._product_rate_plan_number = None
        self._subscription_product_features = None
        self._unique_token = None
        self.discriminator = None
        if charge_overrides is not None:
            self.charge_overrides = charge_overrides
        if clearing_existing_features is not None:
            self.clearing_existing_features = clearing_existing_features
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if externally_managed_plan_id is not None:
            self.externally_managed_plan_id = externally_managed_plan_id
        if product_rate_plan_id is not None:
            self.product_rate_plan_id = product_rate_plan_id
        if product_rate_plan_number is not None:
            self.product_rate_plan_number = product_rate_plan_number
        if subscription_product_features is not None:
            self.subscription_product_features = subscription_product_features
        if unique_token is not None:
            self.unique_token = unique_token

    @property
    def charge_overrides(self):
        """Gets the charge_overrides of this ChangePlanRatePlanOverride.  # noqa: E501

        List of charges associated with the rate plan.   # noqa: E501

        :return: The charge_overrides of this ChangePlanRatePlanOverride.  # noqa: E501
        :rtype: list[GetChargeOverride]
        """
        return self._charge_overrides

    @charge_overrides.setter
    def charge_overrides(self, charge_overrides):
        """Sets the charge_overrides of this ChangePlanRatePlanOverride.

        List of charges associated with the rate plan.   # noqa: E501

        :param charge_overrides: The charge_overrides of this ChangePlanRatePlanOverride.  # noqa: E501
        :type: list[GetChargeOverride]
        """

        self._charge_overrides = charge_overrides

    @property
    def clearing_existing_features(self):
        """Gets the clearing_existing_features of this ChangePlanRatePlanOverride.  # noqa: E501

        Specifies whether all features in the rate plan will be cleared.   # noqa: E501

        :return: The clearing_existing_features of this ChangePlanRatePlanOverride.  # noqa: E501
        :rtype: bool
        """
        return self._clearing_existing_features

    @clearing_existing_features.setter
    def clearing_existing_features(self, clearing_existing_features):
        """Sets the clearing_existing_features of this ChangePlanRatePlanOverride.

        Specifies whether all features in the rate plan will be cleared.   # noqa: E501

        :param clearing_existing_features: The clearing_existing_features of this ChangePlanRatePlanOverride.  # noqa: E501
        :type: bool
        """

        self._clearing_existing_features = clearing_existing_features

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ChangePlanRatePlanOverride.  # noqa: E501

        Container for custom fields of the Rate Plan object. The custom fields of the Rate Plan object are used when rate plans are subscribed.   # noqa: E501

        :return: The custom_fields of this ChangePlanRatePlanOverride.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ChangePlanRatePlanOverride.

        Container for custom fields of the Rate Plan object. The custom fields of the Rate Plan object are used when rate plans are subscribed.   # noqa: E501

        :param custom_fields: The custom_fields of this ChangePlanRatePlanOverride.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def externally_managed_plan_id(self):
        """Gets the externally_managed_plan_id of this ChangePlanRatePlanOverride.  # noqa: E501

        Indicates the unique identifier for the rate plan purchased on a third-party store. This field is used to represent a subscription rate plan created through third-party stores.   # noqa: E501

        :return: The externally_managed_plan_id of this ChangePlanRatePlanOverride.  # noqa: E501
        :rtype: str
        """
        return self._externally_managed_plan_id

    @externally_managed_plan_id.setter
    def externally_managed_plan_id(self, externally_managed_plan_id):
        """Sets the externally_managed_plan_id of this ChangePlanRatePlanOverride.

        Indicates the unique identifier for the rate plan purchased on a third-party store. This field is used to represent a subscription rate plan created through third-party stores.   # noqa: E501

        :param externally_managed_plan_id: The externally_managed_plan_id of this ChangePlanRatePlanOverride.  # noqa: E501
        :type: str
        """

        self._externally_managed_plan_id = externally_managed_plan_id

    @property
    def product_rate_plan_id(self):
        """Gets the product_rate_plan_id of this ChangePlanRatePlanOverride.  # noqa: E501

        Internal identifier of the product rate plan that the rate plan is based on.   # noqa: E501

        :return: The product_rate_plan_id of this ChangePlanRatePlanOverride.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_id

    @product_rate_plan_id.setter
    def product_rate_plan_id(self, product_rate_plan_id):
        """Sets the product_rate_plan_id of this ChangePlanRatePlanOverride.

        Internal identifier of the product rate plan that the rate plan is based on.   # noqa: E501

        :param product_rate_plan_id: The product_rate_plan_id of this ChangePlanRatePlanOverride.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_id = product_rate_plan_id

    @property
    def product_rate_plan_number(self):
        """Gets the product_rate_plan_number of this ChangePlanRatePlanOverride.  # noqa: E501

        Number of a product rate plan for this subscription.   # noqa: E501

        :return: The product_rate_plan_number of this ChangePlanRatePlanOverride.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_number

    @product_rate_plan_number.setter
    def product_rate_plan_number(self, product_rate_plan_number):
        """Sets the product_rate_plan_number of this ChangePlanRatePlanOverride.

        Number of a product rate plan for this subscription.   # noqa: E501

        :param product_rate_plan_number: The product_rate_plan_number of this ChangePlanRatePlanOverride.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_number = product_rate_plan_number

    @property
    def subscription_product_features(self):
        """Gets the subscription_product_features of this ChangePlanRatePlanOverride.  # noqa: E501

        List of features associated with the rate plan. The system compares the `subscriptionProductFeatures` and `featureId` fields in the request with the counterpart fields in a rate plan. The comparison results are as follows: * If there is no `subscriptionProductFeatures` field or the field is empty, features in the rate plan remain unchanged. But if the `clearingExistingFeatures` field is additionally set to true, all features in the rate plan are cleared. * If the `subscriptionProductFeatures` field contains the `featureId` nested fields, as well as the optional `description` and `customFields` nested fields, the features indicated by the featureId nested fields in the request overwrite all features in the rate plan.   # noqa: E501

        :return: The subscription_product_features of this ChangePlanRatePlanOverride.  # noqa: E501
        :rtype: list[RatePlanFeatureOverride]
        """
        return self._subscription_product_features

    @subscription_product_features.setter
    def subscription_product_features(self, subscription_product_features):
        """Sets the subscription_product_features of this ChangePlanRatePlanOverride.

        List of features associated with the rate plan. The system compares the `subscriptionProductFeatures` and `featureId` fields in the request with the counterpart fields in a rate plan. The comparison results are as follows: * If there is no `subscriptionProductFeatures` field or the field is empty, features in the rate plan remain unchanged. But if the `clearingExistingFeatures` field is additionally set to true, all features in the rate plan are cleared. * If the `subscriptionProductFeatures` field contains the `featureId` nested fields, as well as the optional `description` and `customFields` nested fields, the features indicated by the featureId nested fields in the request overwrite all features in the rate plan.   # noqa: E501

        :param subscription_product_features: The subscription_product_features of this ChangePlanRatePlanOverride.  # noqa: E501
        :type: list[RatePlanFeatureOverride]
        """

        self._subscription_product_features = subscription_product_features

    @property
    def unique_token(self):
        """Gets the unique_token of this ChangePlanRatePlanOverride.  # noqa: E501

        Unique identifier for the rate plan. This identifier enables you to refer to the rate plan before the rate plan has an internal identifier in Zuora.  For instance, suppose that you want to use a single order to add a product to a subscription and later update the same product. When you add the product, you can set a unique identifier for the rate plan. Then when you update the product, you can use the same unique identifier to specify which rate plan to modify.   # noqa: E501

        :return: The unique_token of this ChangePlanRatePlanOverride.  # noqa: E501
        :rtype: str
        """
        return self._unique_token

    @unique_token.setter
    def unique_token(self, unique_token):
        """Sets the unique_token of this ChangePlanRatePlanOverride.

        Unique identifier for the rate plan. This identifier enables you to refer to the rate plan before the rate plan has an internal identifier in Zuora.  For instance, suppose that you want to use a single order to add a product to a subscription and later update the same product. When you add the product, you can set a unique identifier for the rate plan. Then when you update the product, you can use the same unique identifier to specify which rate plan to modify.   # noqa: E501

        :param unique_token: The unique_token of this ChangePlanRatePlanOverride.  # noqa: E501
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
        if issubclass(ChangePlanRatePlanOverride, dict):
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
        if not isinstance(other, ChangePlanRatePlanOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
