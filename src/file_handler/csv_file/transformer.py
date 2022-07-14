from typing import Dict

from models.mapping.database import DatabaseMapping

from file_handler.base.transformer import Transformer
from processing.processor import Processor


class CSVTransformer(Transformer):
    def transform(self, database_mapping: DatabaseMapping, processor: Processor) -> Dict[str, str]:
        raise NotImplementedError()
