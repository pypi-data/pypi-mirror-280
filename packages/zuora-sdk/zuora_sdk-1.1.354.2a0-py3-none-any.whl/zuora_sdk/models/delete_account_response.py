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

class DeleteAccountResponse(CommonResponse):
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
        'job_id': 'str',
        'job_status': 'OperationJobStatus'
    }
    if hasattr(CommonResponse, "swagger_types"):
        swagger_types.update(CommonResponse.swagger_types)

    attribute_map = {
        'id': 'id',
        'job_id': 'jobId',
        'job_status': 'jobStatus'
    }
    if hasattr(CommonResponse, "attribute_map"):
        attribute_map.update(CommonResponse.attribute_map)

    def __init__(self, id=None, job_id=None, job_status=None, *args, **kwargs):  # noqa: E501
        """DeleteAccountResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._job_id = None
        self._job_status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if job_id is not None:
            self.job_id = job_id
        if job_status is not None:
            self.job_status = job_status
        CommonResponse.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this DeleteAccountResponse.  # noqa: E501

        The ID of the deleted account.  # noqa: E501

        :return: The id of this DeleteAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteAccountResponse.

        The ID of the deleted account.  # noqa: E501

        :param id: The id of this DeleteAccountResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def job_id(self):
        """Gets the job_id of this DeleteAccountResponse.  # noqa: E501

        The ID of the job that handles the account deletion operation.   You can specify the value of this field as the value of the `jobId` path parameter in the [Retrieve an operation job](https://www.zuora.com/developer/api-references/api/operation/Get_OperationJob/) API operation to query job information.   # noqa: E501

        :return: The job_id of this DeleteAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DeleteAccountResponse.

        The ID of the job that handles the account deletion operation.   You can specify the value of this field as the value of the `jobId` path parameter in the [Retrieve an operation job](https://www.zuora.com/developer/api-references/api/operation/Get_OperationJob/) API operation to query job information.   # noqa: E501

        :param job_id: The job_id of this DeleteAccountResponse.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def job_status(self):
        """Gets the job_status of this DeleteAccountResponse.  # noqa: E501


        :return: The job_status of this DeleteAccountResponse.  # noqa: E501
        :rtype: OperationJobStatus
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this DeleteAccountResponse.


        :param job_status: The job_status of this DeleteAccountResponse.  # noqa: E501
        :type: OperationJobStatus
        """

        self._job_status = job_status

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
        if issubclass(DeleteAccountResponse, dict):
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
        if not isinstance(other, DeleteAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
