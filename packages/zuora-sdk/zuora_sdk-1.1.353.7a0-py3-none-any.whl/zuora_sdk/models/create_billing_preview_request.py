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

class CreateBillingPreviewRequest(object):
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
        'assume_renewal': 'str',
        'charge_type_to_exclude': 'str',
        'including_draft_items': 'bool',
        'including_evergreen_subscription': 'bool',
        'target_date': 'date'
    }

    attribute_map = {
        'account_id': 'accountId',
        'account_number': 'accountNumber',
        'assume_renewal': 'assumeRenewal',
        'charge_type_to_exclude': 'chargeTypeToExclude',
        'including_draft_items': 'includingDraftItems',
        'including_evergreen_subscription': 'includingEvergreenSubscription',
        'target_date': 'targetDate'
    }

    def __init__(self, account_id=None, account_number=None, assume_renewal=None, charge_type_to_exclude=None, including_draft_items=None, including_evergreen_subscription=None, target_date=None):  # noqa: E501
        """CreateBillingPreviewRequest - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._account_number = None
        self._assume_renewal = None
        self._charge_type_to_exclude = None
        self._including_draft_items = None
        self._including_evergreen_subscription = None
        self._target_date = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if account_number is not None:
            self.account_number = account_number
        if assume_renewal is not None:
            self.assume_renewal = assume_renewal
        if charge_type_to_exclude is not None:
            self.charge_type_to_exclude = charge_type_to_exclude
        if including_draft_items is not None:
            self.including_draft_items = including_draft_items
        if including_evergreen_subscription is not None:
            self.including_evergreen_subscription = including_evergreen_subscription
        self.target_date = target_date

    @property
    def account_id(self):
        """Gets the account_id of this CreateBillingPreviewRequest.  # noqa: E501

        The ID of the customer account to which the billing preview applies.  **Note**: When posting billing preview, you must specify either `accountId` or `accountNumber` in the request body.   # noqa: E501

        :return: The account_id of this CreateBillingPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CreateBillingPreviewRequest.

        The ID of the customer account to which the billing preview applies.  **Note**: When posting billing preview, you must specify either `accountId` or `accountNumber` in the request body.   # noqa: E501

        :param account_id: The account_id of this CreateBillingPreviewRequest.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_number(self):
        """Gets the account_number of this CreateBillingPreviewRequest.  # noqa: E501

        The number of the customer account to which the billing preview applies.  **Note**: When posting billing preview, you must specify either `accountId` or `accountNumber` in the request body.   # noqa: E501

        :return: The account_number of this CreateBillingPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this CreateBillingPreviewRequest.

        The number of the customer account to which the billing preview applies.  **Note**: When posting billing preview, you must specify either `accountId` or `accountNumber` in the request body.   # noqa: E501

        :param account_number: The account_number of this CreateBillingPreviewRequest.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def assume_renewal(self):
        """Gets the assume_renewal of this CreateBillingPreviewRequest.  # noqa: E501

        Indicates whether to generate a preview of future invoice items and credit memo items with the assumption that the subscriptions are renewed.  Set one of the following values in this field to decide how the assumption is applied in the billing preview.    * **All:** The assumption is applied to all the subscriptions. Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the target date.      * **None:** (Default) The assumption is not applied to the subscriptions. Zuora generates preview invoice item data and credit memo item data based on the current term end date and the target date.        * If the target date is later than the current term end date, Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the current term end date.      * If the target date is earlier than the current term end date, Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the target date.    * **Autorenew:** The assumption is applied to the subscriptions that have auto-renew enabled. Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the target date.  **Note:**    - This field can only be used if the subscription renewal term is not set to 0.           - The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :return: The assume_renewal of this CreateBillingPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._assume_renewal

    @assume_renewal.setter
    def assume_renewal(self, assume_renewal):
        """Sets the assume_renewal of this CreateBillingPreviewRequest.

        Indicates whether to generate a preview of future invoice items and credit memo items with the assumption that the subscriptions are renewed.  Set one of the following values in this field to decide how the assumption is applied in the billing preview.    * **All:** The assumption is applied to all the subscriptions. Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the target date.      * **None:** (Default) The assumption is not applied to the subscriptions. Zuora generates preview invoice item data and credit memo item data based on the current term end date and the target date.        * If the target date is later than the current term end date, Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the current term end date.      * If the target date is earlier than the current term end date, Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the target date.    * **Autorenew:** The assumption is applied to the subscriptions that have auto-renew enabled. Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the target date.  **Note:**    - This field can only be used if the subscription renewal term is not set to 0.           - The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :param assume_renewal: The assume_renewal of this CreateBillingPreviewRequest.  # noqa: E501
        :type: str
        """

        self._assume_renewal = assume_renewal

    @property
    def charge_type_to_exclude(self):
        """Gets the charge_type_to_exclude of this CreateBillingPreviewRequest.  # noqa: E501

        The charge types to exclude from the billing preview.  **Possible values:** OneTime, Recurring, Usage, and any combination of these values.   # noqa: E501

        :return: The charge_type_to_exclude of this CreateBillingPreviewRequest.  # noqa: E501
        :rtype: str
        """
        return self._charge_type_to_exclude

    @charge_type_to_exclude.setter
    def charge_type_to_exclude(self, charge_type_to_exclude):
        """Sets the charge_type_to_exclude of this CreateBillingPreviewRequest.

        The charge types to exclude from the billing preview.  **Possible values:** OneTime, Recurring, Usage, and any combination of these values.   # noqa: E501

        :param charge_type_to_exclude: The charge_type_to_exclude of this CreateBillingPreviewRequest.  # noqa: E501
        :type: str
        """

        self._charge_type_to_exclude = charge_type_to_exclude

    @property
    def including_draft_items(self):
        """Gets the including_draft_items of this CreateBillingPreviewRequest.  # noqa: E501

        Whether draft document items are included in the billing preview run. By default, draft document items are not included.  This field loads draft invoice items and credit memo items. The `chargeTypeToExclude`, `targetDate`, `includingEvergreenSubscription`, and `assumeRenewal` fields do not affect the behavior of the `includingDraftItems` field.             # noqa: E501

        :return: The including_draft_items of this CreateBillingPreviewRequest.  # noqa: E501
        :rtype: bool
        """
        return self._including_draft_items

    @including_draft_items.setter
    def including_draft_items(self, including_draft_items):
        """Sets the including_draft_items of this CreateBillingPreviewRequest.

        Whether draft document items are included in the billing preview run. By default, draft document items are not included.  This field loads draft invoice items and credit memo items. The `chargeTypeToExclude`, `targetDate`, `includingEvergreenSubscription`, and `assumeRenewal` fields do not affect the behavior of the `includingDraftItems` field.             # noqa: E501

        :param including_draft_items: The including_draft_items of this CreateBillingPreviewRequest.  # noqa: E501
        :type: bool
        """

        self._including_draft_items = including_draft_items

    @property
    def including_evergreen_subscription(self):
        """Gets the including_evergreen_subscription of this CreateBillingPreviewRequest.  # noqa: E501

        Indicates if evergreen subscriptions are included in the billingPreview call.   # noqa: E501

        :return: The including_evergreen_subscription of this CreateBillingPreviewRequest.  # noqa: E501
        :rtype: bool
        """
        return self._including_evergreen_subscription

    @including_evergreen_subscription.setter
    def including_evergreen_subscription(self, including_evergreen_subscription):
        """Sets the including_evergreen_subscription of this CreateBillingPreviewRequest.

        Indicates if evergreen subscriptions are included in the billingPreview call.   # noqa: E501

        :param including_evergreen_subscription: The including_evergreen_subscription of this CreateBillingPreviewRequest.  # noqa: E501
        :type: bool
        """

        self._including_evergreen_subscription = including_evergreen_subscription

    @property
    def target_date(self):
        """Gets the target_date of this CreateBillingPreviewRequest.  # noqa: E501

        The target date for the billingPreview call. The billingPreview call generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the TargetDate.   If the TargetDate is later than the subscription current term end date, the preview invoice item data and credit memo item data is generated from the first day of the customer's next billing period to the current term end date. If you want to generate preview invoice item data and credit memo item data past the end of the subscription current term, specify the `AssumeRenewal` field in the request.   **Note:** The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :return: The target_date of this CreateBillingPreviewRequest.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this CreateBillingPreviewRequest.

        The target date for the billingPreview call. The billingPreview call generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the TargetDate.   If the TargetDate is later than the subscription current term end date, the preview invoice item data and credit memo item data is generated from the first day of the customer's next billing period to the current term end date. If you want to generate preview invoice item data and credit memo item data past the end of the subscription current term, specify the `AssumeRenewal` field in the request.   **Note:** The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :param target_date: The target_date of this CreateBillingPreviewRequest.  # noqa: E501
        :type: date
        """
        if target_date is None:
            raise ValueError("Invalid value for `target_date`, must not be `None`")  # noqa: E501

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
        if issubclass(CreateBillingPreviewRequest, dict):
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
        if not isinstance(other, CreateBillingPreviewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
