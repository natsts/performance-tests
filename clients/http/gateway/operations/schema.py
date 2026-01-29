from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict


class Type(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class Status(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Описание структуры операции
    """
    id: str
    type: Type
    status: Status
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Описание структуры чека операции
    """
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Описание структуры статистики по операциям для определенного счета.
    """
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class MakeOperationRequestSchema(BaseModel):
    """
    Структура данных для выполнения операции
    """
    model_config = ConfigDict(populate_by_name=True)

    status: Status
    amount: int
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения операций пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции покупки.
    """
    category: str


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа выполнения операции
    """
    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа получения чека
    """
    receipt: OperationReceiptSchema


class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения операций
    """
    operations: OperationSchema


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа олучения статистики по операциям для определенного счета.
    """
    summary: OperationsSummarySchema
