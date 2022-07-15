import csv
import datetime
import logging
from typing import Optional
from database.postgres import PostgresAdapter
from models.database.product import Product
from models.database.sale import Sale
from models.database.salesperson import Salesperson
from models.file.file_config import FileConfig
from models.mapping.database import DatabaseMapping

from file_handler.base.loader import Loader
from models.mapping.products import ProductsMapping
from models.mapping.sales import SalesMapping
from models.mapping.salespeople import SalespeopleMapping


class CSVLoader(Loader):
    def __init__(self) -> None:
        self.database_adapter = PostgresAdapter()

    def initialize(self, company_name: str):
        try:
            self.database_adapter.initialize_db(company_name)
        except:
            print('DB already initialized')

    def load(self, company_name: str, database_mapping: DatabaseMapping, file_config: FileConfig, batchsize: Optional[int] = 1e5):
        print('Inicializando banco')
        self.initialize(company_name)
        print('Iniciando carregamento do banco')
        self.load_products(company_name, database_mapping.products_mapping, file_config)
        self.load_sales(company_name, database_mapping.sales_mapping, file_config)
        self.load_salespeople(company_name, database_mapping.salespeople_mapping, file_config)

    def load_products(self, company_name: str, products_mapping: ProductsMapping, file_config: FileConfig, batchsize=1e5):
        with open(
            f'data/{company_name}/{products_mapping.model_filename}',
            'r',
            encoding=file_config.encoding
        ) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=file_config.separator)
            buffer = []
            for product in reader:
                if len(buffer) == batchsize:
                    self.database_adapter.create_products(buffer)
                    buffer.clear()

                try:
                    buffer.append(Product(
                        id=product[products_mapping.id],
                        type=product[products_mapping.type],
                        description=product[products_mapping.description],
                        company_name=company_name
                    ))
                except KeyError:
                    print(product)

            # Checando por produtos restantes (última iteração teve menos que batchsize)
            if len(buffer) > 0:
                self.database_adapter.create_products(buffer)
                buffer.clear()


    def load_sales(self, company_name: str, sales_mapping: SalesMapping, file_config: FileConfig, batchsize=1e5):
        with open(
            f'data/{company_name}/{sales_mapping.model_filename}',
            'r',
            encoding=file_config.encoding
        ) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=file_config.separator)
            buffer = []
            for sale in reader:
                if len(buffer) == batchsize:
                    self.database_adapter.create_sales(buffer)
                    buffer.clear()

                try:
                    buffer.append(Sale(
                        id=sale[sales_mapping.id],
                        date=sale[sales_mapping.date],
                        amount=sale[sales_mapping.amount],
                        value=sale[sales_mapping.value].replace(',', '.'),
                        product_id=sale[sales_mapping.product_id],
                        salesperson_id=sale[sales_mapping.salesperson_id],
                        client_cnpj=sale[sales_mapping.client_cnpj],
                        company_name=company_name
                    ))
                except KeyError:
                    print(sale)

            # Checando por produtos restantes (última iteração teve menos que batchsize)
            if len(buffer) > 0:
                self.database_adapter.create_sales(buffer)
                buffer.clear()

    def load_salespeople(self, company_name: str, salespeople_mapping: SalespeopleMapping, file_config: FileConfig, batchsize=1e5):
        with open(
            f'data/{company_name}/{salespeople_mapping.model_filename}',
            'r',
            encoding=file_config.encoding
        ) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=file_config.separator)
            buffer = []
            for salesperson in reader:
                if len(buffer) == batchsize:
                    self.database_adapter.create_sales(buffer)
                    buffer.clear()

                try:
                    buffer.append(Salesperson(
                        id=salesperson[salespeople_mapping.id],
                        manager_id=salesperson[salespeople_mapping.manager_id],
                        company_name=company_name
                    ))
                except KeyError:
                    print(salesperson)

            # Checando por produtos restantes (última iteração teve menos que batchsize)
            if len(buffer) > 0:
                self.database_adapter.create_salespeople(buffer)
                buffer.clear()
    
