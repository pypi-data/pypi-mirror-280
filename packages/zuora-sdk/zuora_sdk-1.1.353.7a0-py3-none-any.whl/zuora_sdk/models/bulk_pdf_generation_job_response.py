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

class BulkPdfGenerationJobResponse(CommonResponse):
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
        'job_id': 'str',
        'invalid_ids': 'list[str]'
    }
    if hasattr(CommonResponse, "swagger_types"):
        swagger_types.update(CommonResponse.swagger_types)

    attribute_map = {
        'job_id': 'jobId',
        'invalid_ids': 'invalidIds'
    }
    if hasattr(CommonResponse, "attribute_map"):
        attribute_map.update(CommonResponse.attribute_map)

    def __init__(self, job_id=None, invalid_ids=None, *args, **kwargs):  # noqa: E501
        """BulkPdfGenerationJobResponse - a model defined in Swagger"""  # noqa: E501
        self._job_id = None
        self._invalid_ids = None
        self.discriminator = None
        if job_id is not None:
            self.job_id = job_id
        if invalid_ids is not None:
            self.invalid_ids = invalid_ids
        CommonResponse.__init__(self, *args, **kwargs)

    @property
    def job_id(self):
        """Gets the job_id of this BulkPdfGenerationJobResponse.  # noqa: E501

        Unique Id for the Job Triggered.   # noqa: E501

        :return: The job_id of this BulkPdfGenerationJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BulkPdfGenerationJobResponse.

        Unique Id for the Job Triggered.   # noqa: E501

        :param job_id: The job_id of this BulkPdfGenerationJobResponse.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def invalid_ids(self):
        """Gets the invalid_ids of this BulkPdfGenerationJobResponse.  # noqa: E501

        Collection of Ids that are not valid.    Id is considered to be invalid if,      * Billing Document Id doesn't exist in the database for the corresponding Billing Document Type   * generateMissingPDF property is false in the Job Request and Valid PDF doesn't exist for the Billing Document Id   # noqa: E501

        :return: The invalid_ids of this BulkPdfGenerationJobResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._invalid_ids

    @invalid_ids.setter
    def invalid_ids(self, invalid_ids):
        """Sets the invalid_ids of this BulkPdfGenerationJobResponse.

        Collection of Ids that are not valid.    Id is considered to be invalid if,      * Billing Document Id doesn't exist in the database for the corresponding Billing Document Type   * generateMissingPDF property is false in the Job Request and Valid PDF doesn't exist for the Billing Document Id   # noqa: E501

        :param invalid_ids: The invalid_ids of this BulkPdfGenerationJobResponse.  # noqa: E501
        :type: list[str]
        """

        self._invalid_ids = invalid_ids

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
        if issubclass(BulkPdfGenerationJobResponse, dict):
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
        if not isinstance(other, BulkPdfGenerationJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
