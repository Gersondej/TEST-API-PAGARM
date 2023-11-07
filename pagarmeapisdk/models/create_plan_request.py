# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_plan_item_request import CreatePlanItemRequest
from pagarmeapisdk.models.create_pricing_scheme_request import CreatePricingSchemeRequest


class CreatePlanRequest(object):

    """Implementation of the 'CreatePlanRequest' model.

    Request for creating a plan

    Attributes:
        name (str): Plan's name
        description (str): Description
        statement_descriptor (str): Text that will be printed on the credit
            card's statement
        items (List[CreatePlanItemRequest]): Plan items
        shippable (bool): Indicates if the plan is shippable
        payment_methods (List[str]): Allowed payment methods for the plan
        installments (List[int]): Number of installments
        currency (str): Currency
        interval (str): Interval
        interval_count (int): Interval counts between two charges. For
            instance, if the interval is 'month' and count is 2, the customer
            will be charged once every two months.
        billing_days (List[int]): Allowed billings days for the subscription,
            in case the plan type is 'exact_day'
        billing_type (str): Billing type
        pricing_scheme (CreatePricingSchemeRequest): Plan's pricing scheme
        metadata (Dict[str, str]): Metadata
        minimum_price (int): Minimum price that will be charged
        cycles (int): Number of cycles
        quantity (int): Quantity
        trial_period_days (int): Trial period, where the customer will not be
            charged.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "description": 'description',
        "statement_descriptor": 'statement_descriptor',
        "items": 'items',
        "shippable": 'shippable',
        "payment_methods": 'payment_methods',
        "installments": 'installments',
        "currency": 'currency',
        "interval": 'interval',
        "interval_count": 'interval_count',
        "billing_days": 'billing_days',
        "billing_type": 'billing_type',
        "pricing_scheme": 'pricing_scheme',
        "metadata": 'metadata',
        "minimum_price": 'minimum_price',
        "cycles": 'cycles',
        "quantity": 'quantity',
        "trial_period_days": 'trial_period_days'
    }

    _optionals = [
        'minimum_price',
        'cycles',
        'quantity',
        'trial_period_days',
    ]

    def __init__(self,
                 name=None,
                 description=None,
                 statement_descriptor=None,
                 items=None,
                 shippable=None,
                 payment_methods=None,
                 installments=None,
                 currency=None,
                 interval=None,
                 interval_count=None,
                 billing_days=None,
                 billing_type=None,
                 pricing_scheme=None,
                 metadata=None,
                 minimum_price=APIHelper.SKIP,
                 cycles=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 trial_period_days=APIHelper.SKIP):
        """Constructor for the CreatePlanRequest class"""

        # Initialize members of the class
        self.name = name 
        self.description = description 
        self.statement_descriptor = statement_descriptor 
        self.items = items 
        self.shippable = shippable 
        self.payment_methods = payment_methods 
        self.installments = installments 
        self.currency = currency 
        self.interval = interval 
        self.interval_count = interval_count 
        self.billing_days = billing_days 
        self.billing_type = billing_type 
        self.pricing_scheme = pricing_scheme 
        self.metadata = metadata 
        if minimum_price is not APIHelper.SKIP:
            self.minimum_price = minimum_price 
        if cycles is not APIHelper.SKIP:
            self.cycles = cycles 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if trial_period_days is not APIHelper.SKIP:
            self.trial_period_days = trial_period_days 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        statement_descriptor = dictionary.get("statement_descriptor") if dictionary.get("statement_descriptor") else None
        items = None
        if dictionary.get('items') is not None:
            items = [CreatePlanItemRequest.from_dictionary(x) for x in dictionary.get('items')]
        shippable = dictionary.get("shippable") if "shippable" in dictionary.keys() else None
        payment_methods = dictionary.get("payment_methods") if dictionary.get("payment_methods") else None
        installments = dictionary.get("installments") if dictionary.get("installments") else None
        currency = dictionary.get("currency") if dictionary.get("currency") else None
        interval = dictionary.get("interval") if dictionary.get("interval") else None
        interval_count = dictionary.get("interval_count") if dictionary.get("interval_count") else None
        billing_days = dictionary.get("billing_days") if dictionary.get("billing_days") else None
        billing_type = dictionary.get("billing_type") if dictionary.get("billing_type") else None
        pricing_scheme = CreatePricingSchemeRequest.from_dictionary(dictionary.get('pricing_scheme')) if dictionary.get('pricing_scheme') else None
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else None
        minimum_price = dictionary.get("minimum_price") if dictionary.get("minimum_price") else APIHelper.SKIP
        cycles = dictionary.get("cycles") if dictionary.get("cycles") else APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        trial_period_days = dictionary.get("trial_period_days") if dictionary.get("trial_period_days") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   description,
                   statement_descriptor,
                   items,
                   shippable,
                   payment_methods,
                   installments,
                   currency,
                   interval,
                   interval_count,
                   billing_days,
                   billing_type,
                   pricing_scheme,
                   metadata,
                   minimum_price,
                   cycles,
                   quantity,
                   trial_period_days)
