from typing import Dict
from abc import ABC, abstractmethod

from models.processing.entity_parser import EntityParserModel


class EntityParser(ABC):
    model: EntityParserModel

    @abstractmethod
    def parse(self, entity: Dict[str, str]) -> Dict[str, str]:
        pass
