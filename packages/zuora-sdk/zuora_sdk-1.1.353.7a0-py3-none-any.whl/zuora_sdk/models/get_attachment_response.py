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
from zuora_sdk.models.common_response import CommonResponse  # noqa: F401,E501

class GetAttachmentResponse(CommonResponse):
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
        'request_id': 'str',
        'created_by': 'str',
        'created_on': 'str',
        'description': 'str',
        'file_content_type': 'str',
        'file_id': 'str',
        'file_name': 'str',
        'id': 'str',
        'success': 'bool',
        'updated_by': 'str',
        'updated_on': 'str'
    }
    if hasattr(CommonResponse, "swagger_types"):
        swagger_types.update(CommonResponse.swagger_types)

    attribute_map = {
        'request_id': 'requestId',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'description': 'description',
        'file_content_type': 'fileContentType',
        'file_id': 'fileId',
        'file_name': 'fileName',
        'id': 'id',
        'success': 'success',
        'updated_by': 'updatedBy',
        'updated_on': 'updatedOn'
    }
    if hasattr(CommonResponse, "attribute_map"):
        attribute_map.update(CommonResponse.attribute_map)

    def __init__(self, request_id=None, created_by=None, created_on=None, description=None, file_content_type=None, file_id=None, file_name=None, id=None, success=None, updated_by=None, updated_on=None, *args, **kwargs):  # noqa: E501
        """GetAttachmentResponse - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._created_by = None
        self._created_on = None
        self._description = None
        self._file_content_type = None
        self._file_id = None
        self._file_name = None
        self._id = None
        self._success = None
        self._updated_by = None
        self._updated_on = None
        self.discriminator = None
        if request_id is not None:
            self.request_id = request_id
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if description is not None:
            self.description = description
        if file_content_type is not None:
            self.file_content_type = file_content_type
        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name
        if id is not None:
            self.id = id
        if success is not None:
            self.success = success
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_on is not None:
            self.updated_on = updated_on
        CommonResponse.__init__(self, *args, **kwargs)

    @property
    def request_id(self):
        """Gets the request_id of this GetAttachmentResponse.  # noqa: E501

        The request ID of this process.   # noqa: E501

        :return: The request_id of this GetAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this GetAttachmentResponse.

        The request ID of this process.   # noqa: E501

        :param request_id: The request_id of this GetAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def created_by(self):
        """Gets the created_by of this GetAttachmentResponse.  # noqa: E501

        Zuora user id who added this attachment to the object.   # noqa: E501

        :return: The created_by of this GetAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetAttachmentResponse.

        Zuora user id who added this attachment to the object.   # noqa: E501

        :param created_by: The created_by of this GetAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this GetAttachmentResponse.  # noqa: E501

        Date and time when the attachment was added to the object.   # noqa: E501

        :return: The created_on of this GetAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this GetAttachmentResponse.

        Date and time when the attachment was added to the object.   # noqa: E501

        :param created_on: The created_on of this GetAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    @property
    def description(self):
        """Gets the description of this GetAttachmentResponse.  # noqa: E501

        Description of the attachment.   # noqa: E501

        :return: The description of this GetAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetAttachmentResponse.

        Description of the attachment.   # noqa: E501

        :param description: The description of this GetAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file_content_type(self):
        """Gets the file_content_type of this GetAttachmentResponse.  # noqa: E501

        File type.   # noqa: E501

        :return: The file_content_type of this GetAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_content_type

    @file_content_type.setter
    def file_content_type(self, file_content_type):
        """Sets the file_content_type of this GetAttachmentResponse.

        File type.   # noqa: E501

        :param file_content_type: The file_content_type of this GetAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._file_content_type = file_content_type

    @property
    def file_id(self):
        """Gets the file_id of this GetAttachmentResponse.  # noqa: E501

        File ID of the attached file. Use this file ID with [Get files](https://www.zuora.com/developer/api-references/api/operation/Get_Files) to download the file.   # noqa: E501

        :return: The file_id of this GetAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this GetAttachmentResponse.

        File ID of the attached file. Use this file ID with [Get files](https://www.zuora.com/developer/api-references/api/operation/Get_Files) to download the file.   # noqa: E501

        :param file_id: The file_id of this GetAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def file_name(self):
        """Gets the file_name of this GetAttachmentResponse.  # noqa: E501

        Attachment file name.   # noqa: E501

        :return: The file_name of this GetAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this GetAttachmentResponse.

        Attachment file name.   # noqa: E501

        :param file_name: The file_name of this GetAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def id(self):
        """Gets the id of this GetAttachmentResponse.  # noqa: E501

        Id of this attachment.   # noqa: E501

        :return: The id of this GetAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAttachmentResponse.

        Id of this attachment.   # noqa: E501

        :param id: The id of this GetAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def success(self):
        """Gets the success of this GetAttachmentResponse.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this GetAttachmentResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GetAttachmentResponse.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this GetAttachmentResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def updated_by(self):
        """Gets the updated_by of this GetAttachmentResponse.  # noqa: E501

        Zuora user id who last updated the attachment.   # noqa: E501

        :return: The updated_by of this GetAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this GetAttachmentResponse.

        Zuora user id who last updated the attachment.   # noqa: E501

        :param updated_by: The updated_by of this GetAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def updated_on(self):
        """Gets the updated_on of this GetAttachmentResponse.  # noqa: E501

        Date and time when the attachment was last updated.   # noqa: E501

        :return: The updated_on of this GetAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this GetAttachmentResponse.

        Date and time when the attachment was last updated.   # noqa: E501

        :param updated_on: The updated_on of this GetAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._updated_on = updated_on

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
        if issubclass(GetAttachmentResponse, dict):
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
        if not isinstance(other, GetAttachmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
