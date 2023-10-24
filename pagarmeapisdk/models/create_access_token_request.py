# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class CreateAccessTokenRequest(object):

    """Implementation of the 'CreateAccessTokenRequest' model.

    Request for creating a new Access Token

    Attributes:
        expires_in (int): Minutes to expire the token

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "expires_in": 'expires_in'
    }

    _optionals = [
        'expires_in',
    ]

    def __init__(self,
                 expires_in=APIHelper.SKIP):
        """Constructor for the CreateAccessTokenRequest class"""

        # Initialize members of the class
        if expires_in is not APIHelper.SKIP:
            self.expires_in = expires_in 

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
        expires_in = dictionary.get("expires_in") if dictionary.get("expires_in") else APIHelper.SKIP
        # Return an object of this model
        return cls(expires_in)
