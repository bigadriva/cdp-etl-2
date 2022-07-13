from abc import ABC, abstractmethod
from typing import List

from models.api.connector import ConnectorModel

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
    def create_connector(self, connector: ConnectorModel):
        pass

    @abstractmethod
    def read_connector(self, company_name: str) -> ConnectorModel:
        """Busca o conector da empresa passada.
        
        Parameters
        ----------
        company_name : str
            O nome da empresa cujo conector se busca

        Raises
        ------
        ConnectorNotFoundError
            Se não houver um conector para a empresa passada no banco, então
            será gerada a exceção ConnectorNotFoundError

        Returns
        -------
        ConnectorModel
            O modelo de dados do conector preenchido com as informações
            relevantes
        """
        pass

    @abstractmethod
    def update_connector(self, company_name: str, connector: ConnectorModel) -> None:
        pass

    @abstractmethod
    def delete_connector(self, company_name: str) -> None:
        pass


class ConnectorNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
