from typing import List
from fastapi import APIRouter

from connector.factory import ConnectorFactory

from models.api.connector import APIConnector

from database.elastic import ElasticAdapter

router = APIRouter()


@router.post('')
def create_connector(connector: APIConnector):
    elastic_adapter = ElasticAdapter()
    elastic_adapter.create_connector(connector)

@router.get('/{company_name}')
def get_connector(company_name: str) -> APIConnector:
    elastic_adapter = ElasticAdapter()
    return elastic_adapter.read_connector(company_name)

@router.put('{company_name}')
def update_connector(company_name: str, connector: APIConnector):
    elastic_adapter = ElasticAdapter()
    elastic_adapter.update_connector(company_name, connector)

@router.delete('/{company_name}')
def delete_connector(company_name: str):
    elastic_adapter = ElasticAdapter()
    elastic_adapter.delete_connector(company_name)
