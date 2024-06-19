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

class GetJournalEntrySegmentResponse(object):
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
        'segment_name': 'str',
        'segment_value': 'str'
    }

    attribute_map = {
        'segment_name': 'segmentName',
        'segment_value': 'segmentValue'
    }

    def __init__(self, segment_name=None, segment_value=None):  # noqa: E501
        """GetJournalEntrySegmentResponse - a model defined in Swagger"""  # noqa: E501
        self._segment_name = None
        self._segment_value = None
        self.discriminator = None
        if segment_name is not None:
            self.segment_name = segment_name
        if segment_value is not None:
            self.segment_value = segment_value

    @property
    def segment_name(self):
        """Gets the segment_name of this GetJournalEntrySegmentResponse.  # noqa: E501

        Name of segment.   # noqa: E501

        :return: The segment_name of this GetJournalEntrySegmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._segment_name

    @segment_name.setter
    def segment_name(self, segment_name):
        """Sets the segment_name of this GetJournalEntrySegmentResponse.

        Name of segment.   # noqa: E501

        :param segment_name: The segment_name of this GetJournalEntrySegmentResponse.  # noqa: E501
        :type: str
        """

        self._segment_name = segment_name

    @property
    def segment_value(self):
        """Gets the segment_value of this GetJournalEntrySegmentResponse.  # noqa: E501

        Value of segment in this summary journal entry.   # noqa: E501

        :return: The segment_value of this GetJournalEntrySegmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._segment_value

    @segment_value.setter
    def segment_value(self, segment_value):
        """Sets the segment_value of this GetJournalEntrySegmentResponse.

        Value of segment in this summary journal entry.   # noqa: E501

        :param segment_value: The segment_value of this GetJournalEntrySegmentResponse.  # noqa: E501
        :type: str
        """

        self._segment_value = segment_value

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
        if issubclass(GetJournalEntrySegmentResponse, dict):
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
        if not isinstance(other, GetJournalEntrySegmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
