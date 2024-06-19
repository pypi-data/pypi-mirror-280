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

class CreateSequenceSetsResponse(object):
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
        'sequence_sets': 'list[GetSequenceSetResponse]',
        'success': 'bool'
    }

    attribute_map = {
        'sequence_sets': 'sequenceSets',
        'success': 'success'
    }

    def __init__(self, sequence_sets=None, success=None):  # noqa: E501
        """CreateSequenceSetsResponse - a model defined in Swagger"""  # noqa: E501
        self._sequence_sets = None
        self._success = None
        self.discriminator = None
        if sequence_sets is not None:
            self.sequence_sets = sequence_sets
        if success is not None:
            self.success = success

    @property
    def sequence_sets(self):
        """Gets the sequence_sets of this CreateSequenceSetsResponse.  # noqa: E501

        Array of sequence sets configured for billing documents, payments, and refunds.   # noqa: E501

        :return: The sequence_sets of this CreateSequenceSetsResponse.  # noqa: E501
        :rtype: list[GetSequenceSetResponse]
        """
        return self._sequence_sets

    @sequence_sets.setter
    def sequence_sets(self, sequence_sets):
        """Sets the sequence_sets of this CreateSequenceSetsResponse.

        Array of sequence sets configured for billing documents, payments, and refunds.   # noqa: E501

        :param sequence_sets: The sequence_sets of this CreateSequenceSetsResponse.  # noqa: E501
        :type: list[GetSequenceSetResponse]
        """

        self._sequence_sets = sequence_sets

    @property
    def success(self):
        """Gets the success of this CreateSequenceSetsResponse.  # noqa: E501

        Indicates whether the call succeeded.   # noqa: E501

        :return: The success of this CreateSequenceSetsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CreateSequenceSetsResponse.

        Indicates whether the call succeeded.   # noqa: E501

        :param success: The success of this CreateSequenceSetsResponse.  # noqa: E501
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
        if issubclass(CreateSequenceSetsResponse, dict):
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
        if not isinstance(other, CreateSequenceSetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
