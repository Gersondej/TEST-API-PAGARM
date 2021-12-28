# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_card_response import GetCardResponse
from pagarmeapisdk.models.get_customer_response import GetCustomerResponse
from pagarmeapisdk.models.get_discount_response import GetDiscountResponse
from pagarmeapisdk.models.get_increment_response import GetIncrementResponse
from pagarmeapisdk.models.get_period_response import GetPeriodResponse
from pagarmeapisdk.models.get_setup_response import GetSetupResponse
from pagarmeapisdk.models.get_subscription_item_response import GetSubscriptionItemResponse


class GetSubscriptionResponse(object):

    """Implementation of the 'GetSubscriptionResponse' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        code (string): TODO: type description here.
        start_at (datetime): TODO: type description here.
        interval (string): TODO: type description here.
        interval_count (int): TODO: type description here.
        billing_type (string): TODO: type description here.
        current_cycle (GetPeriodResponse): TODO: type description here.
        payment_method (string): TODO: type description here.
        currency (string): TODO: type description here.
        installments (int): TODO: type description here.
        status (string): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        customer (GetCustomerResponse): TODO: type description here.
        card (GetCardResponse): TODO: type description here.
        items (list of GetSubscriptionItemResponse): TODO: type description
            here.
        statement_descriptor (string): TODO: type description here.
        metadata (dict): TODO: type description here.
        setup (GetSetupResponse): TODO: type description here.
        gateway_affiliation_id (string): Affiliation Code
        next_billing_at (datetime): TODO: type description here.
        billing_day (int): TODO: type description here.
        minimum_price (int): TODO: type description here.
        canceled_at (datetime): TODO: type description here.
        discounts (list of GetDiscountResponse): Subscription discounts
        increments (list of GetIncrementResponse): Subscription increments
        boleto_due_days (int): Days until boleto expires

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "code": 'code',
        "start_at": 'start_at',
        "interval": 'interval',
        "interval_count": 'interval_count',
        "billing_type": 'billing_type',
        "payment_method": 'payment_method',
        "currency": 'currency',
        "installments": 'installments',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "card": 'card',
        "items": 'items',
        "statement_descriptor": 'statement_descriptor',
        "metadata": 'metadata',
        "setup": 'setup',
        "gateway_affiliation_id": 'gateway_affiliation_id',
        "increments": 'increments',
        "current_cycle": 'current_cycle',
        "customer": 'customer',
        "next_billing_at": 'next_billing_at',
        "billing_day": 'billing_day',
        "minimum_price": 'minimum_price',
        "canceled_at": 'canceled_at',
        "discounts": 'discounts',
        "boleto_due_days": 'boleto_due_days'
    }

    def __init__(self,
                 id=None,
                 code=None,
                 start_at=None,
                 interval=None,
                 interval_count=None,
                 billing_type=None,
                 payment_method=None,
                 currency=None,
                 installments=None,
                 status=None,
                 created_at=None,
                 updated_at=None,
                 card=None,
                 items=None,
                 statement_descriptor=None,
                 metadata=None,
                 setup=None,
                 gateway_affiliation_id=None,
                 increments=None,
                 current_cycle=None,
                 customer=None,
                 next_billing_at=None,
                 billing_day=None,
                 minimum_price=None,
                 canceled_at=None,
                 discounts=None,
                 boleto_due_days=None):
        """Constructor for the GetSubscriptionResponse class"""

        # Initialize members of the class
        self.id = id
        self.code = code
        self.start_at = APIHelper.RFC3339DateTime(start_at) if start_at else None
        self.interval = interval
        self.interval_count = interval_count
        self.billing_type = billing_type
        self.current_cycle = current_cycle
        self.payment_method = payment_method
        self.currency = currency
        self.installments = installments
        self.status = status
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.customer = customer
        self.card = card
        self.items = items
        self.statement_descriptor = statement_descriptor
        self.metadata = metadata
        self.setup = setup
        self.gateway_affiliation_id = gateway_affiliation_id
        self.next_billing_at = APIHelper.RFC3339DateTime(next_billing_at) if next_billing_at else None
        self.billing_day = billing_day
        self.minimum_price = minimum_price
        self.canceled_at = APIHelper.RFC3339DateTime(canceled_at) if canceled_at else None
        self.discounts = discounts
        self.increments = increments
        self.boleto_due_days = boleto_due_days

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
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get('id')
        code = dictionary.get('code')
        start_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_at")).datetime if dictionary.get("start_at") else None
        interval = dictionary.get('interval')
        interval_count = dictionary.get('interval_count')
        billing_type = dictionary.get('billing_type')
        payment_method = dictionary.get('payment_method')
        currency = dictionary.get('currency')
        installments = dictionary.get('installments')
        status = dictionary.get('status')
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        card = GetCardResponse.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None
        items = None
        if dictionary.get('items') is not None:
            items = [GetSubscriptionItemResponse.from_dictionary(x) for x in dictionary.get('items')]
        statement_descriptor = dictionary.get('statement_descriptor')
        metadata = dictionary.get('metadata')
        setup = GetSetupResponse.from_dictionary(dictionary.get('setup')) if dictionary.get('setup') else None
        gateway_affiliation_id = dictionary.get('gateway_affiliation_id')
        increments = None
        if dictionary.get('increments') is not None:
            increments = [GetIncrementResponse.from_dictionary(x) for x in dictionary.get('increments')]
        current_cycle = GetPeriodResponse.from_dictionary(dictionary.get('current_cycle')) if dictionary.get('current_cycle') else None
        customer = GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        next_billing_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_billing_at")).datetime if dictionary.get("next_billing_at") else None
        billing_day = dictionary.get('billing_day')
        minimum_price = dictionary.get('minimum_price')
        canceled_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("canceled_at")).datetime if dictionary.get("canceled_at") else None
        discounts = None
        if dictionary.get('discounts') is not None:
            discounts = [GetDiscountResponse.from_dictionary(x) for x in dictionary.get('discounts')]
        boleto_due_days = dictionary.get('boleto_due_days')

        # Return an object of this model
        return cls(id,
                   code,
                   start_at,
                   interval,
                   interval_count,
                   billing_type,
                   payment_method,
                   currency,
                   installments,
                   status,
                   created_at,
                   updated_at,
                   card,
                   items,
                   statement_descriptor,
                   metadata,
                   setup,
                   gateway_affiliation_id,
                   increments,
                   current_cycle,
                   customer,
                   next_billing_at,
                   billing_day,
                   minimum_price,
                   canceled_at,
                   discounts,
                   boleto_due_days)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
