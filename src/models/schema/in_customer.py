from pydantic import validator

from src.models.base_model import BaseSchema
from src.exceptions.core import HTTPUnprocessableEntityError

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
