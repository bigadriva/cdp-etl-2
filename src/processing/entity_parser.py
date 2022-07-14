from typing import Dict
from abc import ABC, abstractmethod


class EntityParser(ABC):
    @abstractmethod
    def parse(entity: Dict[str, str]) -> Dict[str, str]:
        pass
