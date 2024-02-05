# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_pricing_scheme_response import GetPricingSchemeResponse


class GetPlanItemResponse(object):

    """Implementation of the 'GetPlanItemResponse' model.

    Response object for getting a plan item

    Attributes:
        id (str): TODO: type description here.
        name (str): TODO: type description here.
        status (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        pricing_scheme (GetPricingSchemeResponse): TODO: type description
            here.
        description (str): TODO: type description here.
        plan (GetPlanResponse): TODO: type description here.
        quantity (int): TODO: type description here.
        cycles (int): TODO: type description here.
        deleted_at (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "pricing_scheme": 'pricing_scheme',
        "description": 'description',
        "plan": 'plan',
        "quantity": 'quantity',
        "cycles": 'cycles',
        "deleted_at": 'deleted_at'
    }

    _optionals = [
        'id',
        'name',
        'status',
        'created_at',
        'updated_at',
        'pricing_scheme',
        'description',
        'plan',
        'quantity',
        'cycles',
        'deleted_at',
    ]

    _nullables = [
        'id',
        'name',
        'status',
        'created_at',
        'updated_at',
        'pricing_scheme',
        'description',
        'plan',
        'quantity',
        'cycles',
        'deleted_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 plan=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 cycles=APIHelper.SKIP,
                 deleted_at=APIHelper.SKIP):
        """Constructor for the GetPlanItemResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if status is not APIHelper.SKIP:
            self.status = status 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if description is not APIHelper.SKIP:
            self.description = description 
        if plan is not APIHelper.SKIP:
            self.plan = plan 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if cycles is not APIHelper.SKIP:
            self.cycles = cycles 
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
        from pagarmeapisdk.models.get_plan_response import GetPlanResponse

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if "name" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        if 'pricing_scheme' in dictionary.keys():
            pricing_scheme = GetPricingSchemeResponse.from_dictionary(dictionary.get('pricing_scheme')) if dictionary.get('pricing_scheme') else None
        else:
            pricing_scheme = APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        if 'plan' in dictionary.keys():
            plan = GetPlanResponse.from_dictionary(dictionary.get('plan')) if dictionary.get('plan') else None
        else:
            plan = APIHelper.SKIP
        quantity = dictionary.get("quantity") if "quantity" in dictionary.keys() else APIHelper.SKIP
        cycles = dictionary.get("cycles") if "cycles" in dictionary.keys() else APIHelper.SKIP
        if 'deleted_at' in dictionary.keys():
            deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        else:
            deleted_at = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   status,
                   created_at,
                   updated_at,
                   pricing_scheme,
                   description,
                   plan,
                   quantity,
                   cycles,
                   deleted_at)
