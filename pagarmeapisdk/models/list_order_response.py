# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_order_response import GetOrderResponse
from pagarmeapisdk.models.paging_response import PagingResponse


class ListOrderResponse(object):

    """Implementation of the 'ListOrderResponse' model.

    Response object for listing order objects

    Attributes:
        data (List[GetOrderResponse]): The order object
        paging (PagingResponse): Paging object

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data',
        "paging": 'paging'
    }

    _optionals = [
        'data',
        'paging',
    ]

    _nullables = [
        'data',
        'paging',
    ]

    def __init__(self,
                 data=APIHelper.SKIP,
                 paging=APIHelper.SKIP):
        """Constructor for the ListOrderResponse class"""

        # Initialize members of the class
        if data is not APIHelper.SKIP:
            self.data = data 
        if paging is not APIHelper.SKIP:
            self.paging = paging 

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
        if 'data' in dictionary.keys():
            data = [GetOrderResponse.from_dictionary(x) for x in dictionary.get('data')] if dictionary.get('data') else None
        else:
            data = APIHelper.SKIP
        if 'paging' in dictionary.keys():
            paging = PagingResponse.from_dictionary(dictionary.get('paging')) if dictionary.get('paging') else None
        else:
            paging = APIHelper.SKIP
        # Return an object of this model
        return cls(data,
                   paging)
