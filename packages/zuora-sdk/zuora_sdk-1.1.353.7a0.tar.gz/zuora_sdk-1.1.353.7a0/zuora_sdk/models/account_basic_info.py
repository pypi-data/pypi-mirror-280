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

class AccountBasicInfo(object):
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
        'account_number': 'str',
        'batch': 'str',
        'communication_profile_id': 'str',
        'credit_memo_template_id': 'str',
        'crm_id': 'str',
        'debit_memo_template_id': 'str',
        'id': 'str',
        'invoice_template_id': 'str',
        'last_metrics_update': 'str',
        'name': 'str',
        'notes': 'str',
        'parent_id': 'str',
        'partner_account': 'bool',
        'profile_number': 'str',
        'purchase_order_number': 'str',
        'sales_rep': 'str',
        'sequence_set_id': 'str',
        'status': 'AccountStatus',
        'tags': 'str',
        'customer_service_rep_name': 'str',
        'organization_label': 'str',
        'summary_statement_template_id': 'str',
        'class__ns': 'str',
        'customer_type__ns': 'AccountObjectNSFieldsCustomerTypeNS',
        'department__ns': 'str',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'location__ns': 'str',
        'subsidiary__ns': 'str',
        'sync_date__ns': 'str',
        'syncto_net_suite__ns': 'AccountObjectNSFieldsSynctoNetSuiteNS'
    }

    attribute_map = {
        'account_number': 'accountNumber',
        'batch': 'batch',
        'communication_profile_id': 'communicationProfileId',
        'credit_memo_template_id': 'creditMemoTemplateId',
        'crm_id': 'crmId',
        'debit_memo_template_id': 'debitMemoTemplateId',
        'id': 'id',
        'invoice_template_id': 'invoiceTemplateId',
        'last_metrics_update': 'lastMetricsUpdate',
        'name': 'name',
        'notes': 'notes',
        'parent_id': 'parentId',
        'partner_account': 'partnerAccount',
        'profile_number': 'profileNumber',
        'purchase_order_number': 'purchaseOrderNumber',
        'sales_rep': 'salesRep',
        'sequence_set_id': 'sequenceSetId',
        'status': 'status',
        'tags': 'tags',
        'customer_service_rep_name': 'customerServiceRepName',
        'organization_label': 'organizationLabel',
        'summary_statement_template_id': 'summaryStatementTemplateId',
        'class__ns': 'Class__NS',
        'customer_type__ns': 'CustomerType__NS',
        'department__ns': 'Department__NS',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'location__ns': 'Location__NS',
        'subsidiary__ns': 'Subsidiary__NS',
        'sync_date__ns': 'SyncDate__NS',
        'syncto_net_suite__ns': 'SynctoNetSuite__NS'
    }

    def __init__(self, account_number=None, batch=None, communication_profile_id=None, credit_memo_template_id=None, crm_id=None, debit_memo_template_id=None, id=None, invoice_template_id=None, last_metrics_update=None, name=None, notes=None, parent_id=None, partner_account=None, profile_number=None, purchase_order_number=None, sales_rep=None, sequence_set_id=None, status=None, tags=None, customer_service_rep_name=None, organization_label=None, summary_statement_template_id=None, class__ns=None, customer_type__ns=None, department__ns=None, integration_id__ns=None, integration_status__ns=None, location__ns=None, subsidiary__ns=None, sync_date__ns=None, syncto_net_suite__ns=None):  # noqa: E501
        """AccountBasicInfo - a model defined in Swagger"""  # noqa: E501
        self._account_number = None
        self._batch = None
        self._communication_profile_id = None
        self._credit_memo_template_id = None
        self._crm_id = None
        self._debit_memo_template_id = None
        self._id = None
        self._invoice_template_id = None
        self._last_metrics_update = None
        self._name = None
        self._notes = None
        self._parent_id = None
        self._partner_account = None
        self._profile_number = None
        self._purchase_order_number = None
        self._sales_rep = None
        self._sequence_set_id = None
        self._status = None
        self._tags = None
        self._customer_service_rep_name = None
        self._organization_label = None
        self._summary_statement_template_id = None
        self._class__ns = None
        self._customer_type__ns = None
        self._department__ns = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._location__ns = None
        self._subsidiary__ns = None
        self._sync_date__ns = None
        self._syncto_net_suite__ns = None
        self.discriminator = None
        if account_number is not None:
            self.account_number = account_number
        if batch is not None:
            self.batch = batch
        if communication_profile_id is not None:
            self.communication_profile_id = communication_profile_id
        if credit_memo_template_id is not None:
            self.credit_memo_template_id = credit_memo_template_id
        if crm_id is not None:
            self.crm_id = crm_id
        if debit_memo_template_id is not None:
            self.debit_memo_template_id = debit_memo_template_id
        if id is not None:
            self.id = id
        if invoice_template_id is not None:
            self.invoice_template_id = invoice_template_id
        if last_metrics_update is not None:
            self.last_metrics_update = last_metrics_update
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if parent_id is not None:
            self.parent_id = parent_id
        if partner_account is not None:
            self.partner_account = partner_account
        if profile_number is not None:
            self.profile_number = profile_number
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if sales_rep is not None:
            self.sales_rep = sales_rep
        if sequence_set_id is not None:
            self.sequence_set_id = sequence_set_id
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if customer_service_rep_name is not None:
            self.customer_service_rep_name = customer_service_rep_name
        if organization_label is not None:
            self.organization_label = organization_label
        if summary_statement_template_id is not None:
            self.summary_statement_template_id = summary_statement_template_id
        if class__ns is not None:
            self.class__ns = class__ns
        if customer_type__ns is not None:
            self.customer_type__ns = customer_type__ns
        if department__ns is not None:
            self.department__ns = department__ns
        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if location__ns is not None:
            self.location__ns = location__ns
        if subsidiary__ns is not None:
            self.subsidiary__ns = subsidiary__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if syncto_net_suite__ns is not None:
            self.syncto_net_suite__ns = syncto_net_suite__ns

    @property
    def account_number(self):
        """Gets the account_number of this AccountBasicInfo.  # noqa: E501

        Account number.   # noqa: E501

        :return: The account_number of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this AccountBasicInfo.

        Account number.   # noqa: E501

        :param account_number: The account_number of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def batch(self):
        """Gets the batch of this AccountBasicInfo.  # noqa: E501

        The alias name given to a batch. A string of 50 characters or less.   # noqa: E501

        :return: The batch of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """Sets the batch of this AccountBasicInfo.

        The alias name given to a batch. A string of 50 characters or less.   # noqa: E501

        :param batch: The batch of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._batch = batch

    @property
    def communication_profile_id(self):
        """Gets the communication_profile_id of this AccountBasicInfo.  # noqa: E501

        The ID of the communication profile that this account is linked to.  # noqa: E501

        :return: The communication_profile_id of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._communication_profile_id

    @communication_profile_id.setter
    def communication_profile_id(self, communication_profile_id):
        """Sets the communication_profile_id of this AccountBasicInfo.

        The ID of the communication profile that this account is linked to.  # noqa: E501

        :param communication_profile_id: The communication_profile_id of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._communication_profile_id = communication_profile_id

    @property
    def credit_memo_template_id(self):
        """Gets the credit_memo_template_id of this AccountBasicInfo.  # noqa: E501

        **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoicbe_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the credit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08a6246fdf101626b1b3fe0144b.   # noqa: E501

        :return: The credit_memo_template_id of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_template_id

    @credit_memo_template_id.setter
    def credit_memo_template_id(self, credit_memo_template_id):
        """Sets the credit_memo_template_id of this AccountBasicInfo.

        **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoicbe_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the credit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08a6246fdf101626b1b3fe0144b.   # noqa: E501

        :param credit_memo_template_id: The credit_memo_template_id of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._credit_memo_template_id = credit_memo_template_id

    @property
    def crm_id(self):
        """Gets the crm_id of this AccountBasicInfo.  # noqa: E501

        CRM account ID for the account, up to 100 characters.   # noqa: E501

        :return: The crm_id of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._crm_id

    @crm_id.setter
    def crm_id(self, crm_id):
        """Sets the crm_id of this AccountBasicInfo.

        CRM account ID for the account, up to 100 characters.   # noqa: E501

        :param crm_id: The crm_id of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._crm_id = crm_id

    @property
    def debit_memo_template_id(self):
        """Gets the debit_memo_template_id of this AccountBasicInfo.  # noqa: E501

        **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the debit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08d62470a8501626b19d24f19e2.   # noqa: E501

        :return: The debit_memo_template_id of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._debit_memo_template_id

    @debit_memo_template_id.setter
    def debit_memo_template_id(self, debit_memo_template_id):
        """Sets the debit_memo_template_id of this AccountBasicInfo.

        **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the debit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08d62470a8501626b19d24f19e2.   # noqa: E501

        :param debit_memo_template_id: The debit_memo_template_id of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._debit_memo_template_id = debit_memo_template_id

    @property
    def id(self):
        """Gets the id of this AccountBasicInfo.  # noqa: E501

        Account ID.   # noqa: E501

        :return: The id of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountBasicInfo.

        Account ID.   # noqa: E501

        :param id: The id of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_template_id(self):
        """Gets the invoice_template_id of this AccountBasicInfo.  # noqa: E501

        Invoice template ID, configured in Billing Settings in the Zuora UI.   # noqa: E501

        :return: The invoice_template_id of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._invoice_template_id

    @invoice_template_id.setter
    def invoice_template_id(self, invoice_template_id):
        """Sets the invoice_template_id of this AccountBasicInfo.

        Invoice template ID, configured in Billing Settings in the Zuora UI.   # noqa: E501

        :param invoice_template_id: The invoice_template_id of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._invoice_template_id = invoice_template_id

    @property
    def last_metrics_update(self):
        """Gets the last_metrics_update of this AccountBasicInfo.  # noqa: E501

        The date and time when account metrics are last updated, if the account is a partner account.  **Note**:    - This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Manage_customer_accounts/AAA_Overview_of_customer_accounts/Reseller_Account\" target=\"_blank\">Reseller Account</a> feature enabled.   - If you have the Reseller Account feature enabled, and set the `partnerAccount` field to `false` for an account, the value of the `lastMetricsUpdate` field is automatically set to `null` in the response.    - If you ever set the `partnerAccount` field to `true` for an account, the value of `lastMetricsUpdate` field is the time when the account metrics are last updated.   # noqa: E501

        :return: The last_metrics_update of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_metrics_update

    @last_metrics_update.setter
    def last_metrics_update(self, last_metrics_update):
        """Sets the last_metrics_update of this AccountBasicInfo.

        The date and time when account metrics are last updated, if the account is a partner account.  **Note**:    - This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Manage_customer_accounts/AAA_Overview_of_customer_accounts/Reseller_Account\" target=\"_blank\">Reseller Account</a> feature enabled.   - If you have the Reseller Account feature enabled, and set the `partnerAccount` field to `false` for an account, the value of the `lastMetricsUpdate` field is automatically set to `null` in the response.    - If you ever set the `partnerAccount` field to `true` for an account, the value of `lastMetricsUpdate` field is the time when the account metrics are last updated.   # noqa: E501

        :param last_metrics_update: The last_metrics_update of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._last_metrics_update = last_metrics_update

    @property
    def name(self):
        """Gets the name of this AccountBasicInfo.  # noqa: E501

        Account name.   # noqa: E501

        :return: The name of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountBasicInfo.

        Account name.   # noqa: E501

        :param name: The name of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this AccountBasicInfo.  # noqa: E501

        Notes associated with the account, up to 65,535 characters.   # noqa: E501

        :return: The notes of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AccountBasicInfo.

        Notes associated with the account, up to 65,535 characters.   # noqa: E501

        :param notes: The notes of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def parent_id(self):
        """Gets the parent_id of this AccountBasicInfo.  # noqa: E501

        Identifier of the parent customer account for this Account object. The length is 32 characters. Use this field if you have <a href=\"https://knowledgecenter.zuora.com/Billing/Subscriptions/Customer_Accounts/A_Customer_Account_Introduction#Customer_Hierarchy\" target=\"_blank\">Customer Hierarchy</a> enabled.  # noqa: E501

        :return: The parent_id of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this AccountBasicInfo.

        Identifier of the parent customer account for this Account object. The length is 32 characters. Use this field if you have <a href=\"https://knowledgecenter.zuora.com/Billing/Subscriptions/Customer_Accounts/A_Customer_Account_Introduction#Customer_Hierarchy\" target=\"_blank\">Customer Hierarchy</a> enabled.  # noqa: E501

        :param parent_id: The parent_id of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def partner_account(self):
        """Gets the partner_account of this AccountBasicInfo.  # noqa: E501

        Whether the customer account is a partner, distributor, or reseller.    **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Manage_customer_accounts/AAA_Overview_of_customer_accounts/Reseller_Account\" target=\"_blank\">Reseller Account</a> feature enabled.   # noqa: E501

        :return: The partner_account of this AccountBasicInfo.  # noqa: E501
        :rtype: bool
        """
        return self._partner_account

    @partner_account.setter
    def partner_account(self, partner_account):
        """Sets the partner_account of this AccountBasicInfo.

        Whether the customer account is a partner, distributor, or reseller.    **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Manage_customer_accounts/AAA_Overview_of_customer_accounts/Reseller_Account\" target=\"_blank\">Reseller Account</a> feature enabled.   # noqa: E501

        :param partner_account: The partner_account of this AccountBasicInfo.  # noqa: E501
        :type: bool
        """

        self._partner_account = partner_account

    @property
    def profile_number(self):
        """Gets the profile_number of this AccountBasicInfo.  # noqa: E501

        The number of the communication profile that this account is linked to.  # noqa: E501

        :return: The profile_number of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._profile_number

    @profile_number.setter
    def profile_number(self, profile_number):
        """Sets the profile_number of this AccountBasicInfo.

        The number of the communication profile that this account is linked to.  # noqa: E501

        :param profile_number: The profile_number of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._profile_number = profile_number

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this AccountBasicInfo.  # noqa: E501

        The purchase order number provided by your customer for services, products, or both purchased.  # noqa: E501

        :return: The purchase_order_number of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this AccountBasicInfo.

        The purchase order number provided by your customer for services, products, or both purchased.  # noqa: E501

        :param purchase_order_number: The purchase_order_number of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._purchase_order_number = purchase_order_number

    @property
    def sales_rep(self):
        """Gets the sales_rep of this AccountBasicInfo.  # noqa: E501

        The name of the sales representative associated with this account, if applicable. Maximum of 50 characters.  # noqa: E501

        :return: The sales_rep of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._sales_rep

    @sales_rep.setter
    def sales_rep(self, sales_rep):
        """Sets the sales_rep of this AccountBasicInfo.

        The name of the sales representative associated with this account, if applicable. Maximum of 50 characters.  # noqa: E501

        :param sales_rep: The sales_rep of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._sales_rep = sales_rep

    @property
    def sequence_set_id(self):
        """Gets the sequence_set_id of this AccountBasicInfo.  # noqa: E501

        The ID of the billing document sequence set that is assigned to the customer account.    # noqa: E501

        :return: The sequence_set_id of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._sequence_set_id

    @sequence_set_id.setter
    def sequence_set_id(self, sequence_set_id):
        """Sets the sequence_set_id of this AccountBasicInfo.

        The ID of the billing document sequence set that is assigned to the customer account.    # noqa: E501

        :param sequence_set_id: The sequence_set_id of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._sequence_set_id = sequence_set_id

    @property
    def status(self):
        """Gets the status of this AccountBasicInfo.  # noqa: E501


        :return: The status of this AccountBasicInfo.  # noqa: E501
        :rtype: AccountStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountBasicInfo.


        :param status: The status of this AccountBasicInfo.  # noqa: E501
        :type: AccountStatus
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this AccountBasicInfo.  # noqa: E501


        :return: The tags of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AccountBasicInfo.


        :param tags: The tags of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def customer_service_rep_name(self):
        """Gets the customer_service_rep_name of this AccountBasicInfo.  # noqa: E501

        customer ServiceRep Name.   # noqa: E501

        :return: The customer_service_rep_name of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._customer_service_rep_name

    @customer_service_rep_name.setter
    def customer_service_rep_name(self, customer_service_rep_name):
        """Sets the customer_service_rep_name of this AccountBasicInfo.

        customer ServiceRep Name.   # noqa: E501

        :param customer_service_rep_name: The customer_service_rep_name of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._customer_service_rep_name = customer_service_rep_name

    @property
    def organization_label(self):
        """Gets the organization_label of this AccountBasicInfo.  # noqa: E501

        organization label.   # noqa: E501

        :return: The organization_label of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._organization_label

    @organization_label.setter
    def organization_label(self, organization_label):
        """Sets the organization_label of this AccountBasicInfo.

        organization label.   # noqa: E501

        :param organization_label: The organization_label of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._organization_label = organization_label

    @property
    def summary_statement_template_id(self):
        """Gets the summary_statement_template_id of this AccountBasicInfo.  # noqa: E501

        summary statement template ID.   # noqa: E501

        :return: The summary_statement_template_id of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._summary_statement_template_id

    @summary_statement_template_id.setter
    def summary_statement_template_id(self, summary_statement_template_id):
        """Sets the summary_statement_template_id of this AccountBasicInfo.

        summary statement template ID.   # noqa: E501

        :param summary_statement_template_id: The summary_statement_template_id of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._summary_statement_template_id = summary_statement_template_id

    @property
    def class__ns(self):
        """Gets the class__ns of this AccountBasicInfo.  # noqa: E501

        Value of the Class field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The class__ns of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._class__ns

    @class__ns.setter
    def class__ns(self, class__ns):
        """Sets the class__ns of this AccountBasicInfo.

        Value of the Class field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param class__ns: The class__ns of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._class__ns = class__ns

    @property
    def customer_type__ns(self):
        """Gets the customer_type__ns of this AccountBasicInfo.  # noqa: E501


        :return: The customer_type__ns of this AccountBasicInfo.  # noqa: E501
        :rtype: AccountObjectNSFieldsCustomerTypeNS
        """
        return self._customer_type__ns

    @customer_type__ns.setter
    def customer_type__ns(self, customer_type__ns):
        """Sets the customer_type__ns of this AccountBasicInfo.


        :param customer_type__ns: The customer_type__ns of this AccountBasicInfo.  # noqa: E501
        :type: AccountObjectNSFieldsCustomerTypeNS
        """

        self._customer_type__ns = customer_type__ns

    @property
    def department__ns(self):
        """Gets the department__ns of this AccountBasicInfo.  # noqa: E501

        Value of the Department field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The department__ns of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._department__ns

    @department__ns.setter
    def department__ns(self, department__ns):
        """Sets the department__ns of this AccountBasicInfo.

        Value of the Department field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param department__ns: The department__ns of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._department__ns = department__ns

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this AccountBasicInfo.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this AccountBasicInfo.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this AccountBasicInfo.  # noqa: E501

        Status of the account's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this AccountBasicInfo.

        Status of the account's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._integration_status__ns = integration_status__ns

    @property
    def location__ns(self):
        """Gets the location__ns of this AccountBasicInfo.  # noqa: E501

        Value of the Location field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The location__ns of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._location__ns

    @location__ns.setter
    def location__ns(self, location__ns):
        """Sets the location__ns of this AccountBasicInfo.

        Value of the Location field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param location__ns: The location__ns of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._location__ns = location__ns

    @property
    def subsidiary__ns(self):
        """Gets the subsidiary__ns of this AccountBasicInfo.  # noqa: E501

        Value of the Subsidiary field for the corresponding customer account in NetSuite. The Subsidiary field is required if you use NetSuite OneWorld. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The subsidiary__ns of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._subsidiary__ns

    @subsidiary__ns.setter
    def subsidiary__ns(self, subsidiary__ns):
        """Sets the subsidiary__ns of this AccountBasicInfo.

        Value of the Subsidiary field for the corresponding customer account in NetSuite. The Subsidiary field is required if you use NetSuite OneWorld. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param subsidiary__ns: The subsidiary__ns of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._subsidiary__ns = subsidiary__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this AccountBasicInfo.  # noqa: E501

        Date when the account was sychronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this AccountBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this AccountBasicInfo.

        Date when the account was sychronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this AccountBasicInfo.  # noqa: E501
        :type: str
        """

        self._sync_date__ns = sync_date__ns

    @property
    def syncto_net_suite__ns(self):
        """Gets the syncto_net_suite__ns of this AccountBasicInfo.  # noqa: E501


        :return: The syncto_net_suite__ns of this AccountBasicInfo.  # noqa: E501
        :rtype: AccountObjectNSFieldsSynctoNetSuiteNS
        """
        return self._syncto_net_suite__ns

    @syncto_net_suite__ns.setter
    def syncto_net_suite__ns(self, syncto_net_suite__ns):
        """Sets the syncto_net_suite__ns of this AccountBasicInfo.


        :param syncto_net_suite__ns: The syncto_net_suite__ns of this AccountBasicInfo.  # noqa: E501
        :type: AccountObjectNSFieldsSynctoNetSuiteNS
        """

        self._syncto_net_suite__ns = syncto_net_suite__ns

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
        if issubclass(AccountBasicInfo, dict):
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
        if not isinstance(other, AccountBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
