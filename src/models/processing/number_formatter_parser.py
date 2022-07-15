from typing import List

from models.processing.entity_parser import EntityParserModel


class NumberFormatterParserModel(EntityParserModel):
    field_names: List[str]
    thousand_separator: str
    decimal_separator: str
