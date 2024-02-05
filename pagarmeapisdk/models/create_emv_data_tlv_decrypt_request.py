# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreateEmvDataTlvDecryptRequest(object):

    """Implementation of the 'CreateEmvDataTlvDecryptRequest' model.

    TODO: type model description here.

    Attributes:
        tag (str): Emv tag
        lenght (str): Emv lenght
        value (str): Emv value

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tag": 'tag',
        "lenght": 'lenght',
        "value": 'value'
    }

    def __init__(self,
                 tag=None,
                 lenght=None,
                 value=None):
        """Constructor for the CreateEmvDataTlvDecryptRequest class"""

        # Initialize members of the class
        self.tag = tag 
        self.lenght = lenght 
        self.value = value 

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
        tag = dictionary.get("tag") if dictionary.get("tag") else None
        lenght = dictionary.get("lenght") if dictionary.get("lenght") else None
        value = dictionary.get("value") if dictionary.get("value") else None
        # Return an object of this model
        return cls(tag,
                   lenght,
                   value)
