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

class GetDebitMemoApplicationPartsResponse(object):
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
        'application_parts': 'list[GetDebitMemoApplicationPart]',
        'next_page': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'application_parts': 'applicationParts',
        'next_page': 'nextPage',
        'success': 'success'
    }

    def __init__(self, application_parts=None, next_page=None, success=None):  # noqa: E501
        """GetDebitMemoApplicationPartsResponse - a model defined in Swagger"""  # noqa: E501
        self._application_parts = None
        self._next_page = None
        self._success = None
        self.discriminator = None
        if application_parts is not None:
            self.application_parts = application_parts
        if next_page is not None:
            self.next_page = next_page
        if success is not None:
            self.success = success

    @property
    def application_parts(self):
        """Gets the application_parts of this GetDebitMemoApplicationPartsResponse.  # noqa: E501

        Container for application parts.   # noqa: E501

        :return: The application_parts of this GetDebitMemoApplicationPartsResponse.  # noqa: E501
        :rtype: list[GetDebitMemoApplicationPart]
        """
        return self._application_parts

    @application_parts.setter
    def application_parts(self, application_parts):
        """Sets the application_parts of this GetDebitMemoApplicationPartsResponse.

        Container for application parts.   # noqa: E501

        :param application_parts: The application_parts of this GetDebitMemoApplicationPartsResponse.  # noqa: E501
        :type: list[GetDebitMemoApplicationPart]
        """

        self._application_parts = application_parts

    @property
    def next_page(self):
        """Gets the next_page of this GetDebitMemoApplicationPartsResponse.  # noqa: E501

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :return: The next_page of this GetDebitMemoApplicationPartsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this GetDebitMemoApplicationPartsResponse.

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :param next_page: The next_page of this GetDebitMemoApplicationPartsResponse.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def success(self):
        """Gets the success of this GetDebitMemoApplicationPartsResponse.  # noqa: E501

        Returns `true` if the request was processed successfully.  # noqa: E501

        :return: The success of this GetDebitMemoApplicationPartsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GetDebitMemoApplicationPartsResponse.

        Returns `true` if the request was processed successfully.  # noqa: E501

        :param success: The success of this GetDebitMemoApplicationPartsResponse.  # noqa: E501
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
        if issubclass(GetDebitMemoApplicationPartsResponse, dict):
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
        if not isinstance(other, GetDebitMemoApplicationPartsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
