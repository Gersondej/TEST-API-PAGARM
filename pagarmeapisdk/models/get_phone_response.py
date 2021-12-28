# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class GetPhoneResponse(object):

    """Implementation of the 'GetPhoneResponse' model.

    TODO: type model description here.

    Attributes:
        country_code (string): TODO: type description here.
        number (string): TODO: type description here.
        area_code (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "country_code": 'country_code',
        "number": 'number',
        "area_code": 'area_code'
    }

    def __init__(self,
                 country_code=None,
                 number=None,
                 area_code=None):
        """Constructor for the GetPhoneResponse class"""

        # Initialize members of the class
        self.country_code = country_code
        self.number = number
        self.area_code = area_code

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
        country_code = dictionary.get('country_code')
        number = dictionary.get('number')
        area_code = dictionary.get('area_code')

        # Return an object of this model
        return cls(country_code,
                   number,
                   area_code)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
