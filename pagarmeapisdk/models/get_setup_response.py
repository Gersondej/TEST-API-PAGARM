# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetSetupResponse(object):

    """Implementation of the 'GetSetupResponse' model.

    Response object for getting the setup from a subscription

    Attributes:
        id (str): TODO: type description here.
        description (str): TODO: type description here.
        amount (int): TODO: type description here.
        status (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "description": 'description',
        "amount": 'amount',
        "status": 'status'
    }

    _optionals = [
        'id',
        'description',
        'amount',
        'status',
    ]

    _nullables = [
        'id',
        'description',
        'amount',
        'status',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the GetSetupResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if description is not APIHelper.SKIP:
            self.description = description 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if status is not APIHelper.SKIP:
            self.status = status 

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
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   description,
                   amount,
                   status)
