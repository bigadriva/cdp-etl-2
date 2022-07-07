from models.mapping.base import Mapping


class SalesMapping(Mapping):
    id: str
    date: str
    amount: str
    value: str
    product_id: str
    salesperson_id: str
    client_cnpj: str
