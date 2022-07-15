from abc import ABC, abstractmethod
from typing import List

from models.connector.connector import ConnectorModel

from models.database.product import Product
from models.database.sale import Sale
from models.database.salesperson import Salesperson
from models.processing.processor import ProcessorModel


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

    @abstractmethod
    def create_processor(self, processor: ProcessorModel) -> None:
        """Cria um conector
        
        Parameters
        ----------
        processor : ProcessorModel
            O modelo do processador com os dados relevantes
        """
        pass

    @abstractmethod
    def read_processor(self, company_name: str) -> ProcessorModel:
        """Busca o processador para a empresa passada.
        
        Parameters
        ----------
        company_name : str
            O nome da empresa cujo processador se deseja buscar.

        Raises
        ------
        ProcessorNotFoundError

        Returns
        -------
        ProcessorModel
            O modelo de processador com os dados relevantes.
        """


class ConnectorNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ProcessorNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
