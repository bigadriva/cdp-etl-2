from pathlib import Path
from typing import List

from abc import ABC, abstractmethod
from models.file.file_config import FileConfig

from models.mapping.database import DatabaseMapping


class Connector(ABC):
    company_name: str
    host: str
    port: int
    file_config: FileConfig
    database_mapping: DatabaseMapping
    downloaded_files_paths: List[Path]

    @abstractmethod
    def validate_connection(self) -> bool:
        pass

    @abstractmethod
    def download_data(self, target_dir: str) -> List[Path]:
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
