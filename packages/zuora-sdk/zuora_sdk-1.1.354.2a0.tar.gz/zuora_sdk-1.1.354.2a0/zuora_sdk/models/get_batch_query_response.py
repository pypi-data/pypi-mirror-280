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

class GetBatchQueryResponse(object):
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
        'api_version': 'str',
        'batch_id': 'str',
        'batch_type': 'BatchQueryBatchType',
        'file_id': 'str',
        'full': 'bool',
        'message': 'str',
        'name': 'str',
        'query': 'str',
        'record_count': 'str',
        'segments': 'list[str]',
        'status': 'BatchQueryStatus',
        'localized_status': 'BatchQueryStatus',
        'deleted': 'DeletedRecord'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'batch_id': 'batchId',
        'batch_type': 'batchType',
        'file_id': 'fileId',
        'full': 'full',
        'message': 'message',
        'name': 'name',
        'query': 'query',
        'record_count': 'recordCount',
        'segments': 'segments',
        'status': 'status',
        'localized_status': 'localizedStatus',
        'deleted': 'deleted'
    }

    def __init__(self, api_version=None, batch_id=None, batch_type=None, file_id=None, full=None, message=None, name=None, query=None, record_count=None, segments=None, status=None, localized_status=None, deleted=None):  # noqa: E501
        """GetBatchQueryResponse - a model defined in Swagger"""  # noqa: E501
        self._api_version = None
        self._batch_id = None
        self._batch_type = None
        self._file_id = None
        self._full = None
        self._message = None
        self._name = None
        self._query = None
        self._record_count = None
        self._segments = None
        self._status = None
        self._localized_status = None
        self._deleted = None
        self.discriminator = None
        if api_version is not None:
            self.api_version = api_version
        if batch_id is not None:
            self.batch_id = batch_id
        if batch_type is not None:
            self.batch_type = batch_type
        if file_id is not None:
            self.file_id = file_id
        if full is not None:
            self.full = full
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if query is not None:
            self.query = query
        if record_count is not None:
            self.record_count = record_count
        if segments is not None:
            self.segments = segments
        if status is not None:
            self.status = status
        if localized_status is not None:
            self.localized_status = localized_status
        if deleted is not None:
            self.deleted = deleted

    @property
    def api_version(self):
        """Gets the api_version of this GetBatchQueryResponse.  # noqa: E501

        The API version for the query. If an API version is not specified, the latest version is used by default. Using the latest WSDL version is most useful for reporting use cases. For integration purposes, specify the WSDL version to ensure consistent query behavior, that is, what is supported and included in the response returned by the API.  **Note**: As of API version 69 and later, Zuora changed the format of certain fields. See <a href=\"https://knowledgecenter.zuora.com/Zuora_Central_Platform/API/G_SOAP_API/AB_Getting_started_with_the__SOAP_API/C_Date_Field_Changes_in_the_SOAP_API\" target=\"_blank\">Date Field Changes in the SOAP API</a> for more information and a list of affected fields.   # noqa: E501

        :return: The api_version of this GetBatchQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this GetBatchQueryResponse.

        The API version for the query. If an API version is not specified, the latest version is used by default. Using the latest WSDL version is most useful for reporting use cases. For integration purposes, specify the WSDL version to ensure consistent query behavior, that is, what is supported and included in the response returned by the API.  **Note**: As of API version 69 and later, Zuora changed the format of certain fields. See <a href=\"https://knowledgecenter.zuora.com/Zuora_Central_Platform/API/G_SOAP_API/AB_Getting_started_with_the__SOAP_API/C_Date_Field_Changes_in_the_SOAP_API\" target=\"_blank\">Date Field Changes in the SOAP API</a> for more information and a list of affected fields.   # noqa: E501

        :param api_version: The api_version of this GetBatchQueryResponse.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def batch_id(self):
        """Gets the batch_id of this GetBatchQueryResponse.  # noqa: E501

        A 32-character ID of the query batch.   # noqa: E501

        :return: The batch_id of this GetBatchQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this GetBatchQueryResponse.

        A 32-character ID of the query batch.   # noqa: E501

        :param batch_id: The batch_id of this GetBatchQueryResponse.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def batch_type(self):
        """Gets the batch_type of this GetBatchQueryResponse.  # noqa: E501


        :return: The batch_type of this GetBatchQueryResponse.  # noqa: E501
        :rtype: BatchQueryBatchType
        """
        return self._batch_type

    @batch_type.setter
    def batch_type(self, batch_type):
        """Sets the batch_type of this GetBatchQueryResponse.


        :param batch_type: The batch_type of this GetBatchQueryResponse.  # noqa: E501
        :type: BatchQueryBatchType
        """

        self._batch_type = batch_type

    @property
    def file_id(self):
        """Gets the file_id of this GetBatchQueryResponse.  # noqa: E501

        The ID of the query results file.  Use Get Results Files to download the query results file. The query results file is formatted as requested in the batch job. Supported formats are CSV, GZIP, and ZIP.   # noqa: E501

        :return: The file_id of this GetBatchQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this GetBatchQueryResponse.

        The ID of the query results file.  Use Get Results Files to download the query results file. The query results file is formatted as requested in the batch job. Supported formats are CSV, GZIP, and ZIP.   # noqa: E501

        :param file_id: The file_id of this GetBatchQueryResponse.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def full(self):
        """Gets the full of this GetBatchQueryResponse.  # noqa: E501

        This field indicates a full or incremental load. `True` = Full and `False` = Incremental.   # noqa: E501

        :return: The full of this GetBatchQueryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._full

    @full.setter
    def full(self, full):
        """Sets the full of this GetBatchQueryResponse.

        This field indicates a full or incremental load. `True` = Full and `False` = Incremental.   # noqa: E501

        :param full: The full of this GetBatchQueryResponse.  # noqa: E501
        :type: bool
        """

        self._full = full

    @property
    def message(self):
        """Gets the message of this GetBatchQueryResponse.  # noqa: E501

        The error message.   # noqa: E501

        :return: The message of this GetBatchQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this GetBatchQueryResponse.

        The error message.   # noqa: E501

        :param message: The message of this GetBatchQueryResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this GetBatchQueryResponse.  # noqa: E501

        Name of the query supplied in the request.   # noqa: E501

        :return: The name of this GetBatchQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetBatchQueryResponse.

        Name of the query supplied in the request.   # noqa: E501

        :param name: The name of this GetBatchQueryResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def query(self):
        """Gets the query of this GetBatchQueryResponse.  # noqa: E501

        The requested query string.   # noqa: E501

        :return: The query of this GetBatchQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this GetBatchQueryResponse.

        The requested query string.   # noqa: E501

        :param query: The query of this GetBatchQueryResponse.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def record_count(self):
        """Gets the record_count of this GetBatchQueryResponse.  # noqa: E501

        The number of records included in the query output file.   # noqa: E501

        :return: The record_count of this GetBatchQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._record_count

    @record_count.setter
    def record_count(self, record_count):
        """Sets the record_count of this GetBatchQueryResponse.

        The number of records included in the query output file.   # noqa: E501

        :param record_count: The record_count of this GetBatchQueryResponse.  # noqa: E501
        :type: str
        """

        self._record_count = record_count

    @property
    def segments(self):
        """Gets the segments of this GetBatchQueryResponse.  # noqa: E501

        Array of IDs of query results files. Replaces fileId for full data loads in stateful mode if <a href = \"https://knowledgecenter.zuora.com/Zuora_Central_Platform/API/AB_Aggregate_Query_API/G_File_Segmentation\" target=\"_blank\">File Segmentation</a> is enabled.  Use Get Results Files to download each query results file. Each query results file contains at most 500,000 records and is formatted as requested in the batch job. Supported formats are CSV, GZIP, and ZIP.   # noqa: E501

        :return: The segments of this GetBatchQueryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this GetBatchQueryResponse.

        Array of IDs of query results files. Replaces fileId for full data loads in stateful mode if <a href = \"https://knowledgecenter.zuora.com/Zuora_Central_Platform/API/AB_Aggregate_Query_API/G_File_Segmentation\" target=\"_blank\">File Segmentation</a> is enabled.  Use Get Results Files to download each query results file. Each query results file contains at most 500,000 records and is formatted as requested in the batch job. Supported formats are CSV, GZIP, and ZIP.   # noqa: E501

        :param segments: The segments of this GetBatchQueryResponse.  # noqa: E501
        :type: list[str]
        """

        self._segments = segments

    @property
    def status(self):
        """Gets the status of this GetBatchQueryResponse.  # noqa: E501


        :return: The status of this GetBatchQueryResponse.  # noqa: E501
        :rtype: BatchQueryStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetBatchQueryResponse.


        :param status: The status of this GetBatchQueryResponse.  # noqa: E501
        :type: BatchQueryStatus
        """

        self._status = status

    @property
    def localized_status(self):
        """Gets the localized_status of this GetBatchQueryResponse.  # noqa: E501


        :return: The localized_status of this GetBatchQueryResponse.  # noqa: E501
        :rtype: BatchQueryStatus
        """
        return self._localized_status

    @localized_status.setter
    def localized_status(self, localized_status):
        """Sets the localized_status of this GetBatchQueryResponse.


        :param localized_status: The localized_status of this GetBatchQueryResponse.  # noqa: E501
        :type: BatchQueryStatus
        """

        self._localized_status = localized_status

    @property
    def deleted(self):
        """Gets the deleted of this GetBatchQueryResponse.  # noqa: E501


        :return: The deleted of this GetBatchQueryResponse.  # noqa: E501
        :rtype: DeletedRecord
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this GetBatchQueryResponse.


        :param deleted: The deleted of this GetBatchQueryResponse.  # noqa: E501
        :type: DeletedRecord
        """

        self._deleted = deleted

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
        if issubclass(GetBatchQueryResponse, dict):
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
        if not isinstance(other, GetBatchQueryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
