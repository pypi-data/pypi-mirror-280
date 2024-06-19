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

class PaymentTransactionLogResponse(object):
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
        'avs_response_code': 'str',
        'batch_id': 'str',
        'cvv_response_code': 'str',
        'gateway': 'str',
        'gateway_reason_code': 'str',
        'gateway_reason_code_description': 'str',
        'gateway_state': 'GatewayState',
        'gateway_transaction_type': 'GetPaymentTransactionLogResponseGatewayTransactionType',
        'id': 'str',
        'payment_id': 'str',
        'request_string': 'str',
        'response_string': 'str',
        'transaction_date': 'datetime',
        'transaction_id': 'str'
    }

    attribute_map = {
        'avs_response_code': 'AVSResponseCode',
        'batch_id': 'BatchId',
        'cvv_response_code': 'CVVResponseCode',
        'gateway': 'Gateway',
        'gateway_reason_code': 'GatewayReasonCode',
        'gateway_reason_code_description': 'GatewayReasonCodeDescription',
        'gateway_state': 'GatewayState',
        'gateway_transaction_type': 'GatewayTransactionType',
        'id': 'Id',
        'payment_id': 'PaymentId',
        'request_string': 'RequestString',
        'response_string': 'ResponseString',
        'transaction_date': 'TransactionDate',
        'transaction_id': 'TransactionId'
    }

    def __init__(self, avs_response_code=None, batch_id=None, cvv_response_code=None, gateway=None, gateway_reason_code=None, gateway_reason_code_description=None, gateway_state=None, gateway_transaction_type=None, id=None, payment_id=None, request_string=None, response_string=None, transaction_date=None, transaction_id=None):  # noqa: E501
        """PaymentTransactionLogResponse - a model defined in Swagger"""  # noqa: E501
        self._avs_response_code = None
        self._batch_id = None
        self._cvv_response_code = None
        self._gateway = None
        self._gateway_reason_code = None
        self._gateway_reason_code_description = None
        self._gateway_state = None
        self._gateway_transaction_type = None
        self._id = None
        self._payment_id = None
        self._request_string = None
        self._response_string = None
        self._transaction_date = None
        self._transaction_id = None
        self.discriminator = None
        if avs_response_code is not None:
            self.avs_response_code = avs_response_code
        if batch_id is not None:
            self.batch_id = batch_id
        if cvv_response_code is not None:
            self.cvv_response_code = cvv_response_code
        if gateway is not None:
            self.gateway = gateway
        if gateway_reason_code is not None:
            self.gateway_reason_code = gateway_reason_code
        if gateway_reason_code_description is not None:
            self.gateway_reason_code_description = gateway_reason_code_description
        if gateway_state is not None:
            self.gateway_state = gateway_state
        if gateway_transaction_type is not None:
            self.gateway_transaction_type = gateway_transaction_type
        if id is not None:
            self.id = id
        if payment_id is not None:
            self.payment_id = payment_id
        if request_string is not None:
            self.request_string = request_string
        if response_string is not None:
            self.response_string = response_string
        if transaction_date is not None:
            self.transaction_date = transaction_date
        if transaction_id is not None:
            self.transaction_id = transaction_id

    @property
    def avs_response_code(self):
        """Gets the avs_response_code of this PaymentTransactionLogResponse.  # noqa: E501

        The response code returned by the payment gateway referring to the AVS international response of the payment transaction.   # noqa: E501

        :return: The avs_response_code of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._avs_response_code

    @avs_response_code.setter
    def avs_response_code(self, avs_response_code):
        """Sets the avs_response_code of this PaymentTransactionLogResponse.

        The response code returned by the payment gateway referring to the AVS international response of the payment transaction.   # noqa: E501

        :param avs_response_code: The avs_response_code of this PaymentTransactionLogResponse.  # noqa: E501
        :type: str
        """

        self._avs_response_code = avs_response_code

    @property
    def batch_id(self):
        """Gets the batch_id of this PaymentTransactionLogResponse.  # noqa: E501

        The ID of the batch used to send the transaction if the request was sent in a batch.   # noqa: E501

        :return: The batch_id of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this PaymentTransactionLogResponse.

        The ID of the batch used to send the transaction if the request was sent in a batch.   # noqa: E501

        :param batch_id: The batch_id of this PaymentTransactionLogResponse.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def cvv_response_code(self):
        """Gets the cvv_response_code of this PaymentTransactionLogResponse.  # noqa: E501

        The response code returned by the payment gateway referring to the CVV international response of the payment transaction.   # noqa: E501

        :return: The cvv_response_code of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._cvv_response_code

    @cvv_response_code.setter
    def cvv_response_code(self, cvv_response_code):
        """Sets the cvv_response_code of this PaymentTransactionLogResponse.

        The response code returned by the payment gateway referring to the CVV international response of the payment transaction.   # noqa: E501

        :param cvv_response_code: The cvv_response_code of this PaymentTransactionLogResponse.  # noqa: E501
        :type: str
        """

        self._cvv_response_code = cvv_response_code

    @property
    def gateway(self):
        """Gets the gateway of this PaymentTransactionLogResponse.  # noqa: E501

        The name of the payment gateway used to transact the current payment transaction log.   # noqa: E501

        :return: The gateway of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this PaymentTransactionLogResponse.

        The name of the payment gateway used to transact the current payment transaction log.   # noqa: E501

        :param gateway: The gateway of this PaymentTransactionLogResponse.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def gateway_reason_code(self):
        """Gets the gateway_reason_code of this PaymentTransactionLogResponse.  # noqa: E501

        The code returned by the payment gateway for the payment. This code is gateway-dependent.   # noqa: E501

        :return: The gateway_reason_code of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._gateway_reason_code

    @gateway_reason_code.setter
    def gateway_reason_code(self, gateway_reason_code):
        """Sets the gateway_reason_code of this PaymentTransactionLogResponse.

        The code returned by the payment gateway for the payment. This code is gateway-dependent.   # noqa: E501

        :param gateway_reason_code: The gateway_reason_code of this PaymentTransactionLogResponse.  # noqa: E501
        :type: str
        """

        self._gateway_reason_code = gateway_reason_code

    @property
    def gateway_reason_code_description(self):
        """Gets the gateway_reason_code_description of this PaymentTransactionLogResponse.  # noqa: E501

        The message returned by the payment gateway for the payment. This message is gateway-dependent.    # noqa: E501

        :return: The gateway_reason_code_description of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._gateway_reason_code_description

    @gateway_reason_code_description.setter
    def gateway_reason_code_description(self, gateway_reason_code_description):
        """Sets the gateway_reason_code_description of this PaymentTransactionLogResponse.

        The message returned by the payment gateway for the payment. This message is gateway-dependent.    # noqa: E501

        :param gateway_reason_code_description: The gateway_reason_code_description of this PaymentTransactionLogResponse.  # noqa: E501
        :type: str
        """

        self._gateway_reason_code_description = gateway_reason_code_description

    @property
    def gateway_state(self):
        """Gets the gateway_state of this PaymentTransactionLogResponse.  # noqa: E501


        :return: The gateway_state of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: GatewayState
        """
        return self._gateway_state

    @gateway_state.setter
    def gateway_state(self, gateway_state):
        """Sets the gateway_state of this PaymentTransactionLogResponse.


        :param gateway_state: The gateway_state of this PaymentTransactionLogResponse.  # noqa: E501
        :type: GatewayState
        """

        self._gateway_state = gateway_state

    @property
    def gateway_transaction_type(self):
        """Gets the gateway_transaction_type of this PaymentTransactionLogResponse.  # noqa: E501


        :return: The gateway_transaction_type of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: GetPaymentTransactionLogResponseGatewayTransactionType
        """
        return self._gateway_transaction_type

    @gateway_transaction_type.setter
    def gateway_transaction_type(self, gateway_transaction_type):
        """Sets the gateway_transaction_type of this PaymentTransactionLogResponse.


        :param gateway_transaction_type: The gateway_transaction_type of this PaymentTransactionLogResponse.  # noqa: E501
        :type: GetPaymentTransactionLogResponseGatewayTransactionType
        """

        self._gateway_transaction_type = gateway_transaction_type

    @property
    def id(self):
        """Gets the id of this PaymentTransactionLogResponse.  # noqa: E501

        The ID of the payment transaction log.   # noqa: E501

        :return: The id of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTransactionLogResponse.

        The ID of the payment transaction log.   # noqa: E501

        :param id: The id of this PaymentTransactionLogResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def payment_id(self):
        """Gets the payment_id of this PaymentTransactionLogResponse.  # noqa: E501

        The ID of the payment wherein the payment transaction log was recorded.    # noqa: E501

        :return: The payment_id of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this PaymentTransactionLogResponse.

        The ID of the payment wherein the payment transaction log was recorded.    # noqa: E501

        :param payment_id: The payment_id of this PaymentTransactionLogResponse.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def request_string(self):
        """Gets the request_string of this PaymentTransactionLogResponse.  # noqa: E501

        The payment transaction request string sent to the payment gateway.    # noqa: E501

        :return: The request_string of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_string

    @request_string.setter
    def request_string(self, request_string):
        """Sets the request_string of this PaymentTransactionLogResponse.

        The payment transaction request string sent to the payment gateway.    # noqa: E501

        :param request_string: The request_string of this PaymentTransactionLogResponse.  # noqa: E501
        :type: str
        """

        self._request_string = request_string

    @property
    def response_string(self):
        """Gets the response_string of this PaymentTransactionLogResponse.  # noqa: E501

        The payment transaction response string returned by the payment gateway.    # noqa: E501

        :return: The response_string of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._response_string

    @response_string.setter
    def response_string(self, response_string):
        """Sets the response_string of this PaymentTransactionLogResponse.

        The payment transaction response string returned by the payment gateway.    # noqa: E501

        :param response_string: The response_string of this PaymentTransactionLogResponse.  # noqa: E501
        :type: str
        """

        self._response_string = response_string

    @property
    def transaction_date(self):
        """Gets the transaction_date of this PaymentTransactionLogResponse.  # noqa: E501

        The transaction date when the payment was performed.    # noqa: E501

        :return: The transaction_date of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this PaymentTransactionLogResponse.

        The transaction date when the payment was performed.    # noqa: E501

        :param transaction_date: The transaction_date of this PaymentTransactionLogResponse.  # noqa: E501
        :type: datetime
        """

        self._transaction_date = transaction_date

    @property
    def transaction_id(self):
        """Gets the transaction_id of this PaymentTransactionLogResponse.  # noqa: E501

        The transaction ID returned by the payment gateway. This field is used to reconcile payment transactions between the payment gateway and records in Zuora.   # noqa: E501

        :return: The transaction_id of this PaymentTransactionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this PaymentTransactionLogResponse.

        The transaction ID returned by the payment gateway. This field is used to reconcile payment transactions between the payment gateway and records in Zuora.   # noqa: E501

        :param transaction_id: The transaction_id of this PaymentTransactionLogResponse.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

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
        if issubclass(PaymentTransactionLogResponse, dict):
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
        if not isinstance(other, PaymentTransactionLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
