import datetime
from typing import Dict

from models.processing.number_formatter_parser import NumberFormatterParserModel

from processing.entity_parser import EntityParser


class NumberFormatterParser(EntityParser):
    def __init__(self, model: NumberFormatterParserModel) -> None:
        self.model: NumberFormatterParserModel = model

    def parse(self, entity: Dict[str, str]) -> Dict[str, str]:
        field_names = self.model.field_names
        thousand_separator = self.model.thousand_separator
        decimal_separator = self.model.decimal_separator

        for field_name in field_names:
            if field_name in entity:
                entity[field_name] = float(
                    entity[field_name] \
                        .replace(thousand_separator, '') \
                        .replace(decimal_separator, '.')
                )
        return entity
