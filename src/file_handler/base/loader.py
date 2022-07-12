from abc import ABC, abstractmethod
from typing import Optional
from database.base import DatabaseAdapter
from models.file.file_config import FileConfig

from models.mapping.database import DatabaseMapping
from models.mapping.products import ProductsMapping
from models.mapping.sales import SalesMapping
from models.mapping.salespeople import SalespeopleMapping


class Loader(ABC):
    database_adapter: DatabaseAdapter

    @abstractmethod
    def initialize(self, company_name: str):
        pass

    @abstractmethod
    def load(self, company_name: str, database_mapping: DatabaseMapping, file_config: FileConfig, batchsize: Optional[int] = 1e5):
        pass

    @abstractmethod
    def load_sales(self, sales_mapping: SalesMapping, file_config: FileConfig, batchsize: Optional[int] = 1e5):
        pass

    @abstractmethod
    def load_products(self, products_mapping: ProductsMapping, file_config: FileConfig, batchsize: Optional[int] = 1e5):
        pass

    @abstractmethod
    def load_salespeople(self, salespeople_mapping: SalespeopleMapping, file_config: FileConfig, batchsize: Optional[int] = 1e5):
        pass
