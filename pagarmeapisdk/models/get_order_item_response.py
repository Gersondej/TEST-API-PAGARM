# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.get_seller_response import GetSellerResponse


class GetOrderItemResponse(object):

    """Implementation of the 'GetOrderItemResponse' model.

    Response object for getting an order item

    Attributes:
        id (string): Id
        amount (int): TODO: type description here.
        description (string): TODO: type description here.
        quantity (int): TODO: type description here.
        get_seller_response (GetSellerResponse): Seller data
        category (string): Category
        code (string): Code

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "amount": 'amount',
        "description": 'description',
        "quantity": 'quantity',
        "category": 'category',
        "code": 'code',
        "get_seller_response": 'GetSellerResponse'
    }

    def __init__(self,
                 id=None,
                 amount=None,
                 description=None,
                 quantity=None,
                 category=None,
                 code=None,
                 get_seller_response=None):
        """Constructor for the GetOrderItemResponse class"""

        # Initialize members of the class
        self.id = id
        self.amount = amount
        self.description = description
        self.quantity = quantity
        self.get_seller_response = get_seller_response
        self.category = category
        self.code = code

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
        amount = dictionary.get('amount')
        description = dictionary.get('description')
        quantity = dictionary.get('quantity')
        category = dictionary.get('category')
        code = dictionary.get('code')
        get_seller_response = GetSellerResponse.from_dictionary(dictionary.get('GetSellerResponse')) if dictionary.get('GetSellerResponse') else None

        # Return an object of this model
        return cls(id,
                   amount,
                   description,
                   quantity,
                   category,
                   code,
                   get_seller_response)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
