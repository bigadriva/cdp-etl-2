from typing import Dict, List, Optional
from fastapi import APIRouter, HTTPException
from connector.factory import ConnectorFactory
from database.base import ConnectorNotFoundError

from models.connector.connector import ConnectorModel

from database.elastic import ElasticAdapter
from models.mapping.database import DatabaseMapping

router = APIRouter()


@router.post('', status_code=201)
def create_connector(connector: ConnectorModel):
    elastic_adapter = ElasticAdapter()
    elastic_adapter.create_connector(connector)

@router.get('/{company_name}')
def get_connector(company_name: str) -> ConnectorModel:
    try:
        elastic_adapter = ElasticAdapter()
        response = elastic_adapter.read_connector(company_name)
    except ConnectorNotFoundError:
        raise HTTPException(
            status_code=404,
            detail='Conector não encontrado para essa empresa'
        )

    return response


@router.put('/{company_name}', status_code=201)
def update_connector(company_name: str, connector: ConnectorModel):
    elastic_adapter = ElasticAdapter()
    elastic_adapter.update_connector(company_name, connector)

@router.delete('/{company_name}', status_code=200)
def delete_connector(company_name: str):
    elastic_adapter = ElasticAdapter()
    elastic_adapter.delete_connector(company_name)


@router.get('/{company_name}/filenames')
def get_filenames(company_name: str, remote: Optional[bool] = True) -> Dict[str, List[str]]:
    response = {
        'status': 'ok',
        'message': 'Nomes de arquivos encontrados com sucesso',
        'filenames': []
    }
    try:
        adapter = ElasticAdapter()
        connector_model = adapter.read_connector(company_name)
        connector = ConnectorFactory.create_connector(connector_model)
        filenames = connector.list_filenames()
        response['filenames'].extend(filenames)
    except ConnectorNotFoundError:
        response['status'] = 'failed'
        response['message'] = 'Conector não encontrado para essa empresa'

    return response


@router.get('/{company_name}/database_mapping')
def get_database_mapping(company_name: str) -> DatabaseMapping:
    """Busca o mapeamendo do banco de dados para a empresa passada.
    
    Parameters
    ----------
    company_name : str
        O nome da empresa cujo mapeamento foi pedido

    Raises
    ------
    ConectorNotFoundError
        Conector não encontrado para essa empresa

    Returns
    -------
    200:
        Mapeamento do banco de dados
    \n
    404:
        Conector não encontrado para essa empresa
    """
    response = None
    try:
        adapter = ElasticAdapter()
        connector_model = adapter.read_connector(company_name)
        response = connector_model.database_mapping
    except ConnectorNotFoundError:
        raise HTTPException(404, detail='Conector não encontrado para essa empresa')

    return response


@router.post('/{company_name}/database_mapping', status_code=201)
def create_database_mapping(company_name: str, database_mapping: DatabaseMapping):
    """Cria um mapeamento de banco de dados para o conector da empresa.
    
    Parameters
    ----------
    company_name : str
        O nome da empresa que se deseja realizar o mapeamento
    \n
    database_mapping : DatabaseMapping
        O mapeamento do banco de dados
    
    Raises
    ------
    ConnectionNotFoundError:
        Conector não encontrado para essa empresa

    Returns
    -------
    201:
        Mapeamento Criado
    \n
    404:
        Conector não encontrado para essa empresa
    \n
    422:
        Estrutura do mapeamento está inválida
    """
    try:
        adapter = ElasticAdapter()
        connector_model = adapter.read_connector(company_name)
        connector_model.database_mapping = database_mapping
        adapter.update_connector(connector_model.company_name, connector_model)
    except ConnectorNotFoundError:
        raise HTTPException(
            404,
            detail='Conector não encontrado para essa empresa'
        )
