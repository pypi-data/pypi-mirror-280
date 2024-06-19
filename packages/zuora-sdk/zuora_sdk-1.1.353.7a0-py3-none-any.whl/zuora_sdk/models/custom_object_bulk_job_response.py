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

class CustomObjectBulkJobResponse(object):
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
        'created_by_id': 'str',
        'created_date': 'datetime',
        'id': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime',
        'error': 'CustomObjectBulkJobResponseError',
        'namespace': 'CustomObjectBulkJobResponseNamespace',
        'object': 'str',
        'operation': 'CustomObjectBulkJobResponseOperation',
        'processing_time': 'int',
        'records_processed': 'int',
        'status': 'CustomObjectBulkJobResponseStatus'
    }

    attribute_map = {
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'id': 'Id',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate',
        'error': 'error',
        'namespace': 'namespace',
        'object': 'object',
        'operation': 'operation',
        'processing_time': 'processingTime',
        'records_processed': 'recordsProcessed',
        'status': 'status'
    }

    def __init__(self, created_by_id=None, created_date=None, id=None, updated_by_id=None, updated_date=None, error=None, namespace=None, object=None, operation=None, processing_time=None, records_processed=None, status=None):  # noqa: E501
        """CustomObjectBulkJobResponse - a model defined in Swagger"""  # noqa: E501
        self._created_by_id = None
        self._created_date = None
        self._id = None
        self._updated_by_id = None
        self._updated_date = None
        self._error = None
        self._namespace = None
        self._object = None
        self._operation = None
        self._processing_time = None
        self._records_processed = None
        self._status = None
        self.discriminator = None
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if id is not None:
            self.id = id
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date
        if error is not None:
            self.error = error
        if namespace is not None:
            self.namespace = namespace
        if object is not None:
            self.object = object
        if operation is not None:
            self.operation = operation
        if processing_time is not None:
            self.processing_time = processing_time
        if records_processed is not None:
            self.records_processed = records_processed
        if status is not None:
            self.status = status

    @property
    def created_by_id(self):
        """Gets the created_by_id of this CustomObjectBulkJobResponse.  # noqa: E501

        The ID of the user who creates the job.  # noqa: E501

        :return: The created_by_id of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this CustomObjectBulkJobResponse.

        The ID of the user who creates the job.  # noqa: E501

        :param created_by_id: The created_by_id of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this CustomObjectBulkJobResponse.  # noqa: E501

        The time when the bulk job is created.  # noqa: E501

        :return: The created_date of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this CustomObjectBulkJobResponse.

        The time when the bulk job is created.  # noqa: E501

        :param created_date: The created_date of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def id(self):
        """Gets the id of this CustomObjectBulkJobResponse.  # noqa: E501

        The custom object bulk job ID.  # noqa: E501

        :return: The id of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomObjectBulkJobResponse.

        The custom object bulk job ID.  # noqa: E501

        :param id: The id of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this CustomObjectBulkJobResponse.  # noqa: E501

        The ID of the user who updates the job.  # noqa: E501

        :return: The updated_by_id of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this CustomObjectBulkJobResponse.

        The ID of the user who updates the job.  # noqa: E501

        :param updated_by_id: The updated_by_id of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this CustomObjectBulkJobResponse.  # noqa: E501

        The time when the bulk job is updated.  # noqa: E501

        :return: The updated_date of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this CustomObjectBulkJobResponse.

        The time when the bulk job is updated.  # noqa: E501

        :param updated_date: The updated_date of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

    @property
    def error(self):
        """Gets the error of this CustomObjectBulkJobResponse.  # noqa: E501


        :return: The error of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: CustomObjectBulkJobResponseError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CustomObjectBulkJobResponse.


        :param error: The error of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: CustomObjectBulkJobResponseError
        """

        self._error = error

    @property
    def namespace(self):
        """Gets the namespace of this CustomObjectBulkJobResponse.  # noqa: E501


        :return: The namespace of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: CustomObjectBulkJobResponseNamespace
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CustomObjectBulkJobResponse.


        :param namespace: The namespace of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: CustomObjectBulkJobResponseNamespace
        """

        self._namespace = namespace

    @property
    def object(self):
        """Gets the object of this CustomObjectBulkJobResponse.  # noqa: E501

        The object to that the bulk operation performs on.  # noqa: E501

        :return: The object of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this CustomObjectBulkJobResponse.

        The object to that the bulk operation performs on.  # noqa: E501

        :param object: The object of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def operation(self):
        """Gets the operation of this CustomObjectBulkJobResponse.  # noqa: E501


        :return: The operation of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: CustomObjectBulkJobResponseOperation
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this CustomObjectBulkJobResponse.


        :param operation: The operation of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: CustomObjectBulkJobResponseOperation
        """

        self._operation = operation

    @property
    def processing_time(self):
        """Gets the processing_time of this CustomObjectBulkJobResponse.  # noqa: E501

        The amount of time elapsed, in milliseconds, from the submission to the completion of the bulk job.  # noqa: E501

        :return: The processing_time of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: int
        """
        return self._processing_time

    @processing_time.setter
    def processing_time(self, processing_time):
        """Sets the processing_time of this CustomObjectBulkJobResponse.

        The amount of time elapsed, in milliseconds, from the submission to the completion of the bulk job.  # noqa: E501

        :param processing_time: The processing_time of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: int
        """

        self._processing_time = processing_time

    @property
    def records_processed(self):
        """Gets the records_processed of this CustomObjectBulkJobResponse.  # noqa: E501

        The number of object records processed by the bulk job.  # noqa: E501

        :return: The records_processed of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: int
        """
        return self._records_processed

    @records_processed.setter
    def records_processed(self, records_processed):
        """Sets the records_processed of this CustomObjectBulkJobResponse.

        The number of object records processed by the bulk job.  # noqa: E501

        :param records_processed: The records_processed of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: int
        """

        self._records_processed = records_processed

    @property
    def status(self):
        """Gets the status of this CustomObjectBulkJobResponse.  # noqa: E501


        :return: The status of this CustomObjectBulkJobResponse.  # noqa: E501
        :rtype: CustomObjectBulkJobResponseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CustomObjectBulkJobResponse.


        :param status: The status of this CustomObjectBulkJobResponse.  # noqa: E501
        :type: CustomObjectBulkJobResponseStatus
        """

        self._status = status

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
        if issubclass(CustomObjectBulkJobResponse, dict):
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
        if not isinstance(other, CustomObjectBulkJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
