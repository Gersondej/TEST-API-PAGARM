# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_recipient_response import GetRecipientResponse


class GetBalanceResponse(object):

    """Implementation of the 'GetBalanceResponse' model.

    Balance

    Attributes:
        currency (str): Currency
        available_amount (long|int): Amount available for transferring
        recipient (GetRecipientResponse): Recipient
        transferred_amount (long|int): TODO: type description here.
        waiting_funds_amount (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency": 'currency',
        "available_amount": 'available_amount',
        "recipient": 'recipient',
        "transferred_amount": 'transferred_amount',
        "waiting_funds_amount": 'waiting_funds_amount'
    }

    _optionals = [
        'currency',
        'available_amount',
        'recipient',
        'transferred_amount',
        'waiting_funds_amount',
    ]

    _nullables = [
        'currency',
        'available_amount',
        'recipient',
        'transferred_amount',
        'waiting_funds_amount',
    ]

    def __init__(self,
                 currency=APIHelper.SKIP,
                 available_amount=APIHelper.SKIP,
                 recipient=APIHelper.SKIP,
                 transferred_amount=APIHelper.SKIP,
                 waiting_funds_amount=APIHelper.SKIP):
        """Constructor for the GetBalanceResponse class"""

        # Initialize members of the class
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if available_amount is not APIHelper.SKIP:
            self.available_amount = available_amount 
        if recipient is not APIHelper.SKIP:
            self.recipient = recipient 
        if transferred_amount is not APIHelper.SKIP:
            self.transferred_amount = transferred_amount 
        if waiting_funds_amount is not APIHelper.SKIP:
            self.waiting_funds_amount = waiting_funds_amount 

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
        currency = dictionary.get("currency") if "currency" in dictionary.keys() else APIHelper.SKIP
        available_amount = dictionary.get("available_amount") if "available_amount" in dictionary.keys() else APIHelper.SKIP
        if 'recipient' in dictionary.keys():
            recipient = GetRecipientResponse.from_dictionary(dictionary.get('recipient')) if dictionary.get('recipient') else None
        else:
            recipient = APIHelper.SKIP
        transferred_amount = dictionary.get("transferred_amount") if "transferred_amount" in dictionary.keys() else APIHelper.SKIP
        waiting_funds_amount = dictionary.get("waiting_funds_amount") if "waiting_funds_amount" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(currency,
                   available_amount,
                   recipient,
                   transferred_amount,
                   waiting_funds_amount)
