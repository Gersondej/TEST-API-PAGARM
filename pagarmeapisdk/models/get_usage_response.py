# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_subscription_item_response import GetSubscriptionItemResponse


class GetUsageResponse(object):

    """Implementation of the 'GetUsageResponse' model.

    Response object for getting a usage

    Attributes:
        id (str): Id
        quantity (int): Quantity
        description (str): Description
        used_at (datetime): Used at
        created_at (datetime): Creation date
        status (str): Status
        deleted_at (datetime): TODO: type description here.
        subscription_item (GetSubscriptionItemResponse): Subscription item
        code (str): Identification code in the client system
        group (str): Identification group in the client system
        amount (int): Field used in item scheme type 'Percent'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "quantity": 'quantity',
        "description": 'description',
        "used_at": 'used_at',
        "created_at": 'created_at',
        "status": 'status',
        "deleted_at": 'deleted_at',
        "subscription_item": 'subscription_item',
        "code": 'code',
        "group": 'group',
        "amount": 'amount'
    }

    _optionals = [
        'id',
        'quantity',
        'description',
        'used_at',
        'created_at',
        'status',
        'deleted_at',
        'subscription_item',
        'code',
        'group',
        'amount',
    ]

    _nullables = [
        'id',
        'quantity',
        'description',
        'used_at',
        'created_at',
        'status',
        'deleted_at',
        'subscription_item',
        'code',
        'group',
        'amount',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 used_at=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 deleted_at=APIHelper.SKIP,
                 subscription_item=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 group=APIHelper.SKIP,
                 amount=APIHelper.SKIP):
        """Constructor for the GetUsageResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if description is not APIHelper.SKIP:
            self.description = description 
        if used_at is not APIHelper.SKIP:
            self.used_at = APIHelper.apply_datetime_converter(used_at, APIHelper.RFC3339DateTime) if used_at else None 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if status is not APIHelper.SKIP:
            self.status = status 
        if deleted_at is not APIHelper.SKIP:
            self.deleted_at = APIHelper.apply_datetime_converter(deleted_at, APIHelper.RFC3339DateTime) if deleted_at else None 
        if subscription_item is not APIHelper.SKIP:
            self.subscription_item = subscription_item 
        if code is not APIHelper.SKIP:
            self.code = code 
        if group is not APIHelper.SKIP:
            self.group = group 
        if amount is not APIHelper.SKIP:
            self.amount = amount 

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
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        quantity = dictionary.get("quantity") if "quantity" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        if 'used_at' in dictionary.keys():
            used_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("used_at")).datetime if dictionary.get("used_at") else None
        else:
            used_at = APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'deleted_at' in dictionary.keys():
            deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        else:
            deleted_at = APIHelper.SKIP
        if 'subscription_item' in dictionary.keys():
            subscription_item = GetSubscriptionItemResponse.from_dictionary(dictionary.get('subscription_item')) if dictionary.get('subscription_item') else None
        else:
            subscription_item = APIHelper.SKIP
        code = dictionary.get("code") if "code" in dictionary.keys() else APIHelper.SKIP
        group = dictionary.get("group") if "group" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   quantity,
                   description,
                   used_at,
                   created_at,
                   status,
                   deleted_at,
                   subscription_item,
                   code,
                   group,
                   amount)
