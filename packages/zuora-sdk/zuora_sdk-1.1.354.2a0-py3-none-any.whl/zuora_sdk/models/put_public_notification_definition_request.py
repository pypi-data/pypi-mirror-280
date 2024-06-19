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

class PutPublicNotificationDefinitionRequest(object):
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
        'active': 'bool',
        'associated_account': 'str',
        'callout': 'PutPublicNotificationDefinitionRequestCallout',
        'callout_active': 'bool',
        'communication_profile_id': 'str',
        'description': 'str',
        'email_active': 'bool',
        'email_template_id': 'str',
        'filter_rule': 'PutPublicNotificationDefinitionRequestFilterRule',
        'filter_rule_params': 'dict(str, str)',
        'name': 'str'
    }

    attribute_map = {
        'active': 'active',
        'associated_account': 'associatedAccount',
        'callout': 'callout',
        'callout_active': 'calloutActive',
        'communication_profile_id': 'communicationProfileId',
        'description': 'description',
        'email_active': 'emailActive',
        'email_template_id': 'emailTemplateId',
        'filter_rule': 'filterRule',
        'filter_rule_params': 'filterRuleParams',
        'name': 'name'
    }

    def __init__(self, active=True, associated_account=None, callout=None, callout_active=False, communication_profile_id=None, description=None, email_active=False, email_template_id=None, filter_rule=None, filter_rule_params=None, name=None):  # noqa: E501
        """PutPublicNotificationDefinitionRequest - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._associated_account = None
        self._callout = None
        self._callout_active = None
        self._communication_profile_id = None
        self._description = None
        self._email_active = None
        self._email_template_id = None
        self._filter_rule = None
        self._filter_rule_params = None
        self._name = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if associated_account is not None:
            self.associated_account = associated_account
        if callout is not None:
            self.callout = callout
        if callout_active is not None:
            self.callout_active = callout_active
        if communication_profile_id is not None:
            self.communication_profile_id = communication_profile_id
        if description is not None:
            self.description = description
        if email_active is not None:
            self.email_active = email_active
        if email_template_id is not None:
            self.email_template_id = email_template_id
        if filter_rule is not None:
            self.filter_rule = filter_rule
        if filter_rule_params is not None:
            self.filter_rule_params = filter_rule_params
        if name is not None:
            self.name = name

    @property
    def active(self):
        """Gets the active of this PutPublicNotificationDefinitionRequest.  # noqa: E501

        The status of the notification definition. The default value is `true`.  # noqa: E501

        :return: The active of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PutPublicNotificationDefinitionRequest.

        The status of the notification definition. The default value is `true`.  # noqa: E501

        :param active: The active of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def associated_account(self):
        """Gets the associated_account of this PutPublicNotificationDefinitionRequest.  # noqa: E501

        Indicates with which type of account this notification is associated. Depending on your environment, you can use one of the following values: * `Account.Id`: ID of the primary customer account related to the notification. It is also the default value. * `ParentAccount.Id`: this option is available only if you have <a href=\"https://knowledgecenter.zuora.com/Billing/Subscriptions/Customer_Accounts/A_Customer_Account_Introduction#Customer_Hierarchy\" target=\"_blank\">Customer Hierarchy</a> enabled for your tenant. * `SubscriptionOwnerAccount.Id`: this option is available if the base object of the notification is Order Action.  **Note:** before specifying this field, we recommend that you use [Data Source](https://knowledgecenter.zuora.com/Billing/Reporting/D_Data_Sources_and_Exports/C_Data_Source_Reference) to check the available types of accounts for the current notification.     # noqa: E501

        :return: The associated_account of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._associated_account

    @associated_account.setter
    def associated_account(self, associated_account):
        """Sets the associated_account of this PutPublicNotificationDefinitionRequest.

        Indicates with which type of account this notification is associated. Depending on your environment, you can use one of the following values: * `Account.Id`: ID of the primary customer account related to the notification. It is also the default value. * `ParentAccount.Id`: this option is available only if you have <a href=\"https://knowledgecenter.zuora.com/Billing/Subscriptions/Customer_Accounts/A_Customer_Account_Introduction#Customer_Hierarchy\" target=\"_blank\">Customer Hierarchy</a> enabled for your tenant. * `SubscriptionOwnerAccount.Id`: this option is available if the base object of the notification is Order Action.  **Note:** before specifying this field, we recommend that you use [Data Source](https://knowledgecenter.zuora.com/Billing/Reporting/D_Data_Sources_and_Exports/C_Data_Source_Reference) to check the available types of accounts for the current notification.     # noqa: E501

        :param associated_account: The associated_account of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :type: str
        """

        self._associated_account = associated_account

    @property
    def callout(self):
        """Gets the callout of this PutPublicNotificationDefinitionRequest.  # noqa: E501


        :return: The callout of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :rtype: PutPublicNotificationDefinitionRequestCallout
        """
        return self._callout

    @callout.setter
    def callout(self, callout):
        """Sets the callout of this PutPublicNotificationDefinitionRequest.


        :param callout: The callout of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :type: PutPublicNotificationDefinitionRequestCallout
        """

        self._callout = callout

    @property
    def callout_active(self):
        """Gets the callout_active of this PutPublicNotificationDefinitionRequest.  # noqa: E501

        The status of the callout action. The default value is `false`.  # noqa: E501

        :return: The callout_active of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._callout_active

    @callout_active.setter
    def callout_active(self, callout_active):
        """Sets the callout_active of this PutPublicNotificationDefinitionRequest.

        The status of the callout action. The default value is `false`.  # noqa: E501

        :param callout_active: The callout_active of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :type: bool
        """

        self._callout_active = callout_active

    @property
    def communication_profile_id(self):
        """Gets the communication_profile_id of this PutPublicNotificationDefinitionRequest.  # noqa: E501

        The profile that notification definition belongs to. If you want to update the notification to a system notification, you should pass 'SystemNotification'. '   # noqa: E501

        :return: The communication_profile_id of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._communication_profile_id

    @communication_profile_id.setter
    def communication_profile_id(self, communication_profile_id):
        """Sets the communication_profile_id of this PutPublicNotificationDefinitionRequest.

        The profile that notification definition belongs to. If you want to update the notification to a system notification, you should pass 'SystemNotification'. '   # noqa: E501

        :param communication_profile_id: The communication_profile_id of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :type: str
        """

        self._communication_profile_id = communication_profile_id

    @property
    def description(self):
        """Gets the description of this PutPublicNotificationDefinitionRequest.  # noqa: E501

        The description of the notification definition.  # noqa: E501

        :return: The description of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutPublicNotificationDefinitionRequest.

        The description of the notification definition.  # noqa: E501

        :param description: The description of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_active(self):
        """Gets the email_active of this PutPublicNotificationDefinitionRequest.  # noqa: E501

        The status of the email action. The default value is `false`.  # noqa: E501

        :return: The email_active of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._email_active

    @email_active.setter
    def email_active(self, email_active):
        """Sets the email_active of this PutPublicNotificationDefinitionRequest.

        The status of the email action. The default value is `false`.  # noqa: E501

        :param email_active: The email_active of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :type: bool
        """

        self._email_active = email_active

    @property
    def email_template_id(self):
        """Gets the email_template_id of this PutPublicNotificationDefinitionRequest.  # noqa: E501

        The ID of the email template. If emailActive is updated from false to true, an email template is required, and the EventType of the email template MUST be the same as the EventType of the notification definition.   # noqa: E501

        :return: The email_template_id of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_template_id

    @email_template_id.setter
    def email_template_id(self, email_template_id):
        """Sets the email_template_id of this PutPublicNotificationDefinitionRequest.

        The ID of the email template. If emailActive is updated from false to true, an email template is required, and the EventType of the email template MUST be the same as the EventType of the notification definition.   # noqa: E501

        :param email_template_id: The email_template_id of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :type: str
        """

        self._email_template_id = email_template_id

    @property
    def filter_rule(self):
        """Gets the filter_rule of this PutPublicNotificationDefinitionRequest.  # noqa: E501


        :return: The filter_rule of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :rtype: PutPublicNotificationDefinitionRequestFilterRule
        """
        return self._filter_rule

    @filter_rule.setter
    def filter_rule(self, filter_rule):
        """Sets the filter_rule of this PutPublicNotificationDefinitionRequest.


        :param filter_rule: The filter_rule of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :type: PutPublicNotificationDefinitionRequestFilterRule
        """

        self._filter_rule = filter_rule

    @property
    def filter_rule_params(self):
        """Gets the filter_rule_params of this PutPublicNotificationDefinitionRequest.  # noqa: E501

        The parameter values used to configure the filter rule.   # noqa: E501

        :return: The filter_rule_params of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._filter_rule_params

    @filter_rule_params.setter
    def filter_rule_params(self, filter_rule_params):
        """Sets the filter_rule_params of this PutPublicNotificationDefinitionRequest.

        The parameter values used to configure the filter rule.   # noqa: E501

        :param filter_rule_params: The filter_rule_params of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._filter_rule_params = filter_rule_params

    @property
    def name(self):
        """Gets the name of this PutPublicNotificationDefinitionRequest.  # noqa: E501

        The name of the notification definition, which is unique in the profile.  # noqa: E501

        :return: The name of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutPublicNotificationDefinitionRequest.

        The name of the notification definition, which is unique in the profile.  # noqa: E501

        :param name: The name of this PutPublicNotificationDefinitionRequest.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(PutPublicNotificationDefinitionRequest, dict):
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
        if not isinstance(other, PutPublicNotificationDefinitionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
