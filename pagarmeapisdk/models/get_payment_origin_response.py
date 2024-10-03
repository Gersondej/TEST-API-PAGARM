# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetPaymentOriginResponse(object):

    """Implementation of the 'GetPaymentOriginResponse' model.

    TODO: type model description here.

    Attributes:
        charge_id (str): TODO: type description here.
        brand_id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "charge_id": 'charge_id',
        "brand_id": 'brand_id'
    }

    _optionals = [
        'charge_id',
        'brand_id',
    ]

    def __init__(self,
                 charge_id=APIHelper.SKIP,
                 brand_id=APIHelper.SKIP):
        """Constructor for the GetPaymentOriginResponse class"""

        # Initialize members of the class
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id 
        if brand_id is not APIHelper.SKIP:
            self.brand_id = brand_id 

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
        charge_id = dictionary.get("charge_id") if dictionary.get("charge_id") else APIHelper.SKIP
        brand_id = dictionary.get("brand_id") if dictionary.get("brand_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(charge_id,
                   brand_id)
