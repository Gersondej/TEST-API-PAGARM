# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.create_payment_authentication_request import CreatePaymentAuthenticationRequest


class CreateCheckoutDebitCardPaymentRequest(object):

    """Implementation of the 'CreateCheckoutDebitCardPaymentRequest' model.

    Checkout credit card payment request

    Attributes:
        statement_descriptor (string): Card invoice text descriptor
        authentication (CreatePaymentAuthenticationRequest): Creates payment
            authentication

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "authentication": 'authentication',
        "statement_descriptor": 'statement_descriptor'
    }

    def __init__(self,
                 authentication=None,
                 statement_descriptor=None):
        """Constructor for the CreateCheckoutDebitCardPaymentRequest class"""

        # Initialize members of the class
        self.statement_descriptor = statement_descriptor
        self.authentication = authentication

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
        authentication = CreatePaymentAuthenticationRequest.from_dictionary(dictionary.get('authentication')) if dictionary.get('authentication') else None
        statement_descriptor = dictionary.get('statement_descriptor')

        # Return an object of this model
        return cls(authentication,
                   statement_descriptor)
