# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.create_bank_transfer_payment_request import CreateBankTransferPaymentRequest
from pagarmeapisdk.models.create_boleto_payment_request import CreateBoletoPaymentRequest
from pagarmeapisdk.models.create_cash_payment_request import CreateCashPaymentRequest
from pagarmeapisdk.models.create_credit_card_payment_request import CreateCreditCardPaymentRequest
from pagarmeapisdk.models.create_debit_card_payment_request import CreateDebitCardPaymentRequest
from pagarmeapisdk.models.create_private_label_payment_request import CreatePrivateLabelPaymentRequest
from pagarmeapisdk.models.create_voucher_payment_request import CreateVoucherPaymentRequest


class UpdateChargePaymentMethodRequest(object):

    """Implementation of the 'UpdateChargePaymentMethodRequest' model.

    Request for updating the payment method of a charge

    Attributes:
        update_subscription (bool): Indicates if the payment method from the
            subscription must also be updated
        payment_method (string): The new payment method
        credit_card (CreateCreditCardPaymentRequest): Credit card data
        debit_card (CreateDebitCardPaymentRequest): Debit card data
        boleto (CreateBoletoPaymentRequest): Boleto data
        voucher (CreateVoucherPaymentRequest): Voucher data
        cash (CreateCashPaymentRequest): Cash data
        bank_transfer (CreateBankTransferPaymentRequest): Bank Transfer data
        private_label (CreatePrivateLabelPaymentRequest): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "update_subscription": 'update_subscription',
        "payment_method": 'payment_method',
        "credit_card": 'credit_card',
        "debit_card": 'debit_card',
        "boleto": 'boleto',
        "voucher": 'voucher',
        "cash": 'cash',
        "bank_transfer": 'bank_transfer',
        "private_label": 'private_label'
    }

    def __init__(self,
                 update_subscription=None,
                 payment_method=None,
                 credit_card=None,
                 debit_card=None,
                 boleto=None,
                 voucher=None,
                 cash=None,
                 bank_transfer=None,
                 private_label=None):
        """Constructor for the UpdateChargePaymentMethodRequest class"""

        # Initialize members of the class
        self.update_subscription = update_subscription
        self.payment_method = payment_method
        self.credit_card = credit_card
        self.debit_card = debit_card
        self.boleto = boleto
        self.voucher = voucher
        self.cash = cash
        self.bank_transfer = bank_transfer
        self.private_label = private_label

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
        update_subscription = dictionary.get('update_subscription')
        payment_method = dictionary.get('payment_method')
        credit_card = CreateCreditCardPaymentRequest.from_dictionary(dictionary.get('credit_card')) if dictionary.get('credit_card') else None
        debit_card = CreateDebitCardPaymentRequest.from_dictionary(dictionary.get('debit_card')) if dictionary.get('debit_card') else None
        boleto = CreateBoletoPaymentRequest.from_dictionary(dictionary.get('boleto')) if dictionary.get('boleto') else None
        voucher = CreateVoucherPaymentRequest.from_dictionary(dictionary.get('voucher')) if dictionary.get('voucher') else None
        cash = CreateCashPaymentRequest.from_dictionary(dictionary.get('cash')) if dictionary.get('cash') else None
        bank_transfer = CreateBankTransferPaymentRequest.from_dictionary(dictionary.get('bank_transfer')) if dictionary.get('bank_transfer') else None
        private_label = CreatePrivateLabelPaymentRequest.from_dictionary(dictionary.get('private_label')) if dictionary.get('private_label') else None

        # Return an object of this model
        return cls(update_subscription,
                   payment_method,
                   credit_card,
                   debit_card,
                   boleto,
                   voucher,
                   cash,
                   bank_transfer,
                   private_label)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
