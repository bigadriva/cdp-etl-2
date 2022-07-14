from typing import List

from models.processing.entity_parser import EntityParserModel


class FieldAggregatorParserModel(EntityParserModel):
    field_names: List[str]
    method: str
