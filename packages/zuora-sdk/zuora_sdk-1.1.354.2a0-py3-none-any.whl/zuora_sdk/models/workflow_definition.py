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

class WorkflowDefinition(object):
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
        'active_version': 'WorkflowDefinitionActiveVersion',
        'callout_trigger': 'bool',
        'created_at': 'str',
        'description': 'str',
        'id': 'int',
        'interval': 'str',
        'name': 'str',
        'ondemand_trigger': 'bool',
        'scheduled_trigger': 'bool',
        'status': 'str',
        'timezone': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'active_version': 'active_version',
        'callout_trigger': 'calloutTrigger',
        'created_at': 'createdAt',
        'description': 'description',
        'id': 'id',
        'interval': 'interval',
        'name': 'name',
        'ondemand_trigger': 'ondemandTrigger',
        'scheduled_trigger': 'scheduledTrigger',
        'status': 'status',
        'timezone': 'timezone',
        'updated_at': 'updatedAt'
    }

    def __init__(self, active_version=None, callout_trigger=None, created_at=None, description=None, id=None, interval=None, name=None, ondemand_trigger=None, scheduled_trigger=None, status=None, timezone=None, updated_at=None):  # noqa: E501
        """WorkflowDefinition - a model defined in Swagger"""  # noqa: E501
        self._active_version = None
        self._callout_trigger = None
        self._created_at = None
        self._description = None
        self._id = None
        self._interval = None
        self._name = None
        self._ondemand_trigger = None
        self._scheduled_trigger = None
        self._status = None
        self._timezone = None
        self._updated_at = None
        self.discriminator = None
        if active_version is not None:
            self.active_version = active_version
        if callout_trigger is not None:
            self.callout_trigger = callout_trigger
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if interval is not None:
            self.interval = interval
        if name is not None:
            self.name = name
        if ondemand_trigger is not None:
            self.ondemand_trigger = ondemand_trigger
        if scheduled_trigger is not None:
            self.scheduled_trigger = scheduled_trigger
        if status is not None:
            self.status = status
        if timezone is not None:
            self.timezone = timezone
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def active_version(self):
        """Gets the active_version of this WorkflowDefinition.  # noqa: E501


        :return: The active_version of this WorkflowDefinition.  # noqa: E501
        :rtype: WorkflowDefinitionActiveVersion
        """
        return self._active_version

    @active_version.setter
    def active_version(self, active_version):
        """Sets the active_version of this WorkflowDefinition.


        :param active_version: The active_version of this WorkflowDefinition.  # noqa: E501
        :type: WorkflowDefinitionActiveVersion
        """

        self._active_version = active_version

    @property
    def callout_trigger(self):
        """Gets the callout_trigger of this WorkflowDefinition.  # noqa: E501

        Indicates whether the callout trigger is enabled for the retrieved workflow.   # noqa: E501

        :return: The callout_trigger of this WorkflowDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._callout_trigger

    @callout_trigger.setter
    def callout_trigger(self, callout_trigger):
        """Sets the callout_trigger of this WorkflowDefinition.

        Indicates whether the callout trigger is enabled for the retrieved workflow.   # noqa: E501

        :param callout_trigger: The callout_trigger of this WorkflowDefinition.  # noqa: E501
        :type: bool
        """

        self._callout_trigger = callout_trigger

    @property
    def created_at(self):
        """Gets the created_at of this WorkflowDefinition.  # noqa: E501

        The date and time when the workflow is created, in the `YYYY-MM-DD HH:MM:SS` format.   # noqa: E501

        :return: The created_at of this WorkflowDefinition.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WorkflowDefinition.

        The date and time when the workflow is created, in the `YYYY-MM-DD HH:MM:SS` format.   # noqa: E501

        :param created_at: The created_at of this WorkflowDefinition.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this WorkflowDefinition.  # noqa: E501

        The description of the workflow definition.   # noqa: E501

        :return: The description of this WorkflowDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowDefinition.

        The description of the workflow definition.   # noqa: E501

        :param description: The description of this WorkflowDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this WorkflowDefinition.  # noqa: E501

        The unique ID of the workflow definition.   # noqa: E501

        :return: The id of this WorkflowDefinition.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkflowDefinition.

        The unique ID of the workflow definition.   # noqa: E501

        :param id: The id of this WorkflowDefinition.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interval(self):
        """Gets the interval of this WorkflowDefinition.  # noqa: E501

        The schedule of the workflow, in a CRON expression. Returns null if the schedued trigger is disabled.   # noqa: E501

        :return: The interval of this WorkflowDefinition.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this WorkflowDefinition.

        The schedule of the workflow, in a CRON expression. Returns null if the schedued trigger is disabled.   # noqa: E501

        :param interval: The interval of this WorkflowDefinition.  # noqa: E501
        :type: str
        """

        self._interval = interval

    @property
    def name(self):
        """Gets the name of this WorkflowDefinition.  # noqa: E501

        The name of the workflow definition.   # noqa: E501

        :return: The name of this WorkflowDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowDefinition.

        The name of the workflow definition.   # noqa: E501

        :param name: The name of this WorkflowDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ondemand_trigger(self):
        """Gets the ondemand_trigger of this WorkflowDefinition.  # noqa: E501

        Indicates whether the ondemand trigger is enabled for the workflow.   # noqa: E501

        :return: The ondemand_trigger of this WorkflowDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._ondemand_trigger

    @ondemand_trigger.setter
    def ondemand_trigger(self, ondemand_trigger):
        """Sets the ondemand_trigger of this WorkflowDefinition.

        Indicates whether the ondemand trigger is enabled for the workflow.   # noqa: E501

        :param ondemand_trigger: The ondemand_trigger of this WorkflowDefinition.  # noqa: E501
        :type: bool
        """

        self._ondemand_trigger = ondemand_trigger

    @property
    def scheduled_trigger(self):
        """Gets the scheduled_trigger of this WorkflowDefinition.  # noqa: E501

        Indicates whether the scheduled trigger is enabled for the workflow.   # noqa: E501

        :return: The scheduled_trigger of this WorkflowDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._scheduled_trigger

    @scheduled_trigger.setter
    def scheduled_trigger(self, scheduled_trigger):
        """Sets the scheduled_trigger of this WorkflowDefinition.

        Indicates whether the scheduled trigger is enabled for the workflow.   # noqa: E501

        :param scheduled_trigger: The scheduled_trigger of this WorkflowDefinition.  # noqa: E501
        :type: bool
        """

        self._scheduled_trigger = scheduled_trigger

    @property
    def status(self):
        """Gets the status of this WorkflowDefinition.  # noqa: E501

        The status of the workflow definition.   # noqa: E501

        :return: The status of this WorkflowDefinition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkflowDefinition.

        The status of the workflow definition.   # noqa: E501

        :param status: The status of this WorkflowDefinition.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def timezone(self):
        """Gets the timezone of this WorkflowDefinition.  # noqa: E501

        The timezone that is configured for the scheduler of the workflow. Returns null if the scheduled trigger is disabled.   # noqa: E501

        :return: The timezone of this WorkflowDefinition.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this WorkflowDefinition.

        The timezone that is configured for the scheduler of the workflow. Returns null if the scheduled trigger is disabled.   # noqa: E501

        :param timezone: The timezone of this WorkflowDefinition.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def updated_at(self):
        """Gets the updated_at of this WorkflowDefinition.  # noqa: E501

        The date and time when the workflow is updated the last time, in the `YYYY-MM-DD HH:MM:SS` format.   # noqa: E501

        :return: The updated_at of this WorkflowDefinition.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this WorkflowDefinition.

        The date and time when the workflow is updated the last time, in the `YYYY-MM-DD HH:MM:SS` format.   # noqa: E501

        :param updated_at: The updated_at of this WorkflowDefinition.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(WorkflowDefinition, dict):
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
        if not isinstance(other, WorkflowDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
