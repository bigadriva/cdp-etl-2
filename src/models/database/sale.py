from datetime import date

from pydantic import BaseModel


class Sale(BaseModel):
    id: str
    date: date
    amount: int
    value: float
    product_id: str
    salesperson_id: str
    client_cnpj: str
    company_name: str
