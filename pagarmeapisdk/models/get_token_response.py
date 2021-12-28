# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_card_token_response import GetCardTokenResponse


class GetTokenResponse(object):

    """Implementation of the 'GetTokenResponse' model.

    Token data

    Attributes:
        id (string): TODO: type description here.
        mtype (string): TODO: type description here.
        created_at (datetime): TODO: type description here.
        expires_at (string): TODO: type description here.
        card (GetCardTokenResponse): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "mtype": 'type',
        "created_at": 'created_at',
        "expires_at": 'expires_at',
        "card": 'card'
    }

    def __init__(self,
                 id=None,
                 mtype=None,
                 created_at=None,
                 expires_at=None,
                 card=None):
        """Constructor for the GetTokenResponse class"""

        # Initialize members of the class
        self.id = id
        self.mtype = mtype
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.expires_at = expires_at
        self.card = card

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
        id = dictionary.get('id')
        mtype = dictionary.get('type')
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        expires_at = dictionary.get('expires_at')
        card = GetCardTokenResponse.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None

        # Return an object of this model
        return cls(id,
                   mtype,
                   created_at,
                   expires_at,
                   card)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
