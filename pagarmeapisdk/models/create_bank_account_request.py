# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class CreateBankAccountRequest(object):

    """Implementation of the 'CreateBankAccountRequest' model.

    Request for creating a bank account

    Attributes:
        holder_name (str): Bank account holder name
        holder_type (str): Bank account holder type
        holder_document (str): Bank account holder document
        bank (str): Bank
        branch_number (str): Branch number
        branch_check_digit (str): Branch check digit
        account_number (str): Account number
        account_check_digit (str): Account check digit
        mtype (str): Bank account type
        metadata (Dict[str, str]): Metadata
        pix_key (str): Pix key

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "holder_name": 'holder_name',
        "holder_type": 'holder_type',
        "holder_document": 'holder_document',
        "bank": 'bank',
        "branch_number": 'branch_number',
        "account_number": 'account_number',
        "account_check_digit": 'account_check_digit',
        "mtype": 'type',
        "metadata": 'metadata',
        "branch_check_digit": 'branch_check_digit',
        "pix_key": 'pix_key'
    }

    _optionals = [
        'branch_check_digit',
        'pix_key',
    ]

    _nullables = [
        'branch_check_digit',
        'pix_key',
    ]

    def __init__(self,
                 holder_name=None,
                 holder_type=None,
                 holder_document=None,
                 bank=None,
                 branch_number=None,
                 account_number=None,
                 account_check_digit=None,
                 mtype=None,
                 metadata=None,
                 branch_check_digit=APIHelper.SKIP,
                 pix_key=APIHelper.SKIP):
        """Constructor for the CreateBankAccountRequest class"""

        # Initialize members of the class
        self.holder_name = holder_name 
        self.holder_type = holder_type 
        self.holder_document = holder_document 
        self.bank = bank 
        self.branch_number = branch_number 
        if branch_check_digit is not APIHelper.SKIP:
            self.branch_check_digit = branch_check_digit 
        self.account_number = account_number 
        self.account_check_digit = account_check_digit 
        self.mtype = mtype 
        self.metadata = metadata 
        if pix_key is not APIHelper.SKIP:
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
        holder_name = dictionary.get("holder_name") if dictionary.get("holder_name") else None
        holder_type = dictionary.get("holder_type") if dictionary.get("holder_type") else None
        holder_document = dictionary.get("holder_document") if dictionary.get("holder_document") else None
        bank = dictionary.get("bank") if dictionary.get("bank") else None
        branch_number = dictionary.get("branch_number") if dictionary.get("branch_number") else None
        account_number = dictionary.get("account_number") if dictionary.get("account_number") else None
        account_check_digit = dictionary.get("account_check_digit") if dictionary.get("account_check_digit") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else None
        branch_check_digit = dictionary.get("branch_check_digit") if "branch_check_digit" in dictionary.keys() else APIHelper.SKIP
        pix_key = dictionary.get("pix_key") if "pix_key" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(holder_name,
                   holder_type,
                   holder_document,
                   bank,
                   branch_number,
                   account_number,
                   account_check_digit,
                   mtype,
                   metadata,
                   branch_check_digit,
                   pix_key)
