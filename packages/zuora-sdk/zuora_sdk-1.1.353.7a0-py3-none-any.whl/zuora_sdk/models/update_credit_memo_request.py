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

class UpdateCreditMemoRequest(object):
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
        'auto_apply_upon_posting': 'bool',
        'comment': 'str',
        'effective_date': 'date',
        'exclude_from_auto_apply_rules': 'bool',
        'items': 'list[UpdateCreditMemoItem]',
        'reason_code': 'str',
        'transferred_to_accounting': 'TransferredToAccountingStatus',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'origin__ns': 'str',
        'sync_date__ns': 'str',
        'transaction__ns': 'str'
    }

    attribute_map = {
        'auto_apply_upon_posting': 'autoApplyUponPosting',
        'comment': 'comment',
        'effective_date': 'effectiveDate',
        'exclude_from_auto_apply_rules': 'excludeFromAutoApplyRules',
        'items': 'items',
        'reason_code': 'reasonCode',
        'transferred_to_accounting': 'transferredToAccounting',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'origin__ns': 'Origin__NS',
        'sync_date__ns': 'SyncDate__NS',
        'transaction__ns': 'Transaction__NS'
    }

    def __init__(self, auto_apply_upon_posting=None, comment=None, effective_date=None, exclude_from_auto_apply_rules=None, items=None, reason_code=None, transferred_to_accounting=None, integration_id__ns=None, integration_status__ns=None, origin__ns=None, sync_date__ns=None, transaction__ns=None):  # noqa: E501
        """UpdateCreditMemoRequest - a model defined in Swagger"""  # noqa: E501
        self._auto_apply_upon_posting = None
        self._comment = None
        self._effective_date = None
        self._exclude_from_auto_apply_rules = None
        self._items = None
        self._reason_code = None
        self._transferred_to_accounting = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._origin__ns = None
        self._sync_date__ns = None
        self._transaction__ns = None
        self.discriminator = None
        if auto_apply_upon_posting is not None:
            self.auto_apply_upon_posting = auto_apply_upon_posting
        if comment is not None:
            self.comment = comment
        if effective_date is not None:
            self.effective_date = effective_date
        if exclude_from_auto_apply_rules is not None:
            self.exclude_from_auto_apply_rules = exclude_from_auto_apply_rules
        if items is not None:
            self.items = items
        if reason_code is not None:
            self.reason_code = reason_code
        if transferred_to_accounting is not None:
            self.transferred_to_accounting = transferred_to_accounting
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
    def auto_apply_upon_posting(self):
        """Gets the auto_apply_upon_posting of this UpdateCreditMemoRequest.  # noqa: E501

        Whether the credit memo automatically applies to the invoice upon posting.  # noqa: E501

        :return: The auto_apply_upon_posting of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_apply_upon_posting

    @auto_apply_upon_posting.setter
    def auto_apply_upon_posting(self, auto_apply_upon_posting):
        """Sets the auto_apply_upon_posting of this UpdateCreditMemoRequest.

        Whether the credit memo automatically applies to the invoice upon posting.  # noqa: E501

        :param auto_apply_upon_posting: The auto_apply_upon_posting of this UpdateCreditMemoRequest.  # noqa: E501
        :type: bool
        """

        self._auto_apply_upon_posting = auto_apply_upon_posting

    @property
    def comment(self):
        """Gets the comment of this UpdateCreditMemoRequest.  # noqa: E501

        Comments about the credit memo.  # noqa: E501

        :return: The comment of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UpdateCreditMemoRequest.

        Comments about the credit memo.  # noqa: E501

        :param comment: The comment of this UpdateCreditMemoRequest.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def effective_date(self):
        """Gets the effective_date of this UpdateCreditMemoRequest.  # noqa: E501

        The date when the credit memo takes effect.  # noqa: E501

        :return: The effective_date of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this UpdateCreditMemoRequest.

        The date when the credit memo takes effect.  # noqa: E501

        :param effective_date: The effective_date of this UpdateCreditMemoRequest.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def exclude_from_auto_apply_rules(self):
        """Gets the exclude_from_auto_apply_rules of this UpdateCreditMemoRequest.  # noqa: E501

        Whether the credit memo is excluded from the rule of automatically applying unapplied credit memos to invoices and debit memos during payment runs. If you set this field to `true`, a payment run does not pick up this credit memo or apply it to other invoices or debit memos.  # noqa: E501

        :return: The exclude_from_auto_apply_rules of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_from_auto_apply_rules

    @exclude_from_auto_apply_rules.setter
    def exclude_from_auto_apply_rules(self, exclude_from_auto_apply_rules):
        """Sets the exclude_from_auto_apply_rules of this UpdateCreditMemoRequest.

        Whether the credit memo is excluded from the rule of automatically applying unapplied credit memos to invoices and debit memos during payment runs. If you set this field to `true`, a payment run does not pick up this credit memo or apply it to other invoices or debit memos.  # noqa: E501

        :param exclude_from_auto_apply_rules: The exclude_from_auto_apply_rules of this UpdateCreditMemoRequest.  # noqa: E501
        :type: bool
        """

        self._exclude_from_auto_apply_rules = exclude_from_auto_apply_rules

    @property
    def items(self):
        """Gets the items of this UpdateCreditMemoRequest.  # noqa: E501

        Container for credit memo items.  # noqa: E501

        :return: The items of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: list[UpdateCreditMemoItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this UpdateCreditMemoRequest.

        Container for credit memo items.  # noqa: E501

        :param items: The items of this UpdateCreditMemoRequest.  # noqa: E501
        :type: list[UpdateCreditMemoItem]
        """

        self._items = items

    @property
    def reason_code(self):
        """Gets the reason_code of this UpdateCreditMemoRequest.  # noqa: E501

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.  # noqa: E501

        :return: The reason_code of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this UpdateCreditMemoRequest.

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.  # noqa: E501

        :param reason_code: The reason_code of this UpdateCreditMemoRequest.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def transferred_to_accounting(self):
        """Gets the transferred_to_accounting of this UpdateCreditMemoRequest.  # noqa: E501


        :return: The transferred_to_accounting of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: TransferredToAccountingStatus
        """
        return self._transferred_to_accounting

    @transferred_to_accounting.setter
    def transferred_to_accounting(self, transferred_to_accounting):
        """Sets the transferred_to_accounting of this UpdateCreditMemoRequest.


        :param transferred_to_accounting: The transferred_to_accounting of this UpdateCreditMemoRequest.  # noqa: E501
        :type: TransferredToAccountingStatus
        """

        self._transferred_to_accounting = transferred_to_accounting

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this UpdateCreditMemoRequest.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this UpdateCreditMemoRequest.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this UpdateCreditMemoRequest.  # noqa: E501
        :type: str
        """

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this UpdateCreditMemoRequest.  # noqa: E501

        Status of the credit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this UpdateCreditMemoRequest.

        Status of the credit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this UpdateCreditMemoRequest.  # noqa: E501
        :type: str
        """

        self._integration_status__ns = integration_status__ns

    @property
    def origin__ns(self):
        """Gets the origin__ns of this UpdateCreditMemoRequest.  # noqa: E501

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The origin__ns of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._origin__ns

    @origin__ns.setter
    def origin__ns(self, origin__ns):
        """Sets the origin__ns of this UpdateCreditMemoRequest.

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param origin__ns: The origin__ns of this UpdateCreditMemoRequest.  # noqa: E501
        :type: str
        """

        self._origin__ns = origin__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this UpdateCreditMemoRequest.  # noqa: E501

        Date when the credit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this UpdateCreditMemoRequest.

        Date when the credit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this UpdateCreditMemoRequest.  # noqa: E501
        :type: str
        """

        self._sync_date__ns = sync_date__ns

    @property
    def transaction__ns(self):
        """Gets the transaction__ns of this UpdateCreditMemoRequest.  # noqa: E501

        Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The transaction__ns of this UpdateCreditMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction__ns

    @transaction__ns.setter
    def transaction__ns(self, transaction__ns):
        """Sets the transaction__ns of this UpdateCreditMemoRequest.

        Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param transaction__ns: The transaction__ns of this UpdateCreditMemoRequest.  # noqa: E501
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
        if issubclass(UpdateCreditMemoRequest, dict):
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
        if not isinstance(other, UpdateCreditMemoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
