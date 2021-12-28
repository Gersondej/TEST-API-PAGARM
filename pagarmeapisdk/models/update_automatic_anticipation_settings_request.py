# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UpdateAutomaticAnticipationSettingsRequest(object):

    """Implementation of the 'UpdateAutomaticAnticipationSettingsRequest' model.

    TODO: type model description here.

    Attributes:
        enabled (bool): TODO: type description here.
        mtype (string): TODO: type description here.
        volume_percentage (int): TODO: type description here.
        delay (int): TODO: type description here.
        days (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled',
        "mtype": 'type',
        "volume_percentage": 'volume_percentage',
        "delay": 'delay',
        "days": 'days'
    }

    def __init__(self,
                 enabled=None,
                 mtype=None,
                 volume_percentage=None,
                 delay=None,
                 days=None):
        """Constructor for the UpdateAutomaticAnticipationSettingsRequest class"""

        # Initialize members of the class
        self.enabled = enabled
        self.mtype = mtype
        self.volume_percentage = volume_percentage
        self.delay = delay
        self.days = days

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
        enabled = dictionary.get('enabled')
        mtype = dictionary.get('type')
        volume_percentage = dictionary.get('volume_percentage')
        delay = dictionary.get('delay')
        days = dictionary.get('days')

        # Return an object of this model
        return cls(enabled,
                   mtype,
                   volume_percentage,
                   delay,
                   days)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
