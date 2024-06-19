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

class CreateOpenPaymentMethodTypeRequest(object):
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
        'entity_id': 'str',
        'fields': 'list[OpenPaymentMethodTypeRequestFields]',
        'internal_name': 'str',
        'label': 'str',
        'method_reference_id_field': 'str',
        'sub_type_field': 'str',
        'tenant_id': 'str',
        'user_reference_id_field': 'str'
    }

    attribute_map = {
        'entity_id': 'entityId',
        'fields': 'fields',
        'internal_name': 'internalName',
        'label': 'label',
        'method_reference_id_field': 'methodReferenceIdField',
        'sub_type_field': 'subTypeField',
        'tenant_id': 'tenantId',
        'user_reference_id_field': 'userReferenceIdField'
    }

    def __init__(self, entity_id=None, fields=None, internal_name=None, label=None, method_reference_id_field=None, sub_type_field=None, tenant_id=None, user_reference_id_field=None):  # noqa: E501
        """CreateOpenPaymentMethodTypeRequest - a model defined in Swagger"""  # noqa: E501
        self._entity_id = None
        self._fields = None
        self._internal_name = None
        self._label = None
        self._method_reference_id_field = None
        self._sub_type_field = None
        self._tenant_id = None
        self._user_reference_id_field = None
        self.discriminator = None
        if entity_id is not None:
            self.entity_id = entity_id
        self.fields = fields
        self.internal_name = internal_name
        self.label = label
        self.method_reference_id_field = method_reference_id_field
        if sub_type_field is not None:
            self.sub_type_field = sub_type_field
        self.tenant_id = tenant_id
        if user_reference_id_field is not None:
            self.user_reference_id_field = user_reference_id_field

    @property
    def entity_id(self):
        """Gets the entity_id of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501

        If this custom payment method type is specific to one entity only, provide the entity ID in this field in UUID format, such as `123e4567-e89b-12d3-a456-426614174000`. If no entity UUID is provided, the custom payment method type is available to the global entity and all the sub entities in the tenant.  You can get the entity ID through the [Multi-entity: List entities](https://www.zuora.com/developer/api-references/older-api/operation/Get_Entities/) API operation or the **Manage Entity Profile** administration setting in the UI. To convert the format of the entity ID to UUID, separate the entity ID string in five groups with hyphens, in the form `<8-characters>-<4-characters>-<4-characters>-<4-characters>-<12-characters>` for a total of 36 characters.  Note: After the custom payment method type is created, you can only update this field to be empty.   # noqa: E501

        :return: The entity_id of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this CreateOpenPaymentMethodTypeRequest.

        If this custom payment method type is specific to one entity only, provide the entity ID in this field in UUID format, such as `123e4567-e89b-12d3-a456-426614174000`. If no entity UUID is provided, the custom payment method type is available to the global entity and all the sub entities in the tenant.  You can get the entity ID through the [Multi-entity: List entities](https://www.zuora.com/developer/api-references/older-api/operation/Get_Entities/) API operation or the **Manage Entity Profile** administration setting in the UI. To convert the format of the entity ID to UUID, separate the entity ID string in five groups with hyphens, in the form `<8-characters>-<4-characters>-<4-characters>-<4-characters>-<12-characters>` for a total of 36 characters.  Note: After the custom payment method type is created, you can only update this field to be empty.   # noqa: E501

        :param entity_id: The entity_id of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def fields(self):
        """Gets the fields of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501

        An array containing field metadata of the custom payment method type.  Notes:   - All the following nested metadata must be provided in the request to define a field.    - At least one field must be defined in the fields array for a custom payment method type.    - Up to 20 fields can be defined in the fields array for a custom payment method type.   # noqa: E501

        :return: The fields of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :rtype: list[OpenPaymentMethodTypeRequestFields]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this CreateOpenPaymentMethodTypeRequest.

        An array containing field metadata of the custom payment method type.  Notes:   - All the following nested metadata must be provided in the request to define a field.    - At least one field must be defined in the fields array for a custom payment method type.    - Up to 20 fields can be defined in the fields array for a custom payment method type.   # noqa: E501

        :param fields: The fields of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :type: list[OpenPaymentMethodTypeRequestFields]
        """
        if fields is None:
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def internal_name(self):
        """Gets the internal_name of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501

        A string to identify the custom payment method type in the API name of the payment method type.  This field must be alphanumeric, starting with a capital letter, excluding JSON preserved characters such as  * \\ ’ ”. Additionally, '_' or '-' is not allowed.  This field must be unique in a tenant.  This field is used along with the `tenantId` field by the system to construct and generate the API name of the custom payment method type in the following way:  `<internalName>__c_<tenantId>`  For example, if `internalName` is `AmazonPay`, and `tenantId` is `12368`, the API name of the custom payment method type will be `AmazonPay__c_12368`.  This field cannot be updated after the creation of the custom payment method type.   # noqa: E501

        :return: The internal_name of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._internal_name

    @internal_name.setter
    def internal_name(self, internal_name):
        """Sets the internal_name of this CreateOpenPaymentMethodTypeRequest.

        A string to identify the custom payment method type in the API name of the payment method type.  This field must be alphanumeric, starting with a capital letter, excluding JSON preserved characters such as  * \\ ’ ”. Additionally, '_' or '-' is not allowed.  This field must be unique in a tenant.  This field is used along with the `tenantId` field by the system to construct and generate the API name of the custom payment method type in the following way:  `<internalName>__c_<tenantId>`  For example, if `internalName` is `AmazonPay`, and `tenantId` is `12368`, the API name of the custom payment method type will be `AmazonPay__c_12368`.  This field cannot be updated after the creation of the custom payment method type.   # noqa: E501

        :param internal_name: The internal_name of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :type: str
        """
        if internal_name is None:
            raise ValueError("Invalid value for `internal_name`, must not be `None`")  # noqa: E501

        self._internal_name = internal_name

    @property
    def label(self):
        """Gets the label of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501

        The label that is used to refer to this type in the Zuora UI.  This value must be alphanumeric, excluding JSON preserved characters such as  * \\ ’ ”    # noqa: E501

        :return: The label of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CreateOpenPaymentMethodTypeRequest.

        The label that is used to refer to this type in the Zuora UI.  This value must be alphanumeric, excluding JSON preserved characters such as  * \\ ’ ”    # noqa: E501

        :param label: The label of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def method_reference_id_field(self):
        """Gets the method_reference_id_field of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501

        The identification reference of the custom payment method.  This field should be mapped to a field name defined in the `fields` array for the purpose of being used as a filter in reporting tools such as Payment Method Data Source Exports and Data Query.  This field cannot be updated after the creation of the custom payment method type.   # noqa: E501

        :return: The method_reference_id_field of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._method_reference_id_field

    @method_reference_id_field.setter
    def method_reference_id_field(self, method_reference_id_field):
        """Sets the method_reference_id_field of this CreateOpenPaymentMethodTypeRequest.

        The identification reference of the custom payment method.  This field should be mapped to a field name defined in the `fields` array for the purpose of being used as a filter in reporting tools such as Payment Method Data Source Exports and Data Query.  This field cannot be updated after the creation of the custom payment method type.   # noqa: E501

        :param method_reference_id_field: The method_reference_id_field of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :type: str
        """
        if method_reference_id_field is None:
            raise ValueError("Invalid value for `method_reference_id_field`, must not be `None`")  # noqa: E501

        self._method_reference_id_field = method_reference_id_field

    @property
    def sub_type_field(self):
        """Gets the sub_type_field of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501

        The identification reference indicating the subtype of the custom payment method.  This field should be mapped to a field name defined in the `fields` array for the purpose of being used as a filter in reporting tools such as Data Source Exports and Data Query.  This field cannot be updated after the creation of the custom payment method type.   # noqa: E501

        :return: The sub_type_field of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub_type_field

    @sub_type_field.setter
    def sub_type_field(self, sub_type_field):
        """Sets the sub_type_field of this CreateOpenPaymentMethodTypeRequest.

        The identification reference indicating the subtype of the custom payment method.  This field should be mapped to a field name defined in the `fields` array for the purpose of being used as a filter in reporting tools such as Data Source Exports and Data Query.  This field cannot be updated after the creation of the custom payment method type.   # noqa: E501

        :param sub_type_field: The sub_type_field of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :type: str
        """

        self._sub_type_field = sub_type_field

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501

        Zuora tenant ID. If multi-entity is enabled in your tenant, this is the ID of the parent tenant of all the sub entities.  This field cannot be updated after the creation of the custom payment method type.   # noqa: E501

        :return: The tenant_id of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateOpenPaymentMethodTypeRequest.

        Zuora tenant ID. If multi-entity is enabled in your tenant, this is the ID of the parent tenant of all the sub entities.  This field cannot be updated after the creation of the custom payment method type.   # noqa: E501

        :param tenant_id: The tenant_id of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :type: str
        """
        if tenant_id is None:
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def user_reference_id_field(self):
        """Gets the user_reference_id_field of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501

        The identification reference of the user or customer account.  This field should be mapped to a field name defined in the `fields` array for the purpose of being used as a filter in reporting tools such as Data Source Exports and Data Query.  This field cannot be updated after the creation of the custom payment method type.   # noqa: E501

        :return: The user_reference_id_field of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_reference_id_field

    @user_reference_id_field.setter
    def user_reference_id_field(self, user_reference_id_field):
        """Sets the user_reference_id_field of this CreateOpenPaymentMethodTypeRequest.

        The identification reference of the user or customer account.  This field should be mapped to a field name defined in the `fields` array for the purpose of being used as a filter in reporting tools such as Data Source Exports and Data Query.  This field cannot be updated after the creation of the custom payment method type.   # noqa: E501

        :param user_reference_id_field: The user_reference_id_field of this CreateOpenPaymentMethodTypeRequest.  # noqa: E501
        :type: str
        """

        self._user_reference_id_field = user_reference_id_field

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
        if issubclass(CreateOpenPaymentMethodTypeRequest, dict):
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
        if not isinstance(other, CreateOpenPaymentMethodTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
