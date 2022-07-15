import os
from typing import List

from database.base import ConnectorNotFoundError, DatabaseAdapter, ProcessorNotFoundError

from models.connector.connector import ConnectorModel

from models.database.product import Product
from models.database.sale import Sale
from models.database.salesperson import Salesperson

from elasticsearch import Elasticsearch, NotFoundError

from models.file.file_config import FileConfig
from models.processing.processor import ProcessorModel

class ElasticAdapter(DatabaseAdapter):
    def __init__(self) -> None:
        self.es = Elasticsearch(
            os.getenv('ELASTIC_HOST'),
            basic_auth=(os.getenv('ELASTIC_USER'), os.getenv('ELASTIC_PASSWORD'))
        )

    def initialize_db(self, company_name: str):
        raise NotImplementedError()

    def create_products(self, product: List[Product]):
        raise NotImplementedError()

    def create_sales(self, sale: List[Sale]):
        raise NotImplementedError()

    def create_salespeople(self, salespeople: List[Salesperson]):
        raise NotImplementedError()

    def create_connector(self, connector: ConnectorModel):
        self.es.index(
            index=f'cdp_connectors',
            id=connector.company_name,
            document=connector.dict()
        )

    def read_connector(self, company_name: str) -> ConnectorModel:
        try:
            result = self.es.get(
                index=f'cdp_connectors',
                id=company_name
            )
        except NotFoundError:
            raise ConnectorNotFoundError()

        response = {}

        if result['found']:
            response = result['_source']

            database_mapping = None
            if 'database_mapping' in response:
                database_mapping = response['database_mapping']

            response = ConnectorModel(
                company_name=company_name,
                type=response['type'],
                host=response['host'],
                port=response['port'],
                directory=response['directory'],
                user=response['user'],
                password=response['password'],
                file_config=FileConfig(
                    type=response['file_config']['type'],
                    encoding=response['file_config']['encoding'],
                    separator=response['file_config']['separator']
                ),
                database_mapping=database_mapping
            )

        return response

    def update_connector(self, company_name: str, connector: ConnectorModel) -> None:
        body = {
            'doc': connector.dict()
        }
        self.es.update(index='cdp_connectors', id=company_name, body=body)


    def delete_connector(self, company_name: str) -> None:
        self.es.delete(index='cdp_connectors', id=company_name)

    def create_processor(self, processor: ProcessorModel) -> None:
        self.es.index(
            index='cdp_processors',
            id=processor.company_name,
            document=processor.dict()
        )

    def read_processor(self, company_name: str) -> ProcessorModel:
        try:
            result = self.es.get(
                index='cdp_processors',
                id=company_name
            )
        except NotFoundError:
            raise ProcessorNotFoundError()

        response = {}

        if result['found']:
            response = result['_source']
            response = ProcessorModel(**response)

        return response
