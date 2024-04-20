from typing import List
from uuid import UUID

from src.models.base_model import BaseSchema
from src.models.customer import CustomerSchema


class OutSetPasswordSchema(BaseSchema):
    message: str


class OutDataSetPasswordSchema(BaseSchema):
    data: OutSetPasswordSchema


class OutCustomerSchema(BaseSchema):
    id: UUID
    currency_code: str
    pnl: List[CustomerSchema]


class OutDataPnlSchema(BaseSchema):
    data: OutCustomerSchema
