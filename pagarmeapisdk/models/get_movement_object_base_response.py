# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetMovementObjectBaseResponse(object):

    """Implementation of the 'GetMovementObjectBaseResponse' model.

    Generic response object for getting a MovementObjectBase.

    Attributes:
        object (str): TODO: type description here.
        id (str): TODO: type description here.
        status (str): TODO: type description here.
        amount (str): TODO: type description here.
        created_at (str): TODO: type description here.
        mtype (str): TODO: type description here.
        charge_id (str): TODO: type description here.
        gateway_id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "object": 'object',
        "id": 'id',
        "status": 'status',
        "amount": 'amount',
        "created_at": 'created_at',
        "mtype": 'type',
        "charge_id": 'charge_id',
        "gateway_id": 'gateway_id'
    }

    _optionals = [
        'object',
        'id',
        'status',
        'amount',
        'created_at',
        'mtype',
        'charge_id',
        'gateway_id',
    ]

    _nullables = [
        'id',
        'status',
        'amount',
        'created_at',
        'mtype',
        'charge_id',
        'gateway_id',
    ]

    def __init__(self,
                 object='MovementObject',
                 id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 charge_id=APIHelper.SKIP,
                 gateway_id=APIHelper.SKIP):
        """Constructor for the GetMovementObjectBaseResponse class"""

        # Initialize members of the class
        self.object = object 
        if id is not APIHelper.SKIP:
            self.id = id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id 
        if gateway_id is not APIHelper.SKIP:
            self.gateway_id = gateway_id 

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

        discriminators = {
            'refund': GetMovementObjectRefundResponse.from_dictionary,
            'feeCollection': GetMovementObjectFeeCollectionResponse.from_dictionary,
            'payable': GetMovementObjectPayableResponse.from_dictionary,
            'transfer': GetMovementObjectTransferResponse.from_dictionary,
            'settlement': GetMovementObjectSettlementResponse.from_dictionary
        }
        unboxer = discriminators.get(dictionary.get('object'))

        # Delegate unboxing to another function if a discriminator
        # value for a child class is present.
        if unboxer:
            return unboxer(dictionary)

        # Extract variables from the dictionary
        object = dictionary.get("object") if dictionary.get("object") else 'MovementObject'
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if "created_at" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        charge_id = dictionary.get("charge_id") if "charge_id" in dictionary.keys() else APIHelper.SKIP
        gateway_id = dictionary.get("gateway_id") if "gateway_id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(object,
                   id,
                   status,
                   amount,
                   created_at,
                   mtype,
                   charge_id,
                   gateway_id)

class GetMovementObjectRefundResponse(GetMovementObjectBaseResponse):

    """Implementation of the 'GetMovementObjectRefundResponse' model.

    Generic response object for getting a MovementObjectRefund.
    NOTE: This class inherits from 'GetMovementObjectBaseResponse'.

    Attributes:
        fraud_coverage_fee (str): TODO: type description here.
        charge_fee_recipient_id (str): TODO: type description here.
        bank_account_id (str): TODO: type description here.
        local_transaction_id (str): TODO: type description here.
        updated_at (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fraud_coverage_fee": 'fraud_coverage_fee',
        "charge_fee_recipient_id": 'charge_fee_recipient_id',
        "bank_account_id": 'bank_account_id',
        "local_transaction_id": 'local_transaction_id',
        "updated_at": 'updated_at',
        "object": 'object',
        "id": 'id',
        "status": 'status',
        "amount": 'amount',
        "created_at": 'created_at',
        "mtype": 'type',
        "charge_id": 'charge_id',
        "gateway_id": 'gateway_id'
    }

    _optionals = [
        'fraud_coverage_fee',
        'charge_fee_recipient_id',
        'bank_account_id',
        'local_transaction_id',
        'updated_at',
    ]
    _optionals.extend(GetMovementObjectBaseResponse._optionals)

    _nullables = [
        'fraud_coverage_fee',
        'charge_fee_recipient_id',
        'bank_account_id',
        'local_transaction_id',
        'updated_at',
    ]
    _nullables.extend(GetMovementObjectBaseResponse._nullables)

    def __init__(self,
                 fraud_coverage_fee=APIHelper.SKIP,
                 charge_fee_recipient_id=APIHelper.SKIP,
                 bank_account_id=APIHelper.SKIP,
                 local_transaction_id=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 object='refund',
                 id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 charge_id=APIHelper.SKIP,
                 gateway_id=APIHelper.SKIP):
        """Constructor for the GetMovementObjectRefundResponse class"""

        # Initialize members of the class
        if fraud_coverage_fee is not APIHelper.SKIP:
            self.fraud_coverage_fee = fraud_coverage_fee 
        if charge_fee_recipient_id is not APIHelper.SKIP:
            self.charge_fee_recipient_id = charge_fee_recipient_id 
        if bank_account_id is not APIHelper.SKIP:
            self.bank_account_id = bank_account_id 
        if local_transaction_id is not APIHelper.SKIP:
            self.local_transaction_id = local_transaction_id 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 

        # Call the constructor for the base class
        super(GetMovementObjectRefundResponse, self).__init__(object,
                                                              id,
                                                              status,
                                                              amount,
                                                              created_at,
                                                              mtype,
                                                              charge_id,
                                                              gateway_id)

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
        fraud_coverage_fee = dictionary.get("fraud_coverage_fee") if "fraud_coverage_fee" in dictionary.keys() else APIHelper.SKIP
        charge_fee_recipient_id = dictionary.get("charge_fee_recipient_id") if "charge_fee_recipient_id" in dictionary.keys() else APIHelper.SKIP
        bank_account_id = dictionary.get("bank_account_id") if "bank_account_id" in dictionary.keys() else APIHelper.SKIP
        local_transaction_id = dictionary.get("local_transaction_id") if "local_transaction_id" in dictionary.keys() else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if "updated_at" in dictionary.keys() else APIHelper.SKIP
        object = dictionary.get("object") if dictionary.get("object") else 'refund'
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if "created_at" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        charge_id = dictionary.get("charge_id") if "charge_id" in dictionary.keys() else APIHelper.SKIP
        gateway_id = dictionary.get("gateway_id") if "gateway_id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(fraud_coverage_fee,
                   charge_fee_recipient_id,
                   bank_account_id,
                   local_transaction_id,
                   updated_at,
                   object,
                   id,
                   status,
                   amount,
                   created_at,
                   mtype,
                   charge_id,
                   gateway_id)

class GetMovementObjectFeeCollectionResponse(GetMovementObjectBaseResponse):

    """Implementation of the 'GetMovementObjectFeeCollectionResponse' model.

    Generic response object for getting a MovementObjectFeeCollection.
    NOTE: This class inherits from 'GetMovementObjectBaseResponse'.

    Attributes:
        description (str): TODO: type description here.
        payment_date (str): TODO: type description here.
        recipient_id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "payment_date": 'payment_date',
        "recipient_id": 'recipient_id',
        "object": 'object',
        "id": 'id',
        "status": 'status',
        "amount": 'amount',
        "created_at": 'created_at',
        "mtype": 'type',
        "charge_id": 'charge_id',
        "gateway_id": 'gateway_id'
    }

    _optionals = [
        'description',
        'payment_date',
        'recipient_id',
    ]
    _optionals.extend(GetMovementObjectBaseResponse._optionals)

    _nullables = [
        'description',
        'payment_date',
        'recipient_id',
    ]
    _nullables.extend(GetMovementObjectBaseResponse._nullables)

    def __init__(self,
                 description=APIHelper.SKIP,
                 payment_date=APIHelper.SKIP,
                 recipient_id=APIHelper.SKIP,
                 object='feeCollection',
                 id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 charge_id=APIHelper.SKIP,
                 gateway_id=APIHelper.SKIP):
        """Constructor for the GetMovementObjectFeeCollectionResponse class"""

        # Initialize members of the class
        if description is not APIHelper.SKIP:
            self.description = description 
        if payment_date is not APIHelper.SKIP:
            self.payment_date = payment_date 
        if recipient_id is not APIHelper.SKIP:
            self.recipient_id = recipient_id 

        # Call the constructor for the base class
        super(GetMovementObjectFeeCollectionResponse, self).__init__(object,
                                                                     id,
                                                                     status,
                                                                     amount,
                                                                     created_at,
                                                                     mtype,
                                                                     charge_id,
                                                                     gateway_id)

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
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        payment_date = dictionary.get("payment_date") if "payment_date" in dictionary.keys() else APIHelper.SKIP
        recipient_id = dictionary.get("recipient_id") if "recipient_id" in dictionary.keys() else APIHelper.SKIP
        object = dictionary.get("object") if dictionary.get("object") else 'feeCollection'
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if "created_at" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        charge_id = dictionary.get("charge_id") if "charge_id" in dictionary.keys() else APIHelper.SKIP
        gateway_id = dictionary.get("gateway_id") if "gateway_id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   payment_date,
                   recipient_id,
                   object,
                   id,
                   status,
                   amount,
                   created_at,
                   mtype,
                   charge_id,
                   gateway_id)

class GetMovementObjectPayableResponse(GetMovementObjectBaseResponse):

    """Implementation of the 'GetMovementObjectPayableResponse' model.

    TODO: type model description here.
    NOTE: This class inherits from 'GetMovementObjectBaseResponse'.

    Attributes:
        fee (str): TODO: type description here.
        anticipation_fee (str): TODO: type description here.
        fraud_coverage_fee (str): TODO: type description here.
        installment (str): TODO: type description here.
        split_id (str): TODO: type description here.
        bulk_anticipation_id (str): TODO: type description here.
        anticipation_id (str): TODO: type description here.
        recipient_id (str): TODO: type description here.
        originator_model (str): TODO: type description here.
        originator_model_id (str): TODO: type description here.
        payment_date (str): TODO: type description here.
        original_payment_date (str): TODO: type description here.
        payment_method (str): TODO: type description here.
        accrual_at (str): TODO: type description here.
        liquidation_arrangement_id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "anticipation_fee": 'anticipation_fee',
        "fraud_coverage_fee": 'fraud_coverage_fee',
        "installment": 'installment',
        "split_id": 'split_id',
        "bulk_anticipation_id": 'bulk_anticipation_id',
        "anticipation_id": 'anticipation_id',
        "recipient_id": 'recipient_id',
        "originator_model": 'originator_model',
        "originator_model_id": 'originator_model_id',
        "payment_date": 'payment_date',
        "original_payment_date": 'original_payment_date',
        "payment_method": 'payment_method',
        "accrual_at": 'accrual_at',
        "liquidation_arrangement_id": 'liquidation_arrangement_id',
        "fee": 'fee',
        "object": 'object',
        "id": 'id',
        "status": 'status',
        "amount": 'amount',
        "created_at": 'created_at',
        "mtype": 'type',
        "charge_id": 'charge_id',
        "gateway_id": 'gateway_id'
    }

    _optionals = [
        'fee',
    ]
    _optionals.extend(GetMovementObjectBaseResponse._optionals)

    _nullables = [
        'fee',
    ]
    _nullables.extend(GetMovementObjectBaseResponse._nullables)

    def __init__(self,
                 anticipation_fee=None,
                 fraud_coverage_fee=None,
                 installment=None,
                 split_id=None,
                 bulk_anticipation_id=None,
                 anticipation_id=None,
                 recipient_id=None,
                 originator_model=None,
                 originator_model_id=None,
                 payment_date=None,
                 original_payment_date=None,
                 payment_method=None,
                 accrual_at=None,
                 liquidation_arrangement_id=None,
                 fee=APIHelper.SKIP,
                 object='payable',
                 id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 charge_id=APIHelper.SKIP,
                 gateway_id=APIHelper.SKIP):
        """Constructor for the GetMovementObjectPayableResponse class"""

        # Initialize members of the class
        if fee is not APIHelper.SKIP:
            self.fee = fee 
        self.anticipation_fee = anticipation_fee 
        self.fraud_coverage_fee = fraud_coverage_fee 
        self.installment = installment 
        self.split_id = split_id 
        self.bulk_anticipation_id = bulk_anticipation_id 
        self.anticipation_id = anticipation_id 
        self.recipient_id = recipient_id 
        self.originator_model = originator_model 
        self.originator_model_id = originator_model_id 
        self.payment_date = payment_date 
        self.original_payment_date = original_payment_date 
        self.payment_method = payment_method 
        self.accrual_at = accrual_at 
        self.liquidation_arrangement_id = liquidation_arrangement_id 

        # Call the constructor for the base class
        super(GetMovementObjectPayableResponse, self).__init__(object,
                                                               id,
                                                               status,
                                                               amount,
                                                               created_at,
                                                               mtype,
                                                               charge_id,
                                                               gateway_id)

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
        anticipation_fee = dictionary.get("anticipation_fee") if dictionary.get("anticipation_fee") else None
        fraud_coverage_fee = dictionary.get("fraud_coverage_fee") if dictionary.get("fraud_coverage_fee") else None
        installment = dictionary.get("installment") if dictionary.get("installment") else None
        split_id = dictionary.get("split_id") if dictionary.get("split_id") else None
        bulk_anticipation_id = dictionary.get("bulk_anticipation_id") if dictionary.get("bulk_anticipation_id") else None
        anticipation_id = dictionary.get("anticipation_id") if dictionary.get("anticipation_id") else None
        recipient_id = dictionary.get("recipient_id") if dictionary.get("recipient_id") else None
        originator_model = dictionary.get("originator_model") if dictionary.get("originator_model") else None
        originator_model_id = dictionary.get("originator_model_id") if dictionary.get("originator_model_id") else None
        payment_date = dictionary.get("payment_date") if dictionary.get("payment_date") else None
        original_payment_date = dictionary.get("original_payment_date") if dictionary.get("original_payment_date") else None
        payment_method = dictionary.get("payment_method") if dictionary.get("payment_method") else None
        accrual_at = dictionary.get("accrual_at") if dictionary.get("accrual_at") else None
        liquidation_arrangement_id = dictionary.get("liquidation_arrangement_id") if dictionary.get("liquidation_arrangement_id") else None
        fee = dictionary.get("fee") if "fee" in dictionary.keys() else APIHelper.SKIP
        object = dictionary.get("object") if dictionary.get("object") else 'payable'
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if "created_at" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        charge_id = dictionary.get("charge_id") if "charge_id" in dictionary.keys() else APIHelper.SKIP
        gateway_id = dictionary.get("gateway_id") if "gateway_id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(anticipation_fee,
                   fraud_coverage_fee,
                   installment,
                   split_id,
                   bulk_anticipation_id,
                   anticipation_id,
                   recipient_id,
                   originator_model,
                   originator_model_id,
                   payment_date,
                   original_payment_date,
                   payment_method,
                   accrual_at,
                   liquidation_arrangement_id,
                   fee,
                   object,
                   id,
                   status,
                   amount,
                   created_at,
                   mtype,
                   charge_id,
                   gateway_id)

class GetMovementObjectTransferResponse(GetMovementObjectBaseResponse):

    """Implementation of the 'GetMovementObjectTransferResponse' model.

    TODO: type model description here.
    NOTE: This class inherits from 'GetMovementObjectBaseResponse'.

    Attributes:
        source_type (str): TODO: type description here.
        source_id (str): TODO: type description here.
        target_type (str): TODO: type description here.
        target_id (str): TODO: type description here.
        fee (str): TODO: type description here.
        funding_date (str): TODO: type description here.
        funding_estimated_date (str): TODO: type description here.
        bank_account (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "source_type": 'source_type',
        "source_id": 'source_id',
        "target_type": 'target_type',
        "target_id": 'target_id',
        "fee": 'fee',
        "funding_date": 'funding_date',
        "funding_estimated_date": 'funding_estimated_date',
        "bank_account": 'bank_account',
        "object": 'object',
        "id": 'id',
        "status": 'status',
        "amount": 'amount',
        "created_at": 'created_at',
        "mtype": 'type',
        "charge_id": 'charge_id',
        "gateway_id": 'gateway_id'
    }

    _optionals = [
        'source_type',
        'source_id',
        'target_type',
        'target_id',
        'fee',
        'funding_date',
        'funding_estimated_date',
        'bank_account',
    ]
    _optionals.extend(GetMovementObjectBaseResponse._optionals)

    _nullables = [
        'source_type',
        'source_id',
        'target_type',
        'target_id',
        'fee',
        'funding_date',
        'funding_estimated_date',
        'bank_account',
    ]
    _nullables.extend(GetMovementObjectBaseResponse._nullables)

    def __init__(self,
                 source_type=APIHelper.SKIP,
                 source_id=APIHelper.SKIP,
                 target_type=APIHelper.SKIP,
                 target_id=APIHelper.SKIP,
                 fee=APIHelper.SKIP,
                 funding_date=APIHelper.SKIP,
                 funding_estimated_date=APIHelper.SKIP,
                 bank_account=APIHelper.SKIP,
                 object='transfer',
                 id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 charge_id=APIHelper.SKIP,
                 gateway_id=APIHelper.SKIP):
        """Constructor for the GetMovementObjectTransferResponse class"""

        # Initialize members of the class
        if source_type is not APIHelper.SKIP:
            self.source_type = source_type 
        if source_id is not APIHelper.SKIP:
            self.source_id = source_id 
        if target_type is not APIHelper.SKIP:
            self.target_type = target_type 
        if target_id is not APIHelper.SKIP:
            self.target_id = target_id 
        if fee is not APIHelper.SKIP:
            self.fee = fee 
        if funding_date is not APIHelper.SKIP:
            self.funding_date = funding_date 
        if funding_estimated_date is not APIHelper.SKIP:
            self.funding_estimated_date = funding_estimated_date 
        if bank_account is not APIHelper.SKIP:
            self.bank_account = bank_account 

        # Call the constructor for the base class
        super(GetMovementObjectTransferResponse, self).__init__(object,
                                                                id,
                                                                status,
                                                                amount,
                                                                created_at,
                                                                mtype,
                                                                charge_id,
                                                                gateway_id)

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
        source_type = dictionary.get("source_type") if "source_type" in dictionary.keys() else APIHelper.SKIP
        source_id = dictionary.get("source_id") if "source_id" in dictionary.keys() else APIHelper.SKIP
        target_type = dictionary.get("target_type") if "target_type" in dictionary.keys() else APIHelper.SKIP
        target_id = dictionary.get("target_id") if "target_id" in dictionary.keys() else APIHelper.SKIP
        fee = dictionary.get("fee") if "fee" in dictionary.keys() else APIHelper.SKIP
        funding_date = dictionary.get("funding_date") if "funding_date" in dictionary.keys() else APIHelper.SKIP
        funding_estimated_date = dictionary.get("funding_estimated_date") if "funding_estimated_date" in dictionary.keys() else APIHelper.SKIP
        bank_account = dictionary.get("bank_account") if "bank_account" in dictionary.keys() else APIHelper.SKIP
        object = dictionary.get("object") if dictionary.get("object") else 'transfer'
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if "created_at" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        charge_id = dictionary.get("charge_id") if "charge_id" in dictionary.keys() else APIHelper.SKIP
        gateway_id = dictionary.get("gateway_id") if "gateway_id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(source_type,
                   source_id,
                   target_type,
                   target_id,
                   fee,
                   funding_date,
                   funding_estimated_date,
                   bank_account,
                   object,
                   id,
                   status,
                   amount,
                   created_at,
                   mtype,
                   charge_id,
                   gateway_id)

class GetMovementObjectSettlementResponse(GetMovementObjectBaseResponse):

    """Implementation of the 'GetMovementObjectSettlementResponse' model.

    Generic response object for getting a MovementObjectSettlement.
    NOTE: This class inherits from 'GetMovementObjectBaseResponse'.

    Attributes:
        product (str): TODO: type description here.
        brand (str): TODO: type description here.
        payment_date (str): TODO: type description here.
        recipient_id (str): TODO: type description here.
        document_type (str): TODO: type description here.
        document (str): TODO: type description here.
        contract_obligation_id (str): TODO: type description here.
        liquidation_arrangement_id (str): TODO: type description here.
        external_engine_payment_id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product": 'product',
        "brand": 'brand',
        "payment_date": 'payment_date',
        "recipient_id": 'recipient_id',
        "document_type": 'document_type',
        "document": 'document',
        "contract_obligation_id": 'contract_obligation_id',
        "liquidation_arrangement_id": 'liquidation_arrangement_id',
        "external_engine_payment_id": 'external_engine_payment_id',
        "object": 'object',
        "id": 'id',
        "status": 'status',
        "amount": 'amount',
        "created_at": 'created_at',
        "mtype": 'type',
        "charge_id": 'charge_id',
        "gateway_id": 'gateway_id'
    }

    _optionals = [
        'product',
        'brand',
        'payment_date',
        'recipient_id',
        'document_type',
        'document',
        'contract_obligation_id',
        'liquidation_arrangement_id',
        'external_engine_payment_id',
    ]
    _optionals.extend(GetMovementObjectBaseResponse._optionals)

    _nullables = [
        'product',
        'brand',
        'payment_date',
        'recipient_id',
        'document_type',
        'document',
        'contract_obligation_id',
        'liquidation_arrangement_id',
        'external_engine_payment_id',
    ]
    _nullables.extend(GetMovementObjectBaseResponse._nullables)

    def __init__(self,
                 product=APIHelper.SKIP,
                 brand=APIHelper.SKIP,
                 payment_date=APIHelper.SKIP,
                 recipient_id=APIHelper.SKIP,
                 document_type=APIHelper.SKIP,
                 document=APIHelper.SKIP,
                 contract_obligation_id=APIHelper.SKIP,
                 liquidation_arrangement_id=APIHelper.SKIP,
                 external_engine_payment_id=APIHelper.SKIP,
                 object='settlement',
                 id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 charge_id=APIHelper.SKIP,
                 gateway_id=APIHelper.SKIP):
        """Constructor for the GetMovementObjectSettlementResponse class"""

        # Initialize members of the class
        if product is not APIHelper.SKIP:
            self.product = product 
        if brand is not APIHelper.SKIP:
            self.brand = brand 
        if payment_date is not APIHelper.SKIP:
            self.payment_date = payment_date 
        if recipient_id is not APIHelper.SKIP:
            self.recipient_id = recipient_id 
        if document_type is not APIHelper.SKIP:
            self.document_type = document_type 
        if document is not APIHelper.SKIP:
            self.document = document 
        if contract_obligation_id is not APIHelper.SKIP:
            self.contract_obligation_id = contract_obligation_id 
        if liquidation_arrangement_id is not APIHelper.SKIP:
            self.liquidation_arrangement_id = liquidation_arrangement_id 
        if external_engine_payment_id is not APIHelper.SKIP:
            self.external_engine_payment_id = external_engine_payment_id 

        # Call the constructor for the base class
        super(GetMovementObjectSettlementResponse, self).__init__(object,
                                                                  id,
                                                                  status,
                                                                  amount,
                                                                  created_at,
                                                                  mtype,
                                                                  charge_id,
                                                                  gateway_id)

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
        product = dictionary.get("product") if "product" in dictionary.keys() else APIHelper.SKIP
        brand = dictionary.get("brand") if "brand" in dictionary.keys() else APIHelper.SKIP
        payment_date = dictionary.get("payment_date") if "payment_date" in dictionary.keys() else APIHelper.SKIP
        recipient_id = dictionary.get("recipient_id") if "recipient_id" in dictionary.keys() else APIHelper.SKIP
        document_type = dictionary.get("document_type") if "document_type" in dictionary.keys() else APIHelper.SKIP
        document = dictionary.get("document") if "document" in dictionary.keys() else APIHelper.SKIP
        contract_obligation_id = dictionary.get("contract_obligation_id") if "contract_obligation_id" in dictionary.keys() else APIHelper.SKIP
        liquidation_arrangement_id = dictionary.get("liquidation_arrangement_id") if "liquidation_arrangement_id" in dictionary.keys() else APIHelper.SKIP
        external_engine_payment_id = dictionary.get("external_engine_payment_id") if "external_engine_payment_id" in dictionary.keys() else APIHelper.SKIP
        object = dictionary.get("object") if dictionary.get("object") else 'settlement'
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if "created_at" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        charge_id = dictionary.get("charge_id") if "charge_id" in dictionary.keys() else APIHelper.SKIP
        gateway_id = dictionary.get("gateway_id") if "gateway_id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(product,
                   brand,
                   payment_date,
                   recipient_id,
                   document_type,
                   document,
                   contract_obligation_id,
                   liquidation_arrangement_id,
                   external_engine_payment_id,
                   object,
                   id,
                   status,
                   amount,
                   created_at,
                   mtype,
                   charge_id,
                   gateway_id)
