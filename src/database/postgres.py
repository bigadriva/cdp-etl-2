import os
from typing import List

from database.base import DatabaseAdapter
from models.api.connector import APIConnector

from models.database.product import Product
from models.database.sale import Sale
from models.database.salesperson import Salesperson

from psycopg2 import connect
from psycopg2.extras import execute_values

class PostgresAdapter(DatabaseAdapter):
    def __init__(self):
        self.user = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.host = os.getenv('POSTGRES_HOST')
        self.port = os.getenv('POSTGRES_PORT')
        self.dbname = os.getenv('POSTGRES_DBNAME')

    def initialize_db(self, company_name: str):
        with connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.dbname
        ) as conn:
            with conn.cursor() as cur:
                # self.create_backup(cur)

                cur.execute(f'CREATE SCHEMA {company_name}')
                cur.execute(f'''
                    CREATE TABLE {company_name}.products (
                        id TEXT,
                        type TEXT,
                        description TEXT,
                        company_name TEXT
                    )
                ''')
                cur.execute(f'''
                    CREATE TABLE {company_name}.sales (
                        id TEXT,
                        date DATE,
                        amount INTEGER,
                        value NUMERIC,
                        product_id TEXT,
                        salesperson_id TEXT,
                        client_cnpj TEXT,
                        company_name TEXT
                    )
                ''')
                cur.execute(f'''
                    CREATE TABLE {company_name}.salespeople (
                        id TEXT,
                        manager_id TEXT,
                        company_name TEXT
                    )
                ''')
            
            conn.commit()

    def create_backup(self, cur, company_name: str):
        cur.execute('SELECT schema_name FROM information_schema.schemata')
        schema = cur.fetchone()
        if schema is not None:
            cur.execute(f'DROP SCHEMA IF EXISTS {company_name}_bkp')
            # cur.execute(f'')

    def create_products(self, products: List[Product]):
        with connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.dbname
        ) as conn:
            with conn.cursor() as cur:

                products_tuple = [
                    (
                        product.id,
                        product.type,
                        product.description,
                        product.company_name
                    ) for product in products
                ]
                statement = f'''
                    INSERT INTO {products[0].company_name}.products (
                        id, type, description, company_name
                    ) VALUES %s'''
                execute_values(cur, statement, products_tuple)

    def create_sales(self, sales: List[Sale]):
        with connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.dbname
        ) as conn:
            with conn.cursor() as cur:

                sales_tuple = [
                    (
                        sale.id,
                        sale.date,
                        sale.amount,
                        sale.value,
                        sale.product_id,
                        sale.salesperson_id,
                        sale.client_cnpj,
                        sale.company_name
                    ) for sale in sales
                ]
                statement = f'''
                    INSERT INTO {sales[0].company_name}.sales (
                        id, date, amount, value, product_id, salesperson_id, client_cnpj, company_name
                    ) VALUES %s'''
                execute_values(cur, statement, sales_tuple)

    def create_salespeople(self, salespeople: List[Salesperson]):
        with connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.dbname
        ) as conn:
            with conn.cursor() as cur:

                salespeople_tuple = [
                    (
                        salesperson.id,
                        salesperson.manager_id,
                        salesperson.company_name
                    ) for salesperson in salespeople
                ]
                statement = f'''
                    INSERT INTO {salespeople[0].company_name}.salespeople (
                        id, type, description, company_name
                    ) VALUES %s'''
                execute_values(cur, statement, salespeople_tuple)

    def create_connector(self, connector: APIConnector):
        raise NotImplementedError()
    def read_connector(self, company_name: str) -> APIConnector:
        raise NotImplementedError()
    def update_connector(self, company_name: str, connector: APIConnector) -> None:
        raise NotImplementedError()
    def delete_connector(self, company_name: str) -> None:
        raise NotImplementedError()