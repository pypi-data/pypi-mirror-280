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

class SettingValueRequest(object):
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
        'body': 'dict(str, object)',
        'children': 'list[ChildrenSettingValueRequest]',
        'id': 'str',
        'method': 'SettingValueRequestMethod',
        'url': 'str'
    }

    attribute_map = {
        'body': 'body',
        'children': 'children',
        'id': 'id',
        'method': 'method',
        'url': 'url'
    }

    def __init__(self, body=None, children=None, id=None, method=None, url=None):  # noqa: E501
        """SettingValueRequest - a model defined in Swagger"""  # noqa: E501
        self._body = None
        self._children = None
        self._id = None
        self._method = None
        self._url = None
        self.discriminator = None
        if body is not None:
            self.body = body
        if children is not None:
            self.children = children
        if id is not None:
            self.id = id
        if method is not None:
            self.method = method
        if url is not None:
            self.url = url

    @property
    def body(self):
        """Gets the body of this SettingValueRequest.  # noqa: E501

        Request payload if any  # noqa: E501

        :return: The body of this SettingValueRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SettingValueRequest.

        Request payload if any  # noqa: E501

        :param body: The body of this SettingValueRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._body = body

    @property
    def children(self):
        """Gets the children of this SettingValueRequest.  # noqa: E501

        An array of requests that can only be executed after its parent request has been executed successfully.   # noqa: E501

        :return: The children of this SettingValueRequest.  # noqa: E501
        :rtype: list[ChildrenSettingValueRequest]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this SettingValueRequest.

        An array of requests that can only be executed after its parent request has been executed successfully.   # noqa: E501

        :param children: The children of this SettingValueRequest.  # noqa: E501
        :type: list[ChildrenSettingValueRequest]
        """

        self._children = children

    @property
    def id(self):
        """Gets the id of this SettingValueRequest.  # noqa: E501

        The id of the request. You can set it to any string. It must be unique within the whole batch.   # noqa: E501

        :return: The id of this SettingValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SettingValueRequest.

        The id of the request. You can set it to any string. It must be unique within the whole batch.   # noqa: E501

        :param id: The id of this SettingValueRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def method(self):
        """Gets the method of this SettingValueRequest.  # noqa: E501


        :return: The method of this SettingValueRequest.  # noqa: E501
        :rtype: SettingValueRequestMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this SettingValueRequest.


        :param method: The method of this SettingValueRequest.  # noqa: E501
        :type: SettingValueRequestMethod
        """

        self._method = method

    @property
    def url(self):
        """Gets the url of this SettingValueRequest.  # noqa: E501

        The relative URL of the setting. It is the same as in the `pathPattern` field in the response body of [Listing all Settings](https://www.zuora.com/developer/api-references/api/operation/Get_ListAllSettings). For example, `/billing-rules`.   # noqa: E501

        :return: The url of this SettingValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SettingValueRequest.

        The relative URL of the setting. It is the same as in the `pathPattern` field in the response body of [Listing all Settings](https://www.zuora.com/developer/api-references/api/operation/Get_ListAllSettings). For example, `/billing-rules`.   # noqa: E501

        :param url: The url of this SettingValueRequest.  # noqa: E501
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
        if issubclass(SettingValueRequest, dict):
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
        if not isinstance(other, SettingValueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
