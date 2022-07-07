from typing import Dict
from abc import ABC, abstractmethod

from models.mapping.database import DatabaseMapping


class Transformer(ABC):
    @abstractmethod
    def transform(self, database_mapping: DatabaseMapping) -> Dict[str, str]:
        pass
