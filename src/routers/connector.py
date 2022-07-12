from fastapi import APIRouter

from connector.factory import ConnectorFactory

from models.api.connector import APIConnector

from database.elastic import ElasticAdapter

router = APIRouter()

@router.get('/{company_name}')
def get_connector(company_name: str) -> APIConnector:
    elastic_adapter = ElasticAdapter()
    return elastic_adapter.read_connector(company_name)


@router.post('/{company_name}')
def create_connector(company_name: str, connector: APIConnector):
    elastic_adapter = ElasticAdapter()
    elastic_adapter.create_connector(connector)

