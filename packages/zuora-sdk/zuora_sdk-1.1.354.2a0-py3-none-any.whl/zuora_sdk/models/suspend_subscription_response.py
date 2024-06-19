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

class SuspendSubscriptionResponse(object):
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
        'credit_memo_id': 'str',
        'invoice_id': 'str',
        'paid_amount': 'float',
        'payment_id': 'str',
        'resume_date': 'date',
        'subscription_id': 'str',
        'success': 'bool',
        'suspend_date': 'date',
        'term_end_date': 'date',
        'total_delta_tcv': 'float',
        'order_number': 'str',
        'status': 'OrderStatus',
        'account_number': 'str',
        'subscription_numbers': 'list[str]',
        'subscriptions': 'list[CreateOrderResponseSubscriptions]'
    }

    attribute_map = {
        'credit_memo_id': 'creditMemoId',
        'invoice_id': 'invoiceId',
        'paid_amount': 'paidAmount',
        'payment_id': 'paymentId',
        'resume_date': 'resumeDate',
        'subscription_id': 'subscriptionId',
        'success': 'success',
        'suspend_date': 'suspendDate',
        'term_end_date': 'termEndDate',
        'total_delta_tcv': 'totalDeltaTcv',
        'order_number': 'orderNumber',
        'status': 'status',
        'account_number': 'accountNumber',
        'subscription_numbers': 'subscriptionNumbers',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, credit_memo_id=None, invoice_id=None, paid_amount=None, payment_id=None, resume_date=None, subscription_id=None, success=None, suspend_date=None, term_end_date=None, total_delta_tcv=None, order_number=None, status=None, account_number=None, subscription_numbers=None, subscriptions=None):  # noqa: E501
        """SuspendSubscriptionResponse - a model defined in Swagger"""  # noqa: E501
        self._credit_memo_id = None
        self._invoice_id = None
        self._paid_amount = None
        self._payment_id = None
        self._resume_date = None
        self._subscription_id = None
        self._success = None
        self._suspend_date = None
        self._term_end_date = None
        self._total_delta_tcv = None
        self._order_number = None
        self._status = None
        self._account_number = None
        self._subscription_numbers = None
        self._subscriptions = None
        self.discriminator = None
        if credit_memo_id is not None:
            self.credit_memo_id = credit_memo_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if paid_amount is not None:
            self.paid_amount = paid_amount
        if payment_id is not None:
            self.payment_id = payment_id
        if resume_date is not None:
            self.resume_date = resume_date
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if success is not None:
            self.success = success
        if suspend_date is not None:
            self.suspend_date = suspend_date
        if term_end_date is not None:
            self.term_end_date = term_end_date
        if total_delta_tcv is not None:
            self.total_delta_tcv = total_delta_tcv
        if order_number is not None:
            self.order_number = order_number
        if status is not None:
            self.status = status
        if account_number is not None:
            self.account_number = account_number
        if subscription_numbers is not None:
            self.subscription_numbers = subscription_numbers
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def credit_memo_id(self):
        """Gets the credit_memo_id of this SuspendSubscriptionResponse.  # noqa: E501

        The credit memo ID, if a credit memo is generated during the subscription process.  **Note:** This container is only available if you set the Zuora REST API minor version to 207.0 or later in the request header, and you have  [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :return: The credit_memo_id of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_id

    @credit_memo_id.setter
    def credit_memo_id(self, credit_memo_id):
        """Sets the credit_memo_id of this SuspendSubscriptionResponse.

        The credit memo ID, if a credit memo is generated during the subscription process.  **Note:** This container is only available if you set the Zuora REST API minor version to 207.0 or later in the request header, and you have  [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :param credit_memo_id: The credit_memo_id of this SuspendSubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._credit_memo_id = credit_memo_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this SuspendSubscriptionResponse.  # noqa: E501

        Invoice ID, if an invoice is generated during the subscription process.   # noqa: E501

        :return: The invoice_id of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this SuspendSubscriptionResponse.

        Invoice ID, if an invoice is generated during the subscription process.   # noqa: E501

        :param invoice_id: The invoice_id of this SuspendSubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def paid_amount(self):
        """Gets the paid_amount of this SuspendSubscriptionResponse.  # noqa: E501

        Payment amount, if a payment is collected.   # noqa: E501

        :return: The paid_amount of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: float
        """
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, paid_amount):
        """Sets the paid_amount of this SuspendSubscriptionResponse.

        Payment amount, if a payment is collected.   # noqa: E501

        :param paid_amount: The paid_amount of this SuspendSubscriptionResponse.  # noqa: E501
        :type: float
        """

        self._paid_amount = paid_amount

    @property
    def payment_id(self):
        """Gets the payment_id of this SuspendSubscriptionResponse.  # noqa: E501

        Payment ID, if a payment is collected.   # noqa: E501

        :return: The payment_id of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this SuspendSubscriptionResponse.

        Payment ID, if a payment is collected.   # noqa: E501

        :param payment_id: The payment_id of this SuspendSubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def resume_date(self):
        """Gets the resume_date of this SuspendSubscriptionResponse.  # noqa: E501

        The date when subscription resumption takes effect, in the format yyyy-mm-dd. It is available for Orders Harmonization and Subscribe/Amend Tenants.   # noqa: E501

        :return: The resume_date of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: date
        """
        return self._resume_date

    @resume_date.setter
    def resume_date(self, resume_date):
        """Sets the resume_date of this SuspendSubscriptionResponse.

        The date when subscription resumption takes effect, in the format yyyy-mm-dd. It is available for Orders Harmonization and Subscribe/Amend Tenants.   # noqa: E501

        :param resume_date: The resume_date of this SuspendSubscriptionResponse.  # noqa: E501
        :type: date
        """

        self._resume_date = resume_date

    @property
    def subscription_id(self):
        """Gets the subscription_id of this SuspendSubscriptionResponse.  # noqa: E501

        The subscription ID. It is available for Orders Harmonization and Subscribe/Amend Tenants.   # noqa: E501

        :return: The subscription_id of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this SuspendSubscriptionResponse.

        The subscription ID. It is available for Orders Harmonization and Subscribe/Amend Tenants.   # noqa: E501

        :param subscription_id: The subscription_id of this SuspendSubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def success(self):
        """Gets the success of this SuspendSubscriptionResponse.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this SuspendSubscriptionResponse.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this SuspendSubscriptionResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def suspend_date(self):
        """Gets the suspend_date of this SuspendSubscriptionResponse.  # noqa: E501

        The date when subscription suspension takes effect, in the format yyyy-mm-dd. It is available for Orders Harmonization and Subscribe/Amend Tenants.   # noqa: E501

        :return: The suspend_date of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: date
        """
        return self._suspend_date

    @suspend_date.setter
    def suspend_date(self, suspend_date):
        """Sets the suspend_date of this SuspendSubscriptionResponse.

        The date when subscription suspension takes effect, in the format yyyy-mm-dd. It is available for Orders Harmonization and Subscribe/Amend Tenants.   # noqa: E501

        :param suspend_date: The suspend_date of this SuspendSubscriptionResponse.  # noqa: E501
        :type: date
        """

        self._suspend_date = suspend_date

    @property
    def term_end_date(self):
        """Gets the term_end_date of this SuspendSubscriptionResponse.  # noqa: E501

        The date when the new subscription term ends, in the format yyyy-mm-dd. It is available for Orders Harmonization and Subscribe/Amend Tenants.   # noqa: E501

        :return: The term_end_date of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: date
        """
        return self._term_end_date

    @term_end_date.setter
    def term_end_date(self, term_end_date):
        """Sets the term_end_date of this SuspendSubscriptionResponse.

        The date when the new subscription term ends, in the format yyyy-mm-dd. It is available for Orders Harmonization and Subscribe/Amend Tenants.   # noqa: E501

        :param term_end_date: The term_end_date of this SuspendSubscriptionResponse.  # noqa: E501
        :type: date
        """

        self._term_end_date = term_end_date

    @property
    def total_delta_tcv(self):
        """Gets the total_delta_tcv of this SuspendSubscriptionResponse.  # noqa: E501

        Change in the total contracted value of the subscription as a result of the update. It is available for Orders Harmonization and Subscribe/Amend Tenants.   # noqa: E501

        :return: The total_delta_tcv of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_delta_tcv

    @total_delta_tcv.setter
    def total_delta_tcv(self, total_delta_tcv):
        """Sets the total_delta_tcv of this SuspendSubscriptionResponse.

        Change in the total contracted value of the subscription as a result of the update. It is available for Orders Harmonization and Subscribe/Amend Tenants.   # noqa: E501

        :param total_delta_tcv: The total_delta_tcv of this SuspendSubscriptionResponse.  # noqa: E501
        :type: float
        """

        self._total_delta_tcv = total_delta_tcv

    @property
    def order_number(self):
        """Gets the order_number of this SuspendSubscriptionResponse.  # noqa: E501

        The order number. It is available for Orders Tenants.   # noqa: E501

        :return: The order_number of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this SuspendSubscriptionResponse.

        The order number. It is available for Orders Tenants.   # noqa: E501

        :param order_number: The order_number of this SuspendSubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._order_number = order_number

    @property
    def status(self):
        """Gets the status of this SuspendSubscriptionResponse.  # noqa: E501


        :return: The status of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: OrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SuspendSubscriptionResponse.


        :param status: The status of this SuspendSubscriptionResponse.  # noqa: E501
        :type: OrderStatus
        """

        self._status = status

    @property
    def account_number(self):
        """Gets the account_number of this SuspendSubscriptionResponse.  # noqa: E501

        The account number that this order has been created under. This is also the invoice owner of the subscriptions included in this order. It is available for Orders Tenants.  # noqa: E501

        :return: The account_number of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this SuspendSubscriptionResponse.

        The account number that this order has been created under. This is also the invoice owner of the subscriptions included in this order. It is available for Orders Tenants.  # noqa: E501

        :param account_number: The account_number of this SuspendSubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def subscription_numbers(self):
        """Gets the subscription_numbers of this SuspendSubscriptionResponse.  # noqa: E501

        The subscription numbers. It is available for Orders Tenants. This field is in Zuora REST API version control. Supported max version is 206.0.   # noqa: E501

        :return: The subscription_numbers of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._subscription_numbers

    @subscription_numbers.setter
    def subscription_numbers(self, subscription_numbers):
        """Sets the subscription_numbers of this SuspendSubscriptionResponse.

        The subscription numbers. It is available for Orders Tenants. This field is in Zuora REST API version control. Supported max version is 206.0.   # noqa: E501

        :param subscription_numbers: The subscription_numbers of this SuspendSubscriptionResponse.  # noqa: E501
        :type: list[str]
        """

        self._subscription_numbers = subscription_numbers

    @property
    def subscriptions(self):
        """Gets the subscriptions of this SuspendSubscriptionResponse.  # noqa: E501

        This field is in Zuora REST API version control. Supported minor versions are 223.0 or later. It is available for Orders Tenants.   # noqa: E501

        :return: The subscriptions of this SuspendSubscriptionResponse.  # noqa: E501
        :rtype: list[CreateOrderResponseSubscriptions]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this SuspendSubscriptionResponse.

        This field is in Zuora REST API version control. Supported minor versions are 223.0 or later. It is available for Orders Tenants.   # noqa: E501

        :param subscriptions: The subscriptions of this SuspendSubscriptionResponse.  # noqa: E501
        :type: list[CreateOrderResponseSubscriptions]
        """

        self._subscriptions = subscriptions

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
        if issubclass(SuspendSubscriptionResponse, dict):
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
        if not isinstance(other, SuspendSubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
