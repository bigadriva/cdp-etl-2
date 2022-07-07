from abc import ABC, abstractmethod

from models.mapping.database import DatabaseMapping


class Loader(ABC):
    @abstractmethod
    def load(self, company_name: str, database_mapping: DatabaseMapping):
        pass
