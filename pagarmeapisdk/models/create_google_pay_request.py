# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.create_google_pay_header_request import CreateGooglePayHeaderRequest


class CreateGooglePayRequest(object):

    """Implementation of the 'CreateGooglePayRequest' model.

    The GooglePay Token Payment Request

    Attributes:
        version (string): The token version
        data (string): The cryptography data
        header (CreateGooglePayHeaderRequest): The GooglePay header request
        signature (string): Detached PKCS #7 signature, Base64 encoded as
            string
        merchant_identifier (string): GooglePay Merchant identifier

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "version": 'version',
        "data": 'data',
        "header": 'header',
        "signature": 'signature',
        "merchant_identifier": 'merchant_identifier'
    }

    def __init__(self,
                 version=None,
                 data=None,
                 header=None,
                 signature=None,
                 merchant_identifier=None):
        """Constructor for the CreateGooglePayRequest class"""

        # Initialize members of the class
        self.version = version
        self.data = data
        self.header = header
        self.signature = signature
        self.merchant_identifier = merchant_identifier

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
        version = dictionary.get('version')
        data = dictionary.get('data')
        header = CreateGooglePayHeaderRequest.from_dictionary(dictionary.get('header')) if dictionary.get('header') else None
        signature = dictionary.get('signature')
        merchant_identifier = dictionary.get('merchant_identifier')

        # Return an object of this model
        return cls(version,
                   data,
                   header,
                   signature,
                   merchant_identifier)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
