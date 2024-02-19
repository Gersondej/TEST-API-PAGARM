# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_price_bracket_response import GetPriceBracketResponse


class GetPricingSchemeResponse(object):

    """Implementation of the 'GetPricingSchemeResponse' model.

    Response object for getting a pricing scheme

    Attributes:
        price (int): TODO: type description here.
        scheme_type (str): TODO: type description here.
        price_brackets (List[GetPriceBracketResponse]): TODO: type description
            here.
        minimum_price (int): TODO: type description here.
        percentage (float): percentual value used in pricing_scheme Percent

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price": 'price',
        "scheme_type": 'scheme_type',
        "price_brackets": 'price_brackets',
        "minimum_price": 'minimum_price',
        "percentage": 'percentage'
    }

    _optionals = [
        'price',
        'scheme_type',
        'price_brackets',
        'minimum_price',
        'percentage',
    ]

    _nullables = [
        'price',
        'scheme_type',
        'price_brackets',
        'minimum_price',
        'percentage',
    ]

    def __init__(self,
                 price=APIHelper.SKIP,
                 scheme_type=APIHelper.SKIP,
                 price_brackets=APIHelper.SKIP,
                 minimum_price=APIHelper.SKIP,
                 percentage=APIHelper.SKIP):
        """Constructor for the GetPricingSchemeResponse class"""

        # Initialize members of the class
        if price is not APIHelper.SKIP:
            self.price = price 
        if scheme_type is not APIHelper.SKIP:
            self.scheme_type = scheme_type 
        if price_brackets is not APIHelper.SKIP:
            self.price_brackets = price_brackets 
        if minimum_price is not APIHelper.SKIP:
            self.minimum_price = minimum_price 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 

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
        price = dictionary.get("price") if "price" in dictionary.keys() else APIHelper.SKIP
        scheme_type = dictionary.get("scheme_type") if "scheme_type" in dictionary.keys() else APIHelper.SKIP
        if 'price_brackets' in dictionary.keys():
            price_brackets = [GetPriceBracketResponse.from_dictionary(x) for x in dictionary.get('price_brackets')] if dictionary.get('price_brackets') else None
        else:
            price_brackets = APIHelper.SKIP
        minimum_price = dictionary.get("minimum_price") if "minimum_price" in dictionary.keys() else APIHelper.SKIP
        percentage = dictionary.get("percentage") if "percentage" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(price,
                   scheme_type,
                   price_brackets,
                   minimum_price,
                   percentage)
