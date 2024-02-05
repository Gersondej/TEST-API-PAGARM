# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreateCardPaymentContactlessPOIRequest(object):

    """Implementation of the 'CreateCardPaymentContactlessPOIRequest' model.

    TODO: type model description here.

    Attributes:
        system_name (str): system name
        model (str): model
        provider (str): provider
        serial_number (str): serial number
        version_number (str): version number

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "system_name": 'system_name',
        "model": 'model',
        "provider": 'provider',
        "serial_number": 'serial_number',
        "version_number": 'version_number'
    }

    def __init__(self,
                 system_name=None,
                 model=None,
                 provider=None,
                 serial_number=None,
                 version_number=None):
        """Constructor for the CreateCardPaymentContactlessPOIRequest class"""

        # Initialize members of the class
        self.system_name = system_name 
        self.model = model 
        self.provider = provider 
        self.serial_number = serial_number 
        self.version_number = version_number 

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
        system_name = dictionary.get("system_name") if dictionary.get("system_name") else None
        model = dictionary.get("model") if dictionary.get("model") else None
        provider = dictionary.get("provider") if dictionary.get("provider") else None
        serial_number = dictionary.get("serial_number") if dictionary.get("serial_number") else None
        version_number = dictionary.get("version_number") if dictionary.get("version_number") else None
        # Return an object of this model
        return cls(system_name,
                   model,
                   provider,
                   serial_number,
                   version_number)
