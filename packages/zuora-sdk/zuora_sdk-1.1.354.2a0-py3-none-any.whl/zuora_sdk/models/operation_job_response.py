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
from zuora_sdk.models.common_response import CommonResponse  # noqa: F401,E501

class OperationJobResponse(CommonResponse):
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
        'id': 'str',
        'object_id': 'str',
        'object_type': 'OperationJobObjectType',
        'operation_type': 'OperationJobType',
        'status': 'OperationJobStatus'
    }
    if hasattr(CommonResponse, "swagger_types"):
        swagger_types.update(CommonResponse.swagger_types)

    attribute_map = {
        'id': 'id',
        'object_id': 'objectId',
        'object_type': 'objectType',
        'operation_type': 'operationType',
        'status': 'status'
    }
    if hasattr(CommonResponse, "attribute_map"):
        attribute_map.update(CommonResponse.attribute_map)

    def __init__(self, id=None, object_id=None, object_type=None, operation_type=None, status=None, *args, **kwargs):  # noqa: E501
        """OperationJobResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._object_id = None
        self._object_type = None
        self._operation_type = None
        self._status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if object_id is not None:
            self.object_id = object_id
        if object_type is not None:
            self.object_type = object_type
        if operation_type is not None:
            self.operation_type = operation_type
        if status is not None:
            self.status = status
        CommonResponse.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this OperationJobResponse.  # noqa: E501

        The ID of the operation job to retrieve information about.  # noqa: E501

        :return: The id of this OperationJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OperationJobResponse.

        The ID of the operation job to retrieve information about.  # noqa: E501

        :param id: The id of this OperationJobResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def object_id(self):
        """Gets the object_id of this OperationJobResponse.  # noqa: E501

        The ID of the business object which is being operated.  # noqa: E501

        :return: The object_id of this OperationJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this OperationJobResponse.

        The ID of the business object which is being operated.  # noqa: E501

        :param object_id: The object_id of this OperationJobResponse.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def object_type(self):
        """Gets the object_type of this OperationJobResponse.  # noqa: E501


        :return: The object_type of this OperationJobResponse.  # noqa: E501
        :rtype: OperationJobObjectType
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this OperationJobResponse.


        :param object_type: The object_type of this OperationJobResponse.  # noqa: E501
        :type: OperationJobObjectType
        """

        self._object_type = object_type

    @property
    def operation_type(self):
        """Gets the operation_type of this OperationJobResponse.  # noqa: E501


        :return: The operation_type of this OperationJobResponse.  # noqa: E501
        :rtype: OperationJobType
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this OperationJobResponse.


        :param operation_type: The operation_type of this OperationJobResponse.  # noqa: E501
        :type: OperationJobType
        """

        self._operation_type = operation_type

    @property
    def status(self):
        """Gets the status of this OperationJobResponse.  # noqa: E501


        :return: The status of this OperationJobResponse.  # noqa: E501
        :rtype: OperationJobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OperationJobResponse.


        :param status: The status of this OperationJobResponse.  # noqa: E501
        :type: OperationJobStatus
        """

        self._status = status

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
        if issubclass(OperationJobResponse, dict):
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
        if not isinstance(other, OperationJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
