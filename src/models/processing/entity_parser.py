from pydantic import BaseModel


class EntityParserModel(BaseModel):
    type: str
    model_applied: str
