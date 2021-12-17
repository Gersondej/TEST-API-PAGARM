# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class GetAnticipationLimitResponse(object):

    """Implementation of the 'GetAnticipationLimitResponse' model.

    Anticipation limit

    Attributes:
        amount (int): Amount
        anticipation_fee (int): Anticipation fee

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "anticipation_fee": 'anticipation_fee'
    }

    def __init__(self,
                 amount=None,
                 anticipation_fee=None):
        """Constructor for the GetAnticipationLimitResponse class"""

        # Initialize members of the class
        self.amount = amount
        self.anticipation_fee = anticipation_fee

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
        amount = dictionary.get('amount')
        anticipation_fee = dictionary.get('anticipation_fee')

        # Return an object of this model
        return cls(amount,
                   anticipation_fee)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
