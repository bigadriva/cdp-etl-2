from fastapi import APIRouter, HTTPException
from database.base import ProcessorNotFoundError
from database.elastic import ElasticAdapter

from models.processing.processor import ProcessorModel


router = APIRouter()

@router.post('', status_code=201)
def create_processor(processor: ProcessorModel):
    """Cria um processador.
    
    Parameters
    ----------
    processor : ProcessorModel
        O modelo do processador com os dados relevantes

    Returns
    -------
    201:
        Processador criado com sucesso
    \n
    422:
        Unprocessable entity
    """
    adapter = ElasticAdapter()
    adapter.create_processor(processor)


@router.get('/{company_name}')
def get_processor(company_name: str) -> ProcessorModel:
    """Busca um processador para a empresa passada.
    
    Parameters
    ----------
    company_name : str
        O nome da empresa que se quer buscar o conector

    Raises
    ------
    404:
        Processador não encontrado para essa empresa

    Returns
    -------
    200[ProcessorModel]:
        O processador para a respectiva empresa
    \n
    404:
        Processador não encontrado para essa empresa
    """
    adapter = ElasticAdapter()
    try:
        processor = adapter.read_processor(company_name)
    except ProcessorNotFoundError:
        raise HTTPException(
            404,
            detail='Processador não encontrado para essa empresa'
        )
    
    return processor
