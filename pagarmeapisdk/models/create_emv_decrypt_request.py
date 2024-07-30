# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_card_payment_contactless_poi_request import CreateCardPaymentContactlessPOIRequest
from pagarmeapisdk.models.create_emv_data_decrypt_request import CreateEmvDataDecryptRequest


class CreateEmvDecryptRequest(object):

    """Implementation of the 'CreateEmvDecryptRequest' model.

    TODO: type model description here.

    Attributes:
        icc_data (str): TODO: type description here.
        card_sequence_number (str): TODO: type description here.
        data (CreateEmvDataDecryptRequest): TODO: type description here.
        poi (CreateCardPaymentContactlessPOIRequest): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "icc_data": 'icc_data',
        "card_sequence_number": 'card_sequence_number',
        "data": 'data',
        "poi": 'poi'
    }

    _optionals = [
        'poi',
    ]

    def __init__(self,
                 icc_data=None,
                 card_sequence_number=None,
                 data=None,
                 poi=APIHelper.SKIP):
        """Constructor for the CreateEmvDecryptRequest class"""

        # Initialize members of the class
        self.icc_data = icc_data 
        self.card_sequence_number = card_sequence_number 
        self.data = data 
        if poi is not APIHelper.SKIP:
            self.poi = poi 

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
        icc_data = dictionary.get("icc_data") if dictionary.get("icc_data") else None
        card_sequence_number = dictionary.get("card_sequence_number") if dictionary.get("card_sequence_number") else None
        data = CreateEmvDataDecryptRequest.from_dictionary(dictionary.get('data')) if dictionary.get('data') else None
        poi = CreateCardPaymentContactlessPOIRequest.from_dictionary(dictionary.get('poi')) if 'poi' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(icc_data,
                   card_sequence_number,
                   data,
                   poi)
