from typing import Literal, Optional
from uuid import UUID

import bcrypt
from pydantic import validator

from src.models.base_model import BaseSchema


class CustomerSchemaBase(BaseSchema):
    customer_id: UUID
    email: str
    country: str
    language: Optional[
        Literal["en", "de"]
    ]  # to ensure that the country field only takes 2 allowed values en and de

    @validator("language")
    def check_language(cls, v):
        if v not in ("en", "de"):
            raise ValueError('Language must be either "en" or "de"')
        return v


class CustomerSchema(CustomerSchemaBase):
    hashed_password: str  # Intended for larger text content

    def set_hashed_password(self, password: str):
        self.hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        )  # TODO: research the library
        # for the password encryption

    def is_password_correct(self, input_password: str):
        input_password_bytes = input_password.encode("utf-8")
        return bcrypt.checkpw(input_password_bytes, self.hashed_password)

    # TODO: Add validation for the password
    # @validator('hashed_password')
    # def validate_password(cls, value):
    #     if len(value) > 255:  # Example condition, adjust based on actual constraints
    #         raise ValueError("Password is too long")
    #     return value


class InCustomerSchema(CustomerSchemaBase):
    hashed_password: Optional[str] = ""
