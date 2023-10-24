# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_billing_address_response import GetBillingAddressResponse
from pagarmeapisdk.models.get_customer_response import GetCustomerResponse


class GetCardResponse(object):

    """Implementation of the 'GetCardResponse' model.

    Response object for getting a credit card

    Attributes:
        id (str): TODO: type description here.
        last_four_digits (str): TODO: type description here.
        brand (str): TODO: type description here.
        holder_name (str): TODO: type description here.
        exp_month (int): TODO: type description here.
        exp_year (int): TODO: type description here.
        status (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        billing_address (GetBillingAddressResponse): TODO: type description
            here.
        customer (GetCustomerResponse): TODO: type description here.
        metadata (Dict[str, str]): TODO: type description here.
        mtype (str): Card type
        holder_document (str): Document number for the card's holder
        deleted_at (datetime): TODO: type description here.
        first_six_digits (str): First six digits
        label (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "last_four_digits": 'last_four_digits',
        "brand": 'brand',
        "holder_name": 'holder_name',
        "exp_month": 'exp_month',
        "exp_year": 'exp_year',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "billing_address": 'billing_address',
        "customer": 'customer',
        "metadata": 'metadata',
        "mtype": 'type',
        "holder_document": 'holder_document',
        "deleted_at": 'deleted_at',
        "first_six_digits": 'first_six_digits',
        "label": 'label'
    }

    _optionals = [
        'id',
        'last_four_digits',
        'brand',
        'holder_name',
        'exp_month',
        'exp_year',
        'status',
        'created_at',
        'updated_at',
        'billing_address',
        'customer',
        'metadata',
        'mtype',
        'holder_document',
        'deleted_at',
        'first_six_digits',
        'label',
    ]

    _nullables = [
        'id',
        'last_four_digits',
        'brand',
        'holder_name',
        'exp_month',
        'exp_year',
        'status',
        'created_at',
        'updated_at',
        'billing_address',
        'customer',
        'metadata',
        'mtype',
        'holder_document',
        'deleted_at',
        'first_six_digits',
        'label',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 last_four_digits=APIHelper.SKIP,
                 brand=APIHelper.SKIP,
                 holder_name=APIHelper.SKIP,
                 exp_month=APIHelper.SKIP,
                 exp_year=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 holder_document=APIHelper.SKIP,
                 deleted_at=APIHelper.SKIP,
                 first_six_digits=APIHelper.SKIP,
                 label=APIHelper.SKIP):
        """Constructor for the GetCardResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if last_four_digits is not APIHelper.SKIP:
            self.last_four_digits = last_four_digits 
        if brand is not APIHelper.SKIP:
            self.brand = brand 
        if holder_name is not APIHelper.SKIP:
            self.holder_name = holder_name 
        if exp_month is not APIHelper.SKIP:
            self.exp_month = exp_month 
        if exp_year is not APIHelper.SKIP:
            self.exp_year = exp_year 
        if status is not APIHelper.SKIP:
            self.status = status 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if holder_document is not APIHelper.SKIP:
            self.holder_document = holder_document 
        if deleted_at is not APIHelper.SKIP:
            self.deleted_at = APIHelper.apply_datetime_converter(deleted_at, APIHelper.RFC3339DateTime) if deleted_at else None 
        if first_six_digits is not APIHelper.SKIP:
            self.first_six_digits = first_six_digits 
        if label is not APIHelper.SKIP:
            self.label = label 

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
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        last_four_digits = dictionary.get("last_four_digits") if "last_four_digits" in dictionary.keys() else APIHelper.SKIP
        brand = dictionary.get("brand") if "brand" in dictionary.keys() else APIHelper.SKIP
        holder_name = dictionary.get("holder_name") if "holder_name" in dictionary.keys() else APIHelper.SKIP
        exp_month = dictionary.get("exp_month") if "exp_month" in dictionary.keys() else APIHelper.SKIP
        exp_year = dictionary.get("exp_year") if "exp_year" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        if 'billing_address' in dictionary.keys():
            billing_address = GetBillingAddressResponse.from_dictionary(dictionary.get('billing_address')) if dictionary.get('billing_address') else None
        else:
            billing_address = APIHelper.SKIP
        if 'customer' in dictionary.keys():
            customer = GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        else:
            customer = APIHelper.SKIP
        metadata = dictionary.get("metadata") if "metadata" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        holder_document = dictionary.get("holder_document") if "holder_document" in dictionary.keys() else APIHelper.SKIP
        if 'deleted_at' in dictionary.keys():
            deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        else:
            deleted_at = APIHelper.SKIP
        first_six_digits = dictionary.get("first_six_digits") if "first_six_digits" in dictionary.keys() else APIHelper.SKIP
        label = dictionary.get("label") if "label" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   last_four_digits,
                   brand,
                   holder_name,
                   exp_month,
                   exp_year,
                   status,
                   created_at,
                   updated_at,
                   billing_address,
                   customer,
                   metadata,
                   mtype,
                   holder_document,
                   deleted_at,
                   first_six_digits,
                   label)
