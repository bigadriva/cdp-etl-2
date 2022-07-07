from abc import ABC, abstractmethod

from models.mapping.database import DatabaseMapping
from models.mapping.products import ProductsMapping
from models.mapping.sales import SalesMapping
from models.mapping.salespeople import SalespeopleMapping


class Loader(ABC):
    @abstractmethod
    def load(self, company_name: str, database_mapping: DatabaseMapping):
        pass

    @abstractmethod
    def load_sales(self, sales_mapping: SalesMapping):
        pass

    @abstractmethod
    def load_products(self, products_mapping: ProductsMapping):
        pass

    @abstractmethod
    def load_salespeople(self, salespeople_mapping: SalespeopleMapping):
        pass
