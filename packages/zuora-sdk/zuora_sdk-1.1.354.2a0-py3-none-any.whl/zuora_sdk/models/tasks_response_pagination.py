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

class TasksResponsePagination(object):
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
        'next_page': 'str',
        'page': 'int',
        'page_length': 'int'
    }

    attribute_map = {
        'next_page': 'next_page',
        'page': 'page',
        'page_length': 'page_length'
    }

    def __init__(self, next_page=None, page=None, page_length=None):  # noqa: E501
        """TasksResponsePagination - a model defined in Swagger"""  # noqa: E501
        self._next_page = None
        self._page = None
        self._page_length = None
        self.discriminator = None
        if next_page is not None:
            self.next_page = next_page
        if page is not None:
            self.page = page
        if page_length is not None:
            self.page_length = page_length

    @property
    def next_page(self):
        """Gets the next_page of this TasksResponsePagination.  # noqa: E501

        A string containing the URL where the next page of data can be retrieved.   # noqa: E501

        :return: The next_page of this TasksResponsePagination.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this TasksResponsePagination.

        A string containing the URL where the next page of data can be retrieved.   # noqa: E501

        :param next_page: The next_page of this TasksResponsePagination.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def page(self):
        """Gets the page of this TasksResponsePagination.  # noqa: E501

        An integer denoting the current page number.   # noqa: E501

        :return: The page of this TasksResponsePagination.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this TasksResponsePagination.

        An integer denoting the current page number.   # noqa: E501

        :param page: The page of this TasksResponsePagination.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_length(self):
        """Gets the page_length of this TasksResponsePagination.  # noqa: E501

        An integer denoting the number of tasks in this response. The maximum value is 100.   # noqa: E501

        :return: The page_length of this TasksResponsePagination.  # noqa: E501
        :rtype: int
        """
        return self._page_length

    @page_length.setter
    def page_length(self, page_length):
        """Sets the page_length of this TasksResponsePagination.

        An integer denoting the number of tasks in this response. The maximum value is 100.   # noqa: E501

        :param page_length: The page_length of this TasksResponsePagination.  # noqa: E501
        :type: int
        """

        self._page_length = page_length

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
        if issubclass(TasksResponsePagination, dict):
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
        if not isinstance(other, TasksResponsePagination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
