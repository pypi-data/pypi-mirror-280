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

class PostCreateOrUpdateEmailTemplateRequestFormat(object):
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
        'cc_email_type': 'PostCreateOrUpdateEmailTemplateRequestFormatCcEmailType',
        'description': 'str',
        'email_body': 'str',
        'email_subject': 'str',
        'encoding_type': 'PostCreateOrUpdateEmailTemplateRequestFormatEncodingType',
        'event_category': 'float',
        'event_type_name': 'str',
        'event_type_namespace': 'str',
        'from_email_address': 'str',
        'from_email_type': 'PostCreateOrUpdateEmailTemplateRequestFormatFromEmailType',
        'from_name': 'str',
        'id': 'str',
        'is_html': 'bool',
        'name': 'str',
        'reply_to_email_address': 'str',
        'reply_to_email_type': 'PostCreateOrUpdateEmailTemplateRequestFormatReplyToEmailType',
        'to_email_address': 'str',
        'to_email_type': 'PostCreateOrUpdateEmailTemplateRequestFormatToEmailType'
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
        'event_category': 'eventCategory',
        'event_type_name': 'eventTypeName',
        'event_type_namespace': 'eventTypeNamespace',
        'from_email_address': 'fromEmailAddress',
        'from_email_type': 'fromEmailType',
        'from_name': 'fromName',
        'id': 'id',
        'is_html': 'isHtml',
        'name': 'name',
        'reply_to_email_address': 'replyToEmailAddress',
        'reply_to_email_type': 'replyToEmailType',
        'to_email_address': 'toEmailAddress',
        'to_email_type': 'toEmailType'
    }

    def __init__(self, active=True, bcc_email_address=None, cc_email_address=None, cc_email_type=None, description=None, email_body=None, email_subject=None, encoding_type=None, event_category=None, event_type_name=None, event_type_namespace=None, from_email_address=None, from_email_type=None, from_name=None, id=None, is_html=False, name=None, reply_to_email_address=None, reply_to_email_type=None, to_email_address=None, to_email_type=None):  # noqa: E501
        """PostCreateOrUpdateEmailTemplateRequestFormat - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._bcc_email_address = None
        self._cc_email_address = None
        self._cc_email_type = None
        self._description = None
        self._email_body = None
        self._email_subject = None
        self._encoding_type = None
        self._event_category = None
        self._event_type_name = None
        self._event_type_namespace = None
        self._from_email_address = None
        self._from_email_type = None
        self._from_name = None
        self._id = None
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
        self.email_body = email_body
        self.email_subject = email_subject
        if encoding_type is not None:
            self.encoding_type = encoding_type
        if event_category is not None:
            self.event_category = event_category
        if event_type_name is not None:
            self.event_type_name = event_type_name
        if event_type_namespace is not None:
            self.event_type_namespace = event_type_namespace
        if from_email_address is not None:
            self.from_email_address = from_email_address
        self.from_email_type = from_email_type
        if from_name is not None:
            self.from_name = from_name
        if id is not None:
            self.id = id
        if is_html is not None:
            self.is_html = is_html
        self.name = name
        if reply_to_email_address is not None:
            self.reply_to_email_address = reply_to_email_address
        if reply_to_email_type is not None:
            self.reply_to_email_type = reply_to_email_type
        if to_email_address is not None:
            self.to_email_address = to_email_address
        self.to_email_type = to_email_type

    @property
    def active(self):
        """Gets the active of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        The status of the email template. The default value is `true`.  # noqa: E501

        :return: The active of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PostCreateOrUpdateEmailTemplateRequestFormat.

        The status of the email template. The default value is `true`.  # noqa: E501

        :param active: The active of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def bcc_email_address(self):
        """Gets the bcc_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        The email bcc address.  # noqa: E501

        :return: The bcc_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._bcc_email_address

    @bcc_email_address.setter
    def bcc_email_address(self, bcc_email_address):
        """Sets the bcc_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.

        The email bcc address.  # noqa: E501

        :param bcc_email_address: The bcc_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """

        self._bcc_email_address = bcc_email_address

    @property
    def cc_email_address(self):
        """Gets the cc_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        The email CC address.  # noqa: E501

        :return: The cc_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._cc_email_address

    @cc_email_address.setter
    def cc_email_address(self, cc_email_address):
        """Sets the cc_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.

        The email CC address.  # noqa: E501

        :param cc_email_address: The cc_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """

        self._cc_email_address = cc_email_address

    @property
    def cc_email_type(self):
        """Gets the cc_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501


        :return: The cc_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: PostCreateOrUpdateEmailTemplateRequestFormatCcEmailType
        """
        return self._cc_email_type

    @cc_email_type.setter
    def cc_email_type(self, cc_email_type):
        """Sets the cc_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.


        :param cc_email_type: The cc_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: PostCreateOrUpdateEmailTemplateRequestFormatCcEmailType
        """

        self._cc_email_type = cc_email_type

    @property
    def description(self):
        """Gets the description of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        The description of the email template.  # noqa: E501

        :return: The description of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostCreateOrUpdateEmailTemplateRequestFormat.

        The description of the email template.  # noqa: E501

        :param description: The description of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_body(self):
        """Gets the email_body of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        The email body. You can add merge fields in the email object using angle brackets.  You can also embed HTML tags if `isHtml` is `true`.  # noqa: E501

        :return: The email_body of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._email_body

    @email_body.setter
    def email_body(self, email_body):
        """Sets the email_body of this PostCreateOrUpdateEmailTemplateRequestFormat.

        The email body. You can add merge fields in the email object using angle brackets.  You can also embed HTML tags if `isHtml` is `true`.  # noqa: E501

        :param email_body: The email_body of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """
        if email_body is None:
            raise ValueError("Invalid value for `email_body`, must not be `None`")  # noqa: E501

        self._email_body = email_body

    @property
    def email_subject(self):
        """Gets the email_subject of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        The email subject. Users can add merge fields in the email subject using angle brackets.  # noqa: E501

        :return: The email_subject of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """Sets the email_subject of this PostCreateOrUpdateEmailTemplateRequestFormat.

        The email subject. Users can add merge fields in the email subject using angle brackets.  # noqa: E501

        :param email_subject: The email_subject of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """
        if email_subject is None:
            raise ValueError("Invalid value for `email_subject`, must not be `None`")  # noqa: E501

        self._email_subject = email_subject

    @property
    def encoding_type(self):
        """Gets the encoding_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501


        :return: The encoding_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: PostCreateOrUpdateEmailTemplateRequestFormatEncodingType
        """
        return self._encoding_type

    @encoding_type.setter
    def encoding_type(self, encoding_type):
        """Sets the encoding_type of this PostCreateOrUpdateEmailTemplateRequestFormat.


        :param encoding_type: The encoding_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: PostCreateOrUpdateEmailTemplateRequestFormatEncodingType
        """

        self._encoding_type = encoding_type

    @property
    def event_category(self):
        """Gets the event_category of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        If you specify this field, the email template is created based on a standard event. See [Standard Event Categories](https://knowledgecenter.zuora.com/Central_Platform/Notifications/A_Standard_Events/Standard_Event_Category_Code_for_Notification_Histories_API) for all standard event category codes.       # noqa: E501

        :return: The event_category of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: float
        """
        return self._event_category

    @event_category.setter
    def event_category(self, event_category):
        """Sets the event_category of this PostCreateOrUpdateEmailTemplateRequestFormat.

        If you specify this field, the email template is created based on a standard event. See [Standard Event Categories](https://knowledgecenter.zuora.com/Central_Platform/Notifications/A_Standard_Events/Standard_Event_Category_Code_for_Notification_Histories_API) for all standard event category codes.       # noqa: E501

        :param event_category: The event_category of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: float
        """

        self._event_category = event_category

    @property
    def event_type_name(self):
        """Gets the event_type_name of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        The name of the custom event or custom scheduled event. If you specify this field, the email template is created based on the corresponding custom event or custom scheduled event.   # noqa: E501

        :return: The event_type_name of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._event_type_name

    @event_type_name.setter
    def event_type_name(self, event_type_name):
        """Sets the event_type_name of this PostCreateOrUpdateEmailTemplateRequestFormat.

        The name of the custom event or custom scheduled event. If you specify this field, the email template is created based on the corresponding custom event or custom scheduled event.   # noqa: E501

        :param event_type_name: The event_type_name of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """

        self._event_type_name = event_type_name

    @property
    def event_type_namespace(self):
        """Gets the event_type_namespace of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        The namespace of the `eventTypeName` field. The `eventTypeName` has the `user.notification` namespace by default.   Note that if the `eventTypeName` is a standard event type, you must specify the `com.zuora.notification` namespace; otherwise, you will get an error.  For example, if you want to create an email template on the `OrderActionProcessed` event, you must specify `com.zuora.notification` for this field.            # noqa: E501

        :return: The event_type_namespace of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._event_type_namespace

    @event_type_namespace.setter
    def event_type_namespace(self, event_type_namespace):
        """Sets the event_type_namespace of this PostCreateOrUpdateEmailTemplateRequestFormat.

        The namespace of the `eventTypeName` field. The `eventTypeName` has the `user.notification` namespace by default.   Note that if the `eventTypeName` is a standard event type, you must specify the `com.zuora.notification` namespace; otherwise, you will get an error.  For example, if you want to create an email template on the `OrderActionProcessed` event, you must specify `com.zuora.notification` for this field.            # noqa: E501

        :param event_type_namespace: The event_type_namespace of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """

        self._event_type_namespace = event_type_namespace

    @property
    def from_email_address(self):
        """Gets the from_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        If fromEmailType is SpecificEmail, this field is required.  # noqa: E501

        :return: The from_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._from_email_address

    @from_email_address.setter
    def from_email_address(self, from_email_address):
        """Sets the from_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.

        If fromEmailType is SpecificEmail, this field is required.  # noqa: E501

        :param from_email_address: The from_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """

        self._from_email_address = from_email_address

    @property
    def from_email_type(self):
        """Gets the from_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501


        :return: The from_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: PostCreateOrUpdateEmailTemplateRequestFormatFromEmailType
        """
        return self._from_email_type

    @from_email_type.setter
    def from_email_type(self, from_email_type):
        """Sets the from_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.


        :param from_email_type: The from_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: PostCreateOrUpdateEmailTemplateRequestFormatFromEmailType
        """
        if from_email_type is None:
            raise ValueError("Invalid value for `from_email_type`, must not be `None`")  # noqa: E501

        self._from_email_type = from_email_type

    @property
    def from_name(self):
        """Gets the from_name of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        The name of the email sender.  # noqa: E501

        :return: The from_name of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this PostCreateOrUpdateEmailTemplateRequestFormat.

        The name of the email sender.  # noqa: E501

        :param from_name: The from_name of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def id(self):
        """Gets the id of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        ID of an existing email template. Specify this field if you want to update an existing email template.   # noqa: E501

        :return: The id of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PostCreateOrUpdateEmailTemplateRequestFormat.

        ID of an existing email template. Specify this field if you want to update an existing email template.   # noqa: E501

        :param id: The id of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_html(self):
        """Gets the is_html of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        Indicates whether the style of email body is HTML. The default value is `false`.  # noqa: E501

        :return: The is_html of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: bool
        """
        return self._is_html

    @is_html.setter
    def is_html(self, is_html):
        """Sets the is_html of this PostCreateOrUpdateEmailTemplateRequestFormat.

        Indicates whether the style of email body is HTML. The default value is `false`.  # noqa: E501

        :param is_html: The is_html of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: bool
        """

        self._is_html = is_html

    @property
    def name(self):
        """Gets the name of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        The name of the email template, a unique name in a tenant.  # noqa: E501

        :return: The name of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostCreateOrUpdateEmailTemplateRequestFormat.

        The name of the email template, a unique name in a tenant.  # noqa: E501

        :param name: The name of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def reply_to_email_address(self):
        """Gets the reply_to_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        If `replyToEmailType` is `SpecificEmail`, this field is required.  # noqa: E501

        :return: The reply_to_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._reply_to_email_address

    @reply_to_email_address.setter
    def reply_to_email_address(self, reply_to_email_address):
        """Sets the reply_to_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.

        If `replyToEmailType` is `SpecificEmail`, this field is required.  # noqa: E501

        :param reply_to_email_address: The reply_to_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """

        self._reply_to_email_address = reply_to_email_address

    @property
    def reply_to_email_type(self):
        """Gets the reply_to_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501


        :return: The reply_to_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: PostCreateOrUpdateEmailTemplateRequestFormatReplyToEmailType
        """
        return self._reply_to_email_type

    @reply_to_email_type.setter
    def reply_to_email_type(self, reply_to_email_type):
        """Sets the reply_to_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.


        :param reply_to_email_type: The reply_to_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: PostCreateOrUpdateEmailTemplateRequestFormatReplyToEmailType
        """

        self._reply_to_email_type = reply_to_email_type

    @property
    def to_email_address(self):
        """Gets the to_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501

        If toEmailType is SpecificEmail, this field is required.  # noqa: E501

        :return: The to_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: str
        """
        return self._to_email_address

    @to_email_address.setter
    def to_email_address(self, to_email_address):
        """Sets the to_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.

        If toEmailType is SpecificEmail, this field is required.  # noqa: E501

        :param to_email_address: The to_email_address of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: str
        """

        self._to_email_address = to_email_address

    @property
    def to_email_type(self):
        """Gets the to_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501


        :return: The to_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :rtype: PostCreateOrUpdateEmailTemplateRequestFormatToEmailType
        """
        return self._to_email_type

    @to_email_type.setter
    def to_email_type(self, to_email_type):
        """Sets the to_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.


        :param to_email_type: The to_email_type of this PostCreateOrUpdateEmailTemplateRequestFormat.  # noqa: E501
        :type: PostCreateOrUpdateEmailTemplateRequestFormatToEmailType
        """
        if to_email_type is None:
            raise ValueError("Invalid value for `to_email_type`, must not be `None`")  # noqa: E501

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
        if issubclass(PostCreateOrUpdateEmailTemplateRequestFormat, dict):
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
        if not isinstance(other, PostCreateOrUpdateEmailTemplateRequestFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
