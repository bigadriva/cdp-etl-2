from typing import Dict
from processing.entity_parser import EntityParser


class FieldAggregatorParser(EntityParser):
    def parse(entity: Dict[str, str]) -> Dict[str, str]:
        raise NotImplementedError()
