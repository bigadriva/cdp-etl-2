import os
from pathlib import Path

from ftplib import FTP, error_perm, error_reply

from typing import List, Optional

from connector.base import ConnectionException, Connector
from database.elastic import ElasticAdapter

from file_handler.file_handler_factory_creator import FileHandlerFactoryCreator

from models.file.file_config import FileConfig
from processing.processor import Processor


class FTPConnector(Connector):
    def __init__(self, company_name: str, type: str, host: str, port: int, directory: str, user: str, password: str, file_config: FileConfig) -> None:
        self.company_name = company_name
        self.type = type
        self.host = host
        self.port = port
        self.file_config = file_config
        self.directory = directory
        self.user = user
        self.password = password
        self.database_adapter = ElasticAdapter()

    def create(self) -> None:
        self.database_adapter.create_connector(self)

    def validate_connection(self) -> bool:
        is_valid = True
        try:
            with FTP(self.host, self.user, self.password) as ftp:
                ftp.voidcmd('NOOP')
        except error_reply:
            is_valid = False
        except error_perm:
            is_valid = False

        return is_valid

    def download_data(self, target_dir: str) -> None:
        if not self.validate_connection():
            raise ConnectionException()

        path = Path(target_dir)
        if not path.exists():
            path.mkdir(parents=True)

        paths = []
        with FTP(self.host, self.user, self.password) as ftp:
            ftp.cwd(self.directory)
            for file_name in ftp.nlst():
                target_file_name = Path(target_dir).joinpath(Path(file_name))
                self.download_file(ftp, target_file_name, file_name)
                paths.append(target_file_name)
        
        self.downloaded_files_paths = paths

        return paths

    def download_file(self, ftp: FTP, target_file_name: str, file_name: str):
        with open(target_file_name, 'wb') as out_file:
            ftp.retrbinary('RETR %s' % file_name, out_file.write)

    def list_filenames(self, remote: Optional[bool] = True):
        if remote:
            filenames = self.list_filenames_remote()
        else:
            filenames = self.list_filenames_local()
        return filenames
    
    def list_filenames_remote(self):
        with FTP(self.host, self.user, self.password) as ftp:
            ftp.cwd(self.directory)
            filenames = ftp.nlst()
        return filenames
    
    def list_filenames_local(self):
        target_dir = f'data/{self.company_name}'
        self.download_data(target_dir)
        filenames = os.listdir(target_dir)
        return filenames

    def extract_columns(self, file_path: Path) -> List[str]:
        factory = FileHandlerFactoryCreator.create_factory(self.file_config)
        analyser = factory.create_analyser()
        return analyser.extract_columns(self.file_config, file_path)

    def validate_mapping(self) -> bool:
        if self.database_mapping is None:
            return False

        factory = FileHandlerFactoryCreator.create_factory(self.file_config)
        validator = factory.create_mapping_validator()
        return validator.validate_mapping(self.database_mapping)

    def transform(self, processor: Processor):
        factory = FileHandlerFactoryCreator.create_factory(self.file_config)
        transformer = factory.create_transformer()
        transformer.transform(self.company_name, self.database_mapping, self.file_config, processor)

    def load(self) -> None:
        factory = FileHandlerFactoryCreator.create_factory(self.file_config)
        loader = factory.create_loader()
        loader.load(self.company_name, self.database_mapping, self.file_config)
