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
from routers.database import router as database_router

def main():
    load_dotenv()

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost', '*'],
        allow_methods=['*'],
        allow_headers=['*']
    )
    app.include_router(
        connector_router,
        tags=['connector'],
        prefix='/connectors'
    )
    app.include_router(
        database_router,
        tags=['database'],
        prefix='/databases'
    )

    uvicorn.run(app, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
