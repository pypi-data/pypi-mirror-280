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

class ProcessingOptionsWithDelayedCapturePayment(object):
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
        'application_order': 'list[str]',
        'apply_credit': 'bool',
        'apply_credit_balance': 'bool',
        'billing_options': 'BillingOptions',
        'collect_payment': 'bool',
        'electronic_payment_options': 'ElectronicPaymentOptionsWithDelayedCapturePayment',
        'refund': 'bool',
        'refund_amount': 'float',
        'refund_reason_code': 'str',
        'run_billing': 'bool',
        'write_off': 'bool',
        'write_off_behavior': 'WriteOffBehavior'
    }

    attribute_map = {
        'application_order': 'applicationOrder',
        'apply_credit': 'applyCredit',
        'apply_credit_balance': 'applyCreditBalance',
        'billing_options': 'billingOptions',
        'collect_payment': 'collectPayment',
        'electronic_payment_options': 'electronicPaymentOptions',
        'refund': 'refund',
        'refund_amount': 'refundAmount',
        'refund_reason_code': 'refundReasonCode',
        'run_billing': 'runBilling',
        'write_off': 'writeOff',
        'write_off_behavior': 'writeOffBehavior'
    }

    def __init__(self, application_order=None, apply_credit=None, apply_credit_balance=None, billing_options=None, collect_payment=None, electronic_payment_options=None, refund=None, refund_amount=None, refund_reason_code=None, run_billing=None, write_off=None, write_off_behavior=None):  # noqa: E501
        """ProcessingOptionsWithDelayedCapturePayment - a model defined in Swagger"""  # noqa: E501
        self._application_order = None
        self._apply_credit = None
        self._apply_credit_balance = None
        self._billing_options = None
        self._collect_payment = None
        self._electronic_payment_options = None
        self._refund = None
        self._refund_amount = None
        self._refund_reason_code = None
        self._run_billing = None
        self._write_off = None
        self._write_off_behavior = None
        self.discriminator = None
        if application_order is not None:
            self.application_order = application_order
        if apply_credit is not None:
            self.apply_credit = apply_credit
        if apply_credit_balance is not None:
            self.apply_credit_balance = apply_credit_balance
        if billing_options is not None:
            self.billing_options = billing_options
        if collect_payment is not None:
            self.collect_payment = collect_payment
        if electronic_payment_options is not None:
            self.electronic_payment_options = electronic_payment_options
        if refund is not None:
            self.refund = refund
        if refund_amount is not None:
            self.refund_amount = refund_amount
        if refund_reason_code is not None:
            self.refund_reason_code = refund_reason_code
        if run_billing is not None:
            self.run_billing = run_billing
        if write_off is not None:
            self.write_off = write_off
        if write_off_behavior is not None:
            self.write_off_behavior = write_off_behavior

    @property
    def application_order(self):
        """Gets the application_order of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501

        The priority order to apply credit memos and/or unapplied payments to an invoice. Possible item values are: `CreditMemo`, `UnappliedPayment`.  **Note:**   - This field is valid only if the `applyCredit` field is set to `true`.   - If no value is specified for this field, the default priority order is used, [\"CreditMemo\", \"UnappliedPayment\"], to apply credit memos first and then apply unapplied payments.   - If only one item is specified, only the items of the spedified type are applied to invoices. For example, if the value is `[\"CreditMemo\"]`, only credit memos are used to apply to invoices.   # noqa: E501

        :return: The application_order of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: list[str]
        """
        return self._application_order

    @application_order.setter
    def application_order(self, application_order):
        """Sets the application_order of this ProcessingOptionsWithDelayedCapturePayment.

        The priority order to apply credit memos and/or unapplied payments to an invoice. Possible item values are: `CreditMemo`, `UnappliedPayment`.  **Note:**   - This field is valid only if the `applyCredit` field is set to `true`.   - If no value is specified for this field, the default priority order is used, [\"CreditMemo\", \"UnappliedPayment\"], to apply credit memos first and then apply unapplied payments.   - If only one item is specified, only the items of the spedified type are applied to invoices. For example, if the value is `[\"CreditMemo\"]`, only credit memos are used to apply to invoices.   # noqa: E501

        :param application_order: The application_order of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: list[str]
        """

        self._application_order = application_order

    @property
    def apply_credit(self):
        """Gets the apply_credit of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501

        Whether to automatically apply credit memos or unapplied payments, or both to an invoice.  If the value is true, the credit memo or unapplied payment on the order account will be automatically applied to the invoices generated by this order. The credit memo generated by this order will not be automatically applied to any invoices.             **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :return: The apply_credit of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: bool
        """
        return self._apply_credit

    @apply_credit.setter
    def apply_credit(self, apply_credit):
        """Sets the apply_credit of this ProcessingOptionsWithDelayedCapturePayment.

        Whether to automatically apply credit memos or unapplied payments, or both to an invoice.  If the value is true, the credit memo or unapplied payment on the order account will be automatically applied to the invoices generated by this order. The credit memo generated by this order will not be automatically applied to any invoices.             **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :param apply_credit: The apply_credit of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: bool
        """

        self._apply_credit = apply_credit

    @property
    def apply_credit_balance(self):
        """Gets the apply_credit_balance of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501

        Indicates if any credit balance on a customer's account is automatically applied to invoices. If no value is specified then this field defaults to false. This feature is not available if you have enabled the Invoice Settlement feature.   # noqa: E501

        :return: The apply_credit_balance of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: bool
        """
        return self._apply_credit_balance

    @apply_credit_balance.setter
    def apply_credit_balance(self, apply_credit_balance):
        """Sets the apply_credit_balance of this ProcessingOptionsWithDelayedCapturePayment.

        Indicates if any credit balance on a customer's account is automatically applied to invoices. If no value is specified then this field defaults to false. This feature is not available if you have enabled the Invoice Settlement feature.   # noqa: E501

        :param apply_credit_balance: The apply_credit_balance of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: bool
        """

        self._apply_credit_balance = apply_credit_balance

    @property
    def billing_options(self):
        """Gets the billing_options of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501


        :return: The billing_options of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: BillingOptions
        """
        return self._billing_options

    @billing_options.setter
    def billing_options(self, billing_options):
        """Sets the billing_options of this ProcessingOptionsWithDelayedCapturePayment.


        :param billing_options: The billing_options of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: BillingOptions
        """

        self._billing_options = billing_options

    @property
    def collect_payment(self):
        """Gets the collect_payment of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501

        Indicates if the current request needs to collect payments. This value can not be 'true' when 'runBilling' flag is 'false'.   # noqa: E501

        :return: The collect_payment of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: bool
        """
        return self._collect_payment

    @collect_payment.setter
    def collect_payment(self, collect_payment):
        """Sets the collect_payment of this ProcessingOptionsWithDelayedCapturePayment.

        Indicates if the current request needs to collect payments. This value can not be 'true' when 'runBilling' flag is 'false'.   # noqa: E501

        :param collect_payment: The collect_payment of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: bool
        """

        self._collect_payment = collect_payment

    @property
    def electronic_payment_options(self):
        """Gets the electronic_payment_options of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501


        :return: The electronic_payment_options of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: ElectronicPaymentOptionsWithDelayedCapturePayment
        """
        return self._electronic_payment_options

    @electronic_payment_options.setter
    def electronic_payment_options(self, electronic_payment_options):
        """Sets the electronic_payment_options of this ProcessingOptionsWithDelayedCapturePayment.


        :param electronic_payment_options: The electronic_payment_options of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: ElectronicPaymentOptionsWithDelayedCapturePayment
        """

        self._electronic_payment_options = electronic_payment_options

    @property
    def refund(self):
        """Gets the refund of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501

        Indicates whether to refund after subscription cancelation. Default is `false`.   **Note**: When refunding a subscription that is not invoiced separately, if you do not enable the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Billing_and_Invoicing/Invoice_Settlement/C_Invoice_Item_Settlement\" target=\"_blank\">Invoice Item Settlement</a> feature, you will encounter the following error during the cancel and refund process: “Cancellation/Refund failed because of the following reason: Invoice is linked to multiple subscriptions. Cancellation was not processed.”   # noqa: E501

        :return: The refund of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: bool
        """
        return self._refund

    @refund.setter
    def refund(self, refund):
        """Sets the refund of this ProcessingOptionsWithDelayedCapturePayment.

        Indicates whether to refund after subscription cancelation. Default is `false`.   **Note**: When refunding a subscription that is not invoiced separately, if you do not enable the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Billing_and_Invoicing/Invoice_Settlement/C_Invoice_Item_Settlement\" target=\"_blank\">Invoice Item Settlement</a> feature, you will encounter the following error during the cancel and refund process: “Cancellation/Refund failed because of the following reason: Invoice is linked to multiple subscriptions. Cancellation was not processed.”   # noqa: E501

        :param refund: The refund of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: bool
        """

        self._refund = refund

    @property
    def refund_amount(self):
        """Gets the refund_amount of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501

        Indicates the amount to be refunded. Required if the `refund` field is `true`.   # noqa: E501

        :return: The refund_amount of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: float
        """
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        """Sets the refund_amount of this ProcessingOptionsWithDelayedCapturePayment.

        Indicates the amount to be refunded. Required if the `refund` field is `true`.   # noqa: E501

        :param refund_amount: The refund_amount of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: float
        """

        self._refund_amount = refund_amount

    @property
    def refund_reason_code(self):
        """Gets the refund_reason_code of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501

        A code identifying the reason for the refund transaction. The value must be an existing payment refund reason code listed in **Payments Settings** > **Configure Reason Codes**. If you do not specify the field or leave the field with an empty value, Zuora uses the default payment refund reason code.   # noqa: E501

        :return: The refund_reason_code of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: str
        """
        return self._refund_reason_code

    @refund_reason_code.setter
    def refund_reason_code(self, refund_reason_code):
        """Sets the refund_reason_code of this ProcessingOptionsWithDelayedCapturePayment.

        A code identifying the reason for the refund transaction. The value must be an existing payment refund reason code listed in **Payments Settings** > **Configure Reason Codes**. If you do not specify the field or leave the field with an empty value, Zuora uses the default payment refund reason code.   # noqa: E501

        :param refund_reason_code: The refund_reason_code of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: str
        """

        self._refund_reason_code = refund_reason_code

    @property
    def run_billing(self):
        """Gets the run_billing of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501

        Indicates if the current request needs to generate an invoice. The invoice will be generated against all subscriptions included in this order.   # noqa: E501

        :return: The run_billing of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: bool
        """
        return self._run_billing

    @run_billing.setter
    def run_billing(self, run_billing):
        """Sets the run_billing of this ProcessingOptionsWithDelayedCapturePayment.

        Indicates if the current request needs to generate an invoice. The invoice will be generated against all subscriptions included in this order.   # noqa: E501

        :param run_billing: The run_billing of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: bool
        """

        self._run_billing = run_billing

    @property
    def write_off(self):
        """Gets the write_off of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501

        Indicates whether to write off the outstanding balance on the invoice after refund. Default is `false`.  **Note**:  - When refunding a subscription that is not invoiced separately, if you do not enable the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Billing_and_Invoicing/Invoice_Settlement/C_Invoice_Item_Settlement\" target=\"_blank\">Invoice Item Settlement</a> feature, you will encounter the following error during the cancel and refund process: “Cancellation/Refund failed because of the following reason: Invoice is linked to multiple subscriptions. Cancellation was not processed.” - The <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Billing_and_Invoicing/Invoice_Settlement\" target=\"_blank\">Invoice Settlement</a> feature must have been enabled for write-off.   # noqa: E501

        :return: The write_off of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: bool
        """
        return self._write_off

    @write_off.setter
    def write_off(self, write_off):
        """Sets the write_off of this ProcessingOptionsWithDelayedCapturePayment.

        Indicates whether to write off the outstanding balance on the invoice after refund. Default is `false`.  **Note**:  - When refunding a subscription that is not invoiced separately, if you do not enable the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Billing_and_Invoicing/Invoice_Settlement/C_Invoice_Item_Settlement\" target=\"_blank\">Invoice Item Settlement</a> feature, you will encounter the following error during the cancel and refund process: “Cancellation/Refund failed because of the following reason: Invoice is linked to multiple subscriptions. Cancellation was not processed.” - The <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Billing_and_Invoicing/Invoice_Settlement\" target=\"_blank\">Invoice Settlement</a> feature must have been enabled for write-off.   # noqa: E501

        :param write_off: The write_off of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: bool
        """

        self._write_off = write_off

    @property
    def write_off_behavior(self):
        """Gets the write_off_behavior of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501


        :return: The write_off_behavior of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :rtype: WriteOffBehavior
        """
        return self._write_off_behavior

    @write_off_behavior.setter
    def write_off_behavior(self, write_off_behavior):
        """Sets the write_off_behavior of this ProcessingOptionsWithDelayedCapturePayment.


        :param write_off_behavior: The write_off_behavior of this ProcessingOptionsWithDelayedCapturePayment.  # noqa: E501
        :type: WriteOffBehavior
        """

        self._write_off_behavior = write_off_behavior

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
        if issubclass(ProcessingOptionsWithDelayedCapturePayment, dict):
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
        if not isinstance(other, ProcessingOptionsWithDelayedCapturePayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
