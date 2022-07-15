from typing import Dict
from abc import ABC, abstractmethod

from models.mapping.database import DatabaseMapping
from processing.processor import Processor


class Transformer(ABC):
    @abstractmethod
    def transform(self, company_name: str, database_mapping: DatabaseMapping, processor: Processor) -> Dict[str, str]:
        pass
