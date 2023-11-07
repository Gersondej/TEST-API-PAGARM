# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class CreateDeviceRequest(object):

    """Implementation of the 'CreateDeviceRequest' model.

    Request for creating a device

    Attributes:
        platform (str): Device's platform

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "platform": 'platform'
    }

    _optionals = [
        'platform',
    ]

    def __init__(self,
                 platform=APIHelper.SKIP):
        """Constructor for the CreateDeviceRequest class"""

        # Initialize members of the class
        if platform is not APIHelper.SKIP:
            self.platform = platform 

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
        platform = dictionary.get("platform") if dictionary.get("platform") else APIHelper.SKIP
        # Return an object of this model
        return cls(platform)
