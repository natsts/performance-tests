from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema,
    GetOperationResponseSchema,
    GetOperationReceiptResponseSchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryQuerySchema,
    GetOperationsSummaryResponseSchema,
    MakeOperationRequestSchema,
    MakePurchaseOperationRequestSchema
)


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(url=f'/api/v1/operations/{operation_id}')

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(url=f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(url='/api/v1/operations',
                        params=QueryParams(**query.model_dump(by_alias=True))
                        )

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(url='/api/v1/operations/operations-summary',
                        params=QueryParams(**query.model_dump(by_alias=True))
                        )

    def make_fee_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создание операции комиссии.

        :param request: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/operations/make-fee-operation',
                         json=request.model_dump(by_alias=True)
                         )

    def make_top_up_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создание операции пополнения.

        :param request: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/operations/make-top-up-operation',
                         json=request.model_dump(by_alias=True)
                         )

    def make_cashback_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создание операции кэшбэка.

        :param request: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/operations/make-cashback-operation',
                         json=request.model_dump(by_alias=True)
                         )

    def make_transfer_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создание операции перевода.

        :param request: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/operations/make-transfer-operation',
                         json=request.model_dump(by_alias=True)
                         )

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Создание операции покупки.

        :param request: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/operations/make-purchase-operation',
                         json=request.model_dump(by_alias=True)
                         )

    def make_bill_payment_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создание операции оплаты по счету.

        :param request: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/operations/make-bill-payment-operation',
                         json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создание операции снятия наличных денег.

        :param request: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/operations/make-cash-withdrawal-operation',
                         json=request.model_dump(by_alias=True)
                         )

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id=operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(accountId=account_id)
        response = self.get_operations_api(query=query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(accountId=account_id)
        response = self.get_operations_summary_api(query=query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> GetOperationResponseSchema:
        request = MakeOperationRequestSchema(cardId=card_id, accountId=account_id)
        response = self.make_fee_operation_api(request=request)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> GetOperationResponseSchema:
        request = MakeOperationRequestSchema(cardId=card_id, accountId=account_id)
        response = self.make_top_up_operation_api(request=request)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> GetOperationResponseSchema:
        request = MakeOperationRequestSchema(cardId=card_id, accountId=account_id)
        response = self.make_cashback_operation_api(request=request)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> GetOperationResponseSchema:
        request = MakeOperationRequestSchema(cardId=card_id, accountId=account_id)
        response = self.make_transfer_operation_api(request=request)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> GetOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(cardId=card_id, accountId=account_id)
        response = self.make_purchase_operation_api(request=request)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> GetOperationResponseSchema:
        request = MakeOperationRequestSchema(cardId=card_id, accountId=account_id)
        response = self.make_bill_payment_operation_api(request=request)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> GetOperationResponseSchema:
        request = MakeOperationRequestSchema(cardId=card_id, accountId=account_id)
        response = self.make_cash_withdrawal_operation_api(request=request)
        return GetOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
        Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

        :return: Готовый к использованию OperationsGatewayHTTPClient.
        """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
