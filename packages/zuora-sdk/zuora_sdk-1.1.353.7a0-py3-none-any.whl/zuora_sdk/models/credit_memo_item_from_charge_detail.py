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

class CreditMemoItemFromChargeDetail(object):
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
        'amount': 'float',
        'charge_id': 'str',
        'comment': 'str',
        'description': 'str',
        'finance_information': 'CreditMemoItemFromChargeDetailFinanceInformation',
        'memo_item_amount': 'float',
        'product_rate_plan_charge_id': 'str',
        'quantity': 'float',
        'service_end_date': 'date',
        'service_start_date': 'date',
        'exclude_item_billing_from_revenue_accounting': 'bool'
    }

    attribute_map = {
        'amount': 'amount',
        'charge_id': 'chargeId',
        'comment': 'comment',
        'description': 'description',
        'finance_information': 'financeInformation',
        'memo_item_amount': 'memoItemAmount',
        'product_rate_plan_charge_id': 'productRatePlanChargeId',
        'quantity': 'quantity',
        'service_end_date': 'serviceEndDate',
        'service_start_date': 'serviceStartDate',
        'exclude_item_billing_from_revenue_accounting': 'excludeItemBillingFromRevenueAccounting'
    }

    def __init__(self, amount=None, charge_id=None, comment=None, description=None, finance_information=None, memo_item_amount=None, product_rate_plan_charge_id=None, quantity=None, service_end_date=None, service_start_date=None, exclude_item_billing_from_revenue_accounting=None):  # noqa: E501
        """CreditMemoItemFromChargeDetail - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._charge_id = None
        self._comment = None
        self._description = None
        self._finance_information = None
        self._memo_item_amount = None
        self._product_rate_plan_charge_id = None
        self._quantity = None
        self._service_end_date = None
        self._service_start_date = None
        self._exclude_item_billing_from_revenue_accounting = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        self.charge_id = charge_id
        if comment is not None:
            self.comment = comment
        if description is not None:
            self.description = description
        if finance_information is not None:
            self.finance_information = finance_information
        if memo_item_amount is not None:
            self.memo_item_amount = memo_item_amount
        self.product_rate_plan_charge_id = product_rate_plan_charge_id
        if quantity is not None:
            self.quantity = quantity
        if service_end_date is not None:
            self.service_end_date = service_end_date
        if service_start_date is not None:
            self.service_start_date = service_start_date
        if exclude_item_billing_from_revenue_accounting is not None:
            self.exclude_item_billing_from_revenue_accounting = exclude_item_billing_from_revenue_accounting

    @property
    def amount(self):
        """Gets the amount of this CreditMemoItemFromChargeDetail.  # noqa: E501

        The amount of the credit memo item.  **Note**: This field is only available if you set the `zuora-version` request header to `224.0` or later.  # noqa: E501

        :return: The amount of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreditMemoItemFromChargeDetail.

        The amount of the credit memo item.  **Note**: This field is only available if you set the `zuora-version` request header to `224.0` or later.  # noqa: E501

        :param amount: The amount of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def charge_id(self):
        """Gets the charge_id of this CreditMemoItemFromChargeDetail.  # noqa: E501

        The ID of the product rate plan charge that the credit memo is created from.  **Note**: This field is not available if you set the `zuora-version` request header to `257.0` or later.  # noqa: E501

        :return: The charge_id of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :rtype: str
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this CreditMemoItemFromChargeDetail.

        The ID of the product rate plan charge that the credit memo is created from.  **Note**: This field is not available if you set the `zuora-version` request header to `257.0` or later.  # noqa: E501

        :param charge_id: The charge_id of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :type: str
        """
        if charge_id is None:
            raise ValueError("Invalid value for `charge_id`, must not be `None`")  # noqa: E501

        self._charge_id = charge_id

    @property
    def comment(self):
        """Gets the comment of this CreditMemoItemFromChargeDetail.  # noqa: E501

        Comments about the product rate plan charge.  **Note**: This field is not available if you set the `zuora-version` request header to `257.0` or later.  # noqa: E501

        :return: The comment of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreditMemoItemFromChargeDetail.

        Comments about the product rate plan charge.  **Note**: This field is not available if you set the `zuora-version` request header to `257.0` or later.  # noqa: E501

        :param comment: The comment of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def description(self):
        """Gets the description of this CreditMemoItemFromChargeDetail.  # noqa: E501

        The description of the product rate plan charge.  **Note**: This field is only available if you set the `zuora-version` request header to `257.0` or later.  # noqa: E501

        :return: The description of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreditMemoItemFromChargeDetail.

        The description of the product rate plan charge.  **Note**: This field is only available if you set the `zuora-version` request header to `257.0` or later.  # noqa: E501

        :param description: The description of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def finance_information(self):
        """Gets the finance_information of this CreditMemoItemFromChargeDetail.  # noqa: E501


        :return: The finance_information of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :rtype: CreditMemoItemFromChargeDetailFinanceInformation
        """
        return self._finance_information

    @finance_information.setter
    def finance_information(self, finance_information):
        """Sets the finance_information of this CreditMemoItemFromChargeDetail.


        :param finance_information: The finance_information of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :type: CreditMemoItemFromChargeDetailFinanceInformation
        """

        self._finance_information = finance_information

    @property
    def memo_item_amount(self):
        """Gets the memo_item_amount of this CreditMemoItemFromChargeDetail.  # noqa: E501

        The amount of the credit memo item.  **Note**: This field is not available if you set the `zuora-version` request header to `224.0` or later.  # noqa: E501

        :return: The memo_item_amount of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :rtype: float
        """
        return self._memo_item_amount

    @memo_item_amount.setter
    def memo_item_amount(self, memo_item_amount):
        """Sets the memo_item_amount of this CreditMemoItemFromChargeDetail.

        The amount of the credit memo item.  **Note**: This field is not available if you set the `zuora-version` request header to `224.0` or later.  # noqa: E501

        :param memo_item_amount: The memo_item_amount of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :type: float
        """

        self._memo_item_amount = memo_item_amount

    @property
    def product_rate_plan_charge_id(self):
        """Gets the product_rate_plan_charge_id of this CreditMemoItemFromChargeDetail.  # noqa: E501

        The ID of the product rate plan charge that the credit memo is created from.  **Note**: This field is only available if you set the `zuora-version` request header to `257.0` or later.  # noqa: E501

        :return: The product_rate_plan_charge_id of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_charge_id

    @product_rate_plan_charge_id.setter
    def product_rate_plan_charge_id(self, product_rate_plan_charge_id):
        """Sets the product_rate_plan_charge_id of this CreditMemoItemFromChargeDetail.

        The ID of the product rate plan charge that the credit memo is created from.  **Note**: This field is only available if you set the `zuora-version` request header to `257.0` or later.  # noqa: E501

        :param product_rate_plan_charge_id: The product_rate_plan_charge_id of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :type: str
        """
        if product_rate_plan_charge_id is None:
            raise ValueError("Invalid value for `product_rate_plan_charge_id`, must not be `None`")  # noqa: E501

        self._product_rate_plan_charge_id = product_rate_plan_charge_id

    @property
    def quantity(self):
        """Gets the quantity of this CreditMemoItemFromChargeDetail.  # noqa: E501

        The number of units for the credit memo item.  # noqa: E501

        :return: The quantity of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CreditMemoItemFromChargeDetail.

        The number of units for the credit memo item.  # noqa: E501

        :param quantity: The quantity of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def service_end_date(self):
        """Gets the service_end_date of this CreditMemoItemFromChargeDetail.  # noqa: E501

        The service end date of the credit memo item. If not specified, the effective end date of the corresponding product rate plan will be used.  # noqa: E501

        :return: The service_end_date of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :rtype: date
        """
        return self._service_end_date

    @service_end_date.setter
    def service_end_date(self, service_end_date):
        """Sets the service_end_date of this CreditMemoItemFromChargeDetail.

        The service end date of the credit memo item. If not specified, the effective end date of the corresponding product rate plan will be used.  # noqa: E501

        :param service_end_date: The service_end_date of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :type: date
        """

        self._service_end_date = service_end_date

    @property
    def service_start_date(self):
        """Gets the service_start_date of this CreditMemoItemFromChargeDetail.  # noqa: E501

        The service start date of the credit memo item. If not specified, the effective start date of the corresponding product rate plan will be used.  # noqa: E501

        :return: The service_start_date of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :rtype: date
        """
        return self._service_start_date

    @service_start_date.setter
    def service_start_date(self, service_start_date):
        """Sets the service_start_date of this CreditMemoItemFromChargeDetail.

        The service start date of the credit memo item. If not specified, the effective start date of the corresponding product rate plan will be used.  # noqa: E501

        :param service_start_date: The service_start_date of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :type: date
        """

        self._service_start_date = service_start_date

    @property
    def exclude_item_billing_from_revenue_accounting(self):
        """Gets the exclude_item_billing_from_revenue_accounting of this CreditMemoItemFromChargeDetail.  # noqa: E501

        The flag to exclude the credit memo item from revenue accounting.  **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :return: The exclude_item_billing_from_revenue_accounting of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_item_billing_from_revenue_accounting

    @exclude_item_billing_from_revenue_accounting.setter
    def exclude_item_billing_from_revenue_accounting(self, exclude_item_billing_from_revenue_accounting):
        """Sets the exclude_item_billing_from_revenue_accounting of this CreditMemoItemFromChargeDetail.

        The flag to exclude the credit memo item from revenue accounting.  **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :param exclude_item_billing_from_revenue_accounting: The exclude_item_billing_from_revenue_accounting of this CreditMemoItemFromChargeDetail.  # noqa: E501
        :type: bool
        """

        self._exclude_item_billing_from_revenue_accounting = exclude_item_billing_from_revenue_accounting

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
        if issubclass(CreditMemoItemFromChargeDetail, dict):
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
        if not isinstance(other, CreditMemoItemFromChargeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
