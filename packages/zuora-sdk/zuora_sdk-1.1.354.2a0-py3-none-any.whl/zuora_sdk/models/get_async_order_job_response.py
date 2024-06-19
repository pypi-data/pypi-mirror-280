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

class GetAsyncOrderJobResponse(object):
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
        'errors': 'str',
        'result': 'AsyncOrderJobResult',
        'status': 'JobStatus',
        'success': 'bool'
    }

    attribute_map = {
        'errors': 'errors',
        'result': 'result',
        'status': 'status',
        'success': 'success'
    }

    def __init__(self, errors=None, result=None, status=None, success=None):  # noqa: E501
        """GetAsyncOrderJobResponse - a model defined in Swagger"""  # noqa: E501
        self._errors = None
        self._result = None
        self._status = None
        self._success = None
        self.discriminator = None
        if errors is not None:
            self.errors = errors
        if result is not None:
            self.result = result
        if status is not None:
            self.status = status
        if success is not None:
            self.success = success

    @property
    def errors(self):
        """Gets the errors of this GetAsyncOrderJobResponse.  # noqa: E501

        Error messages returned if the job failed.  # noqa: E501

        :return: The errors of this GetAsyncOrderJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this GetAsyncOrderJobResponse.

        Error messages returned if the job failed.  # noqa: E501

        :param errors: The errors of this GetAsyncOrderJobResponse.  # noqa: E501
        :type: str
        """

        self._errors = errors

    @property
    def result(self):
        """Gets the result of this GetAsyncOrderJobResponse.  # noqa: E501


        :return: The result of this GetAsyncOrderJobResponse.  # noqa: E501
        :rtype: AsyncOrderJobResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this GetAsyncOrderJobResponse.


        :param result: The result of this GetAsyncOrderJobResponse.  # noqa: E501
        :type: AsyncOrderJobResult
        """

        self._result = result

    @property
    def status(self):
        """Gets the status of this GetAsyncOrderJobResponse.  # noqa: E501


        :return: The status of this GetAsyncOrderJobResponse.  # noqa: E501
        :rtype: JobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetAsyncOrderJobResponse.


        :param status: The status of this GetAsyncOrderJobResponse.  # noqa: E501
        :type: JobStatus
        """

        self._status = status

    @property
    def success(self):
        """Gets the success of this GetAsyncOrderJobResponse.  # noqa: E501

        Indicates whether the operation call succeeded.  # noqa: E501

        :return: The success of this GetAsyncOrderJobResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GetAsyncOrderJobResponse.

        Indicates whether the operation call succeeded.  # noqa: E501

        :param success: The success of this GetAsyncOrderJobResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(GetAsyncOrderJobResponse, dict):
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
        if not isinstance(other, GetAsyncOrderJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
