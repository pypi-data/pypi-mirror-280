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

class GetProductRatePlansByProductResponse(object):
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
        'next_page': 'str',
        'product_rate_plans': 'list[ProductRatePlan]',
        'success': 'bool'
    }

    attribute_map = {
        'next_page': 'nextPage',
        'product_rate_plans': 'productRatePlans',
        'success': 'success'
    }

    def __init__(self, next_page=None, product_rate_plans=None, success=None):  # noqa: E501
        """GetProductRatePlansByProductResponse - a model defined in Swagger"""  # noqa: E501
        self._next_page = None
        self._product_rate_plans = None
        self._success = None
        self.discriminator = None
        if next_page is not None:
            self.next_page = next_page
        if product_rate_plans is not None:
            self.product_rate_plans = product_rate_plans
        if success is not None:
            self.success = success

    @property
    def next_page(self):
        """Gets the next_page of this GetProductRatePlansByProductResponse.  # noqa: E501

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :return: The next_page of this GetProductRatePlansByProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this GetProductRatePlansByProductResponse.

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :param next_page: The next_page of this GetProductRatePlansByProductResponse.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def product_rate_plans(self):
        """Gets the product_rate_plans of this GetProductRatePlansByProductResponse.  # noqa: E501

        Container for one or more product rate plans.   # noqa: E501

        :return: The product_rate_plans of this GetProductRatePlansByProductResponse.  # noqa: E501
        :rtype: list[ProductRatePlan]
        """
        return self._product_rate_plans

    @product_rate_plans.setter
    def product_rate_plans(self, product_rate_plans):
        """Sets the product_rate_plans of this GetProductRatePlansByProductResponse.

        Container for one or more product rate plans.   # noqa: E501

        :param product_rate_plans: The product_rate_plans of this GetProductRatePlansByProductResponse.  # noqa: E501
        :type: list[ProductRatePlan]
        """

        self._product_rate_plans = product_rate_plans

    @property
    def success(self):
        """Gets the success of this GetProductRatePlansByProductResponse.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this GetProductRatePlansByProductResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GetProductRatePlansByProductResponse.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this GetProductRatePlansByProductResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(GetProductRatePlansByProductResponse, dict):
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
        if not isinstance(other, GetProductRatePlansByProductResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
