from models.processing.entity_parser import EntityParserModel

from processing.entity_parser import EntityParser
from processing.date_formatter import DateFormatterParser
from processing.field_aggregator import FieldAggregatorParser


class EntityParserFactory:
    constructors = {
        'field_aggregator': FieldAggregatorParser,
        'date_formatter': DateFormatterParser
    }

    @staticmethod
    def create_parser(model: EntityParserModel) -> EntityParser:
        constructor = EntityParserFactory.constructors[model.type]
        parser = constructor(model)
        return parser

