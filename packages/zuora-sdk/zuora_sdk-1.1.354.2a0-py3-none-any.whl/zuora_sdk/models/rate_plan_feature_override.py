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

class RatePlanFeatureOverride(object):
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
        'custom_fields': 'dict(str, object)',
        'description': 'str',
        'feature_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'custom_fields': 'customFields',
        'description': 'description',
        'feature_id': 'featureId',
        'id': 'id'
    }

    def __init__(self, custom_fields=None, description=None, feature_id=None, id=None):  # noqa: E501
        """RatePlanFeatureOverride - a model defined in Swagger"""  # noqa: E501
        self._custom_fields = None
        self._description = None
        self._feature_id = None
        self._id = None
        self.discriminator = None
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if description is not None:
            self.description = description
        if feature_id is not None:
            self.feature_id = feature_id
        if id is not None:
            self.id = id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this RatePlanFeatureOverride.  # noqa: E501

        A container for custom fields of the feature.   # noqa: E501

        :return: The custom_fields of this RatePlanFeatureOverride.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this RatePlanFeatureOverride.

        A container for custom fields of the feature.   # noqa: E501

        :param custom_fields: The custom_fields of this RatePlanFeatureOverride.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def description(self):
        """Gets the description of this RatePlanFeatureOverride.  # noqa: E501

        A description of the feature.  # noqa: E501

        :return: The description of this RatePlanFeatureOverride.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RatePlanFeatureOverride.

        A description of the feature.  # noqa: E501

        :param description: The description of this RatePlanFeatureOverride.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def feature_id(self):
        """Gets the feature_id of this RatePlanFeatureOverride.  # noqa: E501

        Internal identifier of the feature in the product catalog.   # noqa: E501

        :return: The feature_id of this RatePlanFeatureOverride.  # noqa: E501
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this RatePlanFeatureOverride.

        Internal identifier of the feature in the product catalog.   # noqa: E501

        :param feature_id: The feature_id of this RatePlanFeatureOverride.  # noqa: E501
        :type: str
        """

        self._feature_id = feature_id

    @property
    def id(self):
        """Gets the id of this RatePlanFeatureOverride.  # noqa: E501

        Internal identifier of the rate plan feature override.   # noqa: E501

        :return: The id of this RatePlanFeatureOverride.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RatePlanFeatureOverride.

        Internal identifier of the rate plan feature override.   # noqa: E501

        :param id: The id of this RatePlanFeatureOverride.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(RatePlanFeatureOverride, dict):
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
        if not isinstance(other, RatePlanFeatureOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
