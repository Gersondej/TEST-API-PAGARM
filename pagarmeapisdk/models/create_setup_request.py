# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.create_payment_request import CreatePaymentRequest


class CreateSetupRequest(object):

    """Implementation of the 'CreateSetupRequest' model.

    Request for creating a Setup for a subscription. The setup is an order
    that will be created at the subscription creation.

    Attributes:
        amount (int): Setup amount
        description (str): Description
        payment (CreatePaymentRequest): Payment data

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "description": 'description',
        "payment": 'payment'
    }

    def __init__(self,
                 amount=None,
                 description=None,
                 payment=None):
        """Constructor for the CreateSetupRequest class"""

        # Initialize members of the class
        self.amount = amount 
        self.description = description 
        self.payment = payment 

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
        amount = dictionary.get("amount") if dictionary.get("amount") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        payment = CreatePaymentRequest.from_dictionary(dictionary.get('payment')) if dictionary.get('payment') else None
        # Return an object of this model
        return cls(amount,
                   description,
                   payment)
