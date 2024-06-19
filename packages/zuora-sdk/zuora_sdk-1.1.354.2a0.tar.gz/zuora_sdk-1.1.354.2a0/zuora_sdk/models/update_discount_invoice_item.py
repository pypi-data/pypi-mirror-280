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

class UpdateDiscountInvoiceItem(object):
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
        'processing_type': 'str',
        'accounting_code': 'str',
        'adjustment_liability_accounting_code': 'str',
        'adjustment_revenue_accounting_code': 'str',
        'amount': 'float',
        'charge_date': 'str',
        'charge_name': 'str',
        'contract_asset_accounting_code': 'str',
        'contract_liability_accounting_code': 'str',
        'contract_recognized_revenue_accounting_code': 'str',
        'deferred_revenue_accounting_code': 'str',
        'description': 'str',
        'id': 'str',
        'item_type': 'str',
        'purchase_order_number': 'str',
        'recognized_revenue_accounting_code': 'str',
        'rev_rec_code': 'str',
        'rev_rec_trigger_condition': 'RevRecTrigger',
        'revenue_recognition_rule_name': 'str',
        'sku': 'str',
        'unbilled_receivables_accounting_code': 'str',
        'unit_price': 'float',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'sync_date__ns': 'str'
    }

    attribute_map = {
        'processing_type': 'processingType',
        'accounting_code': 'accountingCode',
        'adjustment_liability_accounting_code': 'adjustmentLiabilityAccountingCode',
        'adjustment_revenue_accounting_code': 'adjustmentRevenueAccountingCode',
        'amount': 'amount',
        'charge_date': 'chargeDate',
        'charge_name': 'chargeName',
        'contract_asset_accounting_code': 'contractAssetAccountingCode',
        'contract_liability_accounting_code': 'contractLiabilityAccountingCode',
        'contract_recognized_revenue_accounting_code': 'contractRecognizedRevenueAccountingCode',
        'deferred_revenue_accounting_code': 'deferredRevenueAccountingCode',
        'description': 'description',
        'id': 'id',
        'item_type': 'itemType',
        'purchase_order_number': 'purchaseOrderNumber',
        'recognized_revenue_accounting_code': 'recognizedRevenueAccountingCode',
        'rev_rec_code': 'revRecCode',
        'rev_rec_trigger_condition': 'revRecTriggerCondition',
        'revenue_recognition_rule_name': 'revenueRecognitionRuleName',
        'sku': 'sku',
        'unbilled_receivables_accounting_code': 'unbilledReceivablesAccountingCode',
        'unit_price': 'unitPrice',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'sync_date__ns': 'SyncDate__NS'
    }

    def __init__(self, processing_type=None, accounting_code=None, adjustment_liability_accounting_code=None, adjustment_revenue_accounting_code=None, amount=None, charge_date=None, charge_name=None, contract_asset_accounting_code=None, contract_liability_accounting_code=None, contract_recognized_revenue_accounting_code=None, deferred_revenue_accounting_code=None, description=None, id=None, item_type=None, purchase_order_number=None, recognized_revenue_accounting_code=None, rev_rec_code=None, rev_rec_trigger_condition=None, revenue_recognition_rule_name=None, sku=None, unbilled_receivables_accounting_code=None, unit_price=None, integration_id__ns=None, integration_status__ns=None, sync_date__ns=None):  # noqa: E501
        """UpdateDiscountInvoiceItem - a model defined in Swagger"""  # noqa: E501
        self._processing_type = None
        self._accounting_code = None
        self._adjustment_liability_accounting_code = None
        self._adjustment_revenue_accounting_code = None
        self._amount = None
        self._charge_date = None
        self._charge_name = None
        self._contract_asset_accounting_code = None
        self._contract_liability_accounting_code = None
        self._contract_recognized_revenue_accounting_code = None
        self._deferred_revenue_accounting_code = None
        self._description = None
        self._id = None
        self._item_type = None
        self._purchase_order_number = None
        self._recognized_revenue_accounting_code = None
        self._rev_rec_code = None
        self._rev_rec_trigger_condition = None
        self._revenue_recognition_rule_name = None
        self._sku = None
        self._unbilled_receivables_accounting_code = None
        self._unit_price = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._sync_date__ns = None
        self.discriminator = None
        if processing_type is not None:
            self.processing_type = processing_type
        if accounting_code is not None:
            self.accounting_code = accounting_code
        if adjustment_liability_accounting_code is not None:
            self.adjustment_liability_accounting_code = adjustment_liability_accounting_code
        if adjustment_revenue_accounting_code is not None:
            self.adjustment_revenue_accounting_code = adjustment_revenue_accounting_code
        if amount is not None:
            self.amount = amount
        if charge_date is not None:
            self.charge_date = charge_date
        if charge_name is not None:
            self.charge_name = charge_name
        if contract_asset_accounting_code is not None:
            self.contract_asset_accounting_code = contract_asset_accounting_code
        if contract_liability_accounting_code is not None:
            self.contract_liability_accounting_code = contract_liability_accounting_code
        if contract_recognized_revenue_accounting_code is not None:
            self.contract_recognized_revenue_accounting_code = contract_recognized_revenue_accounting_code
        if deferred_revenue_accounting_code is not None:
            self.deferred_revenue_accounting_code = deferred_revenue_accounting_code
        if description is not None:
            self.description = description
        self.id = id
        if item_type is not None:
            self.item_type = item_type
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if recognized_revenue_accounting_code is not None:
            self.recognized_revenue_accounting_code = recognized_revenue_accounting_code
        if rev_rec_code is not None:
            self.rev_rec_code = rev_rec_code
        if rev_rec_trigger_condition is not None:
            self.rev_rec_trigger_condition = rev_rec_trigger_condition
        if revenue_recognition_rule_name is not None:
            self.revenue_recognition_rule_name = revenue_recognition_rule_name
        if sku is not None:
            self.sku = sku
        if unbilled_receivables_accounting_code is not None:
            self.unbilled_receivables_accounting_code = unbilled_receivables_accounting_code
        if unit_price is not None:
            self.unit_price = unit_price
        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns

    @property
    def processing_type(self):
        """Gets the processing_type of this UpdateDiscountInvoiceItem.  # noqa: E501


        :return: The processing_type of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._processing_type

    @processing_type.setter
    def processing_type(self, processing_type):
        """Sets the processing_type of this UpdateDiscountInvoiceItem.


        :param processing_type: The processing_type of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._processing_type = processing_type

    @property
    def accounting_code(self):
        """Gets the accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501

        The accounting code associated with the discount item.  # noqa: E501

        :return: The accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._accounting_code

    @accounting_code.setter
    def accounting_code(self, accounting_code):
        """Sets the accounting_code of this UpdateDiscountInvoiceItem.

        The accounting code associated with the discount item.  # noqa: E501

        :param accounting_code: The accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._accounting_code = accounting_code

    @property
    def adjustment_liability_accounting_code(self):
        """Gets the adjustment_liability_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501

        The accounting code for adjustment liability. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.  # noqa: E501

        :return: The adjustment_liability_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._adjustment_liability_accounting_code

    @adjustment_liability_accounting_code.setter
    def adjustment_liability_accounting_code(self, adjustment_liability_accounting_code):
        """Sets the adjustment_liability_accounting_code of this UpdateDiscountInvoiceItem.

        The accounting code for adjustment liability. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.  # noqa: E501

        :param adjustment_liability_accounting_code: The adjustment_liability_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._adjustment_liability_accounting_code = adjustment_liability_accounting_code

    @property
    def adjustment_revenue_accounting_code(self):
        """Gets the adjustment_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501

        The accounting code for adjustment revenue. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :return: The adjustment_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._adjustment_revenue_accounting_code

    @adjustment_revenue_accounting_code.setter
    def adjustment_revenue_accounting_code(self, adjustment_revenue_accounting_code):
        """Sets the adjustment_revenue_accounting_code of this UpdateDiscountInvoiceItem.

        The accounting code for adjustment revenue. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :param adjustment_revenue_accounting_code: The adjustment_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._adjustment_revenue_accounting_code = adjustment_revenue_accounting_code

    @property
    def amount(self):
        """Gets the amount of this UpdateDiscountInvoiceItem.  # noqa: E501

        The amount of the discount item. - Should be a negative number. For example, `-10`. - Always a fixed amount no matter whether the discount charge associated with the discount item uses the [fixed-amount model or percentage model](https://knowledgecenter.zuora.com/Billing/Subscriptions/Product_Catalog/B_Charge_Models/B_Discount_Charge_Models#Fixed_amount_model_and_percentage_model). - For tax-exclusive discount items, this amount indicates the discount item amount excluding tax. - For tax-inclusive discount items, this amount indicates the discount item amount including tax.   # noqa: E501

        :return: The amount of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UpdateDiscountInvoiceItem.

        The amount of the discount item. - Should be a negative number. For example, `-10`. - Always a fixed amount no matter whether the discount charge associated with the discount item uses the [fixed-amount model or percentage model](https://knowledgecenter.zuora.com/Billing/Subscriptions/Product_Catalog/B_Charge_Models/B_Discount_Charge_Models#Fixed_amount_model_and_percentage_model). - For tax-exclusive discount items, this amount indicates the discount item amount excluding tax. - For tax-inclusive discount items, this amount indicates the discount item amount including tax.   # noqa: E501

        :param amount: The amount of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def charge_date(self):
        """Gets the charge_date of this UpdateDiscountInvoiceItem.  # noqa: E501

        The date when the discount item is charged, in `yyyy-mm-dd hh:mm:ss` format.  # noqa: E501

        :return: The charge_date of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._charge_date

    @charge_date.setter
    def charge_date(self, charge_date):
        """Sets the charge_date of this UpdateDiscountInvoiceItem.

        The date when the discount item is charged, in `yyyy-mm-dd hh:mm:ss` format.  # noqa: E501

        :param charge_date: The charge_date of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._charge_date = charge_date

    @property
    def charge_name(self):
        """Gets the charge_name of this UpdateDiscountInvoiceItem.  # noqa: E501

        The name of the charge associated with the discount item. This field is required if the `productRatePlanChargeId` field is not specified in the request.   # noqa: E501

        :return: The charge_name of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._charge_name

    @charge_name.setter
    def charge_name(self, charge_name):
        """Sets the charge_name of this UpdateDiscountInvoiceItem.

        The name of the charge associated with the discount item. This field is required if the `productRatePlanChargeId` field is not specified in the request.   # noqa: E501

        :param charge_name: The charge_name of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._charge_name = charge_name

    @property
    def contract_asset_accounting_code(self):
        """Gets the contract_asset_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501

        The accounting code for contract asset. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :return: The contract_asset_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._contract_asset_accounting_code

    @contract_asset_accounting_code.setter
    def contract_asset_accounting_code(self, contract_asset_accounting_code):
        """Sets the contract_asset_accounting_code of this UpdateDiscountInvoiceItem.

        The accounting code for contract asset. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :param contract_asset_accounting_code: The contract_asset_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._contract_asset_accounting_code = contract_asset_accounting_code

    @property
    def contract_liability_accounting_code(self):
        """Gets the contract_liability_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501

        The accounting code for contract liability. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :return: The contract_liability_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._contract_liability_accounting_code

    @contract_liability_accounting_code.setter
    def contract_liability_accounting_code(self, contract_liability_accounting_code):
        """Sets the contract_liability_accounting_code of this UpdateDiscountInvoiceItem.

        The accounting code for contract liability. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :param contract_liability_accounting_code: The contract_liability_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._contract_liability_accounting_code = contract_liability_accounting_code

    @property
    def contract_recognized_revenue_accounting_code(self):
        """Gets the contract_recognized_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501

        The accounting code for contract recognized revenue. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :return: The contract_recognized_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._contract_recognized_revenue_accounting_code

    @contract_recognized_revenue_accounting_code.setter
    def contract_recognized_revenue_accounting_code(self, contract_recognized_revenue_accounting_code):
        """Sets the contract_recognized_revenue_accounting_code of this UpdateDiscountInvoiceItem.

        The accounting code for contract recognized revenue. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :param contract_recognized_revenue_accounting_code: The contract_recognized_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._contract_recognized_revenue_accounting_code = contract_recognized_revenue_accounting_code

    @property
    def deferred_revenue_accounting_code(self):
        """Gets the deferred_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501

        The accounting code for the deferred revenue, such as Monthly Recurring Liability. **Note:** This field is only available if you have Zuora Finance enabled.   # noqa: E501

        :return: The deferred_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._deferred_revenue_accounting_code

    @deferred_revenue_accounting_code.setter
    def deferred_revenue_accounting_code(self, deferred_revenue_accounting_code):
        """Sets the deferred_revenue_accounting_code of this UpdateDiscountInvoiceItem.

        The accounting code for the deferred revenue, such as Monthly Recurring Liability. **Note:** This field is only available if you have Zuora Finance enabled.   # noqa: E501

        :param deferred_revenue_accounting_code: The deferred_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._deferred_revenue_accounting_code = deferred_revenue_accounting_code

    @property
    def description(self):
        """Gets the description of this UpdateDiscountInvoiceItem.  # noqa: E501

        The description of the discount item.   # noqa: E501

        :return: The description of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDiscountInvoiceItem.

        The description of the discount item.   # noqa: E501

        :param description: The description of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this UpdateDiscountInvoiceItem.  # noqa: E501

        The unique ID of the discount item.   # noqa: E501

        :return: The id of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateDiscountInvoiceItem.

        The unique ID of the discount item.   # noqa: E501

        :param id: The id of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def item_type(self):
        """Gets the item_type of this UpdateDiscountInvoiceItem.  # noqa: E501

        The type of the discount item.   # noqa: E501

        :return: The item_type of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this UpdateDiscountInvoiceItem.

        The type of the discount item.   # noqa: E501

        :param item_type: The item_type of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._item_type = item_type

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this UpdateDiscountInvoiceItem.  # noqa: E501

        The purchase order number associated with the discount item.   # noqa: E501

        :return: The purchase_order_number of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this UpdateDiscountInvoiceItem.

        The purchase order number associated with the discount item.   # noqa: E501

        :param purchase_order_number: The purchase_order_number of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._purchase_order_number = purchase_order_number

    @property
    def recognized_revenue_accounting_code(self):
        """Gets the recognized_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501

        The accounting code for the recognized revenue, such as Monthly Recurring Charges or Overage Charges. **Note:** This field is only available if you have Zuora Finance enabled.   # noqa: E501

        :return: The recognized_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._recognized_revenue_accounting_code

    @recognized_revenue_accounting_code.setter
    def recognized_revenue_accounting_code(self, recognized_revenue_accounting_code):
        """Sets the recognized_revenue_accounting_code of this UpdateDiscountInvoiceItem.

        The accounting code for the recognized revenue, such as Monthly Recurring Charges or Overage Charges. **Note:** This field is only available if you have Zuora Finance enabled.   # noqa: E501

        :param recognized_revenue_accounting_code: The recognized_revenue_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._recognized_revenue_accounting_code = recognized_revenue_accounting_code

    @property
    def rev_rec_code(self):
        """Gets the rev_rec_code of this UpdateDiscountInvoiceItem.  # noqa: E501

        The revenue recognition code.  # noqa: E501

        :return: The rev_rec_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._rev_rec_code

    @rev_rec_code.setter
    def rev_rec_code(self, rev_rec_code):
        """Sets the rev_rec_code of this UpdateDiscountInvoiceItem.

        The revenue recognition code.  # noqa: E501

        :param rev_rec_code: The rev_rec_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._rev_rec_code = rev_rec_code

    @property
    def rev_rec_trigger_condition(self):
        """Gets the rev_rec_trigger_condition of this UpdateDiscountInvoiceItem.  # noqa: E501


        :return: The rev_rec_trigger_condition of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: RevRecTrigger
        """
        return self._rev_rec_trigger_condition

    @rev_rec_trigger_condition.setter
    def rev_rec_trigger_condition(self, rev_rec_trigger_condition):
        """Sets the rev_rec_trigger_condition of this UpdateDiscountInvoiceItem.


        :param rev_rec_trigger_condition: The rev_rec_trigger_condition of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: RevRecTrigger
        """

        self._rev_rec_trigger_condition = rev_rec_trigger_condition

    @property
    def revenue_recognition_rule_name(self):
        """Gets the revenue_recognition_rule_name of this UpdateDiscountInvoiceItem.  # noqa: E501

        The name of the revenue recognition rule governing the revenue schedule. **Note:** This field is only available if you have Zuora Finance enabled.   # noqa: E501

        :return: The revenue_recognition_rule_name of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._revenue_recognition_rule_name

    @revenue_recognition_rule_name.setter
    def revenue_recognition_rule_name(self, revenue_recognition_rule_name):
        """Sets the revenue_recognition_rule_name of this UpdateDiscountInvoiceItem.

        The name of the revenue recognition rule governing the revenue schedule. **Note:** This field is only available if you have Zuora Finance enabled.   # noqa: E501

        :param revenue_recognition_rule_name: The revenue_recognition_rule_name of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._revenue_recognition_rule_name = revenue_recognition_rule_name

    @property
    def sku(self):
        """Gets the sku of this UpdateDiscountInvoiceItem.  # noqa: E501

        The SKU of the invoice item. The SKU of the discount item must be different from the SKU of any existing product.   # noqa: E501

        :return: The sku of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this UpdateDiscountInvoiceItem.

        The SKU of the invoice item. The SKU of the discount item must be different from the SKU of any existing product.   # noqa: E501

        :param sku: The sku of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def unbilled_receivables_accounting_code(self):
        """Gets the unbilled_receivables_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501

        The accounting code for unbilled receivables. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :return: The unbilled_receivables_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._unbilled_receivables_accounting_code

    @unbilled_receivables_accounting_code.setter
    def unbilled_receivables_accounting_code(self, unbilled_receivables_accounting_code):
        """Sets the unbilled_receivables_accounting_code of this UpdateDiscountInvoiceItem.

        The accounting code for unbilled receivables. **Note**: This field is only available if you have the Billing - Revenue Integration feature enabled.   # noqa: E501

        :param unbilled_receivables_accounting_code: The unbilled_receivables_accounting_code of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._unbilled_receivables_accounting_code = unbilled_receivables_accounting_code

    @property
    def unit_price(self):
        """Gets the unit_price of this UpdateDiscountInvoiceItem.  # noqa: E501

        The per-unit price of the discount item. If the discount charge associated with the discount item uses the percentage model, the unit price will display as a percentage amount in PDF. For example: if unit price is 5.00, it will display as 5.00% in PDF.   # noqa: E501

        :return: The unit_price of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this UpdateDiscountInvoiceItem.

        The per-unit price of the discount item. If the discount charge associated with the discount item uses the percentage model, the unit price will display as a percentage amount in PDF. For example: if unit price is 5.00, it will display as 5.00% in PDF.   # noqa: E501

        :param unit_price: The unit_price of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this UpdateDiscountInvoiceItem.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this UpdateDiscountInvoiceItem.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this UpdateDiscountInvoiceItem.  # noqa: E501

        Status of the invoice item's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this UpdateDiscountInvoiceItem.

        Status of the invoice item's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this UpdateDiscountInvoiceItem.  # noqa: E501
        :type: str
        """

        self._integration_status__ns = integration_status__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this UpdateDiscountInvoiceItem.  # noqa: E501

        Date when the invoice item was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this UpdateDiscountInvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this UpdateDiscountInvoiceItem.

        Date when the invoice item was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this UpdateDiscountInvoiceItem.  # noqa: E501
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
        if issubclass(UpdateDiscountInvoiceItem, dict):
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
        if not isinstance(other, UpdateDiscountInvoiceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
