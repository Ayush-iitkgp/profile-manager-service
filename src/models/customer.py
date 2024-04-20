from src.models.base_model import BaseSchema
from uuid import UUID
from typing import Literal
from pydantic import validator


class CustomerSchemaBase(BaseSchema):
    customer_id: UUID
    email: str
    country: str
    language: Literal['en', 'de']  # to ensure that the country field only takes 2 allowed values en and de

    @validator('language')
    def check_language(cls, v):
        if v not in ('en', 'de'):
            raise ValueError('Language must be either "en" or "de"')
        return v


class InCustomerSchema(CustomerSchemaBase):
    ...