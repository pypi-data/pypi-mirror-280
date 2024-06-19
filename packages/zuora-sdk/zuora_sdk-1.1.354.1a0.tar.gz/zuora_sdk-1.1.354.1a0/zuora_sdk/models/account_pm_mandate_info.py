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

class AccountPMMandateInfo(object):
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
        'existing_mandate_status': 'PaymentMethodMandateInfoMandateStatus',
        'mandate_creation_date': 'date',
        'mandate_id': 'str',
        'mandate_reason': 'str',
        'mandate_received_status': 'PaymentMethodMandateInfoMandateStatus',
        'mandate_status': 'str',
        'mandate_update_date': 'date',
        'mit_consent_agreement_ref': 'str',
        'mit_consent_agreement_src': 'StoredCredentialProfileConsentAgreementSrc',
        'mit_profile_action': 'StoredCredentialProfileAction',
        'mit_profile_agreed_on': 'date',
        'mit_profile_type': 'str',
        'mit_transaction_id': 'str'
    }

    attribute_map = {
        'existing_mandate_status': 'existingMandateStatus',
        'mandate_creation_date': 'mandateCreationDate',
        'mandate_id': 'mandateId',
        'mandate_reason': 'mandateReason',
        'mandate_received_status': 'mandateReceivedStatus',
        'mandate_status': 'mandateStatus',
        'mandate_update_date': 'mandateUpdateDate',
        'mit_consent_agreement_ref': 'mitConsentAgreementRef',
        'mit_consent_agreement_src': 'mitConsentAgreementSrc',
        'mit_profile_action': 'mitProfileAction',
        'mit_profile_agreed_on': 'mitProfileAgreedOn',
        'mit_profile_type': 'mitProfileType',
        'mit_transaction_id': 'mitTransactionId'
    }

    def __init__(self, existing_mandate_status=None, mandate_creation_date=None, mandate_id=None, mandate_reason=None, mandate_received_status=None, mandate_status=None, mandate_update_date=None, mit_consent_agreement_ref=None, mit_consent_agreement_src=None, mit_profile_action=None, mit_profile_agreed_on=None, mit_profile_type=None, mit_transaction_id=None):  # noqa: E501
        """AccountPMMandateInfo - a model defined in Swagger"""  # noqa: E501
        self._existing_mandate_status = None
        self._mandate_creation_date = None
        self._mandate_id = None
        self._mandate_reason = None
        self._mandate_received_status = None
        self._mandate_status = None
        self._mandate_update_date = None
        self._mit_consent_agreement_ref = None
        self._mit_consent_agreement_src = None
        self._mit_profile_action = None
        self._mit_profile_agreed_on = None
        self._mit_profile_type = None
        self._mit_transaction_id = None
        self.discriminator = None
        if existing_mandate_status is not None:
            self.existing_mandate_status = existing_mandate_status
        if mandate_creation_date is not None:
            self.mandate_creation_date = mandate_creation_date
        if mandate_id is not None:
            self.mandate_id = mandate_id
        if mandate_reason is not None:
            self.mandate_reason = mandate_reason
        if mandate_received_status is not None:
            self.mandate_received_status = mandate_received_status
        if mandate_status is not None:
            self.mandate_status = mandate_status
        if mandate_update_date is not None:
            self.mandate_update_date = mandate_update_date
        if mit_consent_agreement_ref is not None:
            self.mit_consent_agreement_ref = mit_consent_agreement_ref
        if mit_consent_agreement_src is not None:
            self.mit_consent_agreement_src = mit_consent_agreement_src
        if mit_profile_action is not None:
            self.mit_profile_action = mit_profile_action
        if mit_profile_agreed_on is not None:
            self.mit_profile_agreed_on = mit_profile_agreed_on
        if mit_profile_type is not None:
            self.mit_profile_type = mit_profile_type
        if mit_transaction_id is not None:
            self.mit_transaction_id = mit_transaction_id

    @property
    def existing_mandate_status(self):
        """Gets the existing_mandate_status of this AccountPMMandateInfo.  # noqa: E501


        :return: The existing_mandate_status of this AccountPMMandateInfo.  # noqa: E501
        :rtype: PaymentMethodMandateInfoMandateStatus
        """
        return self._existing_mandate_status

    @existing_mandate_status.setter
    def existing_mandate_status(self, existing_mandate_status):
        """Sets the existing_mandate_status of this AccountPMMandateInfo.


        :param existing_mandate_status: The existing_mandate_status of this AccountPMMandateInfo.  # noqa: E501
        :type: PaymentMethodMandateInfoMandateStatus
        """

        self._existing_mandate_status = existing_mandate_status

    @property
    def mandate_creation_date(self):
        """Gets the mandate_creation_date of this AccountPMMandateInfo.  # noqa: E501

        The date on which the mandate was created.   # noqa: E501

        :return: The mandate_creation_date of this AccountPMMandateInfo.  # noqa: E501
        :rtype: date
        """
        return self._mandate_creation_date

    @mandate_creation_date.setter
    def mandate_creation_date(self, mandate_creation_date):
        """Sets the mandate_creation_date of this AccountPMMandateInfo.

        The date on which the mandate was created.   # noqa: E501

        :param mandate_creation_date: The mandate_creation_date of this AccountPMMandateInfo.  # noqa: E501
        :type: date
        """

        self._mandate_creation_date = mandate_creation_date

    @property
    def mandate_id(self):
        """Gets the mandate_id of this AccountPMMandateInfo.  # noqa: E501

        The mandate ID.   # noqa: E501

        :return: The mandate_id of this AccountPMMandateInfo.  # noqa: E501
        :rtype: str
        """
        return self._mandate_id

    @mandate_id.setter
    def mandate_id(self, mandate_id):
        """Sets the mandate_id of this AccountPMMandateInfo.

        The mandate ID.   # noqa: E501

        :param mandate_id: The mandate_id of this AccountPMMandateInfo.  # noqa: E501
        :type: str
        """

        self._mandate_id = mandate_id

    @property
    def mandate_reason(self):
        """Gets the mandate_reason of this AccountPMMandateInfo.  # noqa: E501

        The reason of the mandate from the gateway side.   # noqa: E501

        :return: The mandate_reason of this AccountPMMandateInfo.  # noqa: E501
        :rtype: str
        """
        return self._mandate_reason

    @mandate_reason.setter
    def mandate_reason(self, mandate_reason):
        """Sets the mandate_reason of this AccountPMMandateInfo.

        The reason of the mandate from the gateway side.   # noqa: E501

        :param mandate_reason: The mandate_reason of this AccountPMMandateInfo.  # noqa: E501
        :type: str
        """

        self._mandate_reason = mandate_reason

    @property
    def mandate_received_status(self):
        """Gets the mandate_received_status of this AccountPMMandateInfo.  # noqa: E501


        :return: The mandate_received_status of this AccountPMMandateInfo.  # noqa: E501
        :rtype: PaymentMethodMandateInfoMandateStatus
        """
        return self._mandate_received_status

    @mandate_received_status.setter
    def mandate_received_status(self, mandate_received_status):
        """Sets the mandate_received_status of this AccountPMMandateInfo.


        :param mandate_received_status: The mandate_received_status of this AccountPMMandateInfo.  # noqa: E501
        :type: PaymentMethodMandateInfoMandateStatus
        """

        self._mandate_received_status = mandate_received_status

    @property
    def mandate_status(self):
        """Gets the mandate_status of this AccountPMMandateInfo.  # noqa: E501

        The status of the mandate from the gateway side.   # noqa: E501

        :return: The mandate_status of this AccountPMMandateInfo.  # noqa: E501
        :rtype: str
        """
        return self._mandate_status

    @mandate_status.setter
    def mandate_status(self, mandate_status):
        """Sets the mandate_status of this AccountPMMandateInfo.

        The status of the mandate from the gateway side.   # noqa: E501

        :param mandate_status: The mandate_status of this AccountPMMandateInfo.  # noqa: E501
        :type: str
        """

        self._mandate_status = mandate_status

    @property
    def mandate_update_date(self):
        """Gets the mandate_update_date of this AccountPMMandateInfo.  # noqa: E501

        The date on which the mandate was updated.   # noqa: E501

        :return: The mandate_update_date of this AccountPMMandateInfo.  # noqa: E501
        :rtype: date
        """
        return self._mandate_update_date

    @mandate_update_date.setter
    def mandate_update_date(self, mandate_update_date):
        """Sets the mandate_update_date of this AccountPMMandateInfo.

        The date on which the mandate was updated.   # noqa: E501

        :param mandate_update_date: The mandate_update_date of this AccountPMMandateInfo.  # noqa: E501
        :type: date
        """

        self._mandate_update_date = mandate_update_date

    @property
    def mit_consent_agreement_ref(self):
        """Gets the mit_consent_agreement_ref of this AccountPMMandateInfo.  # noqa: E501

        Reference for the consent agreement that you have established with the customer.     # noqa: E501

        :return: The mit_consent_agreement_ref of this AccountPMMandateInfo.  # noqa: E501
        :rtype: str
        """
        return self._mit_consent_agreement_ref

    @mit_consent_agreement_ref.setter
    def mit_consent_agreement_ref(self, mit_consent_agreement_ref):
        """Sets the mit_consent_agreement_ref of this AccountPMMandateInfo.

        Reference for the consent agreement that you have established with the customer.     # noqa: E501

        :param mit_consent_agreement_ref: The mit_consent_agreement_ref of this AccountPMMandateInfo.  # noqa: E501
        :type: str
        """

        self._mit_consent_agreement_ref = mit_consent_agreement_ref

    @property
    def mit_consent_agreement_src(self):
        """Gets the mit_consent_agreement_src of this AccountPMMandateInfo.  # noqa: E501


        :return: The mit_consent_agreement_src of this AccountPMMandateInfo.  # noqa: E501
        :rtype: StoredCredentialProfileConsentAgreementSrc
        """
        return self._mit_consent_agreement_src

    @mit_consent_agreement_src.setter
    def mit_consent_agreement_src(self, mit_consent_agreement_src):
        """Sets the mit_consent_agreement_src of this AccountPMMandateInfo.


        :param mit_consent_agreement_src: The mit_consent_agreement_src of this AccountPMMandateInfo.  # noqa: E501
        :type: StoredCredentialProfileConsentAgreementSrc
        """

        self._mit_consent_agreement_src = mit_consent_agreement_src

    @property
    def mit_profile_action(self):
        """Gets the mit_profile_action of this AccountPMMandateInfo.  # noqa: E501


        :return: The mit_profile_action of this AccountPMMandateInfo.  # noqa: E501
        :rtype: StoredCredentialProfileAction
        """
        return self._mit_profile_action

    @mit_profile_action.setter
    def mit_profile_action(self, mit_profile_action):
        """Sets the mit_profile_action of this AccountPMMandateInfo.


        :param mit_profile_action: The mit_profile_action of this AccountPMMandateInfo.  # noqa: E501
        :type: StoredCredentialProfileAction
        """

        self._mit_profile_action = mit_profile_action

    @property
    def mit_profile_agreed_on(self):
        """Gets the mit_profile_agreed_on of this AccountPMMandateInfo.  # noqa: E501

        The date on which the stored credential profile is agreed. The date format is `yyyy-mm-dd`.   # noqa: E501

        :return: The mit_profile_agreed_on of this AccountPMMandateInfo.  # noqa: E501
        :rtype: date
        """
        return self._mit_profile_agreed_on

    @mit_profile_agreed_on.setter
    def mit_profile_agreed_on(self, mit_profile_agreed_on):
        """Sets the mit_profile_agreed_on of this AccountPMMandateInfo.

        The date on which the stored credential profile is agreed. The date format is `yyyy-mm-dd`.   # noqa: E501

        :param mit_profile_agreed_on: The mit_profile_agreed_on of this AccountPMMandateInfo.  # noqa: E501
        :type: date
        """

        self._mit_profile_agreed_on = mit_profile_agreed_on

    @property
    def mit_profile_type(self):
        """Gets the mit_profile_type of this AccountPMMandateInfo.  # noqa: E501

        Indicates the type of the stored credential profile. If you do not specify the `mitProfileAction` field, Zuora will automatically create a stored credential profile for the payment method, with the default value `Recurring` set to this field.   # noqa: E501

        :return: The mit_profile_type of this AccountPMMandateInfo.  # noqa: E501
        :rtype: str
        """
        return self._mit_profile_type

    @mit_profile_type.setter
    def mit_profile_type(self, mit_profile_type):
        """Sets the mit_profile_type of this AccountPMMandateInfo.

        Indicates the type of the stored credential profile. If you do not specify the `mitProfileAction` field, Zuora will automatically create a stored credential profile for the payment method, with the default value `Recurring` set to this field.   # noqa: E501

        :param mit_profile_type: The mit_profile_type of this AccountPMMandateInfo.  # noqa: E501
        :type: str
        """

        self._mit_profile_type = mit_profile_type

    @property
    def mit_transaction_id(self):
        """Gets the mit_transaction_id of this AccountPMMandateInfo.  # noqa: E501

        Specifies the ID of the transaction. Only applicable if you set the `mitProfileAction` field to `Persist`.   # noqa: E501

        :return: The mit_transaction_id of this AccountPMMandateInfo.  # noqa: E501
        :rtype: str
        """
        return self._mit_transaction_id

    @mit_transaction_id.setter
    def mit_transaction_id(self, mit_transaction_id):
        """Sets the mit_transaction_id of this AccountPMMandateInfo.

        Specifies the ID of the transaction. Only applicable if you set the `mitProfileAction` field to `Persist`.   # noqa: E501

        :param mit_transaction_id: The mit_transaction_id of this AccountPMMandateInfo.  # noqa: E501
        :type: str
        """

        self._mit_transaction_id = mit_transaction_id

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
        if issubclass(AccountPMMandateInfo, dict):
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
        if not isinstance(other, AccountPMMandateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
