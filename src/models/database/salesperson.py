from typing import Optional
from pydantic import BaseModel


class Salesperson(BaseModel):
    id: str
    manager_id: Optional[str]
    company_name: str
