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

class CreateJournalEntryResponse(object):
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
        'journal_entry_number': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'journal_entry_number': 'journalEntryNumber',
        'success': 'success'
    }

    def __init__(self, journal_entry_number=None, success=None):  # noqa: E501
        """CreateJournalEntryResponse - a model defined in Swagger"""  # noqa: E501
        self._journal_entry_number = None
        self._success = None
        self.discriminator = None
        if journal_entry_number is not None:
            self.journal_entry_number = journal_entry_number
        if success is not None:
            self.success = success

    @property
    def journal_entry_number(self):
        """Gets the journal_entry_number of this CreateJournalEntryResponse.  # noqa: E501

        Journal entry number in the format JE-00000001.   # noqa: E501

        :return: The journal_entry_number of this CreateJournalEntryResponse.  # noqa: E501
        :rtype: str
        """
        return self._journal_entry_number

    @journal_entry_number.setter
    def journal_entry_number(self, journal_entry_number):
        """Sets the journal_entry_number of this CreateJournalEntryResponse.

        Journal entry number in the format JE-00000001.   # noqa: E501

        :param journal_entry_number: The journal_entry_number of this CreateJournalEntryResponse.  # noqa: E501
        :type: str
        """

        self._journal_entry_number = journal_entry_number

    @property
    def success(self):
        """Gets the success of this CreateJournalEntryResponse.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this CreateJournalEntryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CreateJournalEntryResponse.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this CreateJournalEntryResponse.  # noqa: E501
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
        if issubclass(CreateJournalEntryResponse, dict):
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
        if not isinstance(other, CreateJournalEntryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
