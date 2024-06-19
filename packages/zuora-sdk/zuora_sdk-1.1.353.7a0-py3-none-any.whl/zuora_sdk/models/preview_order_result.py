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

class PreviewOrderResult(object):
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
        'charge_metrics': 'list[PreviewOrderResultChargeMetrics]',
        'credit_memos': 'list[PreviewOrderResultCreditMemos]',
        'invoices': 'list[PreviewOrderResultInvoices]',
        'order_delta_metrics': 'PreviewOrderResultDeltaMetrics',
        'order_metrics': 'list[PreviewResultOrderMetricsInner]',
        'ramp_metrics': 'list[OrderRampMetrics]'
    }

    attribute_map = {
        'charge_metrics': 'chargeMetrics',
        'credit_memos': 'creditMemos',
        'invoices': 'invoices',
        'order_delta_metrics': 'orderDeltaMetrics',
        'order_metrics': 'orderMetrics',
        'ramp_metrics': 'rampMetrics'
    }

    def __init__(self, charge_metrics=None, credit_memos=None, invoices=None, order_delta_metrics=None, order_metrics=None, ramp_metrics=None):  # noqa: E501
        """PreviewOrderResult - a model defined in Swagger"""  # noqa: E501
        self._charge_metrics = None
        self._credit_memos = None
        self._invoices = None
        self._order_delta_metrics = None
        self._order_metrics = None
        self._ramp_metrics = None
        self.discriminator = None
        if charge_metrics is not None:
            self.charge_metrics = charge_metrics
        if credit_memos is not None:
            self.credit_memos = credit_memos
        if invoices is not None:
            self.invoices = invoices
        if order_delta_metrics is not None:
            self.order_delta_metrics = order_delta_metrics
        if order_metrics is not None:
            self.order_metrics = order_metrics
        if ramp_metrics is not None:
            self.ramp_metrics = ramp_metrics

    @property
    def charge_metrics(self):
        """Gets the charge_metrics of this PreviewOrderResult.  # noqa: E501


        :return: The charge_metrics of this PreviewOrderResult.  # noqa: E501
        :rtype: list[PreviewOrderResultChargeMetrics]
        """
        return self._charge_metrics

    @charge_metrics.setter
    def charge_metrics(self, charge_metrics):
        """Sets the charge_metrics of this PreviewOrderResult.


        :param charge_metrics: The charge_metrics of this PreviewOrderResult.  # noqa: E501
        :type: list[PreviewOrderResultChargeMetrics]
        """

        self._charge_metrics = charge_metrics

    @property
    def credit_memos(self):
        """Gets the credit_memos of this PreviewOrderResult.  # noqa: E501

        This field is only available if you have the Invoice Settlement feature enabled.  # noqa: E501

        :return: The credit_memos of this PreviewOrderResult.  # noqa: E501
        :rtype: list[PreviewOrderResultCreditMemos]
        """
        return self._credit_memos

    @credit_memos.setter
    def credit_memos(self, credit_memos):
        """Sets the credit_memos of this PreviewOrderResult.

        This field is only available if you have the Invoice Settlement feature enabled.  # noqa: E501

        :param credit_memos: The credit_memos of this PreviewOrderResult.  # noqa: E501
        :type: list[PreviewOrderResultCreditMemos]
        """

        self._credit_memos = credit_memos

    @property
    def invoices(self):
        """Gets the invoices of this PreviewOrderResult.  # noqa: E501


        :return: The invoices of this PreviewOrderResult.  # noqa: E501
        :rtype: list[PreviewOrderResultInvoices]
        """
        return self._invoices

    @invoices.setter
    def invoices(self, invoices):
        """Sets the invoices of this PreviewOrderResult.


        :param invoices: The invoices of this PreviewOrderResult.  # noqa: E501
        :type: list[PreviewOrderResultInvoices]
        """

        self._invoices = invoices

    @property
    def order_delta_metrics(self):
        """Gets the order_delta_metrics of this PreviewOrderResult.  # noqa: E501


        :return: The order_delta_metrics of this PreviewOrderResult.  # noqa: E501
        :rtype: PreviewOrderResultDeltaMetrics
        """
        return self._order_delta_metrics

    @order_delta_metrics.setter
    def order_delta_metrics(self, order_delta_metrics):
        """Sets the order_delta_metrics of this PreviewOrderResult.


        :param order_delta_metrics: The order_delta_metrics of this PreviewOrderResult.  # noqa: E501
        :type: PreviewOrderResultDeltaMetrics
        """

        self._order_delta_metrics = order_delta_metrics

    @property
    def order_metrics(self):
        """Gets the order_metrics of this PreviewOrderResult.  # noqa: E501

        **Note:** As of Zuora Billing Release 306, Zuora has upgraded the methodologies for calculating metrics in [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders). The new methodologies are reflected in the following Order Delta Metrics objects.   * [Order Delta Mrr](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Mrr)  * [Order Delta Tcv](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Tcv)  * [Order Delta Tcb](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Tcb)   It is recommended that all customers use the new [Order Delta Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/AA_Overview_of_Order_Delta_Metrics). If you are an existing [Order Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders/Key_Metrics_for_Orders) customer and want to migrate to Order Delta Metrics, submit a request at [Zuora Global Support](https://support.zuora.com/).   Whereas new customers, and existing customers not currently on [Order Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders/Key_Metrics_for_Orders), will no longer have access to Order Metrics, existing customers currently using Order Metrics will continue to be supported.   # noqa: E501

        :return: The order_metrics of this PreviewOrderResult.  # noqa: E501
        :rtype: list[PreviewResultOrderMetricsInner]
        """
        return self._order_metrics

    @order_metrics.setter
    def order_metrics(self, order_metrics):
        """Sets the order_metrics of this PreviewOrderResult.

        **Note:** As of Zuora Billing Release 306, Zuora has upgraded the methodologies for calculating metrics in [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders). The new methodologies are reflected in the following Order Delta Metrics objects.   * [Order Delta Mrr](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Mrr)  * [Order Delta Tcv](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Tcv)  * [Order Delta Tcb](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Tcb)   It is recommended that all customers use the new [Order Delta Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/AA_Overview_of_Order_Delta_Metrics). If you are an existing [Order Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders/Key_Metrics_for_Orders) customer and want to migrate to Order Delta Metrics, submit a request at [Zuora Global Support](https://support.zuora.com/).   Whereas new customers, and existing customers not currently on [Order Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders/Key_Metrics_for_Orders), will no longer have access to Order Metrics, existing customers currently using Order Metrics will continue to be supported.   # noqa: E501

        :param order_metrics: The order_metrics of this PreviewOrderResult.  # noqa: E501
        :type: list[PreviewResultOrderMetricsInner]
        """

        self._order_metrics = order_metrics

    @property
    def ramp_metrics(self):
        """Gets the ramp_metrics of this PreviewOrderResult.  # noqa: E501

        **Note**: This field is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.  The ramp metrics.   # noqa: E501

        :return: The ramp_metrics of this PreviewOrderResult.  # noqa: E501
        :rtype: list[OrderRampMetrics]
        """
        return self._ramp_metrics

    @ramp_metrics.setter
    def ramp_metrics(self, ramp_metrics):
        """Sets the ramp_metrics of this PreviewOrderResult.

        **Note**: This field is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.  The ramp metrics.   # noqa: E501

        :param ramp_metrics: The ramp_metrics of this PreviewOrderResult.  # noqa: E501
        :type: list[OrderRampMetrics]
        """

        self._ramp_metrics = ramp_metrics

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
        if issubclass(PreviewOrderResult, dict):
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
        if not isinstance(other, PreviewOrderResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
