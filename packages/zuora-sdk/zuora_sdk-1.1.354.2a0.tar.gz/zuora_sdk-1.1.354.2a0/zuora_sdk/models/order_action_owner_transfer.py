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

class OrderActionOwnerTransfer(object):
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
        'bill_to_contact_id': 'str',
        'clearing_existing_bill_to_contact': 'bool',
        'clearing_existing_invoice_group_number': 'bool',
        'clearing_existing_invoice_template': 'bool',
        'clearing_existing_payment_term': 'bool',
        'clearing_existing_sequence_set': 'bool',
        'clearing_existing_sold_to_contact': 'bool',
        'destination_account_number': 'str',
        'destination_invoice_account_number': 'str',
        'invoice_group_number': 'str',
        'invoice_template_id': 'str',
        'payment_term': 'str',
        'sequence_set_id': 'str',
        'sold_to_contact_id': 'str'
    }

    attribute_map = {
        'bill_to_contact_id': 'billToContactId',
        'clearing_existing_bill_to_contact': 'clearingExistingBillToContact',
        'clearing_existing_invoice_group_number': 'clearingExistingInvoiceGroupNumber',
        'clearing_existing_invoice_template': 'clearingExistingInvoiceTemplate',
        'clearing_existing_payment_term': 'clearingExistingPaymentTerm',
        'clearing_existing_sequence_set': 'clearingExistingSequenceSet',
        'clearing_existing_sold_to_contact': 'clearingExistingSoldToContact',
        'destination_account_number': 'destinationAccountNumber',
        'destination_invoice_account_number': 'destinationInvoiceAccountNumber',
        'invoice_group_number': 'invoiceGroupNumber',
        'invoice_template_id': 'invoiceTemplateId',
        'payment_term': 'paymentTerm',
        'sequence_set_id': 'sequenceSetId',
        'sold_to_contact_id': 'soldToContactId'
    }

    def __init__(self, bill_to_contact_id=None, clearing_existing_bill_to_contact=False, clearing_existing_invoice_group_number=False, clearing_existing_invoice_template=False, clearing_existing_payment_term=False, clearing_existing_sequence_set=False, clearing_existing_sold_to_contact=False, destination_account_number=None, destination_invoice_account_number=None, invoice_group_number=None, invoice_template_id=None, payment_term=None, sequence_set_id=None, sold_to_contact_id=None):  # noqa: E501
        """OrderActionOwnerTransfer - a model defined in Swagger"""  # noqa: E501
        self._bill_to_contact_id = None
        self._clearing_existing_bill_to_contact = None
        self._clearing_existing_invoice_group_number = None
        self._clearing_existing_invoice_template = None
        self._clearing_existing_payment_term = None
        self._clearing_existing_sequence_set = None
        self._clearing_existing_sold_to_contact = None
        self._destination_account_number = None
        self._destination_invoice_account_number = None
        self._invoice_group_number = None
        self._invoice_template_id = None
        self._payment_term = None
        self._sequence_set_id = None
        self._sold_to_contact_id = None
        self.discriminator = None
        if bill_to_contact_id is not None:
            self.bill_to_contact_id = bill_to_contact_id
        if clearing_existing_bill_to_contact is not None:
            self.clearing_existing_bill_to_contact = clearing_existing_bill_to_contact
        if clearing_existing_invoice_group_number is not None:
            self.clearing_existing_invoice_group_number = clearing_existing_invoice_group_number
        if clearing_existing_invoice_template is not None:
            self.clearing_existing_invoice_template = clearing_existing_invoice_template
        if clearing_existing_payment_term is not None:
            self.clearing_existing_payment_term = clearing_existing_payment_term
        if clearing_existing_sequence_set is not None:
            self.clearing_existing_sequence_set = clearing_existing_sequence_set
        if clearing_existing_sold_to_contact is not None:
            self.clearing_existing_sold_to_contact = clearing_existing_sold_to_contact
        if destination_account_number is not None:
            self.destination_account_number = destination_account_number
        if destination_invoice_account_number is not None:
            self.destination_invoice_account_number = destination_invoice_account_number
        if invoice_group_number is not None:
            self.invoice_group_number = invoice_group_number
        if invoice_template_id is not None:
            self.invoice_template_id = invoice_template_id
        if payment_term is not None:
            self.payment_term = payment_term
        if sequence_set_id is not None:
            self.sequence_set_id = sequence_set_id
        if sold_to_contact_id is not None:
            self.sold_to_contact_id = sold_to_contact_id

    @property
    def bill_to_contact_id(self):
        """Gets the bill_to_contact_id of this OrderActionOwnerTransfer.  # noqa: E501

        The contact id of the bill to contact that the subscription is being transferred to.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Contact from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :return: The bill_to_contact_id of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: str
        """
        return self._bill_to_contact_id

    @bill_to_contact_id.setter
    def bill_to_contact_id(self, bill_to_contact_id):
        """Sets the bill_to_contact_id of this OrderActionOwnerTransfer.

        The contact id of the bill to contact that the subscription is being transferred to.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Contact from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :param bill_to_contact_id: The bill_to_contact_id of this OrderActionOwnerTransfer.  # noqa: E501
        :type: str
        """

        self._bill_to_contact_id = bill_to_contact_id

    @property
    def clearing_existing_bill_to_contact(self):
        """Gets the clearing_existing_bill_to_contact of this OrderActionOwnerTransfer.  # noqa: E501

        Whether to clear the existing bill-to contact ID at the subscription level. This field is mutually exclusive with the `billToContactId` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :return: The clearing_existing_bill_to_contact of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._clearing_existing_bill_to_contact

    @clearing_existing_bill_to_contact.setter
    def clearing_existing_bill_to_contact(self, clearing_existing_bill_to_contact):
        """Sets the clearing_existing_bill_to_contact of this OrderActionOwnerTransfer.

        Whether to clear the existing bill-to contact ID at the subscription level. This field is mutually exclusive with the `billToContactId` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :param clearing_existing_bill_to_contact: The clearing_existing_bill_to_contact of this OrderActionOwnerTransfer.  # noqa: E501
        :type: bool
        """

        self._clearing_existing_bill_to_contact = clearing_existing_bill_to_contact

    @property
    def clearing_existing_invoice_group_number(self):
        """Gets the clearing_existing_invoice_group_number of this OrderActionOwnerTransfer.  # noqa: E501

        Whether to clear the existing invoice group number at the subscription level. This field is mutually exclusive with the `invoiceGroupNumber` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :return: The clearing_existing_invoice_group_number of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._clearing_existing_invoice_group_number

    @clearing_existing_invoice_group_number.setter
    def clearing_existing_invoice_group_number(self, clearing_existing_invoice_group_number):
        """Sets the clearing_existing_invoice_group_number of this OrderActionOwnerTransfer.

        Whether to clear the existing invoice group number at the subscription level. This field is mutually exclusive with the `invoiceGroupNumber` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :param clearing_existing_invoice_group_number: The clearing_existing_invoice_group_number of this OrderActionOwnerTransfer.  # noqa: E501
        :type: bool
        """

        self._clearing_existing_invoice_group_number = clearing_existing_invoice_group_number

    @property
    def clearing_existing_invoice_template(self):
        """Gets the clearing_existing_invoice_template of this OrderActionOwnerTransfer.  # noqa: E501

        Whether to clear the existing invoice template ID at the subscription level. This field is mutually exclusive with the `invoiceTemplateId` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :return: The clearing_existing_invoice_template of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._clearing_existing_invoice_template

    @clearing_existing_invoice_template.setter
    def clearing_existing_invoice_template(self, clearing_existing_invoice_template):
        """Sets the clearing_existing_invoice_template of this OrderActionOwnerTransfer.

        Whether to clear the existing invoice template ID at the subscription level. This field is mutually exclusive with the `invoiceTemplateId` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :param clearing_existing_invoice_template: The clearing_existing_invoice_template of this OrderActionOwnerTransfer.  # noqa: E501
        :type: bool
        """

        self._clearing_existing_invoice_template = clearing_existing_invoice_template

    @property
    def clearing_existing_payment_term(self):
        """Gets the clearing_existing_payment_term of this OrderActionOwnerTransfer.  # noqa: E501

        Whether to clear the existing payment term at the subscription level. This field is mutually exclusive with the `paymentTerm` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :return: The clearing_existing_payment_term of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._clearing_existing_payment_term

    @clearing_existing_payment_term.setter
    def clearing_existing_payment_term(self, clearing_existing_payment_term):
        """Sets the clearing_existing_payment_term of this OrderActionOwnerTransfer.

        Whether to clear the existing payment term at the subscription level. This field is mutually exclusive with the `paymentTerm` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :param clearing_existing_payment_term: The clearing_existing_payment_term of this OrderActionOwnerTransfer.  # noqa: E501
        :type: bool
        """

        self._clearing_existing_payment_term = clearing_existing_payment_term

    @property
    def clearing_existing_sequence_set(self):
        """Gets the clearing_existing_sequence_set of this OrderActionOwnerTransfer.  # noqa: E501

        Whether to clear the existing sequence set ID at the subscription level. This field is mutually exclusive with the `sequenceSetId` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :return: The clearing_existing_sequence_set of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._clearing_existing_sequence_set

    @clearing_existing_sequence_set.setter
    def clearing_existing_sequence_set(self, clearing_existing_sequence_set):
        """Sets the clearing_existing_sequence_set of this OrderActionOwnerTransfer.

        Whether to clear the existing sequence set ID at the subscription level. This field is mutually exclusive with the `sequenceSetId` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :param clearing_existing_sequence_set: The clearing_existing_sequence_set of this OrderActionOwnerTransfer.  # noqa: E501
        :type: bool
        """

        self._clearing_existing_sequence_set = clearing_existing_sequence_set

    @property
    def clearing_existing_sold_to_contact(self):
        """Gets the clearing_existing_sold_to_contact of this OrderActionOwnerTransfer.  # noqa: E501

        Whether to clear the existing sold-to contact ID at the subscription level. This field is mutually exclusive with the `soldToContactId` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :return: The clearing_existing_sold_to_contact of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._clearing_existing_sold_to_contact

    @clearing_existing_sold_to_contact.setter
    def clearing_existing_sold_to_contact(self, clearing_existing_sold_to_contact):
        """Sets the clearing_existing_sold_to_contact of this OrderActionOwnerTransfer.

        Whether to clear the existing sold-to contact ID at the subscription level. This field is mutually exclusive with the `soldToContactId` field.  **Note**: If you have the [Flexible Billing Attributes](https://knowledgecenter.zuora.com/Billing/Subscriptions/Flexible_Billing_Attributes) feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.   # noqa: E501

        :param clearing_existing_sold_to_contact: The clearing_existing_sold_to_contact of this OrderActionOwnerTransfer.  # noqa: E501
        :type: bool
        """

        self._clearing_existing_sold_to_contact = clearing_existing_sold_to_contact

    @property
    def destination_account_number(self):
        """Gets the destination_account_number of this OrderActionOwnerTransfer.  # noqa: E501

        The account number of the account that the subscription is being transferred to.   # noqa: E501

        :return: The destination_account_number of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: str
        """
        return self._destination_account_number

    @destination_account_number.setter
    def destination_account_number(self, destination_account_number):
        """Sets the destination_account_number of this OrderActionOwnerTransfer.

        The account number of the account that the subscription is being transferred to.   # noqa: E501

        :param destination_account_number: The destination_account_number of this OrderActionOwnerTransfer.  # noqa: E501
        :type: str
        """

        self._destination_account_number = destination_account_number

    @property
    def destination_invoice_account_number(self):
        """Gets the destination_invoice_account_number of this OrderActionOwnerTransfer.  # noqa: E501

        The account number of the invoice owner account that the subscription is being transferred to.   # noqa: E501

        :return: The destination_invoice_account_number of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: str
        """
        return self._destination_invoice_account_number

    @destination_invoice_account_number.setter
    def destination_invoice_account_number(self, destination_invoice_account_number):
        """Sets the destination_invoice_account_number of this OrderActionOwnerTransfer.

        The account number of the invoice owner account that the subscription is being transferred to.   # noqa: E501

        :param destination_invoice_account_number: The destination_invoice_account_number of this OrderActionOwnerTransfer.  # noqa: E501
        :type: str
        """

        self._destination_invoice_account_number = destination_invoice_account_number

    @property
    def invoice_group_number(self):
        """Gets the invoice_group_number of this OrderActionOwnerTransfer.  # noqa: E501

        The number of invoice group associated with the subscription.  **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature enabled.   # noqa: E501

        :return: The invoice_group_number of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: str
        """
        return self._invoice_group_number

    @invoice_group_number.setter
    def invoice_group_number(self, invoice_group_number):
        """Sets the invoice_group_number of this OrderActionOwnerTransfer.

        The number of invoice group associated with the subscription.  **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature enabled.   # noqa: E501

        :param invoice_group_number: The invoice_group_number of this OrderActionOwnerTransfer.  # noqa: E501
        :type: str
        """

        self._invoice_group_number = invoice_group_number

    @property
    def invoice_template_id(self):
        """Gets the invoice_template_id of this OrderActionOwnerTransfer.  # noqa: E501

        The ID of the invoice template associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Template from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :return: The invoice_template_id of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: str
        """
        return self._invoice_template_id

    @invoice_template_id.setter
    def invoice_template_id(self, invoice_template_id):
        """Sets the invoice_template_id of this OrderActionOwnerTransfer.

        The ID of the invoice template associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Template from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :param invoice_template_id: The invoice_template_id of this OrderActionOwnerTransfer.  # noqa: E501
        :type: str
        """

        self._invoice_template_id = invoice_template_id

    @property
    def payment_term(self):
        """Gets the payment_term of this OrderActionOwnerTransfer.  # noqa: E501

        Name of the payment term associated with the account. For example, \"Net 30\". The payment term determines the due dates of invoices.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Term from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :return: The payment_term of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: str
        """
        return self._payment_term

    @payment_term.setter
    def payment_term(self, payment_term):
        """Sets the payment_term of this OrderActionOwnerTransfer.

        Name of the payment term associated with the account. For example, \"Net 30\". The payment term determines the due dates of invoices.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Term from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :param payment_term: The payment_term of this OrderActionOwnerTransfer.  # noqa: E501
        :type: str
        """

        self._payment_term = payment_term

    @property
    def sequence_set_id(self):
        """Gets the sequence_set_id of this OrderActionOwnerTransfer.  # noqa: E501

        The ID of the sequence set associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Set from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :return: The sequence_set_id of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: str
        """
        return self._sequence_set_id

    @sequence_set_id.setter
    def sequence_set_id(self, sequence_set_id):
        """Sets the sequence_set_id of this OrderActionOwnerTransfer.

        The ID of the sequence set associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Set from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :param sequence_set_id: The sequence_set_id of this OrderActionOwnerTransfer.  # noqa: E501
        :type: str
        """

        self._sequence_set_id = sequence_set_id

    @property
    def sold_to_contact_id(self):
        """Gets the sold_to_contact_id of this OrderActionOwnerTransfer.  # noqa: E501

        The ID of the sold-to contact associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Contact from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :return: The sold_to_contact_id of this OrderActionOwnerTransfer.  # noqa: E501
        :rtype: str
        """
        return self._sold_to_contact_id

    @sold_to_contact_id.setter
    def sold_to_contact_id(self, sold_to_contact_id):
        """Sets the sold_to_contact_id of this OrderActionOwnerTransfer.

        The ID of the sold-to contact associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Contact from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :param sold_to_contact_id: The sold_to_contact_id of this OrderActionOwnerTransfer.  # noqa: E501
        :type: str
        """

        self._sold_to_contact_id = sold_to_contact_id

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
        if issubclass(OrderActionOwnerTransfer, dict):
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
        if not isinstance(other, OrderActionOwnerTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
