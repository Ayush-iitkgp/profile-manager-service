from typing import List
from uuid import UUID

from pydantic import validator

from src.exceptions.customer import HTTPUnprocessableEntityError
from src.models.base_model import BaseSchema
from src.models.customer import CustomerSchema


class InSetPasswordSchema(BaseSchema):
    email: str
    password: str
    confirm_password: str

    @validator("confirm_password")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise HTTPUnprocessableEntityError
        return v


class InCustomerSchema(BaseSchema):
    id: UUID
    currency_code: str
    pnl: List[CustomerSchema]
