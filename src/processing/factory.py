from models.processing.entity_parser import EntityParserModel

from processing.entity_parser import EntityParser
from processing.date_formatter import DateFormatterParser
from processing.field_aggregator import FieldAggregatorParser
from processing.number_formatter import NumberFormatterParser


class EntityParserFactory:
    constructors = {
        'field_aggregator': FieldAggregatorParser,
        'date_formatter': DateFormatterParser,
        'number_formatter': NumberFormatterParser
    }

    @staticmethod
    def create_parser(model: EntityParserModel) -> EntityParser:
        constructor = EntityParserFactory.constructors[model.type]
        parser = constructor(model)
        return parser

