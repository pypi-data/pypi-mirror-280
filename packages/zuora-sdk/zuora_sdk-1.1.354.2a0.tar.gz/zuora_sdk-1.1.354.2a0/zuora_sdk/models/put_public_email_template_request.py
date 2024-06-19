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

class PutPublicEmailTemplateRequest(object):
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
        'bcc_email_address': 'str',
        'cc_email_address': 'str',
        'cc_email_type': 'PutPublicEmailTemplateRequestCcEmailType',
        'description': 'str',
        'email_body': 'str',
        'email_subject': 'str',
        'encoding_type': 'PutPublicEmailTemplateRequestEncodingType',
        'from_email_address': 'str',
        'from_email_type': 'PutPublicEmailTemplateRequestFromEmailType',
        'from_name': 'str',
        'is_html': 'bool',
        'name': 'str',
        'reply_to_email_address': 'str',
        'reply_to_email_type': 'PutPublicEmailTemplateRequestReplyToEmailType',
        'to_email_address': 'str',
        'to_email_type': 'PutPublicEmailTemplateRequestToEmailType'
    }

    attribute_map = {
        'active': 'active',
        'bcc_email_address': 'bccEmailAddress',
        'cc_email_address': 'ccEmailAddress',
        'cc_email_type': 'ccEmailType',
        'description': 'description',
        'email_body': 'emailBody',
        'email_subject': 'emailSubject',
        'encoding_type': 'encodingType',
        'from_email_address': 'fromEmailAddress',
        'from_email_type': 'fromEmailType',
        'from_name': 'fromName',
        'is_html': 'isHtml',
        'name': 'name',
        'reply_to_email_address': 'replyToEmailAddress',
        'reply_to_email_type': 'replyToEmailType',
        'to_email_address': 'toEmailAddress',
        'to_email_type': 'toEmailType'
    }

    def __init__(self, active=None, bcc_email_address=None, cc_email_address=None, cc_email_type=None, description=None, email_body=None, email_subject=None, encoding_type=None, from_email_address=None, from_email_type=None, from_name=None, is_html=None, name=None, reply_to_email_address=None, reply_to_email_type=None, to_email_address=None, to_email_type=None):  # noqa: E501
        """PutPublicEmailTemplateRequest - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._bcc_email_address = None
        self._cc_email_address = None
        self._cc_email_type = None
        self._description = None
        self._email_body = None
        self._email_subject = None
        self._encoding_type = None
        self._from_email_address = None
        self._from_email_type = None
        self._from_name = None
        self._is_html = None
        self._name = None
        self._reply_to_email_address = None
        self._reply_to_email_type = None
        self._to_email_address = None
        self._to_email_type = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if bcc_email_address is not None:
            self.bcc_email_address = bcc_email_address
        if cc_email_address is not None:
            self.cc_email_address = cc_email_address
        if cc_email_type is not None:
            self.cc_email_type = cc_email_type
        if description is not None:
            self.description = description
        if email_body is not None:
            self.email_body = email_body
        if email_subject is not None:
            self.email_subject = email_subject
        if encoding_type is not None:
            self.encoding_type = encoding_type
        if from_email_address is not None:
            self.from_email_address = from_email_address
        if from_email_type is not None:
            self.from_email_type = from_email_type
        if from_name is not None:
            self.from_name = from_name
        if is_html is not None:
            self.is_html = is_html
        if name is not None:
            self.name = name
        if reply_to_email_address is not None:
            self.reply_to_email_address = reply_to_email_address
        if reply_to_email_type is not None:
            self.reply_to_email_type = reply_to_email_type
        if to_email_address is not None:
            self.to_email_address = to_email_address
        if to_email_type is not None:
            self.to_email_type = to_email_type

    @property
    def active(self):
        """Gets the active of this PutPublicEmailTemplateRequest.  # noqa: E501

        The status of the email template.  # noqa: E501

        :return: The active of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PutPublicEmailTemplateRequest.

        The status of the email template.  # noqa: E501

        :param active: The active of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def bcc_email_address(self):
        """Gets the bcc_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501

        Email bcc address.  # noqa: E501

        :return: The bcc_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._bcc_email_address

    @bcc_email_address.setter
    def bcc_email_address(self, bcc_email_address):
        """Sets the bcc_email_address of this PutPublicEmailTemplateRequest.

        Email bcc address.  # noqa: E501

        :param bcc_email_address: The bcc_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._bcc_email_address = bcc_email_address

    @property
    def cc_email_address(self):
        """Gets the cc_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501

        Email cc address.  # noqa: E501

        :return: The cc_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._cc_email_address

    @cc_email_address.setter
    def cc_email_address(self, cc_email_address):
        """Sets the cc_email_address of this PutPublicEmailTemplateRequest.

        Email cc address.  # noqa: E501

        :param cc_email_address: The cc_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._cc_email_address = cc_email_address

    @property
    def cc_email_type(self):
        """Gets the cc_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501


        :return: The cc_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: PutPublicEmailTemplateRequestCcEmailType
        """
        return self._cc_email_type

    @cc_email_type.setter
    def cc_email_type(self, cc_email_type):
        """Sets the cc_email_type of this PutPublicEmailTemplateRequest.


        :param cc_email_type: The cc_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: PutPublicEmailTemplateRequestCcEmailType
        """

        self._cc_email_type = cc_email_type

    @property
    def description(self):
        """Gets the description of this PutPublicEmailTemplateRequest.  # noqa: E501

        The description of the email template.  # noqa: E501

        :return: The description of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutPublicEmailTemplateRequest.

        The description of the email template.  # noqa: E501

        :param description: The description of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_body(self):
        """Gets the email_body of this PutPublicEmailTemplateRequest.  # noqa: E501

        The email body. You can add merge fields in the email object using angle brackets.  User can also embed html tags if `isHtml` is `true`.  # noqa: E501

        :return: The email_body of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_body

    @email_body.setter
    def email_body(self, email_body):
        """Sets the email_body of this PutPublicEmailTemplateRequest.

        The email body. You can add merge fields in the email object using angle brackets.  User can also embed html tags if `isHtml` is `true`.  # noqa: E501

        :param email_body: The email_body of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._email_body = email_body

    @property
    def email_subject(self):
        """Gets the email_subject of this PutPublicEmailTemplateRequest.  # noqa: E501

        The email subject. You can add merge fields in the email subject using angle brackets.  # noqa: E501

        :return: The email_subject of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """Sets the email_subject of this PutPublicEmailTemplateRequest.

        The email subject. You can add merge fields in the email subject using angle brackets.  # noqa: E501

        :param email_subject: The email_subject of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._email_subject = email_subject

    @property
    def encoding_type(self):
        """Gets the encoding_type of this PutPublicEmailTemplateRequest.  # noqa: E501


        :return: The encoding_type of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: PutPublicEmailTemplateRequestEncodingType
        """
        return self._encoding_type

    @encoding_type.setter
    def encoding_type(self, encoding_type):
        """Sets the encoding_type of this PutPublicEmailTemplateRequest.


        :param encoding_type: The encoding_type of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: PutPublicEmailTemplateRequestEncodingType
        """

        self._encoding_type = encoding_type

    @property
    def from_email_address(self):
        """Gets the from_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501

        If fromEmailType is SpecificEmail, this field is required  # noqa: E501

        :return: The from_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._from_email_address

    @from_email_address.setter
    def from_email_address(self, from_email_address):
        """Sets the from_email_address of this PutPublicEmailTemplateRequest.

        If fromEmailType is SpecificEmail, this field is required  # noqa: E501

        :param from_email_address: The from_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._from_email_address = from_email_address

    @property
    def from_email_type(self):
        """Gets the from_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501


        :return: The from_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: PutPublicEmailTemplateRequestFromEmailType
        """
        return self._from_email_type

    @from_email_type.setter
    def from_email_type(self, from_email_type):
        """Sets the from_email_type of this PutPublicEmailTemplateRequest.


        :param from_email_type: The from_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: PutPublicEmailTemplateRequestFromEmailType
        """

        self._from_email_type = from_email_type

    @property
    def from_name(self):
        """Gets the from_name of this PutPublicEmailTemplateRequest.  # noqa: E501

        The name of email sender.  # noqa: E501

        :return: The from_name of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this PutPublicEmailTemplateRequest.

        The name of email sender.  # noqa: E501

        :param from_name: The from_name of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def is_html(self):
        """Gets the is_html of this PutPublicEmailTemplateRequest.  # noqa: E501

        Indicates whether the style of email body is HTML.  # noqa: E501

        :return: The is_html of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_html

    @is_html.setter
    def is_html(self, is_html):
        """Sets the is_html of this PutPublicEmailTemplateRequest.

        Indicates whether the style of email body is HTML.  # noqa: E501

        :param is_html: The is_html of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._is_html = is_html

    @property
    def name(self):
        """Gets the name of this PutPublicEmailTemplateRequest.  # noqa: E501

        The name of the email template.  # noqa: E501

        :return: The name of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutPublicEmailTemplateRequest.

        The name of the email template.  # noqa: E501

        :param name: The name of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reply_to_email_address(self):
        """Gets the reply_to_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501

        If replyToEmailType is SpecificEmail, this field is required.  # noqa: E501

        :return: The reply_to_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._reply_to_email_address

    @reply_to_email_address.setter
    def reply_to_email_address(self, reply_to_email_address):
        """Sets the reply_to_email_address of this PutPublicEmailTemplateRequest.

        If replyToEmailType is SpecificEmail, this field is required.  # noqa: E501

        :param reply_to_email_address: The reply_to_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._reply_to_email_address = reply_to_email_address

    @property
    def reply_to_email_type(self):
        """Gets the reply_to_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501


        :return: The reply_to_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: PutPublicEmailTemplateRequestReplyToEmailType
        """
        return self._reply_to_email_type

    @reply_to_email_type.setter
    def reply_to_email_type(self, reply_to_email_type):
        """Sets the reply_to_email_type of this PutPublicEmailTemplateRequest.


        :param reply_to_email_type: The reply_to_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: PutPublicEmailTemplateRequestReplyToEmailType
        """

        self._reply_to_email_type = reply_to_email_type

    @property
    def to_email_address(self):
        """Gets the to_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501

        If toEmailType is SpecificEmail, this field is required.  # noqa: E501

        :return: The to_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._to_email_address

    @to_email_address.setter
    def to_email_address(self, to_email_address):
        """Sets the to_email_address of this PutPublicEmailTemplateRequest.

        If toEmailType is SpecificEmail, this field is required.  # noqa: E501

        :param to_email_address: The to_email_address of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._to_email_address = to_email_address

    @property
    def to_email_type(self):
        """Gets the to_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501


        :return: The to_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501
        :rtype: PutPublicEmailTemplateRequestToEmailType
        """
        return self._to_email_type

    @to_email_type.setter
    def to_email_type(self, to_email_type):
        """Sets the to_email_type of this PutPublicEmailTemplateRequest.


        :param to_email_type: The to_email_type of this PutPublicEmailTemplateRequest.  # noqa: E501
        :type: PutPublicEmailTemplateRequestToEmailType
        """

        self._to_email_type = to_email_type

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
        if issubclass(PutPublicEmailTemplateRequest, dict):
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
        if not isinstance(other, PutPublicEmailTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
