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

class RegenerateBillingRequest(object):
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
        'type': 'str',
        'document_id': 'str',
        'number': 'str'
    }

    attribute_map = {
        'type': 'type',
        'document_id': 'documentId',
        'number': 'number'
    }

    def __init__(self, type=None, document_id=None, number=None):  # noqa: E501
        """RegenerateBillingRequest - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._document_id = None
        self._number = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if document_id is not None:
            self.document_id = document_id
        if number is not None:
            self.number = number

    @property
    def type(self):
        """Gets the type of this RegenerateBillingRequest.  # noqa: E501


        :return: The type of this RegenerateBillingRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RegenerateBillingRequest.


        :param type: The type of this RegenerateBillingRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def document_id(self):
        """Gets the document_id of this RegenerateBillingRequest.  # noqa: E501

        Id of Invoice, CreditMemo, DebitMemo, or InvoiceItemAdjustment   # noqa: E501

        :return: The document_id of this RegenerateBillingRequest.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this RegenerateBillingRequest.

        Id of Invoice, CreditMemo, DebitMemo, or InvoiceItemAdjustment   # noqa: E501

        :param document_id: The document_id of this RegenerateBillingRequest.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def number(self):
        """Gets the number of this RegenerateBillingRequest.  # noqa: E501

        Number of Invoice, CreditMemo, DebitMemo, or InvoiceItemAdjustment   # noqa: E501

        :return: The number of this RegenerateBillingRequest.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this RegenerateBillingRequest.

        Number of Invoice, CreditMemo, DebitMemo, or InvoiceItemAdjustment   # noqa: E501

        :param number: The number of this RegenerateBillingRequest.  # noqa: E501
        :type: str
        """

        self._number = number

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
        if issubclass(RegenerateBillingRequest, dict):
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
        if not isinstance(other, RegenerateBillingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
