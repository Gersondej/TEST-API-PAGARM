# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_phone_request import CreatePhoneRequest


class CreateSubMerchantRequest(object):

    """Implementation of the 'CreateSubMerchantRequest' model.

    SubMerchant

    Attributes:
        payment_facilitator_code (str): Payment Facilitator Code
        code (str): Code
        name (str): Name
        merchant_category_code (str): Merchant Category Code
        document (str): Document number. Only numbers, no special characters.
        mtype (str): Document type. Can be either 'individual' or 'company'
        phone (CreatePhoneRequest): Phone
        address (CreateAddressRequest): Address

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_facilitator_code": 'payment_facilitator_code',
        "code": 'code',
        "name": 'name',
        "merchant_category_code": 'merchant_category_code',
        "document": 'document',
        "mtype": 'type',
        "phone": 'phone',
        "address": 'address'
    }

    def __init__(self,
                 payment_facilitator_code=None,
                 code=None,
                 name=None,
                 merchant_category_code=None,
                 document=None,
                 mtype=None,
                 phone=None,
                 address=None):
        """Constructor for the CreateSubMerchantRequest class"""

        # Initialize members of the class
        self.payment_facilitator_code = payment_facilitator_code 
        self.code = code 
        self.name = name 
        self.merchant_category_code = merchant_category_code 
        self.document = document 
        self.mtype = mtype 
        self.phone = phone 
        self.address = address 

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
        payment_facilitator_code = dictionary.get("payment_facilitator_code") if dictionary.get("payment_facilitator_code") else None
        code = dictionary.get("code") if dictionary.get("code") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        merchant_category_code = dictionary.get("merchant_category_code") if dictionary.get("merchant_category_code") else None
        document = dictionary.get("document") if dictionary.get("document") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        phone = CreatePhoneRequest.from_dictionary(dictionary.get('phone')) if dictionary.get('phone') else None
        address = CreateAddressRequest.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        # Return an object of this model
        return cls(payment_facilitator_code,
                   code,
                   name,
                   merchant_category_code,
                   document,
                   mtype,
                   phone,
                   address)
