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

class CompareSchemaInfoResponse(object):
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
        'custom_fields': 'list[CompareSchemaKeyValue]',
        'custom_objects': 'list[CompareSchemaKeyValue]',
        'data_access_control': 'list[CompareSchemaKeyValue]',
        'meta_data': 'object',
        'notifications': 'list[CompareSchemaKeyValue]',
        'product_catalog': 'list[CompareSchemaKeyValue]',
        'settings': 'list[CompareSchemaKeyValue]',
        'workflows': 'list[CompareSchemaKeyValue]'
    }

    attribute_map = {
        'custom_fields': 'customFields',
        'custom_objects': 'customObjects',
        'data_access_control': 'dataAccessControl',
        'meta_data': 'metaData',
        'notifications': 'notifications',
        'product_catalog': 'productCatalog',
        'settings': 'settings',
        'workflows': 'workflows'
    }

    def __init__(self, custom_fields=None, custom_objects=None, data_access_control=None, meta_data=None, notifications=None, product_catalog=None, settings=None, workflows=None):  # noqa: E501
        """CompareSchemaInfoResponse - a model defined in Swagger"""  # noqa: E501
        self._custom_fields = None
        self._custom_objects = None
        self._data_access_control = None
        self._meta_data = None
        self._notifications = None
        self._product_catalog = None
        self._settings = None
        self._workflows = None
        self.discriminator = None
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if custom_objects is not None:
            self.custom_objects = custom_objects
        if data_access_control is not None:
            self.data_access_control = data_access_control
        if meta_data is not None:
            self.meta_data = meta_data
        if notifications is not None:
            self.notifications = notifications
        if product_catalog is not None:
            self.product_catalog = product_catalog
        if settings is not None:
            self.settings = settings
        if workflows is not None:
            self.workflows = workflows

    @property
    def custom_fields(self):
        """Gets the custom_fields of this CompareSchemaInfoResponse.  # noqa: E501


        :return: The custom_fields of this CompareSchemaInfoResponse.  # noqa: E501
        :rtype: list[CompareSchemaKeyValue]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this CompareSchemaInfoResponse.


        :param custom_fields: The custom_fields of this CompareSchemaInfoResponse.  # noqa: E501
        :type: list[CompareSchemaKeyValue]
        """

        self._custom_fields = custom_fields

    @property
    def custom_objects(self):
        """Gets the custom_objects of this CompareSchemaInfoResponse.  # noqa: E501


        :return: The custom_objects of this CompareSchemaInfoResponse.  # noqa: E501
        :rtype: list[CompareSchemaKeyValue]
        """
        return self._custom_objects

    @custom_objects.setter
    def custom_objects(self, custom_objects):
        """Sets the custom_objects of this CompareSchemaInfoResponse.


        :param custom_objects: The custom_objects of this CompareSchemaInfoResponse.  # noqa: E501
        :type: list[CompareSchemaKeyValue]
        """

        self._custom_objects = custom_objects

    @property
    def data_access_control(self):
        """Gets the data_access_control of this CompareSchemaInfoResponse.  # noqa: E501


        :return: The data_access_control of this CompareSchemaInfoResponse.  # noqa: E501
        :rtype: list[CompareSchemaKeyValue]
        """
        return self._data_access_control

    @data_access_control.setter
    def data_access_control(self, data_access_control):
        """Sets the data_access_control of this CompareSchemaInfoResponse.


        :param data_access_control: The data_access_control of this CompareSchemaInfoResponse.  # noqa: E501
        :type: list[CompareSchemaKeyValue]
        """

        self._data_access_control = data_access_control

    @property
    def meta_data(self):
        """Gets the meta_data of this CompareSchemaInfoResponse.  # noqa: E501

        Json node object contains metadata.  # noqa: E501

        :return: The meta_data of this CompareSchemaInfoResponse.  # noqa: E501
        :rtype: object
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this CompareSchemaInfoResponse.

        Json node object contains metadata.  # noqa: E501

        :param meta_data: The meta_data of this CompareSchemaInfoResponse.  # noqa: E501
        :type: object
        """

        self._meta_data = meta_data

    @property
    def notifications(self):
        """Gets the notifications of this CompareSchemaInfoResponse.  # noqa: E501


        :return: The notifications of this CompareSchemaInfoResponse.  # noqa: E501
        :rtype: list[CompareSchemaKeyValue]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this CompareSchemaInfoResponse.


        :param notifications: The notifications of this CompareSchemaInfoResponse.  # noqa: E501
        :type: list[CompareSchemaKeyValue]
        """

        self._notifications = notifications

    @property
    def product_catalog(self):
        """Gets the product_catalog of this CompareSchemaInfoResponse.  # noqa: E501


        :return: The product_catalog of this CompareSchemaInfoResponse.  # noqa: E501
        :rtype: list[CompareSchemaKeyValue]
        """
        return self._product_catalog

    @product_catalog.setter
    def product_catalog(self, product_catalog):
        """Sets the product_catalog of this CompareSchemaInfoResponse.


        :param product_catalog: The product_catalog of this CompareSchemaInfoResponse.  # noqa: E501
        :type: list[CompareSchemaKeyValue]
        """

        self._product_catalog = product_catalog

    @property
    def settings(self):
        """Gets the settings of this CompareSchemaInfoResponse.  # noqa: E501


        :return: The settings of this CompareSchemaInfoResponse.  # noqa: E501
        :rtype: list[CompareSchemaKeyValue]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this CompareSchemaInfoResponse.


        :param settings: The settings of this CompareSchemaInfoResponse.  # noqa: E501
        :type: list[CompareSchemaKeyValue]
        """

        self._settings = settings

    @property
    def workflows(self):
        """Gets the workflows of this CompareSchemaInfoResponse.  # noqa: E501


        :return: The workflows of this CompareSchemaInfoResponse.  # noqa: E501
        :rtype: list[CompareSchemaKeyValue]
        """
        return self._workflows

    @workflows.setter
    def workflows(self, workflows):
        """Sets the workflows of this CompareSchemaInfoResponse.


        :param workflows: The workflows of this CompareSchemaInfoResponse.  # noqa: E501
        :type: list[CompareSchemaKeyValue]
        """

        self._workflows = workflows

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
        if issubclass(CompareSchemaInfoResponse, dict):
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
        if not isinstance(other, CompareSchemaInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
