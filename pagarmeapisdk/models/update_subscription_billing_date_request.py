# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class UpdateSubscriptionBillingDateRequest(object):

    """Implementation of the 'UpdateSubscriptionBillingDateRequest' model.

    Request for updating the due date from a subscription

    Attributes:
        next_billing_at (datetime): The date when the next subscription
            billing must occur

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "next_billing_at": 'next_billing_at'
    }

    def __init__(self,
                 next_billing_at=None):
        """Constructor for the UpdateSubscriptionBillingDateRequest class"""

        # Initialize members of the class
        self.next_billing_at = APIHelper.apply_datetime_converter(next_billing_at, APIHelper.RFC3339DateTime) if next_billing_at else None 

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
        next_billing_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_billing_at")).datetime if dictionary.get("next_billing_at") else None
        # Return an object of this model
        return cls(next_billing_at)
