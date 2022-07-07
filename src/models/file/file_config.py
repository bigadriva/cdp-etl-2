from pydantic import BaseModel


class FileConfig(BaseModel):
    type: str
    encoding: str
    separator: str
