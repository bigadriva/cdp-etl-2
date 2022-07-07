from typing import Optional
from pydantic import BaseModel


class Sale(BaseModel):
    id: str
    manager_id: Optional[str]
