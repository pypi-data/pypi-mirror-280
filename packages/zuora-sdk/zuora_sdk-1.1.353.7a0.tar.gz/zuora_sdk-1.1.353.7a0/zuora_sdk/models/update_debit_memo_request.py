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

class UpdateDebitMemoRequest(object):
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
        'auto_pay': 'bool',
        'comment': 'str',
        'due_date': 'date',
        'effective_date': 'date',
        'items': 'list[UpdateDebitMemoItem]',
        'reason_code': 'str',
        'transferred_to_accounting': 'TransferredToAccountingStatus',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'sync_date__ns': 'str'
    }

    attribute_map = {
        'auto_pay': 'autoPay',
        'comment': 'comment',
        'due_date': 'dueDate',
        'effective_date': 'effectiveDate',
        'items': 'items',
        'reason_code': 'reasonCode',
        'transferred_to_accounting': 'transferredToAccounting',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'sync_date__ns': 'SyncDate__NS'
    }

    def __init__(self, auto_pay=None, comment=None, due_date=None, effective_date=None, items=None, reason_code=None, transferred_to_accounting=None, integration_id__ns=None, integration_status__ns=None, sync_date__ns=None):  # noqa: E501
        """UpdateDebitMemoRequest - a model defined in Swagger"""  # noqa: E501
        self._auto_pay = None
        self._comment = None
        self._due_date = None
        self._effective_date = None
        self._items = None
        self._reason_code = None
        self._transferred_to_accounting = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._sync_date__ns = None
        self.discriminator = None
        if auto_pay is not None:
            self.auto_pay = auto_pay
        if comment is not None:
            self.comment = comment
        if due_date is not None:
            self.due_date = due_date
        if effective_date is not None:
            self.effective_date = effective_date
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
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns

    @property
    def auto_pay(self):
        """Gets the auto_pay of this UpdateDebitMemoRequest.  # noqa: E501

        Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.   # noqa: E501

        :return: The auto_pay of this UpdateDebitMemoRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this UpdateDebitMemoRequest.

        Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.   # noqa: E501

        :param auto_pay: The auto_pay of this UpdateDebitMemoRequest.  # noqa: E501
        :type: bool
        """

        self._auto_pay = auto_pay

    @property
    def comment(self):
        """Gets the comment of this UpdateDebitMemoRequest.  # noqa: E501

        Comments about the debit memo.   # noqa: E501

        :return: The comment of this UpdateDebitMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UpdateDebitMemoRequest.

        Comments about the debit memo.   # noqa: E501

        :param comment: The comment of this UpdateDebitMemoRequest.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def due_date(self):
        """Gets the due_date of this UpdateDebitMemoRequest.  # noqa: E501

        The date by which the payment for the debit memo is due, in `yyyy-mm-dd` format.   # noqa: E501

        :return: The due_date of this UpdateDebitMemoRequest.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this UpdateDebitMemoRequest.

        The date by which the payment for the debit memo is due, in `yyyy-mm-dd` format.   # noqa: E501

        :param due_date: The due_date of this UpdateDebitMemoRequest.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def effective_date(self):
        """Gets the effective_date of this UpdateDebitMemoRequest.  # noqa: E501

        The date when the debit memo takes effect.   # noqa: E501

        :return: The effective_date of this UpdateDebitMemoRequest.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this UpdateDebitMemoRequest.

        The date when the debit memo takes effect.   # noqa: E501

        :param effective_date: The effective_date of this UpdateDebitMemoRequest.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def items(self):
        """Gets the items of this UpdateDebitMemoRequest.  # noqa: E501

        Container for debit memo items.   # noqa: E501

        :return: The items of this UpdateDebitMemoRequest.  # noqa: E501
        :rtype: list[UpdateDebitMemoItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this UpdateDebitMemoRequest.

        Container for debit memo items.   # noqa: E501

        :param items: The items of this UpdateDebitMemoRequest.  # noqa: E501
        :type: list[UpdateDebitMemoItem]
        """

        self._items = items

    @property
    def reason_code(self):
        """Gets the reason_code of this UpdateDebitMemoRequest.  # noqa: E501

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code   # noqa: E501

        :return: The reason_code of this UpdateDebitMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this UpdateDebitMemoRequest.

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code   # noqa: E501

        :param reason_code: The reason_code of this UpdateDebitMemoRequest.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def transferred_to_accounting(self):
        """Gets the transferred_to_accounting of this UpdateDebitMemoRequest.  # noqa: E501


        :return: The transferred_to_accounting of this UpdateDebitMemoRequest.  # noqa: E501
        :rtype: TransferredToAccountingStatus
        """
        return self._transferred_to_accounting

    @transferred_to_accounting.setter
    def transferred_to_accounting(self, transferred_to_accounting):
        """Sets the transferred_to_accounting of this UpdateDebitMemoRequest.


        :param transferred_to_accounting: The transferred_to_accounting of this UpdateDebitMemoRequest.  # noqa: E501
        :type: TransferredToAccountingStatus
        """

        self._transferred_to_accounting = transferred_to_accounting

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this UpdateDebitMemoRequest.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this UpdateDebitMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this UpdateDebitMemoRequest.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this UpdateDebitMemoRequest.  # noqa: E501
        :type: str
        """

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this UpdateDebitMemoRequest.  # noqa: E501

        Status of the debit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this UpdateDebitMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this UpdateDebitMemoRequest.

        Status of the debit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this UpdateDebitMemoRequest.  # noqa: E501
        :type: str
        """

        self._integration_status__ns = integration_status__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this UpdateDebitMemoRequest.  # noqa: E501

        Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this UpdateDebitMemoRequest.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this UpdateDebitMemoRequest.

        Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this UpdateDebitMemoRequest.  # noqa: E501
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
        if issubclass(UpdateDebitMemoRequest, dict):
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
        if not isinstance(other, UpdateDebitMemoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
