# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetLocationResponse(object):

    """Implementation of the 'GetLocationResponse' model.

    Response object for geetting an order location request

    Attributes:
        latitude (str): Latitude
        longitude (str): Longitude

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "latitude": 'latitude',
        "longitude": 'longitude'
    }

    _optionals = [
        'latitude',
        'longitude',
    ]

    _nullables = [
        'latitude',
        'longitude',
    ]

    def __init__(self,
                 latitude=APIHelper.SKIP,
                 longitude=APIHelper.SKIP):
        """Constructor for the GetLocationResponse class"""

        # Initialize members of the class
        if latitude is not APIHelper.SKIP:
            self.latitude = latitude 
        if longitude is not APIHelper.SKIP:
            self.longitude = longitude 

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
        latitude = dictionary.get("latitude") if "latitude" in dictionary.keys() else APIHelper.SKIP
        longitude = dictionary.get("longitude") if "longitude" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(latitude,
                   longitude)
