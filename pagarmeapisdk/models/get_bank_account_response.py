# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_recipient_response import GetRecipientResponse


class GetBankAccountResponse(object):

    """Implementation of the 'GetBankAccountResponse' model.

    TODO: type model description here.

    Attributes:
        id (string): Id
        holder_name (string): Holder name
        holder_type (string): Holder type
        bank (string): Bank
        branch_number (string): Branch number
        branch_check_digit (string): Branch check digit
        account_number (string): Account number
        account_check_digit (string): Account check digit
        mtype (string): Bank account type
        status (string): Bank account status
        created_at (datetime): Creation date
        updated_at (datetime): Last update date
        deleted_at (datetime): Deletion date
        recipient (GetRecipientResponse): Recipient
        metadata (dict): Metadata
        pix_key (string): Pix Key

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "holder_name": 'holder_name',
        "holder_type": 'holder_type',
        "bank": 'bank',
        "branch_number": 'branch_number',
        "branch_check_digit": 'branch_check_digit',
        "account_number": 'account_number',
        "account_check_digit": 'account_check_digit',
        "mtype": 'type',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "deleted_at": 'deleted_at',
        "metadata": 'metadata',
        "pix_key": 'pix_key',
        "recipient": 'recipient'
    }

    def __init__(self,
                 id=None,
                 holder_name=None,
                 holder_type=None,
                 bank=None,
                 branch_number=None,
                 branch_check_digit=None,
                 account_number=None,
                 account_check_digit=None,
                 mtype=None,
                 status=None,
                 created_at=None,
                 updated_at=None,
                 deleted_at=None,
                 metadata=None,
                 pix_key=None,
                 recipient=None):
        """Constructor for the GetBankAccountResponse class"""

        # Initialize members of the class
        self.id = id
        self.holder_name = holder_name
        self.holder_type = holder_type
        self.bank = bank
        self.branch_number = branch_number
        self.branch_check_digit = branch_check_digit
        self.account_number = account_number
        self.account_check_digit = account_check_digit
        self.mtype = mtype
        self.status = status
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.deleted_at = APIHelper.RFC3339DateTime(deleted_at) if deleted_at else None
        self.recipient = recipient
        self.metadata = metadata
        self.pix_key = pix_key

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
        holder_name = dictionary.get('holder_name')
        holder_type = dictionary.get('holder_type')
        bank = dictionary.get('bank')
        branch_number = dictionary.get('branch_number')
        branch_check_digit = dictionary.get('branch_check_digit')
        account_number = dictionary.get('account_number')
        account_check_digit = dictionary.get('account_check_digit')
        mtype = dictionary.get('type')
        status = dictionary.get('status')
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        metadata = dictionary.get('metadata')
        pix_key = dictionary.get('pix_key')
        recipient = GetRecipientResponse.from_dictionary(dictionary.get('recipient')) if dictionary.get('recipient') else None

        # Return an object of this model
        return cls(id,
                   holder_name,
                   holder_type,
                   bank,
                   branch_number,
                   branch_check_digit,
                   account_number,
                   account_check_digit,
                   mtype,
                   status,
                   created_at,
                   updated_at,
                   deleted_at,
                   metadata,
                   pix_key,
                   recipient)
