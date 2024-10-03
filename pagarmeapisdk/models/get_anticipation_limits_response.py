# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_anticipation_limit_response import GetAnticipationLimitResponse


class GetAnticipationLimitsResponse(object):

    """Implementation of the 'GetAnticipationLimitsResponse' model.

    Anticipation limits

    Attributes:
        max (GetAnticipationLimitResponse): Max limit
        min (GetAnticipationLimitResponse): Min limit

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "max": 'max',
        "min": 'min'
    }

    _optionals = [
        'max',
        'min',
    ]

    _nullables = [
        'max',
        'min',
    ]

    def __init__(self,
                 max=APIHelper.SKIP,
                 min=APIHelper.SKIP):
        """Constructor for the GetAnticipationLimitsResponse class"""

        # Initialize members of the class
        if max is not APIHelper.SKIP:
            self.max = max 
        if min is not APIHelper.SKIP:
            self.min = min 

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
        if 'max' in dictionary.keys():
            max = GetAnticipationLimitResponse.from_dictionary(dictionary.get('max')) if dictionary.get('max') else None
        else:
            max = APIHelper.SKIP
        if 'min' in dictionary.keys():
            min = GetAnticipationLimitResponse.from_dictionary(dictionary.get('min')) if dictionary.get('min') else None
        else:
            min = APIHelper.SKIP
        # Return an object of this model
        return cls(max,
                   min)
