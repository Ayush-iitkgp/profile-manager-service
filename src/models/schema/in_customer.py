from pydantic import Enum, validator

from src.exceptions.core import HTTPUnprocessableEntityError
from src.models.base_model import BaseSchema


class InSetPasswordSchema(BaseSchema):
    email: str
    password: str
    confirm_password: str

    @validator("confirm_password")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise HTTPUnprocessableEntityError
        return v


class InLoginSchema(BaseSchema):
    email: str
    password: str


class AllowedLanguages(str, Enum):
    en = "en"
    de = "de"


class InChangePasswordSchema(BaseSchema):
    customer_id: str
    new_language: AllowedLanguages  # This will throw 4xx error if the input language is not en or de
    # TODO: Test what error you will receive when the input language is anything other than en or de
