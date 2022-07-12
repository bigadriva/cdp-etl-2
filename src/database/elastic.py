from typing import List

from database.base import DatabaseAdapter

from connector.base import Connector
from models.api.connector import APIConnector

from models.database.product import Product
from models.database.sale import Sale
from models.database.salesperson import Salesperson

from elasticsearch import Elasticsearch

from models.file.file_config import FileConfig

class ElasticAdapter(DatabaseAdapter):
    def __init__(self) -> None:
        self.es = Elasticsearch(
            'http://localhost:9200',
            # basic_auth=('elastic', 'elastic')
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
            # document={
            #     'company_name': connector.company_name,
            #     'type': connector.type,
            #     'host': connector.host,
            #     'port': connector.port,
            #     'directory': connector.directory,
            #     'user': connector.user,
            #     'password': connector.password,
            #     'file_config': {
            #         'type': connector.file_config.type,
            #         'encoding': connector.file_config.encoding,
            #         'separator': connector.file_config.separator
            #     },
            #     # 'database_mapping': {
            #     #     'products_mapping': {
            #     #         'id': connector.database_mapping.products_mapping.id,
            #     #         'type': connector.database_mapping.products_mapping.type,
            #     #         'description': connector.database_mapping.products_mapping.description,
            #     #     },
            #     #     'sales_mapping': {
            #     #         'id': connector.database_mapping.sales_mapping.id,
            #     #         'date': connector.database_mapping.sales_mapping.date,
            #     #         'amount': connector.database_mapping.sales_mapping.amount,
            #     #         'value': connector.database_mapping.sales_mapping.value,
            #     #         'product_id': connector.database_mapping.sales_mapping.product_id,
            #     #         'salesperson_id': connector.database_mapping.sales_mapping.salesperson_id,
            #     #         'client_cnpj': connector.database_mapping.sales_mapping.client_cnpj,
            #     #     },
            #     #     'salespeople_mapping': {
            #     #         'id': connector.database_mapping.salespeople_mapping.id,
            #     #         'manager_id': connector.database_mapping.salespeople_mapping.manager_id,
            #     #     }
            #     # }
            # }
        )

    def read_connector(self, company_name: str) -> APIConnector:
        result = self.es.get(
            index=f'cdp-connectors',
            id=company_name
        )

        response = {}

        if result['found']:
            response = result['_source']
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
                )
            )

        return response
