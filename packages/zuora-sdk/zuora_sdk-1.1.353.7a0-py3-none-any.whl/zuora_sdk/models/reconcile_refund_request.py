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

class ReconcileRefundRequest(object):
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
        'action': 'ReconcileRefundRequestAction',
        'action_date': 'str',
        'gateway_reconciliation_reason': 'str',
        'gateway_reconciliation_status': 'str',
        'payout_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'action_date': 'actionDate',
        'gateway_reconciliation_reason': 'gatewayReconciliationReason',
        'gateway_reconciliation_status': 'gatewayReconciliationStatus',
        'payout_id': 'payoutId'
    }

    def __init__(self, action=None, action_date=None, gateway_reconciliation_reason=None, gateway_reconciliation_status=None, payout_id=None):  # noqa: E501
        """ReconcileRefundRequest - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._action_date = None
        self._gateway_reconciliation_reason = None
        self._gateway_reconciliation_status = None
        self._payout_id = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if action_date is not None:
            self.action_date = action_date
        if gateway_reconciliation_reason is not None:
            self.gateway_reconciliation_reason = gateway_reconciliation_reason
        if gateway_reconciliation_status is not None:
            self.gateway_reconciliation_status = gateway_reconciliation_status
        if payout_id is not None:
            self.payout_id = payout_id

    @property
    def action(self):
        """Gets the action of this ReconcileRefundRequest.  # noqa: E501


        :return: The action of this ReconcileRefundRequest.  # noqa: E501
        :rtype: ReconcileRefundRequestAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ReconcileRefundRequest.


        :param action: The action of this ReconcileRefundRequest.  # noqa: E501
        :type: ReconcileRefundRequestAction
        """

        self._action = action

    @property
    def action_date(self):
        """Gets the action_date of this ReconcileRefundRequest.  # noqa: E501

        The date and time of the refund reconciliation action, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The action_date of this ReconcileRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._action_date

    @action_date.setter
    def action_date(self, action_date):
        """Sets the action_date of this ReconcileRefundRequest.

        The date and time of the refund reconciliation action, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param action_date: The action_date of this ReconcileRefundRequest.  # noqa: E501
        :type: str
        """

        self._action_date = action_date

    @property
    def gateway_reconciliation_reason(self):
        """Gets the gateway_reconciliation_reason of this ReconcileRefundRequest.  # noqa: E501

        The reason of gateway reconciliation.   # noqa: E501

        :return: The gateway_reconciliation_reason of this ReconcileRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._gateway_reconciliation_reason

    @gateway_reconciliation_reason.setter
    def gateway_reconciliation_reason(self, gateway_reconciliation_reason):
        """Sets the gateway_reconciliation_reason of this ReconcileRefundRequest.

        The reason of gateway reconciliation.   # noqa: E501

        :param gateway_reconciliation_reason: The gateway_reconciliation_reason of this ReconcileRefundRequest.  # noqa: E501
        :type: str
        """

        self._gateway_reconciliation_reason = gateway_reconciliation_reason

    @property
    def gateway_reconciliation_status(self):
        """Gets the gateway_reconciliation_status of this ReconcileRefundRequest.  # noqa: E501

        The status of gateway reconciliation.   # noqa: E501

        :return: The gateway_reconciliation_status of this ReconcileRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._gateway_reconciliation_status

    @gateway_reconciliation_status.setter
    def gateway_reconciliation_status(self, gateway_reconciliation_status):
        """Sets the gateway_reconciliation_status of this ReconcileRefundRequest.

        The status of gateway reconciliation.   # noqa: E501

        :param gateway_reconciliation_status: The gateway_reconciliation_status of this ReconcileRefundRequest.  # noqa: E501
        :type: str
        """

        self._gateway_reconciliation_status = gateway_reconciliation_status

    @property
    def payout_id(self):
        """Gets the payout_id of this ReconcileRefundRequest.  # noqa: E501

        The payout ID of the refund from the gateway side.   # noqa: E501

        :return: The payout_id of this ReconcileRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._payout_id

    @payout_id.setter
    def payout_id(self, payout_id):
        """Sets the payout_id of this ReconcileRefundRequest.

        The payout ID of the refund from the gateway side.   # noqa: E501

        :param payout_id: The payout_id of this ReconcileRefundRequest.  # noqa: E501
        :type: str
        """

        self._payout_id = payout_id

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
        if issubclass(ReconcileRefundRequest, dict):
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
        if not isinstance(other, ReconcileRefundRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
