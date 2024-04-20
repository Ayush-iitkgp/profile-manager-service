from typing import List
from uuid import UUID

from src.models.base_model import BaseSchema
from src.models.customer import CustomerSchema


class OutSetPasswordSchema(BaseSchema):
    message: str


class OutLoginSchema(BaseSchema):
    customer_id: str
    language: str


class OutDataSetPasswordSchema(BaseSchema):
    data: OutSetPasswordSchema


class OutDataLoginSchema(BaseSchema):
    data: OutLoginSchema


class OutCustomerSchema(BaseSchema):
    id: UUID
    currency_code: str
    pnl: List[CustomerSchema]


class OutDataPnlSchema(BaseSchema):
    data: OutCustomerSchema


class OutChangePasswordSchema(BaseSchema):
    message: str


class OutDataChangePasswordSchema(BaseSchema):
    data: OutChangePasswordSchema
