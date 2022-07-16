import os
from typing import List

from database.base import DatabaseAdapter
from models.connector.connector import ConnectorModel

from models.database.product import Product
from models.database.sale import Sale
from models.database.salesperson import Salesperson

from psycopg2 import connect
from psycopg2.extras import execute_values

from models.processing.processor import ProcessorModel

class PostgresAdapter(DatabaseAdapter):
    def __init__(self):
        self.user = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.host = os.getenv('POSTGRES_HOST')
        self.port = os.getenv('POSTGRES_PORT')
        self.dbname = os.getenv('POSTGRES_DBNAME')

    def initialize_db(self, company_name: str):
        company_name = company_name.replace(' ', '_').lower()
        with connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.dbname
        ) as conn:
            with conn.cursor() as cur:
                # cur.execute(f'DROP SCHEMA IF EXISTS "{company_name}" CASCADE')
                # cur.execute(f'CREATE SCHEMA "{company_name}"')
                cur.execute('''
                    SELECT schema_name
                    FROM information_schema.schemata
                    WHERE schema_name = 'raw'
                ''')

                if cur.fetchone() is None:
                    # Se não houver um resultado, então o schema não está criado
                    cur.execute('CREATE SCHEMA IF NOT EXISTS raw')
                    cur.execute(f'''
                        CREATE TABLE raw.products (
                            id TEXT,
                            type TEXT,
                            description TEXT,
                            company_name TEXT
                        )
                    ''')
                    cur.execute(f'''
                        CREATE TABLE raw.sales (
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
                        CREATE TABLE raw.salespeople (
                            id TEXT,
                            manager_id TEXT,
                            company_name TEXT
                        )
                    ''')
                else:
                    # Caso contrário, o schema já existe e precisamos deletar a
                    # base antiga
                    cur.execute(
                        'DELETE FROM raw.products WHERE company_name = %s',
                        (company_name,)
                    )
                    cur.execute(
                        'DELETE FROM raw.sales WHERE company_name = %s',
                        (company_name,)
                    )
                    cur.execute(
                        'DELETE FROM raw.salespeople WHERE company_name = %s',
                        (company_name,)
                    )
            
            conn.commit()

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
                statement = '''
                    INSERT INTO raw.products (
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
                statement = '''
                    INSERT INTO raw.sales (
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
                    INSERT INTO raw.salespeople (
                        id, manager_id, company_name
                    ) VALUES %s'''
                execute_values(cur, statement, salespeople_tuple)

    def create_connector(self, connector: ConnectorModel):
        raise NotImplementedError()
    def read_connector(self, company_name: str) -> ConnectorModel:
        raise NotImplementedError()
    def update_connector(self, company_name: str, connector: ConnectorModel) -> None:
        raise NotImplementedError()
    def delete_connector(self, company_name: str) -> None:
        raise NotImplementedError()
    def create_processor(self, processor: ProcessorModel) -> None:
        raise NotImplementedError()
    def read_processor(self, company_name: str) -> ProcessorModel:
        raise NotImplementedError()
