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

class GetCalloutHistoryVOType(object):
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
        'attempted_num': 'str',
        'create_time': 'str',
        'event_category': 'str',
        'event_context': 'str',
        'notification': 'str',
        'request_method': 'str',
        'request_url': 'str',
        'response_code': 'str',
        'response_content': 'str'
    }

    attribute_map = {
        'attempted_num': 'attemptedNum',
        'create_time': 'createTime',
        'event_category': 'eventCategory',
        'event_context': 'eventContext',
        'notification': 'notification',
        'request_method': 'requestMethod',
        'request_url': 'requestUrl',
        'response_code': 'responseCode',
        'response_content': 'responseContent'
    }

    def __init__(self, attempted_num=None, create_time=None, event_category=None, event_context=None, notification=None, request_method=None, request_url=None, response_code=None, response_content=None):  # noqa: E501
        """GetCalloutHistoryVOType - a model defined in Swagger"""  # noqa: E501
        self._attempted_num = None
        self._create_time = None
        self._event_category = None
        self._event_context = None
        self._notification = None
        self._request_method = None
        self._request_url = None
        self._response_code = None
        self._response_content = None
        self.discriminator = None
        if attempted_num is not None:
            self.attempted_num = attempted_num
        if create_time is not None:
            self.create_time = create_time
        if event_category is not None:
            self.event_category = event_category
        if event_context is not None:
            self.event_context = event_context
        if notification is not None:
            self.notification = notification
        if request_method is not None:
            self.request_method = request_method
        if request_url is not None:
            self.request_url = request_url
        if response_code is not None:
            self.response_code = response_code
        if response_content is not None:
            self.response_content = response_content

    @property
    def attempted_num(self):
        """Gets the attempted_num of this GetCalloutHistoryVOType.  # noqa: E501

        The number of times the callout was retried.   # noqa: E501

        :return: The attempted_num of this GetCalloutHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._attempted_num

    @attempted_num.setter
    def attempted_num(self, attempted_num):
        """Sets the attempted_num of this GetCalloutHistoryVOType.

        The number of times the callout was retried.   # noqa: E501

        :param attempted_num: The attempted_num of this GetCalloutHistoryVOType.  # noqa: E501
        :type: str
        """

        self._attempted_num = attempted_num

    @property
    def create_time(self):
        """Gets the create_time of this GetCalloutHistoryVOType.  # noqa: E501

        The time that the calloutHistory record was made.   # noqa: E501

        :return: The create_time of this GetCalloutHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GetCalloutHistoryVOType.

        The time that the calloutHistory record was made.   # noqa: E501

        :param create_time: The create_time of this GetCalloutHistoryVOType.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def event_category(self):
        """Gets the event_category of this GetCalloutHistoryVOType.  # noqa: E501

        The event category for the callout.   # noqa: E501

        :return: The event_category of this GetCalloutHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._event_category

    @event_category.setter
    def event_category(self, event_category):
        """Sets the event_category of this GetCalloutHistoryVOType.

        The event category for the callout.   # noqa: E501

        :param event_category: The event_category of this GetCalloutHistoryVOType.  # noqa: E501
        :type: str
        """

        self._event_category = event_category

    @property
    def event_context(self):
        """Gets the event_context of this GetCalloutHistoryVOType.  # noqa: E501

        The context of the callout event.   # noqa: E501

        :return: The event_context of this GetCalloutHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._event_context

    @event_context.setter
    def event_context(self, event_context):
        """Sets the event_context of this GetCalloutHistoryVOType.

        The context of the callout event.   # noqa: E501

        :param event_context: The event_context of this GetCalloutHistoryVOType.  # noqa: E501
        :type: str
        """

        self._event_context = event_context

    @property
    def notification(self):
        """Gets the notification of this GetCalloutHistoryVOType.  # noqa: E501

        The name of the notification.   # noqa: E501

        :return: The notification of this GetCalloutHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this GetCalloutHistoryVOType.

        The name of the notification.   # noqa: E501

        :param notification: The notification of this GetCalloutHistoryVOType.  # noqa: E501
        :type: str
        """

        self._notification = notification

    @property
    def request_method(self):
        """Gets the request_method of this GetCalloutHistoryVOType.  # noqa: E501

        The request method set in notifications settings.   # noqa: E501

        :return: The request_method of this GetCalloutHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._request_method

    @request_method.setter
    def request_method(self, request_method):
        """Sets the request_method of this GetCalloutHistoryVOType.

        The request method set in notifications settings.   # noqa: E501

        :param request_method: The request_method of this GetCalloutHistoryVOType.  # noqa: E501
        :type: str
        """

        self._request_method = request_method

    @property
    def request_url(self):
        """Gets the request_url of this GetCalloutHistoryVOType.  # noqa: E501

        The base url set in notifications settings.   # noqa: E501

        :return: The request_url of this GetCalloutHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._request_url

    @request_url.setter
    def request_url(self, request_url):
        """Sets the request_url of this GetCalloutHistoryVOType.

        The base url set in notifications settings.   # noqa: E501

        :param request_url: The request_url of this GetCalloutHistoryVOType.  # noqa: E501
        :type: str
        """

        self._request_url = request_url

    @property
    def response_code(self):
        """Gets the response_code of this GetCalloutHistoryVOType.  # noqa: E501

        The responseCode of the request.   # noqa: E501

        :return: The response_code of this GetCalloutHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this GetCalloutHistoryVOType.

        The responseCode of the request.   # noqa: E501

        :param response_code: The response_code of this GetCalloutHistoryVOType.  # noqa: E501
        :type: str
        """

        self._response_code = response_code

    @property
    def response_content(self):
        """Gets the response_content of this GetCalloutHistoryVOType.  # noqa: E501


        :return: The response_content of this GetCalloutHistoryVOType.  # noqa: E501
        :rtype: str
        """
        return self._response_content

    @response_content.setter
    def response_content(self, response_content):
        """Sets the response_content of this GetCalloutHistoryVOType.


        :param response_content: The response_content of this GetCalloutHistoryVOType.  # noqa: E501
        :type: str
        """

        self._response_content = response_content

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
        if issubclass(GetCalloutHistoryVOType, dict):
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
        if not isinstance(other, GetCalloutHistoryVOType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
