# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetPlanResponse(object):

    """Implementation of the 'GetPlanResponse' model.

    Response object for getting a plan

    Attributes:
        id (str): TODO: type description here.
        name (str): TODO: type description here.
        description (str): TODO: type description here.
        url (str): TODO: type description here.
        statement_descriptor (str): TODO: type description here.
        interval (str): TODO: type description here.
        interval_count (int): TODO: type description here.
        billing_type (str): TODO: type description here.
        payment_methods (List[str]): TODO: type description here.
        installments (List[int]): TODO: type description here.
        status (str): TODO: type description here.
        currency (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        items (List[GetPlanItemResponse]): TODO: type description here.
        billing_days (List[int]): TODO: type description here.
        shippable (bool): TODO: type description here.
        metadata (Dict[str, str]): TODO: type description here.
        trial_period_days (int): TODO: type description here.
        minimum_price (int): TODO: type description here.
        deleted_at (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "description": 'description',
        "url": 'url',
        "statement_descriptor": 'statement_descriptor',
        "interval": 'interval',
        "interval_count": 'interval_count',
        "billing_type": 'billing_type',
        "payment_methods": 'payment_methods',
        "installments": 'installments',
        "status": 'status',
        "currency": 'currency',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "items": 'items',
        "billing_days": 'billing_days',
        "shippable": 'shippable',
        "metadata": 'metadata',
        "trial_period_days": 'trial_period_days',
        "minimum_price": 'minimum_price',
        "deleted_at": 'deleted_at'
    }

    _optionals = [
        'id',
        'name',
        'description',
        'url',
        'statement_descriptor',
        'interval',
        'interval_count',
        'billing_type',
        'payment_methods',
        'installments',
        'status',
        'currency',
        'created_at',
        'updated_at',
        'items',
        'billing_days',
        'shippable',
        'metadata',
        'trial_period_days',
        'minimum_price',
        'deleted_at',
    ]

    _nullables = [
        'id',
        'name',
        'description',
        'url',
        'statement_descriptor',
        'interval',
        'interval_count',
        'billing_type',
        'payment_methods',
        'installments',
        'status',
        'currency',
        'created_at',
        'updated_at',
        'items',
        'billing_days',
        'shippable',
        'metadata',
        'trial_period_days',
        'minimum_price',
        'deleted_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 url=APIHelper.SKIP,
                 statement_descriptor=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_count=APIHelper.SKIP,
                 billing_type=APIHelper.SKIP,
                 payment_methods=APIHelper.SKIP,
                 installments=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 items=APIHelper.SKIP,
                 billing_days=APIHelper.SKIP,
                 shippable=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 trial_period_days=APIHelper.SKIP,
                 minimum_price=APIHelper.SKIP,
                 deleted_at=APIHelper.SKIP):
        """Constructor for the GetPlanResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if description is not APIHelper.SKIP:
            self.description = description 
        if url is not APIHelper.SKIP:
            self.url = url 
        if statement_descriptor is not APIHelper.SKIP:
            self.statement_descriptor = statement_descriptor 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_count is not APIHelper.SKIP:
            self.interval_count = interval_count 
        if billing_type is not APIHelper.SKIP:
            self.billing_type = billing_type 
        if payment_methods is not APIHelper.SKIP:
            self.payment_methods = payment_methods 
        if installments is not APIHelper.SKIP:
            self.installments = installments 
        if status is not APIHelper.SKIP:
            self.status = status 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if items is not APIHelper.SKIP:
            self.items = items 
        if billing_days is not APIHelper.SKIP:
            self.billing_days = billing_days 
        if shippable is not APIHelper.SKIP:
            self.shippable = shippable 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if trial_period_days is not APIHelper.SKIP:
            self.trial_period_days = trial_period_days 
        if minimum_price is not APIHelper.SKIP:
            self.minimum_price = minimum_price 
        if deleted_at is not APIHelper.SKIP:
            self.deleted_at = APIHelper.apply_datetime_converter(deleted_at, APIHelper.RFC3339DateTime) if deleted_at else None 

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
        from pagarmeapisdk.models.get_plan_item_response import GetPlanItemResponse

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if "name" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        url = dictionary.get("url") if "url" in dictionary.keys() else APIHelper.SKIP
        statement_descriptor = dictionary.get("statement_descriptor") if "statement_descriptor" in dictionary.keys() else APIHelper.SKIP
        interval = dictionary.get("interval") if "interval" in dictionary.keys() else APIHelper.SKIP
        interval_count = dictionary.get("interval_count") if "interval_count" in dictionary.keys() else APIHelper.SKIP
        billing_type = dictionary.get("billing_type") if "billing_type" in dictionary.keys() else APIHelper.SKIP
        payment_methods = dictionary.get("payment_methods") if "payment_methods" in dictionary.keys() else APIHelper.SKIP
        installments = dictionary.get("installments") if "installments" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        currency = dictionary.get("currency") if "currency" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        if 'items' in dictionary.keys():
            items = [GetPlanItemResponse.from_dictionary(x) for x in dictionary.get('items')] if dictionary.get('items') else None
        else:
            items = APIHelper.SKIP
        billing_days = dictionary.get("billing_days") if "billing_days" in dictionary.keys() else APIHelper.SKIP
        shippable = dictionary.get("shippable") if "shippable" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if "metadata" in dictionary.keys() else APIHelper.SKIP
        trial_period_days = dictionary.get("trial_period_days") if "trial_period_days" in dictionary.keys() else APIHelper.SKIP
        minimum_price = dictionary.get("minimum_price") if "minimum_price" in dictionary.keys() else APIHelper.SKIP
        if 'deleted_at' in dictionary.keys():
            deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        else:
            deleted_at = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   description,
                   url,
                   statement_descriptor,
                   interval,
                   interval_count,
                   billing_type,
                   payment_methods,
                   installments,
                   status,
                   currency,
                   created_at,
                   updated_at,
                   items,
                   billing_days,
                   shippable,
                   metadata,
                   trial_period_days,
                   minimum_price,
                   deleted_at)
