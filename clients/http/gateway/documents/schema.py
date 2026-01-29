from pydantic import BaseModel


class DocumentSchema(BaseModel):
    """
    Описание структуры документа
    """
    url: str
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения тарифа по счету.
    """
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения контракта по счету.
    """
    contract: DocumentSchema
