import pydantic


def convert_field_to_camel_case(string: str) -> str:
    return "".join(word if index == 0 else word.capitalize() for index, word in enumerate(string.split("_")))


class BaseModel(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True
        alias_generator = convert_field_to_camel_case


class BaseSchema(BaseModel):
    class Config(BaseModel.Config):
        orm_mode = True