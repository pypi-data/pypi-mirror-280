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

class CreateOrderResponseSubscriptions(object):
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
        'status': 'CreateOrderResponseSubscriptionStatus',
        'subscription_id': 'str',
        'subscription_number': 'str',
        'subscription_owner_id': 'str',
        'subscription_owner_number': 'str',
        'order_actions': 'list[CreateOrderResponseOrderAction]'
    }

    attribute_map = {
        'status': 'status',
        'subscription_id': 'subscriptionId',
        'subscription_number': 'subscriptionNumber',
        'subscription_owner_id': 'subscriptionOwnerId',
        'subscription_owner_number': 'subscriptionOwnerNumber',
        'order_actions': 'OrderActions'
    }

    def __init__(self, status=None, subscription_id=None, subscription_number=None, subscription_owner_id=None, subscription_owner_number=None, order_actions=None):  # noqa: E501
        """CreateOrderResponseSubscriptions - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._subscription_id = None
        self._subscription_number = None
        self._subscription_owner_id = None
        self._subscription_owner_number = None
        self._order_actions = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if subscription_number is not None:
            self.subscription_number = subscription_number
        if subscription_owner_id is not None:
            self.subscription_owner_id = subscription_owner_id
        if subscription_owner_number is not None:
            self.subscription_owner_number = subscription_owner_number
        if order_actions is not None:
            self.order_actions = order_actions

    @property
    def status(self):
        """Gets the status of this CreateOrderResponseSubscriptions.  # noqa: E501


        :return: The status of this CreateOrderResponseSubscriptions.  # noqa: E501
        :rtype: CreateOrderResponseSubscriptionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateOrderResponseSubscriptions.


        :param status: The status of this CreateOrderResponseSubscriptions.  # noqa: E501
        :type: CreateOrderResponseSubscriptionStatus
        """

        self._status = status

    @property
    def subscription_id(self):
        """Gets the subscription_id of this CreateOrderResponseSubscriptions.  # noqa: E501

        Subscription ID of the subscription included in this order. This field is returned instead of the `subscriptionNumber` field if the `returnIds` query parameter is set to `true`.  # noqa: E501

        :return: The subscription_id of this CreateOrderResponseSubscriptions.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this CreateOrderResponseSubscriptions.

        Subscription ID of the subscription included in this order. This field is returned instead of the `subscriptionNumber` field if the `returnIds` query parameter is set to `true`.  # noqa: E501

        :param subscription_id: The subscription_id of this CreateOrderResponseSubscriptions.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def subscription_number(self):
        """Gets the subscription_number of this CreateOrderResponseSubscriptions.  # noqa: E501

        Subscription number of the subscription included in this order.  # noqa: E501

        :return: The subscription_number of this CreateOrderResponseSubscriptions.  # noqa: E501
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this CreateOrderResponseSubscriptions.

        Subscription number of the subscription included in this order.  # noqa: E501

        :param subscription_number: The subscription_number of this CreateOrderResponseSubscriptions.  # noqa: E501
        :type: str
        """

        self._subscription_number = subscription_number

    @property
    def subscription_owner_id(self):
        """Gets the subscription_owner_id of this CreateOrderResponseSubscriptions.  # noqa: E501

        subscription owner account id of the subscription  # noqa: E501

        :return: The subscription_owner_id of this CreateOrderResponseSubscriptions.  # noqa: E501
        :rtype: str
        """
        return self._subscription_owner_id

    @subscription_owner_id.setter
    def subscription_owner_id(self, subscription_owner_id):
        """Sets the subscription_owner_id of this CreateOrderResponseSubscriptions.

        subscription owner account id of the subscription  # noqa: E501

        :param subscription_owner_id: The subscription_owner_id of this CreateOrderResponseSubscriptions.  # noqa: E501
        :type: str
        """

        self._subscription_owner_id = subscription_owner_id

    @property
    def subscription_owner_number(self):
        """Gets the subscription_owner_number of this CreateOrderResponseSubscriptions.  # noqa: E501

        subscription owner account number of the subscription  # noqa: E501

        :return: The subscription_owner_number of this CreateOrderResponseSubscriptions.  # noqa: E501
        :rtype: str
        """
        return self._subscription_owner_number

    @subscription_owner_number.setter
    def subscription_owner_number(self, subscription_owner_number):
        """Sets the subscription_owner_number of this CreateOrderResponseSubscriptions.

        subscription owner account number of the subscription  # noqa: E501

        :param subscription_owner_number: The subscription_owner_number of this CreateOrderResponseSubscriptions.  # noqa: E501
        :type: str
        """

        self._subscription_owner_number = subscription_owner_number

    @property
    def order_actions(self):
        """Gets the order_actions of this CreateOrderResponseSubscriptions.  # noqa: E501

        subscription order action metrics  # noqa: E501

        :return: The order_actions of this CreateOrderResponseSubscriptions.  # noqa: E501
        :rtype: list[CreateOrderResponseOrderAction]
        """
        return self._order_actions

    @order_actions.setter
    def order_actions(self, order_actions):
        """Sets the order_actions of this CreateOrderResponseSubscriptions.

        subscription order action metrics  # noqa: E501

        :param order_actions: The order_actions of this CreateOrderResponseSubscriptions.  # noqa: E501
        :type: list[CreateOrderResponseOrderAction]
        """

        self._order_actions = order_actions

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
        if issubclass(CreateOrderResponseSubscriptions, dict):
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
        if not isinstance(other, CreateOrderResponseSubscriptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
