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
        id (string): TODO: type description here.
        last_four_digits (string): TODO: type description here.
        brand (string): TODO: type description here.
        holder_name (string): TODO: type description here.
        exp_month (int): TODO: type description here.
        exp_year (int): TODO: type description here.
        status (string): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        billing_address (GetBillingAddressResponse): TODO: type description
            here.
        customer (GetCustomerResponse): TODO: type description here.
        metadata (dict): TODO: type description here.
        mtype (string): Card type
        holder_document (string): Document number for the card's holder
        deleted_at (datetime): TODO: type description here.
        first_six_digits (string): First six digits
        label (string): TODO: type description here.

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
        "metadata": 'metadata',
        "mtype": 'type',
        "holder_document": 'holder_document',
        "first_six_digits": 'first_six_digits',
        "label": 'label',
        "customer": 'customer',
        "deleted_at": 'deleted_at'
    }

    def __init__(self,
                 id=None,
                 last_four_digits=None,
                 brand=None,
                 holder_name=None,
                 exp_month=None,
                 exp_year=None,
                 status=None,
                 created_at=None,
                 updated_at=None,
                 billing_address=None,
                 metadata=None,
                 mtype=None,
                 holder_document=None,
                 first_six_digits=None,
                 label=None,
                 customer=None,
                 deleted_at=None):
        """Constructor for the GetCardResponse class"""

        # Initialize members of the class
        self.id = id
        self.last_four_digits = last_four_digits
        self.brand = brand
        self.holder_name = holder_name
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.status = status
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.billing_address = billing_address
        self.customer = customer
        self.metadata = metadata
        self.mtype = mtype
        self.holder_document = holder_document
        self.deleted_at = APIHelper.RFC3339DateTime(deleted_at) if deleted_at else None
        self.first_six_digits = first_six_digits
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
        id = dictionary.get('id')
        last_four_digits = dictionary.get('last_four_digits')
        brand = dictionary.get('brand')
        holder_name = dictionary.get('holder_name')
        exp_month = dictionary.get('exp_month')
        exp_year = dictionary.get('exp_year')
        status = dictionary.get('status')
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        billing_address = GetBillingAddressResponse.from_dictionary(dictionary.get('billing_address')) if dictionary.get('billing_address') else None
        metadata = dictionary.get('metadata')
        mtype = dictionary.get('type')
        holder_document = dictionary.get('holder_document')
        first_six_digits = dictionary.get('first_six_digits')
        label = dictionary.get('label')
        customer = GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None

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
                   metadata,
                   mtype,
                   holder_document,
                   first_six_digits,
                   label,
                   customer,
                   deleted_at)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
