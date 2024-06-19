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

class CreateDebitMemoFromCharge(object):
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
        'account_id': 'str',
        'account_number': 'str',
        'auto_pay': 'bool',
        'auto_post': 'bool',
        'charges': 'list[DebitMemoItemFromChargeDetail]',
        'comment': 'str',
        'custom_rates': 'list[CustomRates]',
        'due_date': 'date',
        'effective_date': 'date',
        'reason_code': 'str',
        'currency': 'str',
        'number': 'str',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'sync_date__ns': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'account_number': 'accountNumber',
        'auto_pay': 'autoPay',
        'auto_post': 'autoPost',
        'charges': 'charges',
        'comment': 'comment',
        'custom_rates': 'customRates',
        'due_date': 'dueDate',
        'effective_date': 'effectiveDate',
        'reason_code': 'reasonCode',
        'currency': 'currency',
        'number': 'number',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'sync_date__ns': 'SyncDate__NS'
    }

    def __init__(self, account_id=None, account_number=None, auto_pay=None, auto_post=False, charges=None, comment=None, custom_rates=None, due_date=None, effective_date=None, reason_code=None, currency=None, number=None, integration_id__ns=None, integration_status__ns=None, sync_date__ns=None):  # noqa: E501
        """CreateDebitMemoFromCharge - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._account_number = None
        self._auto_pay = None
        self._auto_post = None
        self._charges = None
        self._comment = None
        self._custom_rates = None
        self._due_date = None
        self._effective_date = None
        self._reason_code = None
        self._currency = None
        self._number = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._sync_date__ns = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if account_number is not None:
            self.account_number = account_number
        if auto_pay is not None:
            self.auto_pay = auto_pay
        if auto_post is not None:
            self.auto_post = auto_post
        if charges is not None:
            self.charges = charges
        if comment is not None:
            self.comment = comment
        if custom_rates is not None:
            self.custom_rates = custom_rates
        if due_date is not None:
            self.due_date = due_date
        if effective_date is not None:
            self.effective_date = effective_date
        if reason_code is not None:
            self.reason_code = reason_code
        if currency is not None:
            self.currency = currency
        if number is not None:
            self.number = number
        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns

    @property
    def account_id(self):
        """Gets the account_id of this CreateDebitMemoFromCharge.  # noqa: E501

        The ID of the account associated with the debit memo.  **Note**: When creating debit memos from product rate plan charges, you must specify `accountNumber`, `accountId`, or both in the request body. If both fields are specified, they must correspond to the same account.  # noqa: E501

        :return: The account_id of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CreateDebitMemoFromCharge.

        The ID of the account associated with the debit memo.  **Note**: When creating debit memos from product rate plan charges, you must specify `accountNumber`, `accountId`, or both in the request body. If both fields are specified, they must correspond to the same account.  # noqa: E501

        :param account_id: The account_id of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_number(self):
        """Gets the account_number of this CreateDebitMemoFromCharge.  # noqa: E501

        The number of the account associated with the debit memo.  **Note**: When creating debit memos from product rate plan charges, you must specify `accountNumber`, `accountId`, or both in the request body. If both fields are specified, they must correspond to the same account.  # noqa: E501

        :return: The account_number of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this CreateDebitMemoFromCharge.

        The number of the account associated with the debit memo.  **Note**: When creating debit memos from product rate plan charges, you must specify `accountNumber`, `accountId`, or both in the request body. If both fields are specified, they must correspond to the same account.  # noqa: E501

        :param account_number: The account_number of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def auto_pay(self):
        """Gets the auto_pay of this CreateDebitMemoFromCharge.  # noqa: E501

        Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.   # noqa: E501

        :return: The auto_pay of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this CreateDebitMemoFromCharge.

        Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.   # noqa: E501

        :param auto_pay: The auto_pay of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: bool
        """

        self._auto_pay = auto_pay

    @property
    def auto_post(self):
        """Gets the auto_post of this CreateDebitMemoFromCharge.  # noqa: E501

        Whether to automatically post the debit memo after it is created.   Setting this field to `true`, you do not need to separately call the [Post a debit memo](https://www.zuora.com/developer/api-references/api/operation/Put_PostDebitMemo) operation to post the debit memo.   # noqa: E501

        :return: The auto_post of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: bool
        """
        return self._auto_post

    @auto_post.setter
    def auto_post(self, auto_post):
        """Sets the auto_post of this CreateDebitMemoFromCharge.

        Whether to automatically post the debit memo after it is created.   Setting this field to `true`, you do not need to separately call the [Post a debit memo](https://www.zuora.com/developer/api-references/api/operation/Put_PostDebitMemo) operation to post the debit memo.   # noqa: E501

        :param auto_post: The auto_post of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: bool
        """

        self._auto_post = auto_post

    @property
    def charges(self):
        """Gets the charges of this CreateDebitMemoFromCharge.  # noqa: E501

        Container for product rate plan charges. The maximum number of items is 1,000.  # noqa: E501

        :return: The charges of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: list[DebitMemoItemFromChargeDetail]
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this CreateDebitMemoFromCharge.

        Container for product rate plan charges. The maximum number of items is 1,000.  # noqa: E501

        :param charges: The charges of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: list[DebitMemoItemFromChargeDetail]
        """

        self._charges = charges

    @property
    def comment(self):
        """Gets the comment of this CreateDebitMemoFromCharge.  # noqa: E501

        Comments about the debit memo.  # noqa: E501

        :return: The comment of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateDebitMemoFromCharge.

        Comments about the debit memo.  # noqa: E501

        :param comment: The comment of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def custom_rates(self):
        """Gets the custom_rates of this CreateDebitMemoFromCharge.  # noqa: E501

        It contains Home currency and Reporting currency custom rates currencies. The maximum number of items is 2 (you can pass the Home currency item or Reporting currency item or both).  **Note**: The API custom rate feature is permission controlled.  # noqa: E501

        :return: The custom_rates of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: list[CustomRates]
        """
        return self._custom_rates

    @custom_rates.setter
    def custom_rates(self, custom_rates):
        """Sets the custom_rates of this CreateDebitMemoFromCharge.

        It contains Home currency and Reporting currency custom rates currencies. The maximum number of items is 2 (you can pass the Home currency item or Reporting currency item or both).  **Note**: The API custom rate feature is permission controlled.  # noqa: E501

        :param custom_rates: The custom_rates of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: list[CustomRates]
        """

        self._custom_rates = custom_rates

    @property
    def due_date(self):
        """Gets the due_date of this CreateDebitMemoFromCharge.  # noqa: E501

        The date by which the payment for the debit memo is due, in `yyyy-mm-dd` format.  # noqa: E501

        :return: The due_date of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this CreateDebitMemoFromCharge.

        The date by which the payment for the debit memo is due, in `yyyy-mm-dd` format.  # noqa: E501

        :param due_date: The due_date of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def effective_date(self):
        """Gets the effective_date of this CreateDebitMemoFromCharge.  # noqa: E501

        The date when the debit memo takes effect.  # noqa: E501

        :return: The effective_date of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this CreateDebitMemoFromCharge.

        The date when the debit memo takes effect.  # noqa: E501

        :param effective_date: The effective_date of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def reason_code(self):
        """Gets the reason_code of this CreateDebitMemoFromCharge.  # noqa: E501

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.  # noqa: E501

        :return: The reason_code of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this CreateDebitMemoFromCharge.

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.  # noqa: E501

        :param reason_code: The reason_code of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def currency(self):
        """Gets the currency of this CreateDebitMemoFromCharge.  # noqa: E501

        The code of a currency as defined in Billing Settings through the Zuora UI.  If you do not specify a currency during debit memo creation, the default account currency is applied. The currency that you specify in the request must be configured and activated in Billing Settings.  **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Multiple_Currencies\" target=\"_blank\">Multiple Currencies</a> feature in the **Early Adopter** phase enabled.   # noqa: E501

        :return: The currency of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreateDebitMemoFromCharge.

        The code of a currency as defined in Billing Settings through the Zuora UI.  If you do not specify a currency during debit memo creation, the default account currency is applied. The currency that you specify in the request must be configured and activated in Billing Settings.  **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Multiple_Currencies\" target=\"_blank\">Multiple Currencies</a> feature in the **Early Adopter** phase enabled.   # noqa: E501

        :param currency: The currency of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def number(self):
        """Gets the number of this CreateDebitMemoFromCharge.  # noqa: E501

        A customized memo number with the following format requirements:  - Max length: 32 - Acceptable characters: a-z,A-Z,0-9,-,_,  The value must be unique in the system, otherwise it may cause issues with bill runs and subscribe/amend. If it is not provided, memo number will be auto-generated.   # noqa: E501

        :return: The number of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CreateDebitMemoFromCharge.

        A customized memo number with the following format requirements:  - Max length: 32 - Acceptable characters: a-z,A-Z,0-9,-,_,  The value must be unique in the system, otherwise it may cause issues with bill runs and subscribe/amend. If it is not provided, memo number will be auto-generated.   # noqa: E501

        :param number: The number of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this CreateDebitMemoFromCharge.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this CreateDebitMemoFromCharge.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this CreateDebitMemoFromCharge.  # noqa: E501

        Status of the debit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this CreateDebitMemoFromCharge.

        Status of the debit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._integration_status__ns = integration_status__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this CreateDebitMemoFromCharge.  # noqa: E501

        Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this CreateDebitMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this CreateDebitMemoFromCharge.

        Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this CreateDebitMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._sync_date__ns = sync_date__ns

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
        if issubclass(CreateDebitMemoFromCharge, dict):
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
        if not isinstance(other, CreateDebitMemoFromCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
