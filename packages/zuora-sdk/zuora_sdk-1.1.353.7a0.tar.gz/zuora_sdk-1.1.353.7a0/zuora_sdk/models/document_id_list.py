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

class DocumentIdList(object):
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
        'doc_type': 'BillingDocumentType',
        'object_ids': 'list[str]'
    }

    attribute_map = {
        'doc_type': 'docType',
        'object_ids': 'objectIds'
    }

    def __init__(self, doc_type=None, object_ids=None):  # noqa: E501
        """DocumentIdList - a model defined in Swagger"""  # noqa: E501
        self._doc_type = None
        self._object_ids = None
        self.discriminator = None
        if doc_type is not None:
            self.doc_type = doc_type
        if object_ids is not None:
            self.object_ids = object_ids

    @property
    def doc_type(self):
        """Gets the doc_type of this DocumentIdList.  # noqa: E501


        :return: The doc_type of this DocumentIdList.  # noqa: E501
        :rtype: BillingDocumentType
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        """Sets the doc_type of this DocumentIdList.


        :param doc_type: The doc_type of this DocumentIdList.  # noqa: E501
        :type: BillingDocumentType
        """

        self._doc_type = doc_type

    @property
    def object_ids(self):
        """Gets the object_ids of this DocumentIdList.  # noqa: E501

        Collection of Billing Document Ids  # noqa: E501

        :return: The object_ids of this DocumentIdList.  # noqa: E501
        :rtype: list[str]
        """
        return self._object_ids

    @object_ids.setter
    def object_ids(self, object_ids):
        """Sets the object_ids of this DocumentIdList.

        Collection of Billing Document Ids  # noqa: E501

        :param object_ids: The object_ids of this DocumentIdList.  # noqa: E501
        :type: list[str]
        """

        self._object_ids = object_ids

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
        if issubclass(DocumentIdList, dict):
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
        if not isinstance(other, DocumentIdList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
