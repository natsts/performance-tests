from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class IssueCardRequest(TypedDict):
    """
    Структура данных для создания виртуальной/физической карты
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueCardRequest) -> Response:
        """
        Создание виртуальной карты.

        :param request: Словарь с данными новой карты
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/cards/issue-virtual-card', json=request)

    def issue_physical_card_api(self, request: IssueCardRequest) -> Response:
        """
        Создание физической карты.

        :param request: Словарь с данными новой карты
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/cards/issue-physical-card', json=request)
