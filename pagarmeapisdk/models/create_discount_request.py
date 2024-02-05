# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class CreateDiscountRequest(object):

    """Implementation of the 'CreateDiscountRequest' model.

    Request for creating a new discount

    Attributes:
        value (float): The discount value
        discount_type (str): Discount type. Can be either flat or percentage.
        item_id (str): The item where the discount will be applied
        cycles (int): Number of cycles that the discount will be applied
        description (str): Description

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "value": 'value',
        "discount_type": 'discount_type',
        "item_id": 'item_id',
        "cycles": 'cycles',
        "description": 'description'
    }

    _optionals = [
        'cycles',
        'description',
    ]

    def __init__(self,
                 value=None,
                 discount_type=None,
                 item_id=None,
                 cycles=APIHelper.SKIP,
                 description=APIHelper.SKIP):
        """Constructor for the CreateDiscountRequest class"""

        # Initialize members of the class
        self.value = value 
        self.discount_type = discount_type 
        self.item_id = item_id 
        if cycles is not APIHelper.SKIP:
            self.cycles = cycles 
        if description is not APIHelper.SKIP:
            self.description = description 

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
        value = dictionary.get("value") if dictionary.get("value") else None
        discount_type = dictionary.get("discount_type") if dictionary.get("discount_type") else None
        item_id = dictionary.get("item_id") if dictionary.get("item_id") else None
        cycles = dictionary.get("cycles") if dictionary.get("cycles") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        # Return an object of this model
        return cls(value,
                   discount_type,
                   item_id,
                   cycles,
                   description)
