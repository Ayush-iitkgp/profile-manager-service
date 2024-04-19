from src.models.base_model import BaseSchema
from uuid import UUID


class CustomerSchemaBase(BaseSchema):
    currency_code: str


class CustomerSchema(CustomerSchemaBase):
    id: UUID
    currency_code: str


class InCustomerSchema(CustomerSchemaBase):
    ...