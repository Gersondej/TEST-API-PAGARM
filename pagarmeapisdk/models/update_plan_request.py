# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class UpdatePlanRequest(object):

    """Implementation of the 'UpdatePlanRequest' model.

    Request for updating a plan

    Attributes:
        name (str): Plan's name
        description (str): Description
        installments (List[int]): Number os installments
        statement_descriptor (str): Text that will be shown on the credit
            card's statement
        currency (str): Currency
        interval (str): Interval
        interval_count (int): Interval count
        payment_methods (List[str]): Payment methods accepted by the plan
        billing_type (str): Billing type
        status (str): Plan status
        shippable (bool): Indicates if the plan is shippable
        billing_days (List[int]): Billing days accepted by the plan
        metadata (Dict[str, str]): Metadata
        minimum_price (int): Minimum price
        trial_period_days (int): Number of trial period in days, where the
            customer will not be charged

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "description": 'description',
        "installments": 'installments',
        "statement_descriptor": 'statement_descriptor',
        "currency": 'currency',
        "interval": 'interval',
        "interval_count": 'interval_count',
        "payment_methods": 'payment_methods',
        "billing_type": 'billing_type',
        "status": 'status',
        "shippable": 'shippable',
        "billing_days": 'billing_days',
        "metadata": 'metadata',
        "minimum_price": 'minimum_price',
        "trial_period_days": 'trial_period_days'
    }

    _optionals = [
        'minimum_price',
        'trial_period_days',
    ]

    def __init__(self,
                 name=None,
                 description=None,
                 installments=None,
                 statement_descriptor=None,
                 currency=None,
                 interval=None,
                 interval_count=None,
                 payment_methods=None,
                 billing_type=None,
                 status=None,
                 shippable=None,
                 billing_days=None,
                 metadata=None,
                 minimum_price=APIHelper.SKIP,
                 trial_period_days=APIHelper.SKIP):
        """Constructor for the UpdatePlanRequest class"""

        # Initialize members of the class
        self.name = name 
        self.description = description 
        self.installments = installments 
        self.statement_descriptor = statement_descriptor 
        self.currency = currency 
        self.interval = interval 
        self.interval_count = interval_count 
        self.payment_methods = payment_methods 
        self.billing_type = billing_type 
        self.status = status 
        self.shippable = shippable 
        self.billing_days = billing_days 
        self.metadata = metadata 
        if minimum_price is not APIHelper.SKIP:
            self.minimum_price = minimum_price 
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
        installments = dictionary.get("installments") if dictionary.get("installments") else None
        statement_descriptor = dictionary.get("statement_descriptor") if dictionary.get("statement_descriptor") else None
        currency = dictionary.get("currency") if dictionary.get("currency") else None
        interval = dictionary.get("interval") if dictionary.get("interval") else None
        interval_count = dictionary.get("interval_count") if dictionary.get("interval_count") else None
        payment_methods = dictionary.get("payment_methods") if dictionary.get("payment_methods") else None
        billing_type = dictionary.get("billing_type") if dictionary.get("billing_type") else None
        status = dictionary.get("status") if dictionary.get("status") else None
        shippable = dictionary.get("shippable") if "shippable" in dictionary.keys() else None
        billing_days = dictionary.get("billing_days") if dictionary.get("billing_days") else None
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else None
        minimum_price = dictionary.get("minimum_price") if dictionary.get("minimum_price") else APIHelper.SKIP
        trial_period_days = dictionary.get("trial_period_days") if dictionary.get("trial_period_days") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   description,
                   installments,
                   statement_descriptor,
                   currency,
                   interval,
                   interval_count,
                   payment_methods,
                   billing_type,
                   status,
                   shippable,
                   billing_days,
                   metadata,
                   minimum_price,
                   trial_period_days)
