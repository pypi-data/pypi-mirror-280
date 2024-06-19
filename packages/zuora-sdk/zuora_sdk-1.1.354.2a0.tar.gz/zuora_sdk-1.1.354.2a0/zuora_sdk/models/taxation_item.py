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

class TaxationItem(object):
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
        'created_date': 'str',
        'exempt_amount': 'float',
        'finance_information': 'TaxationItemFinanceInformation',
        'id': 'str',
        'invoice_item_id': 'str',
        'jurisdiction': 'str',
        'location_code': 'str',
        'memo_item_id': 'str',
        'name': 'str',
        'source_tax_item_id': 'str',
        'tax_amount': 'float',
        'applicable_tax_un_rounded': 'float',
        'country': 'str',
        'tax_code': 'str',
        'tax_code_description': 'str',
        'tax_date': 'date',
        'tax_mode': 'TaxMode',
        'tax_rate': 'float',
        'tax_rate_description': 'str',
        'tax_rate_type': 'TaxRateType',
        'updated_by_id': 'str',
        'updated_date': 'str'
    }

    attribute_map = {
        'created_by_id': 'createdById',
        'created_date': 'createdDate',
        'exempt_amount': 'exemptAmount',
        'finance_information': 'financeInformation',
        'id': 'id',
        'invoice_item_id': 'invoiceItemId',
        'jurisdiction': 'jurisdiction',
        'location_code': 'locationCode',
        'memo_item_id': 'memoItemId',
        'name': 'name',
        'source_tax_item_id': 'sourceTaxItemId',
        'tax_amount': 'taxAmount',
        'applicable_tax_un_rounded': 'applicableTaxUnRounded',
        'country': 'country',
        'tax_code': 'taxCode',
        'tax_code_description': 'taxCodeDescription',
        'tax_date': 'taxDate',
        'tax_mode': 'taxMode',
        'tax_rate': 'taxRate',
        'tax_rate_description': 'taxRateDescription',
        'tax_rate_type': 'taxRateType',
        'updated_by_id': 'updatedById',
        'updated_date': 'updatedDate'
    }

    def __init__(self, created_by_id=None, created_date=None, exempt_amount=None, finance_information=None, id=None, invoice_item_id=None, jurisdiction=None, location_code=None, memo_item_id=None, name=None, source_tax_item_id=None, tax_amount=None, applicable_tax_un_rounded=None, country=None, tax_code=None, tax_code_description=None, tax_date=None, tax_mode=None, tax_rate=None, tax_rate_description=None, tax_rate_type=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """TaxationItem - a model defined in Swagger"""  # noqa: E501
        self._created_by_id = None
        self._created_date = None
        self._exempt_amount = None
        self._finance_information = None
        self._id = None
        self._invoice_item_id = None
        self._jurisdiction = None
        self._location_code = None
        self._memo_item_id = None
        self._name = None
        self._source_tax_item_id = None
        self._tax_amount = None
        self._applicable_tax_un_rounded = None
        self._country = None
        self._tax_code = None
        self._tax_code_description = None
        self._tax_date = None
        self._tax_mode = None
        self._tax_rate = None
        self._tax_rate_description = None
        self._tax_rate_type = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if exempt_amount is not None:
            self.exempt_amount = exempt_amount
        if finance_information is not None:
            self.finance_information = finance_information
        if id is not None:
            self.id = id
        if invoice_item_id is not None:
            self.invoice_item_id = invoice_item_id
        if jurisdiction is not None:
            self.jurisdiction = jurisdiction
        if location_code is not None:
            self.location_code = location_code
        if memo_item_id is not None:
            self.memo_item_id = memo_item_id
        if name is not None:
            self.name = name
        if source_tax_item_id is not None:
            self.source_tax_item_id = source_tax_item_id
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if applicable_tax_un_rounded is not None:
            self.applicable_tax_un_rounded = applicable_tax_un_rounded
        if country is not None:
            self.country = country
        if tax_code is not None:
            self.tax_code = tax_code
        if tax_code_description is not None:
            self.tax_code_description = tax_code_description
        if tax_date is not None:
            self.tax_date = tax_date
        if tax_mode is not None:
            self.tax_mode = tax_mode
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if tax_rate_description is not None:
            self.tax_rate_description = tax_rate_description
        if tax_rate_type is not None:
            self.tax_rate_type = tax_rate_type
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def created_by_id(self):
        """Gets the created_by_id of this TaxationItem.  # noqa: E501

        The ID of the Zuora user who created the taxation item.  # noqa: E501

        :return: The created_by_id of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this TaxationItem.

        The ID of the Zuora user who created the taxation item.  # noqa: E501

        :param created_by_id: The created_by_id of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this TaxationItem.  # noqa: E501

        The date and time when the taxation item was created in the Zuora system, in `yyyy-mm-dd hh:mm:ss` format.  # noqa: E501

        :return: The created_date of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this TaxationItem.

        The date and time when the taxation item was created in the Zuora system, in `yyyy-mm-dd hh:mm:ss` format.  # noqa: E501

        :param created_date: The created_date of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def exempt_amount(self):
        """Gets the exempt_amount of this TaxationItem.  # noqa: E501

        The calculated tax amount excluded due to the exemption.  # noqa: E501

        :return: The exempt_amount of this TaxationItem.  # noqa: E501
        :rtype: float
        """
        return self._exempt_amount

    @exempt_amount.setter
    def exempt_amount(self, exempt_amount):
        """Sets the exempt_amount of this TaxationItem.

        The calculated tax amount excluded due to the exemption.  # noqa: E501

        :param exempt_amount: The exempt_amount of this TaxationItem.  # noqa: E501
        :type: float
        """

        self._exempt_amount = exempt_amount

    @property
    def finance_information(self):
        """Gets the finance_information of this TaxationItem.  # noqa: E501


        :return: The finance_information of this TaxationItem.  # noqa: E501
        :rtype: TaxationItemFinanceInformation
        """
        return self._finance_information

    @finance_information.setter
    def finance_information(self, finance_information):
        """Sets the finance_information of this TaxationItem.


        :param finance_information: The finance_information of this TaxationItem.  # noqa: E501
        :type: TaxationItemFinanceInformation
        """

        self._finance_information = finance_information

    @property
    def id(self):
        """Gets the id of this TaxationItem.  # noqa: E501

        The ID of the taxation item.  # noqa: E501

        :return: The id of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaxationItem.

        The ID of the taxation item.  # noqa: E501

        :param id: The id of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_item_id(self):
        """Gets the invoice_item_id of this TaxationItem.  # noqa: E501

        The ID of the invoice associated with the taxation item.  # noqa: E501

        :return: The invoice_item_id of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._invoice_item_id

    @invoice_item_id.setter
    def invoice_item_id(self, invoice_item_id):
        """Sets the invoice_item_id of this TaxationItem.

        The ID of the invoice associated with the taxation item.  # noqa: E501

        :param invoice_item_id: The invoice_item_id of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._invoice_item_id = invoice_item_id

    @property
    def jurisdiction(self):
        """Gets the jurisdiction of this TaxationItem.  # noqa: E501

        The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.  # noqa: E501

        :return: The jurisdiction of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._jurisdiction

    @jurisdiction.setter
    def jurisdiction(self, jurisdiction):
        """Sets the jurisdiction of this TaxationItem.

        The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.  # noqa: E501

        :param jurisdiction: The jurisdiction of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._jurisdiction = jurisdiction

    @property
    def location_code(self):
        """Gets the location_code of this TaxationItem.  # noqa: E501

        The identifier for the location based on the value of the `taxCode` field.  # noqa: E501

        :return: The location_code of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._location_code

    @location_code.setter
    def location_code(self, location_code):
        """Sets the location_code of this TaxationItem.

        The identifier for the location based on the value of the `taxCode` field.  # noqa: E501

        :param location_code: The location_code of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._location_code = location_code

    @property
    def memo_item_id(self):
        """Gets the memo_item_id of this TaxationItem.  # noqa: E501

        The identifier for the memo item which is related to this tax item  # noqa: E501

        :return: The memo_item_id of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._memo_item_id

    @memo_item_id.setter
    def memo_item_id(self, memo_item_id):
        """Sets the memo_item_id of this TaxationItem.

        The identifier for the memo item which is related to this tax item  # noqa: E501

        :param memo_item_id: The memo_item_id of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._memo_item_id = memo_item_id

    @property
    def name(self):
        """Gets the name of this TaxationItem.  # noqa: E501

        The name of the taxation item.  # noqa: E501

        :return: The name of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaxationItem.

        The name of the taxation item.  # noqa: E501

        :param name: The name of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source_tax_item_id(self):
        """Gets the source_tax_item_id of this TaxationItem.  # noqa: E501

        The identifier for which tax item the credit memo/debit memo was given to  # noqa: E501

        :return: The source_tax_item_id of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._source_tax_item_id

    @source_tax_item_id.setter
    def source_tax_item_id(self, source_tax_item_id):
        """Sets the source_tax_item_id of this TaxationItem.

        The identifier for which tax item the credit memo/debit memo was given to  # noqa: E501

        :param source_tax_item_id: The source_tax_item_id of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._source_tax_item_id = source_tax_item_id

    @property
    def tax_amount(self):
        """Gets the tax_amount of this TaxationItem.  # noqa: E501

        The amount of the tax applied to the invoice.  # noqa: E501

        :return: The tax_amount of this TaxationItem.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this TaxationItem.

        The amount of the tax applied to the invoice.  # noqa: E501

        :param tax_amount: The tax_amount of this TaxationItem.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def applicable_tax_un_rounded(self):
        """Gets the applicable_tax_un_rounded of this TaxationItem.  # noqa: E501

        The unrounded amount of the tax.  # noqa: E501

        :return: The applicable_tax_un_rounded of this TaxationItem.  # noqa: E501
        :rtype: float
        """
        return self._applicable_tax_un_rounded

    @applicable_tax_un_rounded.setter
    def applicable_tax_un_rounded(self, applicable_tax_un_rounded):
        """Sets the applicable_tax_un_rounded of this TaxationItem.

        The unrounded amount of the tax.  # noqa: E501

        :param applicable_tax_un_rounded: The applicable_tax_un_rounded of this TaxationItem.  # noqa: E501
        :type: float
        """

        self._applicable_tax_un_rounded = applicable_tax_un_rounded

    @property
    def country(self):
        """Gets the country of this TaxationItem.  # noqa: E501

        The field which contains country code.  # noqa: E501

        :return: The country of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this TaxationItem.

        The field which contains country code.  # noqa: E501

        :param country: The country of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def tax_code(self):
        """Gets the tax_code of this TaxationItem.  # noqa: E501

        The tax code identifies which tax rules and tax rates to apply to a specific invoice.  # noqa: E501

        :return: The tax_code of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._tax_code

    @tax_code.setter
    def tax_code(self, tax_code):
        """Sets the tax_code of this TaxationItem.

        The tax code identifies which tax rules and tax rates to apply to a specific invoice.  # noqa: E501

        :param tax_code: The tax_code of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._tax_code = tax_code

    @property
    def tax_code_description(self):
        """Gets the tax_code_description of this TaxationItem.  # noqa: E501

        The description of the tax code.  # noqa: E501

        :return: The tax_code_description of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._tax_code_description

    @tax_code_description.setter
    def tax_code_description(self, tax_code_description):
        """Sets the tax_code_description of this TaxationItem.

        The description of the tax code.  # noqa: E501

        :param tax_code_description: The tax_code_description of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._tax_code_description = tax_code_description

    @property
    def tax_date(self):
        """Gets the tax_date of this TaxationItem.  # noqa: E501

        The date when the tax is applied to the invoice.  # noqa: E501

        :return: The tax_date of this TaxationItem.  # noqa: E501
        :rtype: date
        """
        return self._tax_date

    @tax_date.setter
    def tax_date(self, tax_date):
        """Sets the tax_date of this TaxationItem.

        The date when the tax is applied to the invoice.  # noqa: E501

        :param tax_date: The tax_date of this TaxationItem.  # noqa: E501
        :type: date
        """

        self._tax_date = tax_date

    @property
    def tax_mode(self):
        """Gets the tax_mode of this TaxationItem.  # noqa: E501


        :return: The tax_mode of this TaxationItem.  # noqa: E501
        :rtype: TaxMode
        """
        return self._tax_mode

    @tax_mode.setter
    def tax_mode(self, tax_mode):
        """Sets the tax_mode of this TaxationItem.


        :param tax_mode: The tax_mode of this TaxationItem.  # noqa: E501
        :type: TaxMode
        """

        self._tax_mode = tax_mode

    @property
    def tax_rate(self):
        """Gets the tax_rate of this TaxationItem.  # noqa: E501

        The tax rate applied to the invoice.  # noqa: E501

        :return: The tax_rate of this TaxationItem.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this TaxationItem.

        The tax rate applied to the invoice.  # noqa: E501

        :param tax_rate: The tax_rate of this TaxationItem.  # noqa: E501
        :type: float
        """

        self._tax_rate = tax_rate

    @property
    def tax_rate_description(self):
        """Gets the tax_rate_description of this TaxationItem.  # noqa: E501

        The description of the tax rate.  # noqa: E501

        :return: The tax_rate_description of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._tax_rate_description

    @tax_rate_description.setter
    def tax_rate_description(self, tax_rate_description):
        """Sets the tax_rate_description of this TaxationItem.

        The description of the tax rate.  # noqa: E501

        :param tax_rate_description: The tax_rate_description of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._tax_rate_description = tax_rate_description

    @property
    def tax_rate_type(self):
        """Gets the tax_rate_type of this TaxationItem.  # noqa: E501


        :return: The tax_rate_type of this TaxationItem.  # noqa: E501
        :rtype: TaxRateType
        """
        return self._tax_rate_type

    @tax_rate_type.setter
    def tax_rate_type(self, tax_rate_type):
        """Sets the tax_rate_type of this TaxationItem.


        :param tax_rate_type: The tax_rate_type of this TaxationItem.  # noqa: E501
        :type: TaxRateType
        """

        self._tax_rate_type = tax_rate_type

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this TaxationItem.  # noqa: E501

        The ID of the Zuora user who last updated the taxation item.  # noqa: E501

        :return: The updated_by_id of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this TaxationItem.

        The ID of the Zuora user who last updated the taxation item.  # noqa: E501

        :param updated_by_id: The updated_by_id of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this TaxationItem.  # noqa: E501

        The date and time when the taxation item was last updated, in `yyyy-mm-dd hh:mm:ss` format.  # noqa: E501

        :return: The updated_date of this TaxationItem.  # noqa: E501
        :rtype: str
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this TaxationItem.

        The date and time when the taxation item was last updated, in `yyyy-mm-dd hh:mm:ss` format.  # noqa: E501

        :param updated_date: The updated_date of this TaxationItem.  # noqa: E501
        :type: str
        """

        self._updated_date = updated_date

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
        if issubclass(TaxationItem, dict):
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
        if not isinstance(other, TaxationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
