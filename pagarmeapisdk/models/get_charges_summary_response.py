# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetChargesSummaryResponse(object):

    """Implementation of the 'GetChargesSummaryResponse' model.

    TODO: type model description here.

    Attributes:
        total (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total": 'total'
    }

    _optionals = [
        'total',
    ]

    _nullables = [
        'total',
    ]

    def __init__(self,
                 total=APIHelper.SKIP):
        """Constructor for the GetChargesSummaryResponse class"""

        # Initialize members of the class
        if total is not APIHelper.SKIP:
            self.total = total 

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
        total = dictionary.get("total") if "total" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(total)
