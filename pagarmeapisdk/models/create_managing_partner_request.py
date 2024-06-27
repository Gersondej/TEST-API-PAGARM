# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_register_information_address_request import CreateRegisterInformationAddressRequest
from pagarmeapisdk.models.create_register_information_phone_request import CreateRegisterInformationPhoneRequest


class CreateManagingPartnerRequest(object):

    """Implementation of the 'CreateManagingPartnerRequest' model.

    Managing Partner Request

    Attributes:
        name (str): TODO: type description here.
        email (str): TODO: type description here.
        document (str): TODO: type description here.
        mother_name (str): TODO: type description here.
        birthdate (str): TODO: type description here.
        monthly_income (long|int): TODO: type description here.
        professional_occupation (str): TODO: type description here.
        self_declared_legal_representative (bool): TODO: type description
            here.
        address (CreateRegisterInformationAddressRequest): TODO: type
            description here.
        phone_numbers (List[CreateRegisterInformationPhoneRequest]): TODO:
            type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "email": 'email',
        "document": 'document',
        "birthdate": 'birthdate',
        "monthly_income": 'monthly_income',
        "professional_occupation": 'professional_occupation',
        "self_declared_legal_representative": 'self_declared_legal_representative',
        "address": 'address',
        "phone_numbers": 'phone_numbers',
        "mother_name": 'mother_name'
    }

    _optionals = [
        'mother_name',
    ]

    _nullables = [
        'mother_name',
    ]

    def __init__(self,
                 name=None,
                 email=None,
                 document=None,
                 birthdate=None,
                 monthly_income=None,
                 professional_occupation=None,
                 self_declared_legal_representative=None,
                 address=None,
                 phone_numbers=None,
                 mother_name=APIHelper.SKIP):
        """Constructor for the CreateManagingPartnerRequest class"""

        # Initialize members of the class
        self.name = name 
        self.email = email 
        self.document = document 
        if mother_name is not APIHelper.SKIP:
            self.mother_name = mother_name 
        self.birthdate = birthdate 
        self.monthly_income = monthly_income 
        self.professional_occupation = professional_occupation 
        self.self_declared_legal_representative = self_declared_legal_representative 
        self.address = address 
        self.phone_numbers = phone_numbers 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        email = dictionary.get("email") if dictionary.get("email") else None
        document = dictionary.get("document") if dictionary.get("document") else None
        birthdate = dictionary.get("birthdate") if dictionary.get("birthdate") else None
        monthly_income = dictionary.get("monthly_income") if dictionary.get("monthly_income") else None
        professional_occupation = dictionary.get("professional_occupation") if dictionary.get("professional_occupation") else None
        self_declared_legal_representative = dictionary.get("self_declared_legal_representative") if "self_declared_legal_representative" in dictionary.keys() else None
        address = CreateRegisterInformationAddressRequest.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        phone_numbers = None
        if dictionary.get('phone_numbers') is not None:
            phone_numbers = [CreateRegisterInformationPhoneRequest.from_dictionary(x) for x in dictionary.get('phone_numbers')]
        mother_name = dictionary.get("mother_name") if "mother_name" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   email,
                   document,
                   birthdate,
                   monthly_income,
                   professional_occupation,
                   self_declared_legal_representative,
                   address,
                   phone_numbers,
                   mother_name)
