# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class CreateTransactionReportFileRequest(object):

    """Implementation of the 'CreateTransactionReportFileRequest' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        start_at (datetime): TODO: type description here.
        end_at (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "start_at": 'start_at',
        "end_at": 'end_at'
    }

    _optionals = [
        'start_at',
        'end_at',
    ]

    def __init__(self,
                 name=None,
                 start_at=APIHelper.SKIP,
                 end_at=APIHelper.SKIP):
        """Constructor for the CreateTransactionReportFileRequest class"""

        # Initialize members of the class
        self.name = name 
        if start_at is not APIHelper.SKIP:
            self.start_at = APIHelper.apply_datetime_converter(start_at, APIHelper.RFC3339DateTime) if start_at else None 
        if end_at is not APIHelper.SKIP:
            self.end_at = end_at 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        start_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_at")).datetime if dictionary.get("start_at") else APIHelper.SKIP
        end_at = dictionary.get("end_at") if dictionary.get("end_at") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   start_at,
                   end_at)
