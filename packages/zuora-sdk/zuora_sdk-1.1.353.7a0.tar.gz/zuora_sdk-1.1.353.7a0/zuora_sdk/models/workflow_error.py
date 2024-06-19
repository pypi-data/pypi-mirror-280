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

class WorkflowError(object):
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
        'code': 'WorkflowErrorCode',
        'status': 'int',
        'title': 'str'
    }

    attribute_map = {
        'code': 'code',
        'status': 'status',
        'title': 'title'
    }

    def __init__(self, code=None, status=None, title=None):  # noqa: E501
        """WorkflowError - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._status = None
        self._title = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if status is not None:
            self.status = status
        if title is not None:
            self.title = title

    @property
    def code(self):
        """Gets the code of this WorkflowError.  # noqa: E501


        :return: The code of this WorkflowError.  # noqa: E501
        :rtype: WorkflowErrorCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this WorkflowError.


        :param code: The code of this WorkflowError.  # noqa: E501
        :type: WorkflowErrorCode
        """

        self._code = code

    @property
    def status(self):
        """Gets the status of this WorkflowError.  # noqa: E501

        The http status code for this error  # noqa: E501

        :return: The status of this WorkflowError.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkflowError.

        The http status code for this error  # noqa: E501

        :param status: The status of this WorkflowError.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def title(self):
        """Gets the title of this WorkflowError.  # noqa: E501

        A human readable description describing the error  # noqa: E501

        :return: The title of this WorkflowError.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WorkflowError.

        A human readable description describing the error  # noqa: E501

        :param title: The title of this WorkflowError.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(WorkflowError, dict):
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
        if not isinstance(other, WorkflowError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
