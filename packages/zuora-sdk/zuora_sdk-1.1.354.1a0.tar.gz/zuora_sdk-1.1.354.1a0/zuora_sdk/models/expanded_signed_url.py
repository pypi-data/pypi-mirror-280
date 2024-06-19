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

class ExpandedSignedUrl(object):
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
        'status': 'str',
        'signed_url': 'str'
    }

    attribute_map = {
        'status': 'status',
        'signed_url': 'signed_url'
    }

    def __init__(self, status='success', signed_url='signed url'):  # noqa: E501
        """ExpandedSignedUrl - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._signed_url = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if signed_url is not None:
            self.signed_url = signed_url

    @property
    def status(self):
        """Gets the status of this ExpandedSignedUrl.  # noqa: E501

        Response Status  # noqa: E501

        :return: The status of this ExpandedSignedUrl.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExpandedSignedUrl.

        Response Status  # noqa: E501

        :param status: The status of this ExpandedSignedUrl.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def signed_url(self):
        """Gets the signed_url of this ExpandedSignedUrl.  # noqa: E501

        Signed s3 URL  # noqa: E501

        :return: The signed_url of this ExpandedSignedUrl.  # noqa: E501
        :rtype: str
        """
        return self._signed_url

    @signed_url.setter
    def signed_url(self, signed_url):
        """Sets the signed_url of this ExpandedSignedUrl.

        Signed s3 URL  # noqa: E501

        :param signed_url: The signed_url of this ExpandedSignedUrl.  # noqa: E501
        :type: str
        """

        self._signed_url = signed_url

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
        if issubclass(ExpandedSignedUrl, dict):
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
        if not isinstance(other, ExpandedSignedUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
