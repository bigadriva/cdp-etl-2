from pathlib import Path
from typing import List, Optional

from abc import ABC, abstractmethod
from models.file.file_config import FileConfig

from models.mapping.database import DatabaseMapping

class Connector:
    pass

class Connector(ABC):
    company_name: str
    type: str
    host: str
    port: int
    directory: str
    user: str
    password: str
    file_config: FileConfig
    database_mapping: DatabaseMapping
    downloaded_files_paths: List[Path]

    @abstractmethod
    def create(self) -> None:
        pass

    @abstractmethod
    def validate_connection(self) -> bool:
        pass

    @abstractmethod
    def download_data(self, target_dir: str) -> List[Path]:
        pass

    @abstractmethod
    def list_filenames(self, remote: Optional[bool] = True):
        pass

    @abstractmethod
    def extract_columns(self, file_path: str) -> List[str]:
        pass

    @abstractmethod
    def validate_mapping(self) -> bool:
        pass

    @abstractmethod
    def load_data(self) -> None:
        pass


class ConnectionException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__('Não foi possível realizar a conexão', *args)
