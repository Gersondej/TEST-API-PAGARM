# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_card_response import GetCardResponse
from pagarmeapisdk.models.get_customer_response import GetCustomerResponse
from pagarmeapisdk.models.get_setup_response import GetSetupResponse
from pagarmeapisdk.models.get_subscription_boleto_response import GetSubscriptionBoletoResponse
from pagarmeapisdk.models.get_subscription_split_response import GetSubscriptionSplitResponse


class GetSubscriptionResponse(object):

    """Implementation of the 'GetSubscriptionResponse' model.

    TODO: type model description here.

    Attributes:
        id (str): TODO: type description here.
        code (str): TODO: type description here.
        start_at (datetime): TODO: type description here.
        interval (str): TODO: type description here.
        interval_count (int): TODO: type description here.
        billing_type (str): TODO: type description here.
        current_cycle (GetPeriodResponse): TODO: type description here.
        payment_method (str): TODO: type description here.
        currency (str): TODO: type description here.
        installments (int): TODO: type description here.
        status (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        customer (GetCustomerResponse): TODO: type description here.
        card (GetCardResponse): TODO: type description here.
        items (List[GetSubscriptionItemResponse]): TODO: type description here.
        statement_descriptor (str): TODO: type description here.
        metadata (Dict[str, str]): TODO: type description here.
        setup (GetSetupResponse): TODO: type description here.
        gateway_affiliation_id (str): Affiliation Code
        next_billing_at (datetime): TODO: type description here.
        billing_day (int): TODO: type description here.
        minimum_price (int): TODO: type description here.
        canceled_at (datetime): TODO: type description here.
        discounts (List[GetDiscountResponse]): Subscription discounts
        increments (List[GetIncrementResponse]): Subscription increments
        boleto_due_days (int): Days until boleto expires
        split (GetSubscriptionSplitResponse): Subscription's split response
        boleto (GetSubscriptionBoletoResponse): TODO: type description here.
        manual_billing (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "code": 'code',
        "start_at": 'start_at',
        "interval": 'interval',
        "interval_count": 'interval_count',
        "billing_type": 'billing_type',
        "current_cycle": 'current_cycle',
        "payment_method": 'payment_method',
        "currency": 'currency',
        "installments": 'installments',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "customer": 'customer',
        "card": 'card',
        "items": 'items',
        "statement_descriptor": 'statement_descriptor',
        "metadata": 'metadata',
        "setup": 'setup',
        "gateway_affiliation_id": 'gateway_affiliation_id',
        "next_billing_at": 'next_billing_at',
        "billing_day": 'billing_day',
        "minimum_price": 'minimum_price',
        "canceled_at": 'canceled_at',
        "discounts": 'discounts',
        "increments": 'increments',
        "boleto_due_days": 'boleto_due_days',
        "split": 'split',
        "boleto": 'boleto',
        "manual_billing": 'manual_billing'
    }

    _optionals = [
        'id',
        'code',
        'start_at',
        'interval',
        'interval_count',
        'billing_type',
        'current_cycle',
        'payment_method',
        'currency',
        'installments',
        'status',
        'created_at',
        'updated_at',
        'customer',
        'card',
        'items',
        'statement_descriptor',
        'metadata',
        'setup',
        'gateway_affiliation_id',
        'next_billing_at',
        'billing_day',
        'minimum_price',
        'canceled_at',
        'discounts',
        'increments',
        'boleto_due_days',
        'split',
        'boleto',
        'manual_billing',
    ]

    _nullables = [
        'id',
        'code',
        'start_at',
        'interval',
        'interval_count',
        'billing_type',
        'current_cycle',
        'payment_method',
        'currency',
        'installments',
        'status',
        'created_at',
        'updated_at',
        'customer',
        'card',
        'items',
        'statement_descriptor',
        'metadata',
        'setup',
        'gateway_affiliation_id',
        'next_billing_at',
        'billing_day',
        'minimum_price',
        'canceled_at',
        'discounts',
        'increments',
        'boleto_due_days',
        'split',
        'boleto',
        'manual_billing',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 start_at=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_count=APIHelper.SKIP,
                 billing_type=APIHelper.SKIP,
                 current_cycle=APIHelper.SKIP,
                 payment_method=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 installments=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 card=APIHelper.SKIP,
                 items=APIHelper.SKIP,
                 statement_descriptor=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 setup=APIHelper.SKIP,
                 gateway_affiliation_id=APIHelper.SKIP,
                 next_billing_at=APIHelper.SKIP,
                 billing_day=APIHelper.SKIP,
                 minimum_price=APIHelper.SKIP,
                 canceled_at=APIHelper.SKIP,
                 discounts=APIHelper.SKIP,
                 increments=APIHelper.SKIP,
                 boleto_due_days=APIHelper.SKIP,
                 split=APIHelper.SKIP,
                 boleto=APIHelper.SKIP,
                 manual_billing=APIHelper.SKIP):
        """Constructor for the GetSubscriptionResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if code is not APIHelper.SKIP:
            self.code = code 
        if start_at is not APIHelper.SKIP:
            self.start_at = APIHelper.apply_datetime_converter(start_at, APIHelper.RFC3339DateTime) if start_at else None 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_count is not APIHelper.SKIP:
            self.interval_count = interval_count 
        if billing_type is not APIHelper.SKIP:
            self.billing_type = billing_type 
        if current_cycle is not APIHelper.SKIP:
            self.current_cycle = current_cycle 
        if payment_method is not APIHelper.SKIP:
            self.payment_method = payment_method 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if installments is not APIHelper.SKIP:
            self.installments = installments 
        if status is not APIHelper.SKIP:
            self.status = status 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if card is not APIHelper.SKIP:
            self.card = card 
        if items is not APIHelper.SKIP:
            self.items = items 
        if statement_descriptor is not APIHelper.SKIP:
            self.statement_descriptor = statement_descriptor 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if setup is not APIHelper.SKIP:
            self.setup = setup 
        if gateway_affiliation_id is not APIHelper.SKIP:
            self.gateway_affiliation_id = gateway_affiliation_id 
        if next_billing_at is not APIHelper.SKIP:
            self.next_billing_at = APIHelper.apply_datetime_converter(next_billing_at, APIHelper.RFC3339DateTime) if next_billing_at else None 
        if billing_day is not APIHelper.SKIP:
            self.billing_day = billing_day 
        if minimum_price is not APIHelper.SKIP:
            self.minimum_price = minimum_price 
        if canceled_at is not APIHelper.SKIP:
            self.canceled_at = APIHelper.apply_datetime_converter(canceled_at, APIHelper.RFC3339DateTime) if canceled_at else None 
        if discounts is not APIHelper.SKIP:
            self.discounts = discounts 
        if increments is not APIHelper.SKIP:
            self.increments = increments 
        if boleto_due_days is not APIHelper.SKIP:
            self.boleto_due_days = boleto_due_days 
        if split is not APIHelper.SKIP:
            self.split = split 
        if boleto is not APIHelper.SKIP:
            self.boleto = boleto 
        if manual_billing is not APIHelper.SKIP:
            self.manual_billing = manual_billing 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        from pagarmeapisdk.models.get_period_response import GetPeriodResponse
        from pagarmeapisdk.models.get_subscription_item_response import GetSubscriptionItemResponse
        from pagarmeapisdk.models.get_discount_response import GetDiscountResponse
        from pagarmeapisdk.models.get_increment_response import GetIncrementResponse

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        code = dictionary.get("code") if "code" in dictionary.keys() else APIHelper.SKIP
        if 'start_at' in dictionary.keys():
            start_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_at")).datetime if dictionary.get("start_at") else None
        else:
            start_at = APIHelper.SKIP
        interval = dictionary.get("interval") if "interval" in dictionary.keys() else APIHelper.SKIP
        interval_count = dictionary.get("interval_count") if "interval_count" in dictionary.keys() else APIHelper.SKIP
        billing_type = dictionary.get("billing_type") if "billing_type" in dictionary.keys() else APIHelper.SKIP
        if 'current_cycle' in dictionary.keys():
            current_cycle = GetPeriodResponse.from_dictionary(dictionary.get('current_cycle')) if dictionary.get('current_cycle') else None
        else:
            current_cycle = APIHelper.SKIP
        payment_method = dictionary.get("payment_method") if "payment_method" in dictionary.keys() else APIHelper.SKIP
        currency = dictionary.get("currency") if "currency" in dictionary.keys() else APIHelper.SKIP
        installments = dictionary.get("installments") if "installments" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        if 'customer' in dictionary.keys():
            customer = GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        else:
            customer = APIHelper.SKIP
        if 'card' in dictionary.keys():
            card = GetCardResponse.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None
        else:
            card = APIHelper.SKIP
        if 'items' in dictionary.keys():
            items = [GetSubscriptionItemResponse.from_dictionary(x) for x in dictionary.get('items')] if dictionary.get('items') else None
        else:
            items = APIHelper.SKIP
        statement_descriptor = dictionary.get("statement_descriptor") if "statement_descriptor" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if "metadata" in dictionary.keys() else APIHelper.SKIP
        if 'setup' in dictionary.keys():
            setup = GetSetupResponse.from_dictionary(dictionary.get('setup')) if dictionary.get('setup') else None
        else:
            setup = APIHelper.SKIP
        gateway_affiliation_id = dictionary.get("gateway_affiliation_id") if "gateway_affiliation_id" in dictionary.keys() else APIHelper.SKIP
        if 'next_billing_at' in dictionary.keys():
            next_billing_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_billing_at")).datetime if dictionary.get("next_billing_at") else None
        else:
            next_billing_at = APIHelper.SKIP
        billing_day = dictionary.get("billing_day") if "billing_day" in dictionary.keys() else APIHelper.SKIP
        minimum_price = dictionary.get("minimum_price") if "minimum_price" in dictionary.keys() else APIHelper.SKIP
        if 'canceled_at' in dictionary.keys():
            canceled_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("canceled_at")).datetime if dictionary.get("canceled_at") else None
        else:
            canceled_at = APIHelper.SKIP
        if 'discounts' in dictionary.keys():
            discounts = [GetDiscountResponse.from_dictionary(x) for x in dictionary.get('discounts')] if dictionary.get('discounts') else None
        else:
            discounts = APIHelper.SKIP
        if 'increments' in dictionary.keys():
            increments = [GetIncrementResponse.from_dictionary(x) for x in dictionary.get('increments')] if dictionary.get('increments') else None
        else:
            increments = APIHelper.SKIP
        boleto_due_days = dictionary.get("boleto_due_days") if "boleto_due_days" in dictionary.keys() else APIHelper.SKIP
        if 'split' in dictionary.keys():
            split = GetSubscriptionSplitResponse.from_dictionary(dictionary.get('split')) if dictionary.get('split') else None
        else:
            split = APIHelper.SKIP
        if 'boleto' in dictionary.keys():
            boleto = GetSubscriptionBoletoResponse.from_dictionary(dictionary.get('boleto')) if dictionary.get('boleto') else None
        else:
            boleto = APIHelper.SKIP
        manual_billing = dictionary.get("manual_billing") if "manual_billing" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   code,
                   start_at,
                   interval,
                   interval_count,
                   billing_type,
                   current_cycle,
                   payment_method,
                   currency,
                   installments,
                   status,
                   created_at,
                   updated_at,
                   customer,
                   card,
                   items,
                   statement_descriptor,
                   metadata,
                   setup,
                   gateway_affiliation_id,
                   next_billing_at,
                   billing_day,
                   minimum_price,
                   canceled_at,
                   discounts,
                   increments,
                   boleto_due_days,
                   split,
                   boleto,
                   manual_billing)
