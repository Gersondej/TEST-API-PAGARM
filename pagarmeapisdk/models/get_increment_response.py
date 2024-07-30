# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetIncrementResponse(object):

    """Implementation of the 'GetIncrementResponse' model.

    Response object for getting a increment

    Attributes:
        id (str): TODO: type description here.
        value (float): TODO: type description here.
        increment_type (str): TODO: type description here.
        status (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        cycles (int): TODO: type description here.
        deleted_at (datetime): TODO: type description here.
        description (str): TODO: type description here.
        subscription (GetSubscriptionResponse): TODO: type description here.
        subscription_item (GetSubscriptionItemResponse): The Subscription
            Item

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "value": 'value',
        "increment_type": 'increment_type',
        "status": 'status',
        "created_at": 'created_at',
        "cycles": 'cycles',
        "deleted_at": 'deleted_at',
        "description": 'description',
        "subscription": 'subscription',
        "subscription_item": 'subscription_item'
    }

    _optionals = [
        'id',
        'value',
        'increment_type',
        'status',
        'created_at',
        'cycles',
        'deleted_at',
        'description',
        'subscription',
        'subscription_item',
    ]

    _nullables = [
        'id',
        'value',
        'increment_type',
        'status',
        'created_at',
        'cycles',
        'deleted_at',
        'description',
        'subscription',
        'subscription_item',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 value=APIHelper.SKIP,
                 increment_type=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 cycles=APIHelper.SKIP,
                 deleted_at=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 subscription=APIHelper.SKIP,
                 subscription_item=APIHelper.SKIP):
        """Constructor for the GetIncrementResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if value is not APIHelper.SKIP:
            self.value = value 
        if increment_type is not APIHelper.SKIP:
            self.increment_type = increment_type 
        if status is not APIHelper.SKIP:
            self.status = status 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if cycles is not APIHelper.SKIP:
            self.cycles = cycles 
        if deleted_at is not APIHelper.SKIP:
            self.deleted_at = APIHelper.apply_datetime_converter(deleted_at, APIHelper.RFC3339DateTime) if deleted_at else None 
        if description is not APIHelper.SKIP:
            self.description = description 
        if subscription is not APIHelper.SKIP:
            self.subscription = subscription 
        if subscription_item is not APIHelper.SKIP:
            self.subscription_item = subscription_item 

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
        from pagarmeapisdk.models.get_subscription_item_response import GetSubscriptionItemResponse

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        value = dictionary.get("value") if "value" in dictionary.keys() else APIHelper.SKIP
        increment_type = dictionary.get("increment_type") if "increment_type" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        cycles = dictionary.get("cycles") if "cycles" in dictionary.keys() else APIHelper.SKIP
        if 'deleted_at' in dictionary.keys():
            deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        else:
            deleted_at = APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        if 'subscription' in dictionary.keys():
            subscription = GetSubscriptionResponse.from_dictionary(dictionary.get('subscription')) if dictionary.get('subscription') else None
        else:
            subscription = APIHelper.SKIP
        if 'subscription_item' in dictionary.keys():
            subscription_item = GetSubscriptionItemResponse.from_dictionary(dictionary.get('subscription_item')) if dictionary.get('subscription_item') else None
        else:
            subscription_item = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   value,
                   increment_type,
                   status,
                   created_at,
                   cycles,
                   deleted_at,
                   description,
                   subscription,
                   subscription_item)
