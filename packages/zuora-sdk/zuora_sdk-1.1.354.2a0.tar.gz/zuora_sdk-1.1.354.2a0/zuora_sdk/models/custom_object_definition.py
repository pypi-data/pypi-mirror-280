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

class CustomObjectDefinition(object):
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
        'created_by_id': 'str',
        'created_date': 'datetime',
        'id': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime',
        'schema': 'CustomObjectDefinitionSchema',
        'type': 'str'
    }

    attribute_map = {
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'id': 'Id',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate',
        'schema': 'schema',
        'type': 'type'
    }

    def __init__(self, created_by_id=None, created_date=None, id=None, updated_by_id=None, updated_date=None, schema=None, type=None):  # noqa: E501
        """CustomObjectDefinition - a model defined in Swagger"""  # noqa: E501
        self._created_by_id = None
        self._created_date = None
        self._id = None
        self._updated_by_id = None
        self._updated_date = None
        self._schema = None
        self._type = None
        self.discriminator = None
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if id is not None:
            self.id = id
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date
        if schema is not None:
            self.schema = schema
        if type is not None:
            self.type = type

    @property
    def created_by_id(self):
        """Gets the created_by_id of this CustomObjectDefinition.  # noqa: E501

        The creator's Id  # noqa: E501

        :return: The created_by_id of this CustomObjectDefinition.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this CustomObjectDefinition.

        The creator's Id  # noqa: E501

        :param created_by_id: The created_by_id of this CustomObjectDefinition.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this CustomObjectDefinition.  # noqa: E501

        The creation time of the custom object definition in date-time format.  # noqa: E501

        :return: The created_date of this CustomObjectDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this CustomObjectDefinition.

        The creation time of the custom object definition in date-time format.  # noqa: E501

        :param created_date: The created_date of this CustomObjectDefinition.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def id(self):
        """Gets the id of this CustomObjectDefinition.  # noqa: E501

        The unique Id of the custom object definition  # noqa: E501

        :return: The id of this CustomObjectDefinition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomObjectDefinition.

        The unique Id of the custom object definition  # noqa: E501

        :param id: The id of this CustomObjectDefinition.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this CustomObjectDefinition.  # noqa: E501

        The modifier's Id  # noqa: E501

        :return: The updated_by_id of this CustomObjectDefinition.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this CustomObjectDefinition.

        The modifier's Id  # noqa: E501

        :param updated_by_id: The updated_by_id of this CustomObjectDefinition.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this CustomObjectDefinition.  # noqa: E501

        The update time of the custom object definition in date-time format.  # noqa: E501

        :return: The updated_date of this CustomObjectDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this CustomObjectDefinition.

        The update time of the custom object definition in date-time format.  # noqa: E501

        :param updated_date: The updated_date of this CustomObjectDefinition.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

    @property
    def schema(self):
        """Gets the schema of this CustomObjectDefinition.  # noqa: E501


        :return: The schema of this CustomObjectDefinition.  # noqa: E501
        :rtype: CustomObjectDefinitionSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this CustomObjectDefinition.


        :param schema: The schema of this CustomObjectDefinition.  # noqa: E501
        :type: CustomObjectDefinitionSchema
        """

        self._schema = schema

    @property
    def type(self):
        """Gets the type of this CustomObjectDefinition.  # noqa: E501

        The API name of the custom object  # noqa: E501

        :return: The type of this CustomObjectDefinition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomObjectDefinition.

        The API name of the custom object  # noqa: E501

        :param type: The type of this CustomObjectDefinition.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(CustomObjectDefinition, dict):
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
        if not isinstance(other, CustomObjectDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
