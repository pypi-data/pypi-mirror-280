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

class HostedPageResponse(object):
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
        'page_id': 'str',
        'page_name': 'str',
        'page_type': 'str',
        'page_version': 'str'
    }

    attribute_map = {
        'page_id': 'pageId',
        'page_name': 'pageName',
        'page_type': 'pageType',
        'page_version': 'pageVersion'
    }

    def __init__(self, page_id=None, page_name=None, page_type=None, page_version=None):  # noqa: E501
        """HostedPageResponse - a model defined in Swagger"""  # noqa: E501
        self._page_id = None
        self._page_name = None
        self._page_type = None
        self._page_version = None
        self.discriminator = None
        if page_id is not None:
            self.page_id = page_id
        if page_name is not None:
            self.page_name = page_name
        if page_type is not None:
            self.page_type = page_type
        if page_version is not None:
            self.page_version = page_version

    @property
    def page_id(self):
        """Gets the page_id of this HostedPageResponse.  # noqa: E501

        Page ID of the Payment Page that Zuora assigns when it is created.   # noqa: E501

        :return: The page_id of this HostedPageResponse.  # noqa: E501
        :rtype: str
        """
        return self._page_id

    @page_id.setter
    def page_id(self, page_id):
        """Sets the page_id of this HostedPageResponse.

        Page ID of the Payment Page that Zuora assigns when it is created.   # noqa: E501

        :param page_id: The page_id of this HostedPageResponse.  # noqa: E501
        :type: str
        """

        self._page_id = page_id

    @property
    def page_name(self):
        """Gets the page_name of this HostedPageResponse.  # noqa: E501

        Name of the Payment Page that specified during the page configuration.   # noqa: E501

        :return: The page_name of this HostedPageResponse.  # noqa: E501
        :rtype: str
        """
        return self._page_name

    @page_name.setter
    def page_name(self, page_name):
        """Sets the page_name of this HostedPageResponse.

        Name of the Payment Page that specified during the page configuration.   # noqa: E501

        :param page_name: The page_name of this HostedPageResponse.  # noqa: E501
        :type: str
        """

        self._page_name = page_name

    @property
    def page_type(self):
        """Gets the page_type of this HostedPageResponse.  # noqa: E501

        Payment method type of this Payment Page, e.g. 'Credit Card', 'ACH', or 'Bank Transfer'.   # noqa: E501

        :return: The page_type of this HostedPageResponse.  # noqa: E501
        :rtype: str
        """
        return self._page_type

    @page_type.setter
    def page_type(self, page_type):
        """Sets the page_type of this HostedPageResponse.

        Payment method type of this Payment Page, e.g. 'Credit Card', 'ACH', or 'Bank Transfer'.   # noqa: E501

        :param page_type: The page_type of this HostedPageResponse.  # noqa: E501
        :type: str
        """

        self._page_type = page_type

    @property
    def page_version(self):
        """Gets the page_version of this HostedPageResponse.  # noqa: E501

        Version of the Payment Page. 2 for Payment Pages 2.0.   # noqa: E501

        :return: The page_version of this HostedPageResponse.  # noqa: E501
        :rtype: str
        """
        return self._page_version

    @page_version.setter
    def page_version(self, page_version):
        """Sets the page_version of this HostedPageResponse.

        Version of the Payment Page. 2 for Payment Pages 2.0.   # noqa: E501

        :param page_version: The page_version of this HostedPageResponse.  # noqa: E501
        :type: str
        """

        self._page_version = page_version

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
        if issubclass(HostedPageResponse, dict):
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
        if not isinstance(other, HostedPageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
