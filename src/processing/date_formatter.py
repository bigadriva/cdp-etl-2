import datetime
from typing import Dict

from models.processing.date_formatter_parser import DateFormatterParserModel

from processing.entity_parser import EntityParser


class DateFormatterParser(EntityParser):
    def __init__(self, model: DateFormatterParserModel) -> None:
        self.model: DateFormatterParserModel = model

    def parse(self, entity: Dict[str, str]) -> Dict[str, str]:
        field_name = self.model.field_name
        date_format = self.model.date_format
        if field_name in entity:
            entity[field_name] = datetime.datetime.strptime(
                entity[field_name],
                date_format
            )
        return entity
