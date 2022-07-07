from file_handler.base.analyser import Analyser
from file_handler.base.loader import Loader
from file_handler.base.mapping_validator import MappingValidator
from file_handler.base.transformer import Transformer

from file_handler.csv_file.analyser import CSVAnalyser
from file_handler.csv_file.loader import CSVLoader
from file_handler.csv_file.mapping_validator import CSVMappingValidator
from file_handler.csv_file.transformer import CSVTransformer

from file_handler.file_handler_factory import FileHandlerFactory


class CSVFileHandlerFactory(FileHandlerFactory):
    def create_analyser(self) -> Analyser:
        return CSVAnalyser()


    def create_loader(self) -> Loader:
        return CSVLoader()

    
    def create_mapping_validator(self) -> MappingValidator:
        return CSVMappingValidator()


    def create_transformer(self) -> Transformer:
        return CSVTransformer()
