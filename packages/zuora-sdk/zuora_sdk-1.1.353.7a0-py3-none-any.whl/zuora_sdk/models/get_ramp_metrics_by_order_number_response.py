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

class GetRampMetricsByOrderNumberResponse(object):
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
        'ramp_metrics': 'list[OrderRampMetrics]',
        'process_id': 'str',
        'request_id': 'str',
        'reasons': 'list[FailedReason]',
        'success': 'bool'
    }

    attribute_map = {
        'ramp_metrics': 'rampMetrics',
        'process_id': 'processId',
        'request_id': 'requestId',
        'reasons': 'reasons',
        'success': 'success'
    }

    def __init__(self, ramp_metrics=None, process_id=None, request_id=None, reasons=None, success=None):  # noqa: E501
        """GetRampMetricsByOrderNumberResponse - a model defined in Swagger"""  # noqa: E501
        self._ramp_metrics = None
        self._process_id = None
        self._request_id = None
        self._reasons = None
        self._success = None
        self.discriminator = None
        if ramp_metrics is not None:
            self.ramp_metrics = ramp_metrics
        if process_id is not None:
            self.process_id = process_id
        if request_id is not None:
            self.request_id = request_id
        if reasons is not None:
            self.reasons = reasons
        if success is not None:
            self.success = success

    @property
    def ramp_metrics(self):
        """Gets the ramp_metrics of this GetRampMetricsByOrderNumberResponse.  # noqa: E501


        :return: The ramp_metrics of this GetRampMetricsByOrderNumberResponse.  # noqa: E501
        :rtype: list[OrderRampMetrics]
        """
        return self._ramp_metrics

    @ramp_metrics.setter
    def ramp_metrics(self, ramp_metrics):
        """Sets the ramp_metrics of this GetRampMetricsByOrderNumberResponse.


        :param ramp_metrics: The ramp_metrics of this GetRampMetricsByOrderNumberResponse.  # noqa: E501
        :type: list[OrderRampMetrics]
        """

        self._ramp_metrics = ramp_metrics

    @property
    def process_id(self):
        """Gets the process_id of this GetRampMetricsByOrderNumberResponse.  # noqa: E501

        The Id of the process that handle the operation.   # noqa: E501

        :return: The process_id of this GetRampMetricsByOrderNumberResponse.  # noqa: E501
        :rtype: str
        """
        return self._process_id

    @process_id.setter
    def process_id(self, process_id):
        """Sets the process_id of this GetRampMetricsByOrderNumberResponse.

        The Id of the process that handle the operation.   # noqa: E501

        :param process_id: The process_id of this GetRampMetricsByOrderNumberResponse.  # noqa: E501
        :type: str
        """

        self._process_id = process_id

    @property
    def request_id(self):
        """Gets the request_id of this GetRampMetricsByOrderNumberResponse.  # noqa: E501

        Unique request identifier. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.   # noqa: E501

        :return: The request_id of this GetRampMetricsByOrderNumberResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this GetRampMetricsByOrderNumberResponse.

        Unique request identifier. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.   # noqa: E501

        :param request_id: The request_id of this GetRampMetricsByOrderNumberResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def reasons(self):
        """Gets the reasons of this GetRampMetricsByOrderNumberResponse.  # noqa: E501


        :return: The reasons of this GetRampMetricsByOrderNumberResponse.  # noqa: E501
        :rtype: list[FailedReason]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this GetRampMetricsByOrderNumberResponse.


        :param reasons: The reasons of this GetRampMetricsByOrderNumberResponse.  # noqa: E501
        :type: list[FailedReason]
        """

        self._reasons = reasons

    @property
    def success(self):
        """Gets the success of this GetRampMetricsByOrderNumberResponse.  # noqa: E501

        Indicates whether the call succeeded.   # noqa: E501

        :return: The success of this GetRampMetricsByOrderNumberResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GetRampMetricsByOrderNumberResponse.

        Indicates whether the call succeeded.   # noqa: E501

        :param success: The success of this GetRampMetricsByOrderNumberResponse.  # noqa: E501
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
        if issubclass(GetRampMetricsByOrderNumberResponse, dict):
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
        if not isinstance(other, GetRampMetricsByOrderNumberResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
