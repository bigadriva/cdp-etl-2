from typing import Optional
from pydantic import BaseModel


class FileConfig(BaseModel):
    type: str
    encoding: str
    separator: Optional[str] = None
