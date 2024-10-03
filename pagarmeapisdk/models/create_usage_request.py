# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class CreateUsageRequest(object):

    """Implementation of the 'CreateUsageRequest' model.

    Request for creating a usage

    Attributes:
        quantity (int): TODO: type description here.
        description (str): TODO: type description here.
        used_at (datetime): TODO: type description here.
        code (str): Identification code in the client system
        group (str): identification group in the client system
        amount (int): Field used in item scheme type 'Percent'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quantity": 'quantity',
        "description": 'description',
        "used_at": 'used_at',
        "code": 'code',
        "group": 'group',
        "amount": 'amount'
    }

    _optionals = [
        'code',
        'group',
        'amount',
    ]

    def __init__(self,
                 quantity=None,
                 description=None,
                 used_at=None,
                 code=APIHelper.SKIP,
                 group=APIHelper.SKIP,
                 amount=APIHelper.SKIP):
        """Constructor for the CreateUsageRequest class"""

        # Initialize members of the class
        self.quantity = quantity 
        self.description = description 
        self.used_at = APIHelper.apply_datetime_converter(used_at, APIHelper.RFC3339DateTime) if used_at else None 
        if code is not APIHelper.SKIP:
            self.code = code 
        if group is not APIHelper.SKIP:
            self.group = group 
        if amount is not APIHelper.SKIP:
            self.amount = amount 

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
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        used_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("used_at")).datetime if dictionary.get("used_at") else None
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        group = dictionary.get("group") if dictionary.get("group") else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        # Return an object of this model
        return cls(quantity,
                   description,
                   used_at,
                   code,
                   group,
                   amount)
