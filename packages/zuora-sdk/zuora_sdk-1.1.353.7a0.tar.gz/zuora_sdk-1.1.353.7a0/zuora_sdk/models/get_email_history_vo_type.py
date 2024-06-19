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

class GetEmailHistoryVOType(object):
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
        'bcc': 'str',
        'cc': 'str',
        'error_message': 'str',
        'event_category': 'str',
        'from_email': 'str',
        'notification': 'str',
        'reply_to': 'str',
        'result': 'str',
        'send_time': 'str',
        'subject': 'str',
        'to_email': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'bcc': 'bcc',
        'cc': 'cc',
        'error_message': 'errorMessage',
        'event_category': 'eventCategory',
        'from_email': 'fromEmail',
        'notification': 'notification',
        'reply_to': 'replyTo',
        'result': 'result',
        'send_time': 'sendTime',
        'subject': 'subject',
        'to_email': 'toEmail'
    }

    def __init__(self, account_id=None, bcc=None, cc=None, error_message=None, event_category=None, from_email=None, notification=None, reply_to=None, result=None, send_time=None, subject=None, to_email=None):  # noqa: E501
        """GetEmailHistoryVOType - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._bcc = None
        self._cc = None
        self._error_message = None
        self._event_category = None
        self._from_email = None
        self._notification = None
        self._reply_to = None
        self._result = None
        self._send_time = None
        self._subject = None
        self._to_email = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if bcc is not None:
            self.bcc = bcc
        if cc is not None:
            self.cc = cc
        if error_message is not None:
            self.error_message = error_message
        if event_category is not None:
            self.event_category = event_category
        if from_email is not None:
            self.from_email = from_email
        if notification is not None:
            self.notification = notification
        if reply_to is not None:
            self.reply_to = reply_to
        if result is not None:
            self.result = result
        if send_time is not None:
            self.send_time = send_time
        if subject is not None:
            self.subject = subject
        if to_email is not None:
            self.to_email = to_email

    @property
    def account_id(self):
        """Gets the account_id of this GetEmailHistoryVOType.  # noqa: E501

        ID of an account.   # noqa: E501

        :return: The account_id of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetEmailHistoryVOType.

        ID of an account.   # noqa: E501

        :param account_id: The account_id of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def bcc(self):
        """Gets the bcc of this GetEmailHistoryVOType.  # noqa: E501

        Blind carbon copy recipients of the email.   # noqa: E501

        :return: The bcc of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this GetEmailHistoryVOType.

        Blind carbon copy recipients of the email.   # noqa: E501

        :param bcc: The bcc of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._bcc = bcc

    @property
    def cc(self):
        """Gets the cc of this GetEmailHistoryVOType.  # noqa: E501

        Carbon Copy recipients of the email.   # noqa: E501

        :return: The cc of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this GetEmailHistoryVOType.

        Carbon Copy recipients of the email.   # noqa: E501

        :param cc: The cc of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._cc = cc

    @property
    def error_message(self):
        """Gets the error_message of this GetEmailHistoryVOType.  # noqa: E501

        null if the content of result is \"OK\". A description of the error if the content of result is not \"OK\".   # noqa: E501

        :return: The error_message of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this GetEmailHistoryVOType.

        null if the content of result is \"OK\". A description of the error if the content of result is not \"OK\".   # noqa: E501

        :param error_message: The error_message of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def event_category(self):
        """Gets the event_category of this GetEmailHistoryVOType.  # noqa: E501

        The event category of the email.   # noqa: E501

        :return: The event_category of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._event_category

    @event_category.setter
    def event_category(self, event_category):
        """Sets the event_category of this GetEmailHistoryVOType.

        The event category of the email.   # noqa: E501

        :param event_category: The event_category of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._event_category = event_category

    @property
    def from_email(self):
        """Gets the from_email of this GetEmailHistoryVOType.  # noqa: E501

        The sender of the email.   # noqa: E501

        :return: The from_email of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """Sets the from_email of this GetEmailHistoryVOType.

        The sender of the email.   # noqa: E501

        :param from_email: The from_email of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._from_email = from_email

    @property
    def notification(self):
        """Gets the notification of this GetEmailHistoryVOType.  # noqa: E501

        The name of the notification.   # noqa: E501

        :return: The notification of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this GetEmailHistoryVOType.

        The name of the notification.   # noqa: E501

        :param notification: The notification of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._notification = notification

    @property
    def reply_to(self):
        """Gets the reply_to of this GetEmailHistoryVOType.  # noqa: E501

        The reply-to address as configured in the email template.   # noqa: E501

        :return: The reply_to of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this GetEmailHistoryVOType.

        The reply-to address as configured in the email template.   # noqa: E501

        :param reply_to: The reply_to of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._reply_to = reply_to

    @property
    def result(self):
        """Gets the result of this GetEmailHistoryVOType.  # noqa: E501

        The result from the mail server of sending the email.   # noqa: E501

        :return: The result of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this GetEmailHistoryVOType.

        The result from the mail server of sending the email.   # noqa: E501

        :param result: The result of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def send_time(self):
        """Gets the send_time of this GetEmailHistoryVOType.  # noqa: E501

        The date and time the email was sent.   # noqa: E501

        :return: The send_time of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this GetEmailHistoryVOType.

        The date and time the email was sent.   # noqa: E501

        :param send_time: The send_time of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._send_time = send_time

    @property
    def subject(self):
        """Gets the subject of this GetEmailHistoryVOType.  # noqa: E501

        The subject of the email.   # noqa: E501

        :return: The subject of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this GetEmailHistoryVOType.

        The subject of the email.   # noqa: E501

        :param subject: The subject of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def to_email(self):
        """Gets the to_email of this GetEmailHistoryVOType.  # noqa: E501

        The intended recipient of the email.   # noqa: E501

        :return: The to_email of this GetEmailHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._to_email

    @to_email.setter
    def to_email(self, to_email):
        """Sets the to_email of this GetEmailHistoryVOType.

        The intended recipient of the email.   # noqa: E501

        :param to_email: The to_email of this GetEmailHistoryVOType.  # noqa: E501
        :type: str
        """

        self._to_email = to_email

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
        if issubclass(GetEmailHistoryVOType, dict):
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
        if not isinstance(other, GetEmailHistoryVOType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
