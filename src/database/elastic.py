import os
from typing import List

from database.base import DatabaseAdapter

from models.api.connector import APIConnector

from models.database.product import Product
from models.database.sale import Sale
from models.database.salesperson import Salesperson

from elasticsearch import Elasticsearch

from models.file.file_config import FileConfig

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

    def create_connector(self, connector: APIConnector):
        self.es.index(
            index=f'cdp-connectors',
            id=connector.company_name,
            document=connector.dict()
        )

    def read_connector(self, company_name: str) -> APIConnector:
        result = self.es.get(
            index=f'cdp-connectors',
            id=company_name
        )

        response = {}

        if result['found']:
            response = result['_source']

            database_mapping = None
            if 'database_mapping' in response:
                database_mapping = response['database_mapping']

            response = APIConnector(
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

    def update_connector(self, company_name: str, connector: APIConnector) -> None:
        body = {
            'doc': connector.dict()
        }
        self.es.update(index='cdp-connectors', id=company_name, body=body)


    def delete_connector(self, company_name: str) -> None:
        self.es.delete(index='cdp-connectors', id=company_name)
