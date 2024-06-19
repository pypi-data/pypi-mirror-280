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

class ProductRatePlanChargeObjectNSFields(object):
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
        'class__ns': 'str',
        'deferred_rev_account__ns': 'str',
        'department__ns': 'str',
        'include_children__ns': 'ProductRatePlanChargeObjectNSFieldsIncludeChildrenNS',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'item_type__ns': 'ProductRatePlanChargeObjectNSFieldsItemTypeNS',
        'location__ns': 'str',
        'recognized_rev_account__ns': 'str',
        'rev_rec_end__ns': 'ProductRatePlanChargeObjectNSFieldsRevRecEndNS',
        'rev_rec_start__ns': 'ProductRatePlanChargeObjectNSFieldsRevRecStartNS',
        'rev_rec_template_type__ns': 'str',
        'subsidiary__ns': 'str',
        'sync_date__ns': 'str'
    }

    attribute_map = {
        'class__ns': 'Class__NS',
        'deferred_rev_account__ns': 'DeferredRevAccount__NS',
        'department__ns': 'Department__NS',
        'include_children__ns': 'IncludeChildren__NS',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'item_type__ns': 'ItemType__NS',
        'location__ns': 'Location__NS',
        'recognized_rev_account__ns': 'RecognizedRevAccount__NS',
        'rev_rec_end__ns': 'RevRecEnd__NS',
        'rev_rec_start__ns': 'RevRecStart__NS',
        'rev_rec_template_type__ns': 'RevRecTemplateType__NS',
        'subsidiary__ns': 'Subsidiary__NS',
        'sync_date__ns': 'SyncDate__NS'
    }

    def __init__(self, class__ns=None, deferred_rev_account__ns=None, department__ns=None, include_children__ns=None, integration_id__ns=None, integration_status__ns=None, item_type__ns=None, location__ns=None, recognized_rev_account__ns=None, rev_rec_end__ns=None, rev_rec_start__ns=None, rev_rec_template_type__ns=None, subsidiary__ns=None, sync_date__ns=None):  # noqa: E501
        """ProductRatePlanChargeObjectNSFields - a model defined in Swagger"""  # noqa: E501
        self._class__ns = None
        self._deferred_rev_account__ns = None
        self._department__ns = None
        self._include_children__ns = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._item_type__ns = None
        self._location__ns = None
        self._recognized_rev_account__ns = None
        self._rev_rec_end__ns = None
        self._rev_rec_start__ns = None
        self._rev_rec_template_type__ns = None
        self._subsidiary__ns = None
        self._sync_date__ns = None
        self.discriminator = None
        if class__ns is not None:
            self.class__ns = class__ns
        if deferred_rev_account__ns is not None:
            self.deferred_rev_account__ns = deferred_rev_account__ns
        if department__ns is not None:
            self.department__ns = department__ns
        if include_children__ns is not None:
            self.include_children__ns = include_children__ns
        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if item_type__ns is not None:
            self.item_type__ns = item_type__ns
        if location__ns is not None:
            self.location__ns = location__ns
        if recognized_rev_account__ns is not None:
            self.recognized_rev_account__ns = recognized_rev_account__ns
        if rev_rec_end__ns is not None:
            self.rev_rec_end__ns = rev_rec_end__ns
        if rev_rec_start__ns is not None:
            self.rev_rec_start__ns = rev_rec_start__ns
        if rev_rec_template_type__ns is not None:
            self.rev_rec_template_type__ns = rev_rec_template_type__ns
        if subsidiary__ns is not None:
            self.subsidiary__ns = subsidiary__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns

    @property
    def class__ns(self):
        """Gets the class__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501

        Class associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The class__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: str
        """
        return self._class__ns

    @class__ns.setter
    def class__ns(self, class__ns):
        """Sets the class__ns of this ProductRatePlanChargeObjectNSFields.

        Class associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param class__ns: The class__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: str
        """

        self._class__ns = class__ns

    @property
    def deferred_rev_account__ns(self):
        """Gets the deferred_rev_account__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501

        Deferrred revenue account associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The deferred_rev_account__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: str
        """
        return self._deferred_rev_account__ns

    @deferred_rev_account__ns.setter
    def deferred_rev_account__ns(self, deferred_rev_account__ns):
        """Sets the deferred_rev_account__ns of this ProductRatePlanChargeObjectNSFields.

        Deferrred revenue account associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param deferred_rev_account__ns: The deferred_rev_account__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: str
        """

        self._deferred_rev_account__ns = deferred_rev_account__ns

    @property
    def department__ns(self):
        """Gets the department__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501

        Department associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The department__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: str
        """
        return self._department__ns

    @department__ns.setter
    def department__ns(self, department__ns):
        """Sets the department__ns of this ProductRatePlanChargeObjectNSFields.

        Department associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param department__ns: The department__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: str
        """

        self._department__ns = department__ns

    @property
    def include_children__ns(self):
        """Gets the include_children__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501


        :return: The include_children__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: ProductRatePlanChargeObjectNSFieldsIncludeChildrenNS
        """
        return self._include_children__ns

    @include_children__ns.setter
    def include_children__ns(self, include_children__ns):
        """Sets the include_children__ns of this ProductRatePlanChargeObjectNSFields.


        :param include_children__ns: The include_children__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: ProductRatePlanChargeObjectNSFieldsIncludeChildrenNS
        """

        self._include_children__ns = include_children__ns

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this ProductRatePlanChargeObjectNSFields.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: str
        """

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501

        Status of the product rate plan charge's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this ProductRatePlanChargeObjectNSFields.

        Status of the product rate plan charge's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: str
        """

        self._integration_status__ns = integration_status__ns

    @property
    def item_type__ns(self):
        """Gets the item_type__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501


        :return: The item_type__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: ProductRatePlanChargeObjectNSFieldsItemTypeNS
        """
        return self._item_type__ns

    @item_type__ns.setter
    def item_type__ns(self, item_type__ns):
        """Sets the item_type__ns of this ProductRatePlanChargeObjectNSFields.


        :param item_type__ns: The item_type__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: ProductRatePlanChargeObjectNSFieldsItemTypeNS
        """

        self._item_type__ns = item_type__ns

    @property
    def location__ns(self):
        """Gets the location__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501

        Location associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The location__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: str
        """
        return self._location__ns

    @location__ns.setter
    def location__ns(self, location__ns):
        """Sets the location__ns of this ProductRatePlanChargeObjectNSFields.

        Location associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param location__ns: The location__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: str
        """

        self._location__ns = location__ns

    @property
    def recognized_rev_account__ns(self):
        """Gets the recognized_rev_account__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501

        Recognized revenue account associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The recognized_rev_account__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: str
        """
        return self._recognized_rev_account__ns

    @recognized_rev_account__ns.setter
    def recognized_rev_account__ns(self, recognized_rev_account__ns):
        """Sets the recognized_rev_account__ns of this ProductRatePlanChargeObjectNSFields.

        Recognized revenue account associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param recognized_rev_account__ns: The recognized_rev_account__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: str
        """

        self._recognized_rev_account__ns = recognized_rev_account__ns

    @property
    def rev_rec_end__ns(self):
        """Gets the rev_rec_end__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501


        :return: The rev_rec_end__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: ProductRatePlanChargeObjectNSFieldsRevRecEndNS
        """
        return self._rev_rec_end__ns

    @rev_rec_end__ns.setter
    def rev_rec_end__ns(self, rev_rec_end__ns):
        """Sets the rev_rec_end__ns of this ProductRatePlanChargeObjectNSFields.


        :param rev_rec_end__ns: The rev_rec_end__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: ProductRatePlanChargeObjectNSFieldsRevRecEndNS
        """

        self._rev_rec_end__ns = rev_rec_end__ns

    @property
    def rev_rec_start__ns(self):
        """Gets the rev_rec_start__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501


        :return: The rev_rec_start__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: ProductRatePlanChargeObjectNSFieldsRevRecStartNS
        """
        return self._rev_rec_start__ns

    @rev_rec_start__ns.setter
    def rev_rec_start__ns(self, rev_rec_start__ns):
        """Sets the rev_rec_start__ns of this ProductRatePlanChargeObjectNSFields.


        :param rev_rec_start__ns: The rev_rec_start__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: ProductRatePlanChargeObjectNSFieldsRevRecStartNS
        """

        self._rev_rec_start__ns = rev_rec_start__ns

    @property
    def rev_rec_template_type__ns(self):
        """Gets the rev_rec_template_type__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501

        Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The rev_rec_template_type__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: str
        """
        return self._rev_rec_template_type__ns

    @rev_rec_template_type__ns.setter
    def rev_rec_template_type__ns(self, rev_rec_template_type__ns):
        """Sets the rev_rec_template_type__ns of this ProductRatePlanChargeObjectNSFields.

        Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param rev_rec_template_type__ns: The rev_rec_template_type__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: str
        """

        self._rev_rec_template_type__ns = rev_rec_template_type__ns

    @property
    def subsidiary__ns(self):
        """Gets the subsidiary__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501

        Subsidiary associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The subsidiary__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: str
        """
        return self._subsidiary__ns

    @subsidiary__ns.setter
    def subsidiary__ns(self, subsidiary__ns):
        """Sets the subsidiary__ns of this ProductRatePlanChargeObjectNSFields.

        Subsidiary associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param subsidiary__ns: The subsidiary__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: str
        """

        self._subsidiary__ns = subsidiary__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501

        Date when the product rate plan charge was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this ProductRatePlanChargeObjectNSFields.

        Date when the product rate plan charge was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this ProductRatePlanChargeObjectNSFields.  # noqa: E501
        :type: str
        """

        self._sync_date__ns = sync_date__ns

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
        if issubclass(ProductRatePlanChargeObjectNSFields, dict):
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
        if not isinstance(other, ProductRatePlanChargeObjectNSFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
