from abc import ABC, abstractmethod
from typing import List

from models.api.connector import APIConnector

from models.database.product import Product
from models.database.sale import Sale
from models.database.salesperson import Salesperson


class DatabaseAdapter(ABC):
    user: str
    password: str
    host: str
    port: int
    dbname: str

    @abstractmethod
    def initialize_db(self, company_name: str):
        pass

    @abstractmethod
    def create_products(self, product: List[Product]):
        pass

    @abstractmethod
    def create_sales(self, sale: List[Sale]):
        pass

    @abstractmethod
    def create_salespeople(self, salespeople: List[Salesperson]):
        pass

    @abstractmethod
    def create_connector(self, connector: APIConnector):
        pass

    @abstractmethod
    def read_connector(self, company_name: str) -> APIConnector:
        pass

    @abstractmethod
    def update_connector(self, company_name: str, connector: APIConnector) -> None:
        pass

    @abstractmethod
    def delete_connector(self, company_name: str) -> None:
        pass
