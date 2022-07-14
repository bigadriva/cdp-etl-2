from typing import Dict

from models.processing.processor import ProcessorModel


class Processor:
    model: ProcessorModel

    def process(entity: Dict[str, str]) -> Dict[str, str]:
        raise NotImplementedError()
