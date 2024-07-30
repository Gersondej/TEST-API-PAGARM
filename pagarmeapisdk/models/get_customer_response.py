# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_phones_response import GetPhonesResponse


class GetCustomerResponse(object):

    """Implementation of the 'GetCustomerResponse' model.

    Response object for getting a customer

    Attributes:
        id (str): TODO: type description here.
        name (str): TODO: type description here.
        email (str): TODO: type description here.
        delinquent (bool): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        document (str): TODO: type description here.
        mtype (str): TODO: type description here.
        fb_access_token (str): TODO: type description here.
        address (GetAddressResponse): TODO: type description here.
        metadata (Dict[str, str]): TODO: type description here.
        phones (GetPhonesResponse): TODO: type description here.
        fb_id (long|int): TODO: type description here.
        code (str): Código de referência do cliente no sistema da loja. Max:
            52 caracteres
        document_type (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "email": 'email',
        "delinquent": 'delinquent',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "document": 'document',
        "mtype": 'type',
        "fb_access_token": 'fb_access_token',
        "address": 'address',
        "metadata": 'metadata',
        "phones": 'phones',
        "fb_id": 'fb_id',
        "code": 'code',
        "document_type": 'document_type'
    }

    _optionals = [
        'id',
        'name',
        'email',
        'delinquent',
        'created_at',
        'updated_at',
        'document',
        'mtype',
        'fb_access_token',
        'address',
        'metadata',
        'phones',
        'fb_id',
        'code',
        'document_type',
    ]

    _nullables = [
        'id',
        'name',
        'email',
        'delinquent',
        'created_at',
        'updated_at',
        'document',
        'mtype',
        'fb_access_token',
        'address',
        'metadata',
        'phones',
        'fb_id',
        'code',
        'document_type',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 delinquent=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 document=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 fb_access_token=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 phones=APIHelper.SKIP,
                 fb_id=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 document_type=APIHelper.SKIP):
        """Constructor for the GetCustomerResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if email is not APIHelper.SKIP:
            self.email = email 
        if delinquent is not APIHelper.SKIP:
            self.delinquent = delinquent 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if document is not APIHelper.SKIP:
            self.document = document 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if fb_access_token is not APIHelper.SKIP:
            self.fb_access_token = fb_access_token 
        if address is not APIHelper.SKIP:
            self.address = address 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if phones is not APIHelper.SKIP:
            self.phones = phones 
        if fb_id is not APIHelper.SKIP:
            self.fb_id = fb_id 
        if code is not APIHelper.SKIP:
            self.code = code 
        if document_type is not APIHelper.SKIP:
            self.document_type = document_type 

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
        from pagarmeapisdk.models.get_address_response import GetAddressResponse

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if "name" in dictionary.keys() else APIHelper.SKIP
        email = dictionary.get("email") if "email" in dictionary.keys() else APIHelper.SKIP
        delinquent = dictionary.get("delinquent") if "delinquent" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        document = dictionary.get("document") if "document" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        fb_access_token = dictionary.get("fb_access_token") if "fb_access_token" in dictionary.keys() else APIHelper.SKIP
        if 'address' in dictionary.keys():
            address = GetAddressResponse.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        else:
            address = APIHelper.SKIP
        metadata = dictionary.get("metadata") if "metadata" in dictionary.keys() else APIHelper.SKIP
        if 'phones' in dictionary.keys():
            phones = GetPhonesResponse.from_dictionary(dictionary.get('phones')) if dictionary.get('phones') else None
        else:
            phones = APIHelper.SKIP
        fb_id = dictionary.get("fb_id") if "fb_id" in dictionary.keys() else APIHelper.SKIP
        code = dictionary.get("code") if "code" in dictionary.keys() else APIHelper.SKIP
        document_type = dictionary.get("document_type") if "document_type" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   email,
                   delinquent,
                   created_at,
                   updated_at,
                   document,
                   mtype,
                   fb_access_token,
                   address,
                   metadata,
                   phones,
                   fb_id,
                   code,
                   document_type)
