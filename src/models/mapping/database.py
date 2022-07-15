from models.mapping.base import Mapping
from models.mapping.products import ProductsMapping
from models.mapping.sales import SalesMapping
from models.mapping.salespeople import SalespeopleMapping


class DatabaseMapping(Mapping):
    products_mapping: ProductsMapping
    sales_mapping: SalesMapping
    salespeople_mapping: SalespeopleMapping
