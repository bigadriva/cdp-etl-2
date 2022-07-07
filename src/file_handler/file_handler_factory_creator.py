from file_handler.file_types import FileType

from file_handler.file_handler_factory import FileHandlerFactory
from file_handler.csv_factory import CSVFileHandlerFactory

from models.file.file_config import FileConfig


class FileHandlerFactoryCreator:
    factories = {
        FileType.CSV: CSVFileHandlerFactory()
    }

    @staticmethod
    def create_factory(file_config: FileConfig) -> FileHandlerFactory:
        return FileHandlerFactoryCreator.factories[file_config.type]
