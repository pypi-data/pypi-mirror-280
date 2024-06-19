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

class CreateOrderCreateSubscription(object):
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
        'invoice_separately': 'bool',
        'invoice_template_id': 'str',
        'new_subscription_owner_account': 'CreateOrderSubscriptionOwnerAccount',
        'notes': 'str',
        'payment_term': 'str',
        'sequence_set_id': 'str',
        'sold_to_contact_id': 'str',
        'subscribe_to_products': 'list[CreateSubscribeToProduct]',
        'subscribe_to_rate_plans': 'list[CreateOrderRatePlanOverride]',
        'subscription_number': 'str',
        'subscription_owner_account_number': 'str',
        'terms': 'OrderActionCreateSubscriptionTerms',
        'currency': 'str',
        'invoice_group_number': 'str'
    }

    attribute_map = {
        'bill_to_contact_id': 'billToContactId',
        'invoice_separately': 'invoiceSeparately',
        'invoice_template_id': 'invoiceTemplateId',
        'new_subscription_owner_account': 'newSubscriptionOwnerAccount',
        'notes': 'notes',
        'payment_term': 'paymentTerm',
        'sequence_set_id': 'sequenceSetId',
        'sold_to_contact_id': 'soldToContactId',
        'subscribe_to_products': 'subscribeToProducts',
        'subscribe_to_rate_plans': 'subscribeToRatePlans',
        'subscription_number': 'subscriptionNumber',
        'subscription_owner_account_number': 'subscriptionOwnerAccountNumber',
        'terms': 'terms',
        'currency': 'currency',
        'invoice_group_number': 'invoiceGroupNumber'
    }

    def __init__(self, bill_to_contact_id=None, invoice_separately=None, invoice_template_id=None, new_subscription_owner_account=None, notes=None, payment_term=None, sequence_set_id=None, sold_to_contact_id=None, subscribe_to_products=None, subscribe_to_rate_plans=None, subscription_number=None, subscription_owner_account_number=None, terms=None, currency=None, invoice_group_number=None):  # noqa: E501
        """CreateOrderCreateSubscription - a model defined in Swagger"""  # noqa: E501
        self._bill_to_contact_id = None
        self._invoice_separately = None
        self._invoice_template_id = None
        self._new_subscription_owner_account = None
        self._notes = None
        self._payment_term = None
        self._sequence_set_id = None
        self._sold_to_contact_id = None
        self._subscribe_to_products = None
        self._subscribe_to_rate_plans = None
        self._subscription_number = None
        self._subscription_owner_account_number = None
        self._terms = None
        self._currency = None
        self._invoice_group_number = None
        self.discriminator = None
        if bill_to_contact_id is not None:
            self.bill_to_contact_id = bill_to_contact_id
        if invoice_separately is not None:
            self.invoice_separately = invoice_separately
        if invoice_template_id is not None:
            self.invoice_template_id = invoice_template_id
        if new_subscription_owner_account is not None:
            self.new_subscription_owner_account = new_subscription_owner_account
        if notes is not None:
            self.notes = notes
        if payment_term is not None:
            self.payment_term = payment_term
        if sequence_set_id is not None:
            self.sequence_set_id = sequence_set_id
        if sold_to_contact_id is not None:
            self.sold_to_contact_id = sold_to_contact_id
        if subscribe_to_products is not None:
            self.subscribe_to_products = subscribe_to_products
        if subscribe_to_rate_plans is not None:
            self.subscribe_to_rate_plans = subscribe_to_rate_plans
        if subscription_number is not None:
            self.subscription_number = subscription_number
        if subscription_owner_account_number is not None:
            self.subscription_owner_account_number = subscription_owner_account_number
        if terms is not None:
            self.terms = terms
        if currency is not None:
            self.currency = currency
        if invoice_group_number is not None:
            self.invoice_group_number = invoice_group_number

    @property
    def bill_to_contact_id(self):
        """Gets the bill_to_contact_id of this CreateOrderCreateSubscription.  # noqa: E501

        The ID of the bill-to contact associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Contact from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :return: The bill_to_contact_id of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._bill_to_contact_id

    @bill_to_contact_id.setter
    def bill_to_contact_id(self, bill_to_contact_id):
        """Sets the bill_to_contact_id of this CreateOrderCreateSubscription.

        The ID of the bill-to contact associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Contact from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :param bill_to_contact_id: The bill_to_contact_id of this CreateOrderCreateSubscription.  # noqa: E501
        :type: str
        """

        self._bill_to_contact_id = bill_to_contact_id

    @property
    def invoice_separately(self):
        """Gets the invoice_separately of this CreateOrderCreateSubscription.  # noqa: E501

        Specifies whether the subscription appears on a separate invoice when Zuora generates invoices.   # noqa: E501

        :return: The invoice_separately of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_separately

    @invoice_separately.setter
    def invoice_separately(self, invoice_separately):
        """Sets the invoice_separately of this CreateOrderCreateSubscription.

        Specifies whether the subscription appears on a separate invoice when Zuora generates invoices.   # noqa: E501

        :param invoice_separately: The invoice_separately of this CreateOrderCreateSubscription.  # noqa: E501
        :type: bool
        """

        self._invoice_separately = invoice_separately

    @property
    def invoice_template_id(self):
        """Gets the invoice_template_id of this CreateOrderCreateSubscription.  # noqa: E501

        The ID of the invoice template associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Template from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :return: The invoice_template_id of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._invoice_template_id

    @invoice_template_id.setter
    def invoice_template_id(self, invoice_template_id):
        """Sets the invoice_template_id of this CreateOrderCreateSubscription.

        The ID of the invoice template associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Template from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :param invoice_template_id: The invoice_template_id of this CreateOrderCreateSubscription.  # noqa: E501
        :type: str
        """

        self._invoice_template_id = invoice_template_id

    @property
    def new_subscription_owner_account(self):
        """Gets the new_subscription_owner_account of this CreateOrderCreateSubscription.  # noqa: E501


        :return: The new_subscription_owner_account of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: CreateOrderSubscriptionOwnerAccount
        """
        return self._new_subscription_owner_account

    @new_subscription_owner_account.setter
    def new_subscription_owner_account(self, new_subscription_owner_account):
        """Sets the new_subscription_owner_account of this CreateOrderCreateSubscription.


        :param new_subscription_owner_account: The new_subscription_owner_account of this CreateOrderCreateSubscription.  # noqa: E501
        :type: CreateOrderSubscriptionOwnerAccount
        """

        self._new_subscription_owner_account = new_subscription_owner_account

    @property
    def notes(self):
        """Gets the notes of this CreateOrderCreateSubscription.  # noqa: E501

        Notes about the subscription. These notes are only visible to Zuora users.   # noqa: E501

        :return: The notes of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CreateOrderCreateSubscription.

        Notes about the subscription. These notes are only visible to Zuora users.   # noqa: E501

        :param notes: The notes of this CreateOrderCreateSubscription.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def payment_term(self):
        """Gets the payment_term of this CreateOrderCreateSubscription.  # noqa: E501

        The name of the payment term associated with the subscription. For example, `Net 30`. The payment term determines the due dates of invoices.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Term from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :return: The payment_term of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._payment_term

    @payment_term.setter
    def payment_term(self, payment_term):
        """Sets the payment_term of this CreateOrderCreateSubscription.

        The name of the payment term associated with the subscription. For example, `Net 30`. The payment term determines the due dates of invoices.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Term from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :param payment_term: The payment_term of this CreateOrderCreateSubscription.  # noqa: E501
        :type: str
        """

        self._payment_term = payment_term

    @property
    def sequence_set_id(self):
        """Gets the sequence_set_id of this CreateOrderCreateSubscription.  # noqa: E501

        The ID of the sequence set associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Set from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :return: The sequence_set_id of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._sequence_set_id

    @sequence_set_id.setter
    def sequence_set_id(self, sequence_set_id):
        """Sets the sequence_set_id of this CreateOrderCreateSubscription.

        The ID of the sequence set associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Set from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :param sequence_set_id: The sequence_set_id of this CreateOrderCreateSubscription.  # noqa: E501
        :type: str
        """

        self._sequence_set_id = sequence_set_id

    @property
    def sold_to_contact_id(self):
        """Gets the sold_to_contact_id of this CreateOrderCreateSubscription.  # noqa: E501

        The ID of the sold-to contact associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Contact from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :return: The sold_to_contact_id of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._sold_to_contact_id

    @sold_to_contact_id.setter
    def sold_to_contact_id(self, sold_to_contact_id):
        """Sets the sold_to_contact_id of this CreateOrderCreateSubscription.

        The ID of the sold-to contact associated with the subscription.  **Note**:    - If you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature disabled, this field is unavailable in the request body and the value of this field is `null` in the response body.    - If you have the Flexible Billing Attributes feature enabled, and you do not specify this field in the request or you select **Default Contact from Account** for this field during subscription creation, the value of this field is automatically set to `null` in the response body.   # noqa: E501

        :param sold_to_contact_id: The sold_to_contact_id of this CreateOrderCreateSubscription.  # noqa: E501
        :type: str
        """

        self._sold_to_contact_id = sold_to_contact_id

    @property
    def subscribe_to_products(self):
        """Gets the subscribe_to_products of this CreateOrderCreateSubscription.  # noqa: E501

        For a rate plan, the following fields are available:   - `chargeOverrides`   - `clearingExistingFeatures`   - `customFields`   - `externallyManagedPlanId`   - `newRatePlanId`   - `productRatePlanId`   - `subscriptionProductFeatures`   - `uniqueToken`      # noqa: E501

        :return: The subscribe_to_products of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: list[CreateSubscribeToProduct]
        """
        return self._subscribe_to_products

    @subscribe_to_products.setter
    def subscribe_to_products(self, subscribe_to_products):
        """Sets the subscribe_to_products of this CreateOrderCreateSubscription.

        For a rate plan, the following fields are available:   - `chargeOverrides`   - `clearingExistingFeatures`   - `customFields`   - `externallyManagedPlanId`   - `newRatePlanId`   - `productRatePlanId`   - `subscriptionProductFeatures`   - `uniqueToken`      # noqa: E501

        :param subscribe_to_products: The subscribe_to_products of this CreateOrderCreateSubscription.  # noqa: E501
        :type: list[CreateSubscribeToProduct]
        """

        self._subscribe_to_products = subscribe_to_products

    @property
    def subscribe_to_rate_plans(self):
        """Gets the subscribe_to_rate_plans of this CreateOrderCreateSubscription.  # noqa: E501

        List of rate plans associated with the subscription.  **Note**: The `subscribeToRatePlans` field has been deprecated, this field is replaced by the `subscribeToProducts` field that supports Rate Plans. In a new order request, you can use either `subscribeToRatePlans` or `subscribeToProducts`, not both.   # noqa: E501

        :return: The subscribe_to_rate_plans of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: list[CreateOrderRatePlanOverride]
        """
        return self._subscribe_to_rate_plans

    @subscribe_to_rate_plans.setter
    def subscribe_to_rate_plans(self, subscribe_to_rate_plans):
        """Sets the subscribe_to_rate_plans of this CreateOrderCreateSubscription.

        List of rate plans associated with the subscription.  **Note**: The `subscribeToRatePlans` field has been deprecated, this field is replaced by the `subscribeToProducts` field that supports Rate Plans. In a new order request, you can use either `subscribeToRatePlans` or `subscribeToProducts`, not both.   # noqa: E501

        :param subscribe_to_rate_plans: The subscribe_to_rate_plans of this CreateOrderCreateSubscription.  # noqa: E501
        :type: list[CreateOrderRatePlanOverride]
        """

        self._subscribe_to_rate_plans = subscribe_to_rate_plans

    @property
    def subscription_number(self):
        """Gets the subscription_number of this CreateOrderCreateSubscription.  # noqa: E501

        Subscription number of the subscription. For example, A-S00000001.  If you do not set this field, Zuora will generate the subscription number.   # noqa: E501

        :return: The subscription_number of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this CreateOrderCreateSubscription.

        Subscription number of the subscription. For example, A-S00000001.  If you do not set this field, Zuora will generate the subscription number.   # noqa: E501

        :param subscription_number: The subscription_number of this CreateOrderCreateSubscription.  # noqa: E501
        :type: str
        """

        self._subscription_number = subscription_number

    @property
    def subscription_owner_account_number(self):
        """Gets the subscription_owner_account_number of this CreateOrderCreateSubscription.  # noqa: E501

        Account number of an existing account that will own the subscription. For example, A00000001.  If you do not set this field or the `newSubscriptionOwnerAccount` field, the account that owns the order will also own the subscription. Zuora will return an error if you set this field and the `newSubscriptionOwnerAccount` field.   # noqa: E501

        :return: The subscription_owner_account_number of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._subscription_owner_account_number

    @subscription_owner_account_number.setter
    def subscription_owner_account_number(self, subscription_owner_account_number):
        """Sets the subscription_owner_account_number of this CreateOrderCreateSubscription.

        Account number of an existing account that will own the subscription. For example, A00000001.  If you do not set this field or the `newSubscriptionOwnerAccount` field, the account that owns the order will also own the subscription. Zuora will return an error if you set this field and the `newSubscriptionOwnerAccount` field.   # noqa: E501

        :param subscription_owner_account_number: The subscription_owner_account_number of this CreateOrderCreateSubscription.  # noqa: E501
        :type: str
        """

        self._subscription_owner_account_number = subscription_owner_account_number

    @property
    def terms(self):
        """Gets the terms of this CreateOrderCreateSubscription.  # noqa: E501


        :return: The terms of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: OrderActionCreateSubscriptionTerms
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this CreateOrderCreateSubscription.


        :param terms: The terms of this CreateOrderCreateSubscription.  # noqa: E501
        :type: OrderActionCreateSubscriptionTerms
        """

        self._terms = terms

    @property
    def currency(self):
        """Gets the currency of this CreateOrderCreateSubscription.  # noqa: E501

        The code of currency that is used for this subscription. If the currency is not selected, the default currency from the account will be used. All subscriptions in the same order must use the same currency. The currency for a subscription cannot be changed.  **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Flexible_Billing/Multiple_Currencies\" target=\"_blank\">Multiple Currencies</a> feature enabled.    # noqa: E501

        :return: The currency of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreateOrderCreateSubscription.

        The code of currency that is used for this subscription. If the currency is not selected, the default currency from the account will be used. All subscriptions in the same order must use the same currency. The currency for a subscription cannot be changed.  **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Flexible_Billing/Multiple_Currencies\" target=\"_blank\">Multiple Currencies</a> feature enabled.    # noqa: E501

        :param currency: The currency of this CreateOrderCreateSubscription.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def invoice_group_number(self):
        """Gets the invoice_group_number of this CreateOrderCreateSubscription.  # noqa: E501

        The number of invoice group associated with the subscription.  **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature enabled.   # noqa: E501

        :return: The invoice_group_number of this CreateOrderCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._invoice_group_number

    @invoice_group_number.setter
    def invoice_group_number(self, invoice_group_number):
        """Sets the invoice_group_number of this CreateOrderCreateSubscription.

        The number of invoice group associated with the subscription.  **Note**: This field is available only if you have the <a href=\"https://knowledgecenter.zuora.com/Zuora_Billing/Bill_your_customers/Bill_customers_at_subscription_level/Flexible_Billing_Attributes\" target=\"_blank\">Flexible Billing Attributes</a> feature enabled.   # noqa: E501

        :param invoice_group_number: The invoice_group_number of this CreateOrderCreateSubscription.  # noqa: E501
        :type: str
        """

        self._invoice_group_number = invoice_group_number

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
        if issubclass(CreateOrderCreateSubscription, dict):
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
        if not isinstance(other, CreateOrderCreateSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
