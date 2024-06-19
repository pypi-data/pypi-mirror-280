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

class CreateInvoiceRequest(object):
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
        'comments': 'str',
        'custom_rates': 'list[CustomRates]',
        'due_date': 'date',
        'invoice_date': 'date',
        'invoice_items': 'list[CreateInvoiceItem]',
        'invoice_number': 'str',
        'status': 'BillingDocumentStatus',
        'bill_to_contact_id': 'str',
        'payment_term': 'str',
        'sequence_set': 'str',
        'sold_to_contact_id': 'str',
        'bill_to_contact': 'CreateAccountContact',
        'sold_to_contact': 'CreateAccountContact',
        'sold_to_same_as_bill_to': 'bool',
        'template_id': 'str',
        'transferred_to_accounting': 'TransferredToAccountingStatus',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'sync_date__ns': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'account_number': 'accountNumber',
        'auto_pay': 'autoPay',
        'comments': 'comments',
        'custom_rates': 'customRates',
        'due_date': 'dueDate',
        'invoice_date': 'invoiceDate',
        'invoice_items': 'invoiceItems',
        'invoice_number': 'invoiceNumber',
        'status': 'status',
        'bill_to_contact_id': 'billToContactId',
        'payment_term': 'paymentTerm',
        'sequence_set': 'sequenceSet',
        'sold_to_contact_id': 'soldToContactId',
        'bill_to_contact': 'billToContact',
        'sold_to_contact': 'soldToContact',
        'sold_to_same_as_bill_to': 'soldToSameAsBillTo',
        'template_id': 'templateId',
        'transferred_to_accounting': 'transferredToAccounting',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'sync_date__ns': 'SyncDate__NS'
    }

    def __init__(self, account_id=None, account_number=None, auto_pay=False, comments=None, custom_rates=None, due_date=None, invoice_date=None, invoice_items=None, invoice_number=None, status=None, bill_to_contact_id=None, payment_term=None, sequence_set=None, sold_to_contact_id=None, bill_to_contact=None, sold_to_contact=None, sold_to_same_as_bill_to=None, template_id=None, transferred_to_accounting=None, integration_id__ns=None, integration_status__ns=None, sync_date__ns=None):  # noqa: E501
        """CreateInvoiceRequest - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._account_number = None
        self._auto_pay = None
        self._comments = None
        self._custom_rates = None
        self._due_date = None
        self._invoice_date = None
        self._invoice_items = None
        self._invoice_number = None
        self._status = None
        self._bill_to_contact_id = None
        self._payment_term = None
        self._sequence_set = None
        self._sold_to_contact_id = None
        self._bill_to_contact = None
        self._sold_to_contact = None
        self._sold_to_same_as_bill_to = None
        self._template_id = None
        self._transferred_to_accounting = None
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
        if comments is not None:
            self.comments = comments
        if custom_rates is not None:
            self.custom_rates = custom_rates
        if due_date is not None:
            self.due_date = due_date
        self.invoice_date = invoice_date
        self.invoice_items = invoice_items
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if status is not None:
            self.status = status
        if bill_to_contact_id is not None:
            self.bill_to_contact_id = bill_to_contact_id
        if payment_term is not None:
            self.payment_term = payment_term
        if sequence_set is not None:
            self.sequence_set = sequence_set
        if sold_to_contact_id is not None:
            self.sold_to_contact_id = sold_to_contact_id
        if bill_to_contact is not None:
            self.bill_to_contact = bill_to_contact
        if sold_to_contact is not None:
            self.sold_to_contact = sold_to_contact
        if sold_to_same_as_bill_to is not None:
            self.sold_to_same_as_bill_to = sold_to_same_as_bill_to
        if template_id is not None:
            self.template_id = template_id
        if transferred_to_accounting is not None:
            self.transferred_to_accounting = transferred_to_accounting
        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns

    @property
    def account_id(self):
        """Gets the account_id of this CreateInvoiceRequest.  # noqa: E501

        The ID of the account associated with the invoice.   You must specify either `accountNumber` or `accountId` for a customer account. If both of them are specified, they must refer to the same customer account.   # noqa: E501

        :return: The account_id of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CreateInvoiceRequest.

        The ID of the account associated with the invoice.   You must specify either `accountNumber` or `accountId` for a customer account. If both of them are specified, they must refer to the same customer account.   # noqa: E501

        :param account_id: The account_id of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_number(self):
        """Gets the account_number of this CreateInvoiceRequest.  # noqa: E501

        The Number of the account associated with the invoice. You must specify either `accountNumber` or `accountId` for a customer account. If both of them are specified, they must refer to the same customer account.  # noqa: E501

        :return: The account_number of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this CreateInvoiceRequest.

        The Number of the account associated with the invoice. You must specify either `accountNumber` or `accountId` for a customer account. If both of them are specified, they must refer to the same customer account.  # noqa: E501

        :param account_number: The account_number of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def auto_pay(self):
        """Gets the auto_pay of this CreateInvoiceRequest.  # noqa: E501

        Whether invoices are automatically picked up for processing in the corresponding payment run.  # noqa: E501

        :return: The auto_pay of this CreateInvoiceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this CreateInvoiceRequest.

        Whether invoices are automatically picked up for processing in the corresponding payment run.  # noqa: E501

        :param auto_pay: The auto_pay of this CreateInvoiceRequest.  # noqa: E501
        :type: bool
        """

        self._auto_pay = auto_pay

    @property
    def comments(self):
        """Gets the comments of this CreateInvoiceRequest.  # noqa: E501

        Comments about the invoice.  # noqa: E501

        :return: The comments of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this CreateInvoiceRequest.

        Comments about the invoice.  # noqa: E501

        :param comments: The comments of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def custom_rates(self):
        """Gets the custom_rates of this CreateInvoiceRequest.  # noqa: E501

        It contains Home currency and Reporting currency custom rates currencies. The maximum number of items is 2 (you can pass the Home currency item or Reporting currency item or both).        **Note**: The API custom rate feature is permission controlled.   # noqa: E501

        :return: The custom_rates of this CreateInvoiceRequest.  # noqa: E501
        :rtype: list[CustomRates]
        """
        return self._custom_rates

    @custom_rates.setter
    def custom_rates(self, custom_rates):
        """Sets the custom_rates of this CreateInvoiceRequest.

        It contains Home currency and Reporting currency custom rates currencies. The maximum number of items is 2 (you can pass the Home currency item or Reporting currency item or both).        **Note**: The API custom rate feature is permission controlled.   # noqa: E501

        :param custom_rates: The custom_rates of this CreateInvoiceRequest.  # noqa: E501
        :type: list[CustomRates]
        """

        self._custom_rates = custom_rates

    @property
    def due_date(self):
        """Gets the due_date of this CreateInvoiceRequest.  # noqa: E501

        The date by which the payment for this invoice is due, in `yyyy-mm-dd` format.   # noqa: E501

        :return: The due_date of this CreateInvoiceRequest.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this CreateInvoiceRequest.

        The date by which the payment for this invoice is due, in `yyyy-mm-dd` format.   # noqa: E501

        :param due_date: The due_date of this CreateInvoiceRequest.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def invoice_date(self):
        """Gets the invoice_date of this CreateInvoiceRequest.  # noqa: E501

        The date that appears on the invoice being created, in `yyyy-mm-dd` format. The value cannot fall in a closed accounting period.  # noqa: E501

        :return: The invoice_date of this CreateInvoiceRequest.  # noqa: E501
        :rtype: date
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this CreateInvoiceRequest.

        The date that appears on the invoice being created, in `yyyy-mm-dd` format. The value cannot fall in a closed accounting period.  # noqa: E501

        :param invoice_date: The invoice_date of this CreateInvoiceRequest.  # noqa: E501
        :type: date
        """
        if invoice_date is None:
            raise ValueError("Invalid value for `invoice_date`, must not be `None`")  # noqa: E501

        self._invoice_date = invoice_date

    @property
    def invoice_items(self):
        """Gets the invoice_items of this CreateInvoiceRequest.  # noqa: E501

        Container for invoice items. The maximum number of invoice items is 1,000.  # noqa: E501

        :return: The invoice_items of this CreateInvoiceRequest.  # noqa: E501
        :rtype: list[CreateInvoiceItem]
        """
        return self._invoice_items

    @invoice_items.setter
    def invoice_items(self, invoice_items):
        """Sets the invoice_items of this CreateInvoiceRequest.

        Container for invoice items. The maximum number of invoice items is 1,000.  # noqa: E501

        :param invoice_items: The invoice_items of this CreateInvoiceRequest.  # noqa: E501
        :type: list[CreateInvoiceItem]
        """
        if invoice_items is None:
            raise ValueError("Invalid value for `invoice_items`, must not be `None`")  # noqa: E501

        self._invoice_items = invoice_items

    @property
    def invoice_number(self):
        """Gets the invoice_number of this CreateInvoiceRequest.  # noqa: E501

        A customized invoice number with the following format requirements: - Max length: 32 characters - Acceptable characters: a-z,A-Z,0-9,-,_,  The value must be unique in the system, otherwise it may cause issues with bill runs and subscribe/amend. Check out [things to note and troubleshooting steps](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/IA_Invoices/Unified_Invoicing/Import_external_invoices_as_standalone_invoices?#Customizing_invoice_number).    # noqa: E501

        :return: The invoice_number of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this CreateInvoiceRequest.

        A customized invoice number with the following format requirements: - Max length: 32 characters - Acceptable characters: a-z,A-Z,0-9,-,_,  The value must be unique in the system, otherwise it may cause issues with bill runs and subscribe/amend. Check out [things to note and troubleshooting steps](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/IA_Invoices/Unified_Invoicing/Import_external_invoices_as_standalone_invoices?#Customizing_invoice_number).    # noqa: E501

        :param invoice_number: The invoice_number of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def status(self):
        """Gets the status of this CreateInvoiceRequest.  # noqa: E501


        :return: The status of this CreateInvoiceRequest.  # noqa: E501
        :rtype: BillingDocumentStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateInvoiceRequest.


        :param status: The status of this CreateInvoiceRequest.  # noqa: E501
        :type: BillingDocumentStatus
        """

        self._status = status

    @property
    def bill_to_contact_id(self):
        """Gets the bill_to_contact_id of this CreateInvoiceRequest.  # noqa: E501

        The ID of the bill-to contact associated with the invoice.  # noqa: E501

        :return: The bill_to_contact_id of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._bill_to_contact_id

    @bill_to_contact_id.setter
    def bill_to_contact_id(self, bill_to_contact_id):
        """Sets the bill_to_contact_id of this CreateInvoiceRequest.

        The ID of the bill-to contact associated with the invoice.  # noqa: E501

        :param bill_to_contact_id: The bill_to_contact_id of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._bill_to_contact_id = bill_to_contact_id

    @property
    def payment_term(self):
        """Gets the payment_term of this CreateInvoiceRequest.  # noqa: E501

        The name of payment term associated with the invoice.  # noqa: E501

        :return: The payment_term of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_term

    @payment_term.setter
    def payment_term(self, payment_term):
        """Sets the payment_term of this CreateInvoiceRequest.

        The name of payment term associated with the invoice.  # noqa: E501

        :param payment_term: The payment_term of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._payment_term = payment_term

    @property
    def sequence_set(self):
        """Gets the sequence_set of this CreateInvoiceRequest.  # noqa: E501

        The ID or name of the sequence set associated with the invoice.  # noqa: E501

        :return: The sequence_set of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._sequence_set

    @sequence_set.setter
    def sequence_set(self, sequence_set):
        """Sets the sequence_set of this CreateInvoiceRequest.

        The ID or name of the sequence set associated with the invoice.  # noqa: E501

        :param sequence_set: The sequence_set of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._sequence_set = sequence_set

    @property
    def sold_to_contact_id(self):
        """Gets the sold_to_contact_id of this CreateInvoiceRequest.  # noqa: E501

        The ID of the sold-to contact associated with the invoice.  # noqa: E501

        :return: The sold_to_contact_id of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._sold_to_contact_id

    @sold_to_contact_id.setter
    def sold_to_contact_id(self, sold_to_contact_id):
        """Sets the sold_to_contact_id of this CreateInvoiceRequest.

        The ID of the sold-to contact associated with the invoice.  # noqa: E501

        :param sold_to_contact_id: The sold_to_contact_id of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._sold_to_contact_id = sold_to_contact_id

    @property
    def bill_to_contact(self):
        """Gets the bill_to_contact of this CreateInvoiceRequest.  # noqa: E501


        :return: The bill_to_contact of this CreateInvoiceRequest.  # noqa: E501
        :rtype: CreateAccountContact
        """
        return self._bill_to_contact

    @bill_to_contact.setter
    def bill_to_contact(self, bill_to_contact):
        """Sets the bill_to_contact of this CreateInvoiceRequest.


        :param bill_to_contact: The bill_to_contact of this CreateInvoiceRequest.  # noqa: E501
        :type: CreateAccountContact
        """

        self._bill_to_contact = bill_to_contact

    @property
    def sold_to_contact(self):
        """Gets the sold_to_contact of this CreateInvoiceRequest.  # noqa: E501


        :return: The sold_to_contact of this CreateInvoiceRequest.  # noqa: E501
        :rtype: CreateAccountContact
        """
        return self._sold_to_contact

    @sold_to_contact.setter
    def sold_to_contact(self, sold_to_contact):
        """Sets the sold_to_contact of this CreateInvoiceRequest.


        :param sold_to_contact: The sold_to_contact of this CreateInvoiceRequest.  # noqa: E501
        :type: CreateAccountContact
        """

        self._sold_to_contact = sold_to_contact

    @property
    def sold_to_same_as_bill_to(self):
        """Gets the sold_to_same_as_bill_to of this CreateInvoiceRequest.  # noqa: E501

        Whether the sold-to contact and bill-to contact are the same entity.  The created invoice has the same bill-to contact and sold-to contact entity only when all the following conditions are met in the request body: - This field is set to `true`.  - A bill-to contact is specified. - No sold-to contact is specified.   # noqa: E501

        :return: The sold_to_same_as_bill_to of this CreateInvoiceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sold_to_same_as_bill_to

    @sold_to_same_as_bill_to.setter
    def sold_to_same_as_bill_to(self, sold_to_same_as_bill_to):
        """Sets the sold_to_same_as_bill_to of this CreateInvoiceRequest.

        Whether the sold-to contact and bill-to contact are the same entity.  The created invoice has the same bill-to contact and sold-to contact entity only when all the following conditions are met in the request body: - This field is set to `true`.  - A bill-to contact is specified. - No sold-to contact is specified.   # noqa: E501

        :param sold_to_same_as_bill_to: The sold_to_same_as_bill_to of this CreateInvoiceRequest.  # noqa: E501
        :type: bool
        """

        self._sold_to_same_as_bill_to = sold_to_same_as_bill_to

    @property
    def template_id(self):
        """Gets the template_id of this CreateInvoiceRequest.  # noqa: E501

        The ID of the invoice template. **Note**: This field requires Flexible Billing Attribute.  # noqa: E501

        :return: The template_id of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateInvoiceRequest.

        The ID of the invoice template. **Note**: This field requires Flexible Billing Attribute.  # noqa: E501

        :param template_id: The template_id of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def transferred_to_accounting(self):
        """Gets the transferred_to_accounting of this CreateInvoiceRequest.  # noqa: E501


        :return: The transferred_to_accounting of this CreateInvoiceRequest.  # noqa: E501
        :rtype: TransferredToAccountingStatus
        """
        return self._transferred_to_accounting

    @transferred_to_accounting.setter
    def transferred_to_accounting(self, transferred_to_accounting):
        """Sets the transferred_to_accounting of this CreateInvoiceRequest.


        :param transferred_to_accounting: The transferred_to_accounting of this CreateInvoiceRequest.  # noqa: E501
        :type: TransferredToAccountingStatus
        """

        self._transferred_to_accounting = transferred_to_accounting

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this CreateInvoiceRequest.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this CreateInvoiceRequest.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this CreateInvoiceRequest.  # noqa: E501

        Status of the invoice's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this CreateInvoiceRequest.

        Status of the invoice's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._integration_status__ns = integration_status__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this CreateInvoiceRequest.  # noqa: E501

        Date when the invoice was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this CreateInvoiceRequest.

        Date when the invoice was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this CreateInvoiceRequest.  # noqa: E501
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
        if issubclass(CreateInvoiceRequest, dict):
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
        if not isinstance(other, CreateInvoiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
