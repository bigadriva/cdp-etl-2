from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: str
    type: str
    description: Optional[str]
