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

class RampIntervalMetrics(object):
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
        'description': 'str',
        'discount_tcb': 'float',
        'discount_tcv': 'float',
        'end_date': 'date',
        'gross_tcb': 'float',
        'gross_tcv': 'float',
        'interval_metrics': 'list[RampIntervalChargeMetrics]',
        'name': 'str',
        'net_tcb': 'float',
        'net_tcv': 'float',
        'start_date': 'date'
    }

    attribute_map = {
        'description': 'description',
        'discount_tcb': 'discountTcb',
        'discount_tcv': 'discountTcv',
        'end_date': 'endDate',
        'gross_tcb': 'grossTcb',
        'gross_tcv': 'grossTcv',
        'interval_metrics': 'intervalMetrics',
        'name': 'name',
        'net_tcb': 'netTcb',
        'net_tcv': 'netTcv',
        'start_date': 'startDate'
    }

    def __init__(self, description=None, discount_tcb=None, discount_tcv=None, end_date=None, gross_tcb=None, gross_tcv=None, interval_metrics=None, name=None, net_tcb=None, net_tcv=None, start_date=None):  # noqa: E501
        """RampIntervalMetrics - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._discount_tcb = None
        self._discount_tcv = None
        self._end_date = None
        self._gross_tcb = None
        self._gross_tcv = None
        self._interval_metrics = None
        self._name = None
        self._net_tcb = None
        self._net_tcv = None
        self._start_date = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if discount_tcb is not None:
            self.discount_tcb = discount_tcb
        if discount_tcv is not None:
            self.discount_tcv = discount_tcv
        if end_date is not None:
            self.end_date = end_date
        if gross_tcb is not None:
            self.gross_tcb = gross_tcb
        if gross_tcv is not None:
            self.gross_tcv = gross_tcv
        if interval_metrics is not None:
            self.interval_metrics = interval_metrics
        if name is not None:
            self.name = name
        if net_tcb is not None:
            self.net_tcb = net_tcb
        if net_tcv is not None:
            self.net_tcv = net_tcv
        if start_date is not None:
            self.start_date = start_date

    @property
    def description(self):
        """Gets the description of this RampIntervalMetrics.  # noqa: E501

        The short description of the interval.  # noqa: E501

        :return: The description of this RampIntervalMetrics.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RampIntervalMetrics.

        The short description of the interval.  # noqa: E501

        :param description: The description of this RampIntervalMetrics.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def discount_tcb(self):
        """Gets the discount_tcb of this RampIntervalMetrics.  # noqa: E501

        The discount amount for the TCB.  # noqa: E501

        :return: The discount_tcb of this RampIntervalMetrics.  # noqa: E501
        :rtype: float
        """
        return self._discount_tcb

    @discount_tcb.setter
    def discount_tcb(self, discount_tcb):
        """Sets the discount_tcb of this RampIntervalMetrics.

        The discount amount for the TCB.  # noqa: E501

        :param discount_tcb: The discount_tcb of this RampIntervalMetrics.  # noqa: E501
        :type: float
        """

        self._discount_tcb = discount_tcb

    @property
    def discount_tcv(self):
        """Gets the discount_tcv of this RampIntervalMetrics.  # noqa: E501

        The discount amount for the TCV.  # noqa: E501

        :return: The discount_tcv of this RampIntervalMetrics.  # noqa: E501
        :rtype: float
        """
        return self._discount_tcv

    @discount_tcv.setter
    def discount_tcv(self, discount_tcv):
        """Sets the discount_tcv of this RampIntervalMetrics.

        The discount amount for the TCV.  # noqa: E501

        :param discount_tcv: The discount_tcv of this RampIntervalMetrics.  # noqa: E501
        :type: float
        """

        self._discount_tcv = discount_tcv

    @property
    def end_date(self):
        """Gets the end_date of this RampIntervalMetrics.  # noqa: E501

        The end date of the interval.  # noqa: E501

        :return: The end_date of this RampIntervalMetrics.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this RampIntervalMetrics.

        The end date of the interval.  # noqa: E501

        :param end_date: The end_date of this RampIntervalMetrics.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def gross_tcb(self):
        """Gets the gross_tcb of this RampIntervalMetrics.  # noqa: E501

        The gross TCB value before discount charges are applied.  # noqa: E501

        :return: The gross_tcb of this RampIntervalMetrics.  # noqa: E501
        :rtype: float
        """
        return self._gross_tcb

    @gross_tcb.setter
    def gross_tcb(self, gross_tcb):
        """Sets the gross_tcb of this RampIntervalMetrics.

        The gross TCB value before discount charges are applied.  # noqa: E501

        :param gross_tcb: The gross_tcb of this RampIntervalMetrics.  # noqa: E501
        :type: float
        """

        self._gross_tcb = gross_tcb

    @property
    def gross_tcv(self):
        """Gets the gross_tcv of this RampIntervalMetrics.  # noqa: E501

        The gross TCV value before discount charges are applied.  # noqa: E501

        :return: The gross_tcv of this RampIntervalMetrics.  # noqa: E501
        :rtype: float
        """
        return self._gross_tcv

    @gross_tcv.setter
    def gross_tcv(self, gross_tcv):
        """Sets the gross_tcv of this RampIntervalMetrics.

        The gross TCV value before discount charges are applied.  # noqa: E501

        :param gross_tcv: The gross_tcv of this RampIntervalMetrics.  # noqa: E501
        :type: float
        """

        self._gross_tcv = gross_tcv

    @property
    def interval_metrics(self):
        """Gets the interval_metrics of this RampIntervalMetrics.  # noqa: E501

        Container for the detailed metrics for each rate plan charge in each ramp interval.  # noqa: E501

        :return: The interval_metrics of this RampIntervalMetrics.  # noqa: E501
        :rtype: list[RampIntervalChargeMetrics]
        """
        return self._interval_metrics

    @interval_metrics.setter
    def interval_metrics(self, interval_metrics):
        """Sets the interval_metrics of this RampIntervalMetrics.

        Container for the detailed metrics for each rate plan charge in each ramp interval.  # noqa: E501

        :param interval_metrics: The interval_metrics of this RampIntervalMetrics.  # noqa: E501
        :type: list[RampIntervalChargeMetrics]
        """

        self._interval_metrics = interval_metrics

    @property
    def name(self):
        """Gets the name of this RampIntervalMetrics.  # noqa: E501

        The name of the interval.  # noqa: E501

        :return: The name of this RampIntervalMetrics.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RampIntervalMetrics.

        The name of the interval.  # noqa: E501

        :param name: The name of this RampIntervalMetrics.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def net_tcb(self):
        """Gets the net_tcb of this RampIntervalMetrics.  # noqa: E501

        The net TCB value after discount charges are applied.  # noqa: E501

        :return: The net_tcb of this RampIntervalMetrics.  # noqa: E501
        :rtype: float
        """
        return self._net_tcb

    @net_tcb.setter
    def net_tcb(self, net_tcb):
        """Sets the net_tcb of this RampIntervalMetrics.

        The net TCB value after discount charges are applied.  # noqa: E501

        :param net_tcb: The net_tcb of this RampIntervalMetrics.  # noqa: E501
        :type: float
        """

        self._net_tcb = net_tcb

    @property
    def net_tcv(self):
        """Gets the net_tcv of this RampIntervalMetrics.  # noqa: E501

        The net TCV value after discount charges are applied.  # noqa: E501

        :return: The net_tcv of this RampIntervalMetrics.  # noqa: E501
        :rtype: float
        """
        return self._net_tcv

    @net_tcv.setter
    def net_tcv(self, net_tcv):
        """Sets the net_tcv of this RampIntervalMetrics.

        The net TCV value after discount charges are applied.  # noqa: E501

        :param net_tcv: The net_tcv of this RampIntervalMetrics.  # noqa: E501
        :type: float
        """

        self._net_tcv = net_tcv

    @property
    def start_date(self):
        """Gets the start_date of this RampIntervalMetrics.  # noqa: E501

        The start date of the interval.  # noqa: E501

        :return: The start_date of this RampIntervalMetrics.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this RampIntervalMetrics.

        The start date of the interval.  # noqa: E501

        :param start_date: The start_date of this RampIntervalMetrics.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

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
        if issubclass(RampIntervalMetrics, dict):
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
        if not isinstance(other, RampIntervalMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
