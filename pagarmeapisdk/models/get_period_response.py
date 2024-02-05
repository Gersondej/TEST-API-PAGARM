# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetPeriodResponse(object):

    """Implementation of the 'GetPeriodResponse' model.

    Response object for getting a period

    Attributes:
        start_at (datetime): TODO: type description here.
        end_at (datetime): TODO: type description here.
        id (str): TODO: type description here.
        billing_at (datetime): TODO: type description here.
        subscription (GetSubscriptionResponse): TODO: type description here.
        status (str): TODO: type description here.
        duration (int): TODO: type description here.
        created_at (str): TODO: type description here.
        updated_at (str): TODO: type description here.
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

    _optionals = [
        'start_at',
        'end_at',
        'id',
        'billing_at',
        'subscription',
        'status',
        'duration',
        'created_at',
        'updated_at',
        'cycle',
    ]

    _nullables = [
        'start_at',
        'end_at',
        'id',
        'billing_at',
        'subscription',
        'status',
        'duration',
        'created_at',
        'updated_at',
        'cycle',
    ]

    def __init__(self,
                 start_at=APIHelper.SKIP,
                 end_at=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 billing_at=APIHelper.SKIP,
                 subscription=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 duration=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 cycle=APIHelper.SKIP):
        """Constructor for the GetPeriodResponse class"""

        # Initialize members of the class
        if start_at is not APIHelper.SKIP:
            self.start_at = APIHelper.apply_datetime_converter(start_at, APIHelper.RFC3339DateTime) if start_at else None 
        if end_at is not APIHelper.SKIP:
            self.end_at = APIHelper.apply_datetime_converter(end_at, APIHelper.RFC3339DateTime) if end_at else None 
        if id is not APIHelper.SKIP:
            self.id = id 
        if billing_at is not APIHelper.SKIP:
            self.billing_at = APIHelper.apply_datetime_converter(billing_at, APIHelper.RFC3339DateTime) if billing_at else None 
        if subscription is not APIHelper.SKIP:
            self.subscription = subscription 
        if status is not APIHelper.SKIP:
            self.status = status 
        if duration is not APIHelper.SKIP:
            self.duration = duration 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 
        if cycle is not APIHelper.SKIP:
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
        from pagarmeapisdk.models.get_subscription_response import GetSubscriptionResponse

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        if 'start_at' in dictionary.keys():
            start_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_at")).datetime if dictionary.get("start_at") else None
        else:
            start_at = APIHelper.SKIP
        if 'end_at' in dictionary.keys():
            end_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("end_at")).datetime if dictionary.get("end_at") else None
        else:
            end_at = APIHelper.SKIP
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        if 'billing_at' in dictionary.keys():
            billing_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("billing_at")).datetime if dictionary.get("billing_at") else None
        else:
            billing_at = APIHelper.SKIP
        if 'subscription' in dictionary.keys():
            subscription = GetSubscriptionResponse.from_dictionary(dictionary.get('subscription')) if dictionary.get('subscription') else None
        else:
            subscription = APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        duration = dictionary.get("duration") if "duration" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if "created_at" in dictionary.keys() else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if "updated_at" in dictionary.keys() else APIHelper.SKIP
        cycle = dictionary.get("cycle") if "cycle" in dictionary.keys() else APIHelper.SKIP
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
