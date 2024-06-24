# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.configuration import Server
from pagarmeapisdk.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from pagarmeapisdk.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from pagarmeapisdk.models.get_balance_operation_response import GetBalanceOperationResponse
from pagarmeapisdk.models.list_balance_operation_response import ListBalanceOperationResponse


class BalanceOperationsController(BaseController):

    """A Controller to access Endpoints in the pagarmeapisdk API."""
    def __init__(self, config):
        super(BalanceOperationsController, self).__init__(config)

    def get_balance_operation_by_id(self,
                                    id):
        """Does a GET request to /balance/operations/{id}.

        TODO: type endpoint description here.

        Args:
            id (long|int): TODO: type description here.

        Returns:
            GetBalanceOperationResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/balance/operations/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetBalanceOperationResponse.from_dictionary)
        ).execute()

    def get_balance_operations(self,
                               status=None,
                               created_since=None,
                               created_until=None,
                               recipient_id=None):
        """Does a GET request to /balance/operations.

        TODO: type endpoint description here.

        Args:
            status (str, optional): TODO: type description here.
            created_since (datetime, optional): TODO: type description here.
            created_until (datetime, optional): TODO: type description here.
            recipient_id (str, optional): TODO: type description here.

        Returns:
            ListBalanceOperationResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/balance/operations')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('status')
                         .value(status))
            .query_param(Parameter()
                         .key('created_since')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since)))
            .query_param(Parameter()
                         .key('created_until')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until)))
            .query_param(Parameter()
                         .key('recipient_id')
                         .value(recipient_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListBalanceOperationResponse.from_dictionary)
        ).execute()
