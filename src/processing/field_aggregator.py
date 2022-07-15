from typing import Dict

from models.processing.field_aggregator_parser import FieldAggregatorParserModel

from processing.entity_parser import EntityParser


class FieldAggregatorParser(EntityParser):
    def __init__(self, model: FieldAggregatorParserModel):
        self.model: FieldAggregatorParserModel = model

    def parse(self, entity: Dict[str, str]) -> Dict[str, str]:
        new_entity = entity.copy()
        for field_name in self.model.field_names:
            if field_name in new_entity:
                new_entity.pop(field_name)
        if self.model.method == 'sum':
            new_entity[self.model.target_field_name] = sum(
                entity[field_name]
                for field_name in self.model.field_names
                if field_name in new_entity
            )

        return new_entity
