# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class UpdateSubscriptionStartAtRequest(object):

    """Implementation of the 'UpdateSubscriptionStartAtRequest' model.

    Request for updating the start date from a subscription

    Attributes:
        start_at (datetime): The date when the subscription periods will
            start

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_at": 'start_at'
    }

    def __init__(self,
                 start_at=None):
        """Constructor for the UpdateSubscriptionStartAtRequest class"""

        # Initialize members of the class
        self.start_at = APIHelper.RFC3339DateTime(start_at) if start_at else None

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
        start_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_at")).datetime if dictionary.get("start_at") else None

        # Return an object of this model
        return cls(start_at)
