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

class ProxyActionqueryMoreRequestConf(object):
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
        'batch_size': 'int'
    }

    attribute_map = {
        'batch_size': 'batchSize'
    }

    def __init__(self, batch_size=None):  # noqa: E501
        """ProxyActionqueryMoreRequestConf - a model defined in Swagger"""  # noqa: E501
        self._batch_size = None
        self.discriminator = None
        if batch_size is not None:
            self.batch_size = batch_size

    @property
    def batch_size(self):
        """Gets the batch_size of this ProxyActionqueryMoreRequestConf.  # noqa: E501

        Defines the batch size of the query result. The range is 1 - 2000 (inclusive). If a value higher than 2000 is submitted, only 2000 results are returned.   # noqa: E501

        :return: The batch_size of this ProxyActionqueryMoreRequestConf.  # noqa: E501
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this ProxyActionqueryMoreRequestConf.

        Defines the batch size of the query result. The range is 1 - 2000 (inclusive). If a value higher than 2000 is submitted, only 2000 results are returned.   # noqa: E501

        :param batch_size: The batch_size of this ProxyActionqueryMoreRequestConf.  # noqa: E501
        :type: int
        """

        self._batch_size = batch_size

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
        if issubclass(ProxyActionqueryMoreRequestConf, dict):
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
        if not isinstance(other, ProxyActionqueryMoreRequestConf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
