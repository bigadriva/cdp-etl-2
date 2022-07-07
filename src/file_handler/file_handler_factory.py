from abc import ABC, abstractmethod

from file_handler.base.analyser import Analyser
from file_handler.base.loader import Loader
from file_handler.base.mapping_validator import MappingValidator
from file_handler.base.transformer import Transformer


class FileHandlerFactory(ABC):
    @abstractmethod
    def create_analyser(self) -> Analyser:
        pass
    
    @abstractmethod
    def create_loader(self) -> Loader:
        pass
    
    @abstractmethod
    def create_mapping_validator(self) -> MappingValidator:
        pass
    
    @abstractmethod
    def create_transformer(self) -> Transformer:
        pass
