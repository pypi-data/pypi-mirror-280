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

class CreateCreditMemoFromCharge(object):
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
        'auto_post': 'bool',
        'charges': 'list[CreditMemoItemFromChargeDetail]',
        'comment': 'str',
        'custom_rates': 'list[CustomRates]',
        'effective_date': 'date',
        'exclude_from_auto_apply_rules': 'bool',
        'reason_code': 'str',
        'currency': 'str',
        'number': 'str',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'origin__ns': 'str',
        'sync_date__ns': 'str',
        'transaction__ns': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'account_number': 'accountNumber',
        'auto_post': 'autoPost',
        'charges': 'charges',
        'comment': 'comment',
        'custom_rates': 'customRates',
        'effective_date': 'effectiveDate',
        'exclude_from_auto_apply_rules': 'excludeFromAutoApplyRules',
        'reason_code': 'reasonCode',
        'currency': 'currency',
        'number': 'number',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'origin__ns': 'Origin__NS',
        'sync_date__ns': 'SyncDate__NS',
        'transaction__ns': 'Transaction__NS'
    }

    def __init__(self, account_id=None, account_number=None, auto_post=False, charges=None, comment=None, custom_rates=None, effective_date=None, exclude_from_auto_apply_rules=False, reason_code=None, currency=None, number=None, integration_id__ns=None, integration_status__ns=None, origin__ns=None, sync_date__ns=None, transaction__ns=None):  # noqa: E501
        """CreateCreditMemoFromCharge - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._account_number = None
        self._auto_post = None
        self._charges = None
        self._comment = None
        self._custom_rates = None
        self._effective_date = None
        self._exclude_from_auto_apply_rules = None
        self._reason_code = None
        self._currency = None
        self._number = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._origin__ns = None
        self._sync_date__ns = None
        self._transaction__ns = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if account_number is not None:
            self.account_number = account_number
        if auto_post is not None:
            self.auto_post = auto_post
        if charges is not None:
            self.charges = charges
        if comment is not None:
            self.comment = comment
        if custom_rates is not None:
            self.custom_rates = custom_rates
        if effective_date is not None:
            self.effective_date = effective_date
        if exclude_from_auto_apply_rules is not None:
            self.exclude_from_auto_apply_rules = exclude_from_auto_apply_rules
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
        if origin__ns is not None:
            self.origin__ns = origin__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if transaction__ns is not None:
            self.transaction__ns = transaction__ns

    @property
    def account_id(self):
        """Gets the account_id of this CreateCreditMemoFromCharge.  # noqa: E501

        The ID of the account associated with the credit memo.  **Note**: When creating credit memos from product rate plan charges, you must specify `accountNumber`, `accountId`, or both in the request body. If both fields are specified, they must correspond to the same account.   # noqa: E501

        :return: The account_id of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CreateCreditMemoFromCharge.

        The ID of the account associated with the credit memo.  **Note**: When creating credit memos from product rate plan charges, you must specify `accountNumber`, `accountId`, or both in the request body. If both fields are specified, they must correspond to the same account.   # noqa: E501

        :param account_id: The account_id of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_number(self):
        """Gets the account_number of this CreateCreditMemoFromCharge.  # noqa: E501

        The number of the customer account associated with the credit memo.  **Note**: When creating credit memos from product rate plan charges, you must specify `accountNumber`, `accountId`, or both in the request body. If both fields are specified, they must correspond to the same account.   # noqa: E501

        :return: The account_number of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this CreateCreditMemoFromCharge.

        The number of the customer account associated with the credit memo.  **Note**: When creating credit memos from product rate plan charges, you must specify `accountNumber`, `accountId`, or both in the request body. If both fields are specified, they must correspond to the same account.   # noqa: E501

        :param account_number: The account_number of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def auto_post(self):
        """Gets the auto_post of this CreateCreditMemoFromCharge.  # noqa: E501

        Whether to automatically post the credit memo after it is created.  Setting this field to `true`, you do not need to separately call the [Post a credit memo](https://www.zuora.com/developer/api-references/api/operation/Put_PostCreditMemo) operation to post the credit memo.   # noqa: E501

        :return: The auto_post of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: bool
        """
        return self._auto_post

    @auto_post.setter
    def auto_post(self, auto_post):
        """Sets the auto_post of this CreateCreditMemoFromCharge.

        Whether to automatically post the credit memo after it is created.  Setting this field to `true`, you do not need to separately call the [Post a credit memo](https://www.zuora.com/developer/api-references/api/operation/Put_PostCreditMemo) operation to post the credit memo.   # noqa: E501

        :param auto_post: The auto_post of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: bool
        """

        self._auto_post = auto_post

    @property
    def charges(self):
        """Gets the charges of this CreateCreditMemoFromCharge.  # noqa: E501

        Container for product rate plan charges. The maximum number of items is 1,000.   # noqa: E501

        :return: The charges of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: list[CreditMemoItemFromChargeDetail]
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this CreateCreditMemoFromCharge.

        Container for product rate plan charges. The maximum number of items is 1,000.   # noqa: E501

        :param charges: The charges of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: list[CreditMemoItemFromChargeDetail]
        """

        self._charges = charges

    @property
    def comment(self):
        """Gets the comment of this CreateCreditMemoFromCharge.  # noqa: E501

        Comments about the credit memo.   # noqa: E501

        :return: The comment of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateCreditMemoFromCharge.

        Comments about the credit memo.   # noqa: E501

        :param comment: The comment of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def custom_rates(self):
        """Gets the custom_rates of this CreateCreditMemoFromCharge.  # noqa: E501

        It contains Home currency and Reporting currency custom rates currencies. The maximum number of items is 2 (you can pass the Home currency item or Reporting currency item or both).  **Note**: The API custom rate feature is permission controlled.   # noqa: E501

        :return: The custom_rates of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: list[CustomRates]
        """
        return self._custom_rates

    @custom_rates.setter
    def custom_rates(self, custom_rates):
        """Sets the custom_rates of this CreateCreditMemoFromCharge.

        It contains Home currency and Reporting currency custom rates currencies. The maximum number of items is 2 (you can pass the Home currency item or Reporting currency item or both).  **Note**: The API custom rate feature is permission controlled.   # noqa: E501

        :param custom_rates: The custom_rates of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: list[CustomRates]
        """

        self._custom_rates = custom_rates

    @property
    def effective_date(self):
        """Gets the effective_date of this CreateCreditMemoFromCharge.  # noqa: E501

        The date when the credit memo takes effect.   # noqa: E501

        :return: The effective_date of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this CreateCreditMemoFromCharge.

        The date when the credit memo takes effect.   # noqa: E501

        :param effective_date: The effective_date of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def exclude_from_auto_apply_rules(self):
        """Gets the exclude_from_auto_apply_rules of this CreateCreditMemoFromCharge.  # noqa: E501

        Whether the credit memo is excluded from the rule of automatically applying unapplied credit memos to invoices and debit memos during payment runs. If you set this field to `true`, a payment run does not pick up this credit memo or apply it to other invoices or debit memos.   # noqa: E501

        :return: The exclude_from_auto_apply_rules of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_from_auto_apply_rules

    @exclude_from_auto_apply_rules.setter
    def exclude_from_auto_apply_rules(self, exclude_from_auto_apply_rules):
        """Sets the exclude_from_auto_apply_rules of this CreateCreditMemoFromCharge.

        Whether the credit memo is excluded from the rule of automatically applying unapplied credit memos to invoices and debit memos during payment runs. If you set this field to `true`, a payment run does not pick up this credit memo or apply it to other invoices or debit memos.   # noqa: E501

        :param exclude_from_auto_apply_rules: The exclude_from_auto_apply_rules of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: bool
        """

        self._exclude_from_auto_apply_rules = exclude_from_auto_apply_rules

    @property
    def reason_code(self):
        """Gets the reason_code of this CreateCreditMemoFromCharge.  # noqa: E501

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.   # noqa: E501

        :return: The reason_code of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this CreateCreditMemoFromCharge.

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.   # noqa: E501

        :param reason_code: The reason_code of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def currency(self):
        """Gets the currency of this CreateCreditMemoFromCharge.  # noqa: E501

        The code of a currency as defined in Billing Settings through the Zuora UI.  If you do not specify a currency during credit memo creation, the default account currency is applied. The currency that you specify in the request must be configured and activated in Billing Settings.  **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Multiple_Currencies\" target=\"_blank\">Multiple Currencies</a> feature in the **Early Adopter** phase enabled.   # noqa: E501

        :return: The currency of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreateCreditMemoFromCharge.

        The code of a currency as defined in Billing Settings through the Zuora UI.  If you do not specify a currency during credit memo creation, the default account currency is applied. The currency that you specify in the request must be configured and activated in Billing Settings.  **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Multiple_Currencies\" target=\"_blank\">Multiple Currencies</a> feature in the **Early Adopter** phase enabled.   # noqa: E501

        :param currency: The currency of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def number(self):
        """Gets the number of this CreateCreditMemoFromCharge.  # noqa: E501

        A customized memo number with the following format requirements:  - Max length: 32 - Acceptable characters: a-z,A-Z,0-9,-,_,  The value must be unique in the system, otherwise it may cause issues with bill runs and subscribe/amend. If it is not provided, memo number will be auto-generated.   # noqa: E501

        :return: The number of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CreateCreditMemoFromCharge.

        A customized memo number with the following format requirements:  - Max length: 32 - Acceptable characters: a-z,A-Z,0-9,-,_,  The value must be unique in the system, otherwise it may cause issues with bill runs and subscribe/amend. If it is not provided, memo number will be auto-generated.   # noqa: E501

        :param number: The number of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this CreateCreditMemoFromCharge.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this CreateCreditMemoFromCharge.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this CreateCreditMemoFromCharge.  # noqa: E501

        Status of the credit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this CreateCreditMemoFromCharge.

        Status of the credit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._integration_status__ns = integration_status__ns

    @property
    def origin__ns(self):
        """Gets the origin__ns of this CreateCreditMemoFromCharge.  # noqa: E501

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The origin__ns of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._origin__ns

    @origin__ns.setter
    def origin__ns(self, origin__ns):
        """Sets the origin__ns of this CreateCreditMemoFromCharge.

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param origin__ns: The origin__ns of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._origin__ns = origin__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this CreateCreditMemoFromCharge.  # noqa: E501

        Date when the credit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this CreateCreditMemoFromCharge.

        Date when the credit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._sync_date__ns = sync_date__ns

    @property
    def transaction__ns(self):
        """Gets the transaction__ns of this CreateCreditMemoFromCharge.  # noqa: E501

        Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The transaction__ns of this CreateCreditMemoFromCharge.  # noqa: E501
        :rtype: str
        """
        return self._transaction__ns

    @transaction__ns.setter
    def transaction__ns(self, transaction__ns):
        """Sets the transaction__ns of this CreateCreditMemoFromCharge.

        Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param transaction__ns: The transaction__ns of this CreateCreditMemoFromCharge.  # noqa: E501
        :type: str
        """

        self._transaction__ns = transaction__ns

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
        if issubclass(CreateCreditMemoFromCharge, dict):
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
        if not isinstance(other, CreateCreditMemoFromCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
