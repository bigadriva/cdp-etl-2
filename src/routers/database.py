from fastapi import APIRouter, HTTPException
from connector.factory import ConnectorFactory
from database.base import ConnectorNotFoundError

from database.elastic import ElasticAdapter
from processing.processor import Processor

router = APIRouter()


@router.put('/{company_name}', status_code=201)
def update_company_database(company_name: str):
    try:
        local_target_dir = f'data/{company_name}'
        adapter = ElasticAdapter()
        connector_model = adapter.read_connector(company_name)
        connector = ConnectorFactory.create_connector(connector_model)
        # connector.download_data(local_target_dir)
        # processor_model = adapter.read_processor(company_name)
        # processor = Processor(processor_model)
        # print('Iniciando transform')
        # connector.transform(processor)
        print('Iniciando load')
        connector.load()
        print('Terminou')
    except ConnectorNotFoundError:
        raise HTTPException(
            404,
            detail='Conector não encontrado para essa empresa'
        )
