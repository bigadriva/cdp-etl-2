from abc import ABC, abstractmethod

from models.mapping.database import DatabaseMapping


class MappingValidator(ABC):
    @abstractmethod
    def validate_mapping(self, database_mapping: DatabaseMapping) -> bool:
        pass
