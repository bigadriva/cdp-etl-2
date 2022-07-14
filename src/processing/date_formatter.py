from typing import Dict
from processing.entity_parser import EntityParser


class DateFormatterParser(EntityParser):
    def parse(entity: Dict[str, str]) -> Dict[str, str]:
        raise NotImplementedError()
