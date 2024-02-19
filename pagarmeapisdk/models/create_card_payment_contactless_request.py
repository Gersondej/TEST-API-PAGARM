# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_apple_pay_request import CreateApplePayRequest
from pagarmeapisdk.models.create_emv_decrypt_request import CreateEmvDecryptRequest
from pagarmeapisdk.models.create_google_pay_request import CreateGooglePayRequest


class CreateCardPaymentContactlessRequest(object):

    """Implementation of the 'CreateCardPaymentContactlessRequest' model.

    The card payment contactless request

    Attributes:
        mtype (str): The authentication type
        apple_pay (CreateApplePayRequest): The ApplePay encrypted request
        google_pay (CreateGooglePayRequest): The GooglePay encrypted request
        emv (CreateEmvDecryptRequest): The Emv encrypted request

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "apple_pay": 'apple_pay',
        "google_pay": 'google_pay',
        "emv": 'emv'
    }

    _optionals = [
        'apple_pay',
        'google_pay',
        'emv',
    ]

    def __init__(self,
                 mtype=None,
                 apple_pay=APIHelper.SKIP,
                 google_pay=APIHelper.SKIP,
                 emv=APIHelper.SKIP):
        """Constructor for the CreateCardPaymentContactlessRequest class"""

        # Initialize members of the class
        self.mtype = mtype 
        if apple_pay is not APIHelper.SKIP:
            self.apple_pay = apple_pay 
        if google_pay is not APIHelper.SKIP:
            self.google_pay = google_pay 
        if emv is not APIHelper.SKIP:
            self.emv = emv 

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
        mtype = dictionary.get("type") if dictionary.get("type") else None
        apple_pay = CreateApplePayRequest.from_dictionary(dictionary.get('apple_pay')) if 'apple_pay' in dictionary.keys() else APIHelper.SKIP
        google_pay = CreateGooglePayRequest.from_dictionary(dictionary.get('google_pay')) if 'google_pay' in dictionary.keys() else APIHelper.SKIP
        emv = CreateEmvDecryptRequest.from_dictionary(dictionary.get('emv')) if 'emv' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   apple_pay,
                   google_pay,
                   emv)
