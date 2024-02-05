# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_emv_data_dukpt_decrypt_request import CreateEmvDataDukptDecryptRequest
from pagarmeapisdk.models.create_emv_data_tlv_decrypt_request import CreateEmvDataTlvDecryptRequest


class CreateEmvDataDecryptRequest(object):

    """Implementation of the 'CreateEmvDataDecryptRequest' model.

    TODO: type model description here.

    Attributes:
        cipher (str): Emv Decrypt cipher type
        dukpt (CreateEmvDataDukptDecryptRequest): Dukpt data request
        tags (List[CreateEmvDataTlvDecryptRequest]): Encrypted tags list

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cipher": 'cipher',
        "tags": 'tags',
        "dukpt": 'dukpt'
    }

    _optionals = [
        'dukpt',
    ]

    def __init__(self,
                 cipher=None,
                 tags=None,
                 dukpt=APIHelper.SKIP):
        """Constructor for the CreateEmvDataDecryptRequest class"""

        # Initialize members of the class
        self.cipher = cipher 
        if dukpt is not APIHelper.SKIP:
            self.dukpt = dukpt 
        self.tags = tags 

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
        cipher = dictionary.get("cipher") if dictionary.get("cipher") else None
        tags = None
        if dictionary.get('tags') is not None:
            tags = [CreateEmvDataTlvDecryptRequest.from_dictionary(x) for x in dictionary.get('tags')]
        dukpt = CreateEmvDataDukptDecryptRequest.from_dictionary(dictionary.get('dukpt')) if 'dukpt' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(cipher,
                   tags,
                   dukpt)
