from fastapi import APIRouter, HTTPException
from connector.factory import ConnectorFactory
from database.base import ConnectorNotFoundError

from database.elastic import ElasticAdapter

router = APIRouter()


@router.put('/{company_name}', status_code=202)
def update_company_database(company_name: str):
    try:
        local_target_dir = f'data/{company_name}'
        adapter = ElasticAdapter()
        connector_model = adapter.read_connector(company_name)
        connector = ConnectorFactory.create_connector(connector_model)
        connector.download_data(local_target_dir)
        connector.load_data()
    except ConnectorNotFoundError:
        raise HTTPException(
            404,
            detail='Conector não encontrado para essa empresa'
        )
