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

class SettingValueResponseWrapper(object):
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
        'method': 'SettingValueResponseWrapperMethod',
        'response': 'SettingValueResponse',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'method': 'method',
        'response': 'response',
        'url': 'url'
    }

    def __init__(self, id=None, method=None, response=None, url=None):  # noqa: E501
        """SettingValueResponseWrapper - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._method = None
        self._response = None
        self._url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if method is not None:
            self.method = method
        if response is not None:
            self.response = response
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this SettingValueResponseWrapper.  # noqa: E501

        The Id of the corresponding request.   # noqa: E501

        :return: The id of this SettingValueResponseWrapper.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SettingValueResponseWrapper.

        The Id of the corresponding request.   # noqa: E501

        :param id: The id of this SettingValueResponseWrapper.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def method(self):
        """Gets the method of this SettingValueResponseWrapper.  # noqa: E501


        :return: The method of this SettingValueResponseWrapper.  # noqa: E501
        :rtype: SettingValueResponseWrapperMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this SettingValueResponseWrapper.


        :param method: The method of this SettingValueResponseWrapper.  # noqa: E501
        :type: SettingValueResponseWrapperMethod
        """

        self._method = method

    @property
    def response(self):
        """Gets the response of this SettingValueResponseWrapper.  # noqa: E501


        :return: The response of this SettingValueResponseWrapper.  # noqa: E501
        :rtype: SettingValueResponse
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this SettingValueResponseWrapper.


        :param response: The response of this SettingValueResponseWrapper.  # noqa: E501
        :type: SettingValueResponse
        """

        self._response = response

    @property
    def url(self):
        """Gets the url of this SettingValueResponseWrapper.  # noqa: E501

        The url as specified in the corresponding request.   # noqa: E501

        :return: The url of this SettingValueResponseWrapper.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SettingValueResponseWrapper.

        The url as specified in the corresponding request.   # noqa: E501

        :param url: The url of this SettingValueResponseWrapper.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(SettingValueResponseWrapper, dict):
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
        if not isinstance(other, SettingValueResponseWrapper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
