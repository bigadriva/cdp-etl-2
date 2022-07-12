from dotenv import load_dotenv

from pathlib import Path
from connector.ftp import FTPConnector
from file_handler.csv_factory import CSVFileHandlerFactory
from models.file.file_config import FileConfig
from models.mapping.database import DatabaseMapping
from models.mapping.products import ProductsMapping
from models.mapping.sales import SalesMapping
from models.mapping.salespeople import SalespeopleMapping

import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.connector import router as connector_router

def main():
    load_dotenv()

    # ftp_connector = FTPConnector(
    #     'Catarinense Pharma',
    #     '201.55.119.243',
    #     21,
    #     FileConfig(type='csv', encoding='utf-8-sig', separator=';'),
    #     '/',
    #     'Driva',
    #     '@123driva#'
    # )

    # paths = ftp_connector.download_data('data/catarinense')
    # paths = [
    #     Path('./data/catarinense/DADOS_DRIVA.TXT'),
    #     Path('./data/catarinense/PROD_DRIVA.TXT'),
    #     Path('./data/catarinense/VEND_DRIVA.TXT'),
    # ]
    # for path in paths:
    #     columns = ftp_connector.extract_columns(path)
    #     print(columns)

    # sales_mapping = SalesMapping(
    #     local_data_path='data/catarinense/DADOS_DRIVA.TXT',
    #     id=None,
    #     date='DATA',
    #     amount=['QTD_FAT', 'QTD_LOG_FAT', 'QTD_CAR']
    # )

    # products_mapping = ProductsMapping(
    #     local_data_path='data/catarinense/PROD_DRIVA.TXT',
    #     id='ITEM',
    #     type='FAMILIA',
    #     description='DESC_ITEM'
    # )

    # sales_mapping = SalesMapping(
    #     local_data_path='data/catarinense/DADOS_DRIVA.TXT',
    #     id='NOTA FISCAL',
    #     date='DATA',
    #     amount='QTD_FAT',
    #     value='VAL_FAT',
    #     product_id='COD',
    #     salesperson_id='VEND_NF',
    #     client_cnpj='CNPJ'
    # )

    # salespeople_mapping = SalespeopleMapping(
    #     local_data_path='data/catarinense/VEND_DRIVA.TXT',
    #     id='VEND_CLI',
    #     manager_id='GERENTE'
    # )

    # database_mapping = DatabaseMapping(
    #     local_data_path='data/catarinense',
    #     products_mapping=products_mapping,
    #     sales_mapping=sales_mapping,
    #     salespeople_mapping=salespeople_mapping
    # )
    # ftp_connector.database_mapping = database_mapping
    # ftp_connector.load_data()

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost'],
        allow_methods=['*'],
        allow_headers=['*']
    )
    app.include_router(connector_router, tags=['connector'], prefix='/connectors')

    uvicorn.run(app, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
