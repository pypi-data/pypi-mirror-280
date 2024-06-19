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

class GetProductRatePlanChargeTierResponse(object):
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
        'currency': 'str',
        'ending_unit': 'float',
        'id': 'str',
        'price': 'float',
        'price_format': 'PriceFormatProductRatePlanChargeTier',
        'starting_unit': 'float',
        'tier': 'int',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'currency': 'Currency',
        'ending_unit': 'EndingUnit',
        'id': 'Id',
        'price': 'Price',
        'price_format': 'PriceFormat',
        'starting_unit': 'StartingUnit',
        'tier': 'Tier',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate'
    }

    def __init__(self, created_by_id=None, created_date=None, currency=None, ending_unit=None, id=None, price=None, price_format=None, starting_unit=None, tier=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """GetProductRatePlanChargeTierResponse - a model defined in Swagger"""  # noqa: E501
        self._created_by_id = None
        self._created_date = None
        self._currency = None
        self._ending_unit = None
        self._id = None
        self._price = None
        self._price_format = None
        self._starting_unit = None
        self._tier = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if currency is not None:
            self.currency = currency
        if ending_unit is not None:
            self.ending_unit = ending_unit
        if id is not None:
            self.id = id
        if price is not None:
            self.price = price
        if price_format is not None:
            self.price_format = price_format
        if starting_unit is not None:
            self.starting_unit = starting_unit
        if tier is not None:
            self.tier = tier
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetProductRatePlanChargeTierResponse.  # noqa: E501

        The ID of the Zuora user who created the ProductRatePlanChargeTier object.   # noqa: E501

        :return: The created_by_id of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetProductRatePlanChargeTierResponse.

        The ID of the Zuora user who created the ProductRatePlanChargeTier object.   # noqa: E501

        :param created_by_id: The created_by_id of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this GetProductRatePlanChargeTierResponse.  # noqa: E501

        The date when the ProductRatePlanChargeTier object was created.   # noqa: E501

        :return: The created_date of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this GetProductRatePlanChargeTierResponse.

        The date when the ProductRatePlanChargeTier object was created.   # noqa: E501

        :param created_date: The created_date of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def currency(self):
        """Gets the currency of this GetProductRatePlanChargeTierResponse.  # noqa: E501

        The valid code corresponding to the currency for the tier's price.   # noqa: E501

        :return: The currency of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetProductRatePlanChargeTierResponse.

        The valid code corresponding to the currency for the tier's price.   # noqa: E501

        :param currency: The currency of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def ending_unit(self):
        """Gets the ending_unit of this GetProductRatePlanChargeTierResponse.  # noqa: E501

        The end number of a range of units for the tier.  **Character limit**: 16  **Values**: any positive decimal value   # noqa: E501

        :return: The ending_unit of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :rtype: float
        """
        return self._ending_unit

    @ending_unit.setter
    def ending_unit(self, ending_unit):
        """Sets the ending_unit of this GetProductRatePlanChargeTierResponse.

        The end number of a range of units for the tier.  **Character limit**: 16  **Values**: any positive decimal value   # noqa: E501

        :param ending_unit: The ending_unit of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :type: float
        """

        self._ending_unit = ending_unit

    @property
    def id(self):
        """Gets the id of this GetProductRatePlanChargeTierResponse.  # noqa: E501

        Object identifier.  # noqa: E501

        :return: The id of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetProductRatePlanChargeTierResponse.

        Object identifier.  # noqa: E501

        :param id: The id of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def price(self):
        """Gets the price of this GetProductRatePlanChargeTierResponse.  # noqa: E501

        The price of the tier if the charge is a flat fee, or the price of each unit in the tier if the charge model is tiered pricing.  **Character limit**: 16  **Values**: a valid currency value   # noqa: E501

        :return: The price of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this GetProductRatePlanChargeTierResponse.

        The price of the tier if the charge is a flat fee, or the price of each unit in the tier if the charge model is tiered pricing.  **Character limit**: 16  **Values**: a valid currency value   # noqa: E501

        :param price: The price of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def price_format(self):
        """Gets the price_format of this GetProductRatePlanChargeTierResponse.  # noqa: E501


        :return: The price_format of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :rtype: PriceFormatProductRatePlanChargeTier
        """
        return self._price_format

    @price_format.setter
    def price_format(self, price_format):
        """Sets the price_format of this GetProductRatePlanChargeTierResponse.


        :param price_format: The price_format of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :type: PriceFormatProductRatePlanChargeTier
        """

        self._price_format = price_format

    @property
    def starting_unit(self):
        """Gets the starting_unit of this GetProductRatePlanChargeTierResponse.  # noqa: E501

        The starting number of a range of units for the tier.  **Character limit**: 16  **Values**: any positive decimal value   # noqa: E501

        :return: The starting_unit of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :rtype: float
        """
        return self._starting_unit

    @starting_unit.setter
    def starting_unit(self, starting_unit):
        """Sets the starting_unit of this GetProductRatePlanChargeTierResponse.

        The starting number of a range of units for the tier.  **Character limit**: 16  **Values**: any positive decimal value   # noqa: E501

        :param starting_unit: The starting_unit of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :type: float
        """

        self._starting_unit = starting_unit

    @property
    def tier(self):
        """Gets the tier of this GetProductRatePlanChargeTierResponse.  # noqa: E501

        A unique number that identifies the tier that the price applies to.  **Character limit**: 20  **Values**: automatically generated   # noqa: E501

        :return: The tier of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :rtype: int
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this GetProductRatePlanChargeTierResponse.

        A unique number that identifies the tier that the price applies to.  **Character limit**: 20  **Values**: automatically generated   # noqa: E501

        :param tier: The tier of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :type: int
        """

        self._tier = tier

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this GetProductRatePlanChargeTierResponse.  # noqa: E501

        The ID of the user who last updated the product rate plan charge tier.   # noqa: E501

        :return: The updated_by_id of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this GetProductRatePlanChargeTierResponse.

        The ID of the user who last updated the product rate plan charge tier.   # noqa: E501

        :param updated_by_id: The updated_by_id of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this GetProductRatePlanChargeTierResponse.  # noqa: E501

        The date when the product rate plan charge tier was last updated.   # noqa: E501

        :return: The updated_date of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this GetProductRatePlanChargeTierResponse.

        The date when the product rate plan charge tier was last updated.   # noqa: E501

        :param updated_date: The updated_date of this GetProductRatePlanChargeTierResponse.  # noqa: E501
        :type: datetime
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
        if issubclass(GetProductRatePlanChargeTierResponse, dict):
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
        if not isinstance(other, GetProductRatePlanChargeTierResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
