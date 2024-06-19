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

class GetJournalRunResponse(object):
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
        'aggregate_currency': 'bool',
        'executed_on': 'str',
        'journal_entry_date': 'date',
        'number': 'str',
        'segmentation_rule_name': 'str',
        'status': 'JournalRunStatus',
        'success': 'bool',
        'target_end_date': 'date',
        'target_start_date': 'date',
        'total_journal_entry_count': 'int',
        'organization_labels': 'list[OrganizationLabel]',
        'transaction_types': 'list[GetJournalRunTransactionResponse]'
    }

    attribute_map = {
        'aggregate_currency': 'aggregateCurrency',
        'executed_on': 'executedOn',
        'journal_entry_date': 'journalEntryDate',
        'number': 'number',
        'segmentation_rule_name': 'segmentationRuleName',
        'status': 'status',
        'success': 'success',
        'target_end_date': 'targetEndDate',
        'target_start_date': 'targetStartDate',
        'total_journal_entry_count': 'totalJournalEntryCount',
        'organization_labels': 'organizationLabels',
        'transaction_types': 'transactionTypes'
    }

    def __init__(self, aggregate_currency=None, executed_on=None, journal_entry_date=None, number=None, segmentation_rule_name=None, status=None, success=None, target_end_date=None, target_start_date=None, total_journal_entry_count=None, organization_labels=None, transaction_types=None):  # noqa: E501
        """GetJournalRunResponse - a model defined in Swagger"""  # noqa: E501
        self._aggregate_currency = None
        self._executed_on = None
        self._journal_entry_date = None
        self._number = None
        self._segmentation_rule_name = None
        self._status = None
        self._success = None
        self._target_end_date = None
        self._target_start_date = None
        self._total_journal_entry_count = None
        self._organization_labels = None
        self._transaction_types = None
        self.discriminator = None
        if aggregate_currency is not None:
            self.aggregate_currency = aggregate_currency
        if executed_on is not None:
            self.executed_on = executed_on
        if journal_entry_date is not None:
            self.journal_entry_date = journal_entry_date
        if number is not None:
            self.number = number
        if segmentation_rule_name is not None:
            self.segmentation_rule_name = segmentation_rule_name
        if status is not None:
            self.status = status
        if success is not None:
            self.success = success
        if target_end_date is not None:
            self.target_end_date = target_end_date
        if target_start_date is not None:
            self.target_start_date = target_start_date
        if total_journal_entry_count is not None:
            self.total_journal_entry_count = total_journal_entry_count
        if organization_labels is not None:
            self.organization_labels = organization_labels
        if transaction_types is not None:
            self.transaction_types = transaction_types

    @property
    def aggregate_currency(self):
        """Gets the aggregate_currency of this GetJournalRunResponse.  # noqa: E501


        :return: The aggregate_currency of this GetJournalRunResponse.  # noqa: E501
        :rtype: bool
        """
        return self._aggregate_currency

    @aggregate_currency.setter
    def aggregate_currency(self, aggregate_currency):
        """Sets the aggregate_currency of this GetJournalRunResponse.


        :param aggregate_currency: The aggregate_currency of this GetJournalRunResponse.  # noqa: E501
        :type: bool
        """

        self._aggregate_currency = aggregate_currency

    @property
    def executed_on(self):
        """Gets the executed_on of this GetJournalRunResponse.  # noqa: E501

        Date and time the journal run was executed.   # noqa: E501

        :return: The executed_on of this GetJournalRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._executed_on

    @executed_on.setter
    def executed_on(self, executed_on):
        """Sets the executed_on of this GetJournalRunResponse.

        Date and time the journal run was executed.   # noqa: E501

        :param executed_on: The executed_on of this GetJournalRunResponse.  # noqa: E501
        :type: str
        """

        self._executed_on = executed_on

    @property
    def journal_entry_date(self):
        """Gets the journal_entry_date of this GetJournalRunResponse.  # noqa: E501

        Date of the journal entry.   # noqa: E501

        :return: The journal_entry_date of this GetJournalRunResponse.  # noqa: E501
        :rtype: date
        """
        return self._journal_entry_date

    @journal_entry_date.setter
    def journal_entry_date(self, journal_entry_date):
        """Sets the journal_entry_date of this GetJournalRunResponse.

        Date of the journal entry.   # noqa: E501

        :param journal_entry_date: The journal_entry_date of this GetJournalRunResponse.  # noqa: E501
        :type: date
        """

        self._journal_entry_date = journal_entry_date

    @property
    def number(self):
        """Gets the number of this GetJournalRunResponse.  # noqa: E501

        Journal run number.   # noqa: E501

        :return: The number of this GetJournalRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this GetJournalRunResponse.

        Journal run number.   # noqa: E501

        :param number: The number of this GetJournalRunResponse.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def segmentation_rule_name(self):
        """Gets the segmentation_rule_name of this GetJournalRunResponse.  # noqa: E501

        Name of GL segmentation rule used in the journal run.   # noqa: E501

        :return: The segmentation_rule_name of this GetJournalRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._segmentation_rule_name

    @segmentation_rule_name.setter
    def segmentation_rule_name(self, segmentation_rule_name):
        """Sets the segmentation_rule_name of this GetJournalRunResponse.

        Name of GL segmentation rule used in the journal run.   # noqa: E501

        :param segmentation_rule_name: The segmentation_rule_name of this GetJournalRunResponse.  # noqa: E501
        :type: str
        """

        self._segmentation_rule_name = segmentation_rule_name

    @property
    def status(self):
        """Gets the status of this GetJournalRunResponse.  # noqa: E501


        :return: The status of this GetJournalRunResponse.  # noqa: E501
        :rtype: JournalRunStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetJournalRunResponse.


        :param status: The status of this GetJournalRunResponse.  # noqa: E501
        :type: JournalRunStatus
        """

        self._status = status

    @property
    def success(self):
        """Gets the success of this GetJournalRunResponse.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this GetJournalRunResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GetJournalRunResponse.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this GetJournalRunResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def target_end_date(self):
        """Gets the target_end_date of this GetJournalRunResponse.  # noqa: E501

        The target end date of the journal run.   # noqa: E501

        :return: The target_end_date of this GetJournalRunResponse.  # noqa: E501
        :rtype: date
        """
        return self._target_end_date

    @target_end_date.setter
    def target_end_date(self, target_end_date):
        """Sets the target_end_date of this GetJournalRunResponse.

        The target end date of the journal run.   # noqa: E501

        :param target_end_date: The target_end_date of this GetJournalRunResponse.  # noqa: E501
        :type: date
        """

        self._target_end_date = target_end_date

    @property
    def target_start_date(self):
        """Gets the target_start_date of this GetJournalRunResponse.  # noqa: E501

        The target start date of the journal run.   # noqa: E501

        :return: The target_start_date of this GetJournalRunResponse.  # noqa: E501
        :rtype: date
        """
        return self._target_start_date

    @target_start_date.setter
    def target_start_date(self, target_start_date):
        """Sets the target_start_date of this GetJournalRunResponse.

        The target start date of the journal run.   # noqa: E501

        :param target_start_date: The target_start_date of this GetJournalRunResponse.  # noqa: E501
        :type: date
        """

        self._target_start_date = target_start_date

    @property
    def total_journal_entry_count(self):
        """Gets the total_journal_entry_count of this GetJournalRunResponse.  # noqa: E501

        Total number of journal entries in the journal run.   # noqa: E501

        :return: The total_journal_entry_count of this GetJournalRunResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_journal_entry_count

    @total_journal_entry_count.setter
    def total_journal_entry_count(self, total_journal_entry_count):
        """Sets the total_journal_entry_count of this GetJournalRunResponse.

        Total number of journal entries in the journal run.   # noqa: E501

        :param total_journal_entry_count: The total_journal_entry_count of this GetJournalRunResponse.  # noqa: E501
        :type: int
        """

        self._total_journal_entry_count = total_journal_entry_count

    @property
    def organization_labels(self):
        """Gets the organization_labels of this GetJournalRunResponse.  # noqa: E501

        Organization Labels.   # noqa: E501

        :return: The organization_labels of this GetJournalRunResponse.  # noqa: E501
        :rtype: list[OrganizationLabel]
        """
        return self._organization_labels

    @organization_labels.setter
    def organization_labels(self, organization_labels):
        """Sets the organization_labels of this GetJournalRunResponse.

        Organization Labels.   # noqa: E501

        :param organization_labels: The organization_labels of this GetJournalRunResponse.  # noqa: E501
        :type: list[OrganizationLabel]
        """

        self._organization_labels = organization_labels

    @property
    def transaction_types(self):
        """Gets the transaction_types of this GetJournalRunResponse.  # noqa: E501

        Transaction types included in the journal run.   # noqa: E501

        :return: The transaction_types of this GetJournalRunResponse.  # noqa: E501
        :rtype: list[GetJournalRunTransactionResponse]
        """
        return self._transaction_types

    @transaction_types.setter
    def transaction_types(self, transaction_types):
        """Sets the transaction_types of this GetJournalRunResponse.

        Transaction types included in the journal run.   # noqa: E501

        :param transaction_types: The transaction_types of this GetJournalRunResponse.  # noqa: E501
        :type: list[GetJournalRunTransactionResponse]
        """

        self._transaction_types = transaction_types

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
        if issubclass(GetJournalRunResponse, dict):
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
        if not isinstance(other, GetJournalRunResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
