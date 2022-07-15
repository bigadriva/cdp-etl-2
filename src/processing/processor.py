from typing import Dict, List

from models.processing.processor import ProcessorModel
from processing.entity_parser import EntityParser
from processing.factory import EntityParserFactory


class Processor:
    model: ProcessorModel
    parsers: List[EntityParser]

    def __init__(self, model: ProcessorModel) -> None:
        self.model = model
        self.parsers = [
            EntityParserFactory.create_parser(parser)
            for parser in self.model.number_formatters
        ] + [
            EntityParserFactory.create_parser(parser)
            for parser in self.model.date_formatters
        ] + [
            # Primeiro temos que executar os formatadores, para que quando
            # chegue nos agregadores, os números já estejam formatados e do tipo
            # inteiro ou float, por exemplo.
            EntityParserFactory.create_parser(parser)
            for parser in self.model.field_aggregators
        ]

    def process(self, entity: Dict[str, str]) -> Dict[str, str]:
        for parser in self.parsers:
            entity = parser.parse(entity)
        return entity


    def get_all_processed_models(self) -> List[str]:
        processed_models = set()
        for parser in self.model.date_formatters:
            processed_models.add(parser.model_applied)
        for parser in self.model.field_aggregators:
            processed_models.add(parser.model_applied)
        
        return processed_models
