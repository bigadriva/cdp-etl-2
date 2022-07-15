from typing import List

from models.processing.entity_parser import EntityParserModel


class FieldAggregatorParserModel(EntityParserModel):
    field_names: List[str]
    target_field_name: str
    method: str
