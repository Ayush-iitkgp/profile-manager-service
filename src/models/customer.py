from typing import Literal
from uuid import UUID

from pydantic import validator

from src.models.base_model import BaseSchema


class CustomerSchemaBase(BaseSchema):
    customer_id: UUID
    email: str
    country: str
    language: Literal[
        "en", "de"
    ]  # to ensure that the country field only takes 2 allowed values en and de

    @validator("language")
    def check_language(cls, v):
        if v not in ("en", "de"):
            raise ValueError('Language must be either "en" or "de"')
        return v


class CustomerSchema(CustomerSchemaBase):
    hashed_password: str  # Intended for larger text content

    # OPTIONAL: Add validation for the password
    # @validator('hashed_password')
    # def validate_password(cls, value):
    #     if len(value) > 255:  # Example condition, adjust based on actual constraints
    #         raise ValueError("Password is too long")
    #     return value


class InCustomerSchema(CustomerSchemaBase):
    hashed_password: str = ""
