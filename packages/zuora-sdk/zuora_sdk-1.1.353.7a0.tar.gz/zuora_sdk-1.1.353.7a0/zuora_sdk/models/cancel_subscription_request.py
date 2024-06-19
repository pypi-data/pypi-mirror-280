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

class CancelSubscriptionRequest(object):
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
        'booking_date': 'date',
        'cancellation_effective_date': 'date',
        'cancellation_policy': 'str',
        'collect': 'bool',
        'contract_effective_date': 'date',
        'credit_memo_reason_code': 'str',
        'document_date': 'date',
        'invoice': 'bool',
        'invoice_collect': 'bool',
        'invoice_target_date': 'date',
        'order_date': 'date',
        'run_billing': 'bool',
        'target_date': 'date'
    }

    attribute_map = {
        'application_order': 'applicationOrder',
        'apply_credit': 'applyCredit',
        'apply_credit_balance': 'applyCreditBalance',
        'booking_date': 'bookingDate',
        'cancellation_effective_date': 'cancellationEffectiveDate',
        'cancellation_policy': 'cancellationPolicy',
        'collect': 'collect',
        'contract_effective_date': 'contractEffectiveDate',
        'credit_memo_reason_code': 'creditMemoReasonCode',
        'document_date': 'documentDate',
        'invoice': 'invoice',
        'invoice_collect': 'invoiceCollect',
        'invoice_target_date': 'invoiceTargetDate',
        'order_date': 'orderDate',
        'run_billing': 'runBilling',
        'target_date': 'targetDate'
    }

    def __init__(self, application_order=None, apply_credit=None, apply_credit_balance=None, booking_date=None, cancellation_effective_date=None, cancellation_policy=None, collect=None, contract_effective_date=None, credit_memo_reason_code=None, document_date=None, invoice=None, invoice_collect=None, invoice_target_date=None, order_date=None, run_billing=None, target_date=None):  # noqa: E501
        """CancelSubscriptionRequest - a model defined in Swagger"""  # noqa: E501
        self._application_order = None
        self._apply_credit = None
        self._apply_credit_balance = None
        self._booking_date = None
        self._cancellation_effective_date = None
        self._cancellation_policy = None
        self._collect = None
        self._contract_effective_date = None
        self._credit_memo_reason_code = None
        self._document_date = None
        self._invoice = None
        self._invoice_collect = None
        self._invoice_target_date = None
        self._order_date = None
        self._run_billing = None
        self._target_date = None
        self.discriminator = None
        if application_order is not None:
            self.application_order = application_order
        if apply_credit is not None:
            self.apply_credit = apply_credit
        if apply_credit_balance is not None:
            self.apply_credit_balance = apply_credit_balance
        if booking_date is not None:
            self.booking_date = booking_date
        if cancellation_effective_date is not None:
            self.cancellation_effective_date = cancellation_effective_date
        self.cancellation_policy = cancellation_policy
        if collect is not None:
            self.collect = collect
        if contract_effective_date is not None:
            self.contract_effective_date = contract_effective_date
        if credit_memo_reason_code is not None:
            self.credit_memo_reason_code = credit_memo_reason_code
        if document_date is not None:
            self.document_date = document_date
        if invoice is not None:
            self.invoice = invoice
        if invoice_collect is not None:
            self.invoice_collect = invoice_collect
        if invoice_target_date is not None:
            self.invoice_target_date = invoice_target_date
        if order_date is not None:
            self.order_date = order_date
        if run_billing is not None:
            self.run_billing = run_billing
        if target_date is not None:
            self.target_date = target_date

    @property
    def application_order(self):
        """Gets the application_order of this CancelSubscriptionRequest.  # noqa: E501

        The priority order to apply credit memos and/or unapplied payments to an invoice. Possible item values are: `CreditMemo`, `UnappliedPayment`.  **Note:**   - This field is valid only if the `applyCredit` field is set to `true`.   - If no value is specified for this field, the default priority order is used, [\"CreditMemo\", \"UnappliedPayment\"], to apply credit memos first and then apply unapplied payments.   - If only one item is specified, only the items of the spedified type are applied to invoices. For example, if the value is `[\"CreditMemo\"]`, only credit memos are used to apply to invoices.   # noqa: E501

        :return: The application_order of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._application_order

    @application_order.setter
    def application_order(self, application_order):
        """Sets the application_order of this CancelSubscriptionRequest.

        The priority order to apply credit memos and/or unapplied payments to an invoice. Possible item values are: `CreditMemo`, `UnappliedPayment`.  **Note:**   - This field is valid only if the `applyCredit` field is set to `true`.   - If no value is specified for this field, the default priority order is used, [\"CreditMemo\", \"UnappliedPayment\"], to apply credit memos first and then apply unapplied payments.   - If only one item is specified, only the items of the spedified type are applied to invoices. For example, if the value is `[\"CreditMemo\"]`, only credit memos are used to apply to invoices.   # noqa: E501

        :param application_order: The application_order of this CancelSubscriptionRequest.  # noqa: E501
        :type: list[str]
        """

        self._application_order = application_order

    @property
    def apply_credit(self):
        """Gets the apply_credit of this CancelSubscriptionRequest.  # noqa: E501

        If the value is true, the credit memo or unapplied payment on the order account will be automatically applied to the invoices generated by this order. The credit memo generated by this order will not be automatically applied to any invoices.  **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :return: The apply_credit of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._apply_credit

    @apply_credit.setter
    def apply_credit(self, apply_credit):
        """Sets the apply_credit of this CancelSubscriptionRequest.

        If the value is true, the credit memo or unapplied payment on the order account will be automatically applied to the invoices generated by this order. The credit memo generated by this order will not be automatically applied to any invoices.  **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :param apply_credit: The apply_credit of this CancelSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._apply_credit = apply_credit

    @property
    def apply_credit_balance(self):
        """Gets the apply_credit_balance of this CancelSubscriptionRequest.  # noqa: E501

        Whether to automatically apply a credit balance to an invoice.  If the value is `true`, the credit balance is applied to the invoice. If the value is `false`, no action is taken.   To view the credit balance adjustment, retrieve the details of the invoice using the Get Invoices method.  Prerequisite: `invoice` must be `true`.   **Note:**    - If you are using the field `invoiceCollect` rather than the field `invoice`, the `invoiceCollect` value must be `true`.   - This field is deprecated if you have the Invoice Settlement feature enabled.   # noqa: E501

        :return: The apply_credit_balance of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._apply_credit_balance

    @apply_credit_balance.setter
    def apply_credit_balance(self, apply_credit_balance):
        """Sets the apply_credit_balance of this CancelSubscriptionRequest.

        Whether to automatically apply a credit balance to an invoice.  If the value is `true`, the credit balance is applied to the invoice. If the value is `false`, no action is taken.   To view the credit balance adjustment, retrieve the details of the invoice using the Get Invoices method.  Prerequisite: `invoice` must be `true`.   **Note:**    - If you are using the field `invoiceCollect` rather than the field `invoice`, the `invoiceCollect` value must be `true`.   - This field is deprecated if you have the Invoice Settlement feature enabled.   # noqa: E501

        :param apply_credit_balance: The apply_credit_balance of this CancelSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._apply_credit_balance = apply_credit_balance

    @property
    def booking_date(self):
        """Gets the booking_date of this CancelSubscriptionRequest.  # noqa: E501

        The booking date that you want to set for the amendment contract when you cancel the subscription. The default value is the current date when you make the API call.   # noqa: E501

        :return: The booking_date of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: date
        """
        return self._booking_date

    @booking_date.setter
    def booking_date(self, booking_date):
        """Sets the booking_date of this CancelSubscriptionRequest.

        The booking date that you want to set for the amendment contract when you cancel the subscription. The default value is the current date when you make the API call.   # noqa: E501

        :param booking_date: The booking_date of this CancelSubscriptionRequest.  # noqa: E501
        :type: date
        """

        self._booking_date = booking_date

    @property
    def cancellation_effective_date(self):
        """Gets the cancellation_effective_date of this CancelSubscriptionRequest.  # noqa: E501

        Date the cancellation takes effect, in the format yyyy-mm-dd.  Use only if `cancellationPolicy` is `SpecificDate`. Should not be earlier than the subscription contract-effective date, later than the subscription term-end date, or within a period for which the customer has been invoiced.   # noqa: E501

        :return: The cancellation_effective_date of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: date
        """
        return self._cancellation_effective_date

    @cancellation_effective_date.setter
    def cancellation_effective_date(self, cancellation_effective_date):
        """Sets the cancellation_effective_date of this CancelSubscriptionRequest.

        Date the cancellation takes effect, in the format yyyy-mm-dd.  Use only if `cancellationPolicy` is `SpecificDate`. Should not be earlier than the subscription contract-effective date, later than the subscription term-end date, or within a period for which the customer has been invoiced.   # noqa: E501

        :param cancellation_effective_date: The cancellation_effective_date of this CancelSubscriptionRequest.  # noqa: E501
        :type: date
        """

        self._cancellation_effective_date = cancellation_effective_date

    @property
    def cancellation_policy(self):
        """Gets the cancellation_policy of this CancelSubscriptionRequest.  # noqa: E501

        Cancellation method. Possible values are: `EndOfCurrentTerm`, `EndOfLastInvoicePeriod`, `SpecificDate`. If using `SpecificDate`, the `cancellationEffectiveDate` field is required.   # noqa: E501

        :return: The cancellation_policy of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._cancellation_policy

    @cancellation_policy.setter
    def cancellation_policy(self, cancellation_policy):
        """Sets the cancellation_policy of this CancelSubscriptionRequest.

        Cancellation method. Possible values are: `EndOfCurrentTerm`, `EndOfLastInvoicePeriod`, `SpecificDate`. If using `SpecificDate`, the `cancellationEffectiveDate` field is required.   # noqa: E501

        :param cancellation_policy: The cancellation_policy of this CancelSubscriptionRequest.  # noqa: E501
        :type: str
        """
        if cancellation_policy is None:
            raise ValueError("Invalid value for `cancellation_policy`, must not be `None`")  # noqa: E501

        self._cancellation_policy = cancellation_policy

    @property
    def collect(self):
        """Gets the collect of this CancelSubscriptionRequest.  # noqa: E501

        Collects an automatic payment for a subscription. The collection generated in this operation is only for this subscription, not for the entire customer account.  If the value is `true`, the automatic payment is collected. If the value is `false`, no action is taken.  Prerequisite: The `invoice` or `runBilling` field must be `true`.   **Note**: This field is only available if you set the `zuora-version` request header to `196.0` or later.   # noqa: E501

        :return: The collect of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._collect

    @collect.setter
    def collect(self, collect):
        """Sets the collect of this CancelSubscriptionRequest.

        Collects an automatic payment for a subscription. The collection generated in this operation is only for this subscription, not for the entire customer account.  If the value is `true`, the automatic payment is collected. If the value is `false`, no action is taken.  Prerequisite: The `invoice` or `runBilling` field must be `true`.   **Note**: This field is only available if you set the `zuora-version` request header to `196.0` or later.   # noqa: E501

        :param collect: The collect of this CancelSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._collect = collect

    @property
    def contract_effective_date(self):
        """Gets the contract_effective_date of this CancelSubscriptionRequest.  # noqa: E501

        The date when the customer notifies you that they want to cancel their subscription.   # noqa: E501

        :return: The contract_effective_date of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: date
        """
        return self._contract_effective_date

    @contract_effective_date.setter
    def contract_effective_date(self, contract_effective_date):
        """Sets the contract_effective_date of this CancelSubscriptionRequest.

        The date when the customer notifies you that they want to cancel their subscription.   # noqa: E501

        :param contract_effective_date: The contract_effective_date of this CancelSubscriptionRequest.  # noqa: E501
        :type: date
        """

        self._contract_effective_date = contract_effective_date

    @property
    def credit_memo_reason_code(self):
        """Gets the credit_memo_reason_code of this CancelSubscriptionRequest.  # noqa: E501

        A code identifying the reason for the credit memo transaction that is generated by the request. The value must be an existing reason code. If you do not pass the field or pass the field with empty value, Zuora uses the default reason code.  # noqa: E501

        :return: The credit_memo_reason_code of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_reason_code

    @credit_memo_reason_code.setter
    def credit_memo_reason_code(self, credit_memo_reason_code):
        """Sets the credit_memo_reason_code of this CancelSubscriptionRequest.

        A code identifying the reason for the credit memo transaction that is generated by the request. The value must be an existing reason code. If you do not pass the field or pass the field with empty value, Zuora uses the default reason code.  # noqa: E501

        :param credit_memo_reason_code: The credit_memo_reason_code of this CancelSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._credit_memo_reason_code = credit_memo_reason_code

    @property
    def document_date(self):
        """Gets the document_date of this CancelSubscriptionRequest.  # noqa: E501

        The date of the billing document, in `yyyy-mm-dd` format. It represents the invoice date for invoices, credit memo date for credit memos, and debit memo date for debit memos.  - If this field is specified, the specified date is used as the billing document date.  - If this field is not specified, the date specified in the `targetDate` is used as the billing document date.   # noqa: E501

        :return: The document_date of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: date
        """
        return self._document_date

    @document_date.setter
    def document_date(self, document_date):
        """Sets the document_date of this CancelSubscriptionRequest.

        The date of the billing document, in `yyyy-mm-dd` format. It represents the invoice date for invoices, credit memo date for credit memos, and debit memo date for debit memos.  - If this field is specified, the specified date is used as the billing document date.  - If this field is not specified, the date specified in the `targetDate` is used as the billing document date.   # noqa: E501

        :param document_date: The document_date of this CancelSubscriptionRequest.  # noqa: E501
        :type: date
        """

        self._document_date = document_date

    @property
    def invoice(self):
        """Gets the invoice of this CancelSubscriptionRequest.  # noqa: E501

        **Note:** This field has been replaced by the `runBilling` field. The `invoice` field is only available for backward compatibility.   Creates an invoice for a subscription. The invoice generated in this operation is only for this subscription, not for the entire customer account.   If the value is `true`, an invoice is created. If the value is `false`, no action is taken. The default value is `false`.    This field is in Zuora REST API version control. Supported minor versions are `196.0` and `207.0`. To use this field in the method, you must set the zuora-version parameter to the minor version number in the request header.   # noqa: E501

        :return: The invoice of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this CancelSubscriptionRequest.

        **Note:** This field has been replaced by the `runBilling` field. The `invoice` field is only available for backward compatibility.   Creates an invoice for a subscription. The invoice generated in this operation is only for this subscription, not for the entire customer account.   If the value is `true`, an invoice is created. If the value is `false`, no action is taken. The default value is `false`.    This field is in Zuora REST API version control. Supported minor versions are `196.0` and `207.0`. To use this field in the method, you must set the zuora-version parameter to the minor version number in the request header.   # noqa: E501

        :param invoice: The invoice of this CancelSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._invoice = invoice

    @property
    def invoice_collect(self):
        """Gets the invoice_collect of this CancelSubscriptionRequest.  # noqa: E501

        This field has been replaced by the `invoice` field and the `collect` field. `invoiceCollect` is available only for backward compatibility.  If this field is set to `true`, an invoice is generated and payment automatically collected.  **Note**: This field is only available if you set the `zuora-version` request header to `186.0`, `187.0`, `188.0`, or `189.0`.   # noqa: E501

        :return: The invoice_collect of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_collect

    @invoice_collect.setter
    def invoice_collect(self, invoice_collect):
        """Sets the invoice_collect of this CancelSubscriptionRequest.

        This field has been replaced by the `invoice` field and the `collect` field. `invoiceCollect` is available only for backward compatibility.  If this field is set to `true`, an invoice is generated and payment automatically collected.  **Note**: This field is only available if you set the `zuora-version` request header to `186.0`, `187.0`, `188.0`, or `189.0`.   # noqa: E501

        :param invoice_collect: The invoice_collect of this CancelSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._invoice_collect = invoice_collect

    @property
    def invoice_target_date(self):
        """Gets the invoice_target_date of this CancelSubscriptionRequest.  # noqa: E501

        **Note:** This field has been replaced by the `targetDate` field. The `invoiceTargetDate` field is only available for backward compatibility.   Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.   This field is in Zuora REST API version control. Supported minor versions are `207.0` and earlier.   # noqa: E501

        :return: The invoice_target_date of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: date
        """
        return self._invoice_target_date

    @invoice_target_date.setter
    def invoice_target_date(self, invoice_target_date):
        """Sets the invoice_target_date of this CancelSubscriptionRequest.

        **Note:** This field has been replaced by the `targetDate` field. The `invoiceTargetDate` field is only available for backward compatibility.   Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.   This field is in Zuora REST API version control. Supported minor versions are `207.0` and earlier.   # noqa: E501

        :param invoice_target_date: The invoice_target_date of this CancelSubscriptionRequest.  # noqa: E501
        :type: date
        """

        self._invoice_target_date = invoice_target_date

    @property
    def order_date(self):
        """Gets the order_date of this CancelSubscriptionRequest.  # noqa: E501

        The date when the order is signed. If no additinal contractEffectiveDate is provided, this order will use this order date as the contract effective date. This field must be in the `yyyy-mm-dd` format. This field is required for Orders customers only, not applicable to Orders Harmonization customers.    # noqa: E501

        :return: The order_date of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: date
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this CancelSubscriptionRequest.

        The date when the order is signed. If no additinal contractEffectiveDate is provided, this order will use this order date as the contract effective date. This field must be in the `yyyy-mm-dd` format. This field is required for Orders customers only, not applicable to Orders Harmonization customers.    # noqa: E501

        :param order_date: The order_date of this CancelSubscriptionRequest.  # noqa: E501
        :type: date
        """

        self._order_date = order_date

    @property
    def run_billing(self):
        """Gets the run_billing of this CancelSubscriptionRequest.  # noqa: E501

        Creates an invoice for a subscription. If you have the Invoice Settlement feature enabled, a credit memo might also be created based on the [invoice and credit memo generation rule](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/Credit_and_Debit_Memos/Rules_for_Generating_Invoices_and_Credit_Memos).     The billing documents generated in this operation is only for this subscription, not for the entire customer account.   Possible values:  - `true`: An invoice is created. If you have the Invoice Settlement feature enabled, a credit memo might also be created.   - `false`: No invoice is created.   **Note:** This field is in Zuora REST API version control. Supported minor versions are `211.0` or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :return: The run_billing of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._run_billing

    @run_billing.setter
    def run_billing(self, run_billing):
        """Sets the run_billing of this CancelSubscriptionRequest.

        Creates an invoice for a subscription. If you have the Invoice Settlement feature enabled, a credit memo might also be created based on the [invoice and credit memo generation rule](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/Credit_and_Debit_Memos/Rules_for_Generating_Invoices_and_Credit_Memos).     The billing documents generated in this operation is only for this subscription, not for the entire customer account.   Possible values:  - `true`: An invoice is created. If you have the Invoice Settlement feature enabled, a credit memo might also be created.   - `false`: No invoice is created.   **Note:** This field is in Zuora REST API version control. Supported minor versions are `211.0` or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :param run_billing: The run_billing of this CancelSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._run_billing = run_billing

    @property
    def target_date(self):
        """Gets the target_date of this CancelSubscriptionRequest.  # noqa: E501

        Date through which to calculate charges if an invoice or a credit memo is generated, as yyyy-mm-dd. Default is current date.   **Note:** The credit memo is only available if you have the Invoice Settlement feature enabled.   This field is in Zuora REST API version control. Supported minor versions are `211.0` and later. To use this field in the method, you must set the  `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :return: The target_date of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this CancelSubscriptionRequest.

        Date through which to calculate charges if an invoice or a credit memo is generated, as yyyy-mm-dd. Default is current date.   **Note:** The credit memo is only available if you have the Invoice Settlement feature enabled.   This field is in Zuora REST API version control. Supported minor versions are `211.0` and later. To use this field in the method, you must set the  `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :param target_date: The target_date of this CancelSubscriptionRequest.  # noqa: E501
        :type: date
        """

        self._target_date = target_date

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
        if issubclass(CancelSubscriptionRequest, dict):
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
        if not isinstance(other, CancelSubscriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
