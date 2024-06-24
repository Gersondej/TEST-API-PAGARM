# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_managing_partner_request import CreateManagingPartnerRequest
from pagarmeapisdk.models.create_register_information_address_request import CreateRegisterInformationAddressRequest
from pagarmeapisdk.models.create_register_information_phone_request import CreateRegisterInformationPhoneRequest


class CreateRegisterInformationBaseRequest(object):

    """Implementation of the 'CreateRegisterInformationBaseRequest' model.

    Request object for RegisterInformation.

    Attributes:
        email (str): TODO: type description here.
        document (str): TODO: type description here.
        mtype (str): "individual" ou "corporation"
        site_url (str): TODO: type description here.
        phone_numbers (List[CreateRegisterInformationPhoneRequest]): TODO:
            type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email": 'email',
        "document": 'document',
        "mtype": 'type',
        "phone_numbers": 'phone_numbers',
        "site_url": 'site_url'
    }

    _optionals = [
        'site_url',
    ]

    _nullables = [
        'site_url',
    ]

    def __init__(self,
                 email=None,
                 document=None,
                 mtype=None,
                 phone_numbers=None,
                 site_url=APIHelper.SKIP):
        """Constructor for the CreateRegisterInformationBaseRequest class"""

        # Initialize members of the class
        self.email = email 
        self.document = document 
        self.mtype = mtype 
        if site_url is not APIHelper.SKIP:
            self.site_url = site_url 
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
        email = dictionary.get("email") if dictionary.get("email") else None
        document = dictionary.get("document") if dictionary.get("document") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        phone_numbers = None
        if dictionary.get('phone_numbers') is not None:
            phone_numbers = [CreateRegisterInformationPhoneRequest.from_dictionary(x) for x in dictionary.get('phone_numbers')]
        site_url = dictionary.get("site_url") if "site_url" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(email,
                   document,
                   mtype,
                   phone_numbers,
                   site_url)

class CreateRegisterInformationIndividualRequest(CreateRegisterInformationBaseRequest):

    """Implementation of the 'CreateRegisterInformationIndividualRequest' model.

    TODO: type model description here.
    NOTE: This class inherits from 'CreateRegisterInformationBaseRequest'.

    Attributes:
        name (str): TODO: type description here.
        mother_name (str): TODO: type description here.
        birthdate (str): TODO: type description here.
        monthly_income (long|int): TODO: type description here.
        professional_occupation (str): TODO: type description here.
        address (CreateRegisterInformationAddressRequest): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "birthdate": 'birthdate',
        "monthly_income": 'monthly_income',
        "professional_occupation": 'professional_occupation',
        "address": 'address',
        "email": 'email',
        "document": 'document',
        "mtype": 'type',
        "phone_numbers": 'phone_numbers',
        "mother_name": 'mother_name',
        "site_url": 'site_url'
    }

    _optionals = [
        'mother_name',
    ]
    _optionals.extend(CreateRegisterInformationBaseRequest._optionals)

    _nullables = [
        'mother_name',
    ]
    _nullables.extend(CreateRegisterInformationBaseRequest._nullables)

    def __init__(self,
                 name=None,
                 birthdate=None,
                 monthly_income=None,
                 professional_occupation=None,
                 address=None,
                 email=None,
                 document=None,
                 mtype=None,
                 phone_numbers=None,
                 mother_name=APIHelper.SKIP,
                 site_url=APIHelper.SKIP):
        """Constructor for the CreateRegisterInformationIndividualRequest class"""

        # Initialize members of the class
        self.name = name 
        if mother_name is not APIHelper.SKIP:
            self.mother_name = mother_name 
        self.birthdate = birthdate 
        self.monthly_income = monthly_income 
        self.professional_occupation = professional_occupation 
        self.address = address 

        # Call the constructor for the base class
        super(CreateRegisterInformationIndividualRequest, self).__init__(email,
                                                                         document,
                                                                         mtype,
                                                                         phone_numbers,
                                                                         site_url)

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
        birthdate = dictionary.get("birthdate") if dictionary.get("birthdate") else None
        monthly_income = dictionary.get("monthly_income") if dictionary.get("monthly_income") else None
        professional_occupation = dictionary.get("professional_occupation") if dictionary.get("professional_occupation") else None
        address = CreateRegisterInformationAddressRequest.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        email = dictionary.get("email") if dictionary.get("email") else None
        document = dictionary.get("document") if dictionary.get("document") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        phone_numbers = None
        if dictionary.get('phone_numbers') is not None:
            phone_numbers = [CreateRegisterInformationPhoneRequest.from_dictionary(x) for x in dictionary.get('phone_numbers')]
        mother_name = dictionary.get("mother_name") if "mother_name" in dictionary.keys() else APIHelper.SKIP
        site_url = dictionary.get("site_url") if "site_url" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   birthdate,
                   monthly_income,
                   professional_occupation,
                   address,
                   email,
                   document,
                   mtype,
                   phone_numbers,
                   mother_name,
                   site_url)

class CreateRegisterInformationCorporationRequest(CreateRegisterInformationBaseRequest):

    """Implementation of the 'CreateRegisterInformationCorporationRequest' model.

    TODO: type model description here.
    NOTE: This class inherits from 'CreateRegisterInformationBaseRequest'.

    Attributes:
        company_name (str): TODO: type description here.
        trading_name (str): TODO: type description here.
        annual_revenue (long|int): TODO: type description here.
        corporation_type (str): TODO: type description here.
        founding_date (str): TODO: type description here.
        cnae (str): TODO: type description here.
        managing_partners (List[CreateManagingPartnerRequest]): TODO: type
            description here.
        main_address (CreateRegisterInformationAddressRequest): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "company_name": 'company_name',
        "trading_name": 'trading_name',
        "annual_revenue": 'annual_revenue',
        "managing_partners": 'managing_partners',
        "main_address": 'main_address',
        "email": 'email',
        "document": 'document',
        "mtype": 'type',
        "phone_numbers": 'phone_numbers',
        "corporation_type": 'corporation_type',
        "founding_date": 'founding_date',
        "cnae": 'cnae',
        "site_url": 'site_url'
    }

    _optionals = [
        'corporation_type',
        'founding_date',
        'cnae',
    ]
    _optionals.extend(CreateRegisterInformationBaseRequest._optionals)

    _nullables = [
        'corporation_type',
        'founding_date',
        'cnae',
    ]
    _nullables.extend(CreateRegisterInformationBaseRequest._nullables)

    def __init__(self,
                 company_name=None,
                 trading_name=None,
                 annual_revenue=None,
                 managing_partners=None,
                 main_address=None,
                 email=None,
                 document=None,
                 mtype=None,
                 phone_numbers=None,
                 corporation_type=APIHelper.SKIP,
                 founding_date=APIHelper.SKIP,
                 cnae=APIHelper.SKIP,
                 site_url=APIHelper.SKIP):
        """Constructor for the CreateRegisterInformationCorporationRequest class"""

        # Initialize members of the class
        self.company_name = company_name 
        self.trading_name = trading_name 
        self.annual_revenue = annual_revenue 
        if corporation_type is not APIHelper.SKIP:
            self.corporation_type = corporation_type 
        if founding_date is not APIHelper.SKIP:
            self.founding_date = founding_date 
        if cnae is not APIHelper.SKIP:
            self.cnae = cnae 
        self.managing_partners = managing_partners 
        self.main_address = main_address 

        # Call the constructor for the base class
        super(CreateRegisterInformationCorporationRequest, self).__init__(email,
                                                                          document,
                                                                          mtype,
                                                                          phone_numbers,
                                                                          site_url)

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
        company_name = dictionary.get("company_name") if dictionary.get("company_name") else None
        trading_name = dictionary.get("trading_name") if dictionary.get("trading_name") else None
        annual_revenue = dictionary.get("annual_revenue") if dictionary.get("annual_revenue") else None
        managing_partners = None
        if dictionary.get('managing_partners') is not None:
            managing_partners = [CreateManagingPartnerRequest.from_dictionary(x) for x in dictionary.get('managing_partners')]
        main_address = CreateRegisterInformationAddressRequest.from_dictionary(dictionary.get('main_address')) if dictionary.get('main_address') else None
        email = dictionary.get("email") if dictionary.get("email") else None
        document = dictionary.get("document") if dictionary.get("document") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        phone_numbers = None
        if dictionary.get('phone_numbers') is not None:
            phone_numbers = [CreateRegisterInformationPhoneRequest.from_dictionary(x) for x in dictionary.get('phone_numbers')]
        corporation_type = dictionary.get("corporation_type") if "corporation_type" in dictionary.keys() else APIHelper.SKIP
        founding_date = dictionary.get("founding_date") if "founding_date" in dictionary.keys() else APIHelper.SKIP
        cnae = dictionary.get("cnae") if "cnae" in dictionary.keys() else APIHelper.SKIP
        site_url = dictionary.get("site_url") if "site_url" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(company_name,
                   trading_name,
                   annual_revenue,
                   managing_partners,
                   main_address,
                   email,
                   document,
                   mtype,
                   phone_numbers,
                   corporation_type,
                   founding_date,
                   cnae,
                   site_url)
