# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_subscription_response import GetSubscriptionResponse


class GetPeriodResponse(object):

    """Implementation of the 'GetPeriodResponse' model.

    Response object for getting a period

    Attributes:
        start_at (datetime): TODO: type description here.
        end_at (datetime): TODO: type description here.
        id (string): TODO: type description here.
        billing_at (datetime): TODO: type description here.
        subscription (GetSubscriptionResponse): TODO: type description here.
        status (string): TODO: type description here.
        duration (int): TODO: type description here.
        created_at (string): TODO: type description here.
        updated_at (string): TODO: type description here.
        cycle (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_at": 'start_at',
        "end_at": 'end_at',
        "id": 'id',
        "billing_at": 'billing_at',
        "subscription": 'subscription',
        "status": 'status',
        "duration": 'duration',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "cycle": 'cycle'
    }

    def __init__(self,
                 start_at=None,
                 end_at=None,
                 id=None,
                 billing_at=None,
                 subscription=None,
                 status=None,
                 duration=None,
                 created_at=None,
                 updated_at=None,
                 cycle=None):
        """Constructor for the GetPeriodResponse class"""

        # Initialize members of the class
        self.start_at = APIHelper.RFC3339DateTime(start_at) if start_at else None
        self.end_at = APIHelper.RFC3339DateTime(end_at) if end_at else None
        self.id = id
        self.billing_at = APIHelper.RFC3339DateTime(billing_at) if billing_at else None
        self.subscription = subscription
        self.status = status
        self.duration = duration
        self.created_at = created_at
        self.updated_at = updated_at
        self.cycle = cycle

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
        end_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("end_at")).datetime if dictionary.get("end_at") else None
        id = dictionary.get('id')
        billing_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("billing_at")).datetime if dictionary.get("billing_at") else None
        subscription = GetSubscriptionResponse.from_dictionary(dictionary.get('subscription')) if dictionary.get('subscription') else None
        status = dictionary.get('status')
        duration = dictionary.get('duration')
        created_at = dictionary.get('created_at')
        updated_at = dictionary.get('updated_at')
        cycle = dictionary.get('cycle')

        # Return an object of this model
        return cls(start_at,
                   end_at,
                   id,
                   billing_at,
                   subscription,
                   status,
                   duration,
                   created_at,
                   updated_at,
                   cycle)
