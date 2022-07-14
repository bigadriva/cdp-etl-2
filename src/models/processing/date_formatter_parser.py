from typing import List

from models.processing.entity_parser import EntityParserModel


class DateFormatterParserModel(EntityParserModel):
    type: str
    model_applied: str
    field_name: str
    date_format: str
