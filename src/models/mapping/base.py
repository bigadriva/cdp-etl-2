from pydantic import BaseModel


class Mapping(BaseModel):
    model_filename: str
