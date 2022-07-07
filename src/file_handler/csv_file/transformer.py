from typing import Dict

from models.mapping.database import DatabaseMapping

from file_handler.base.transformer import Transformer


class CSVTransformer(Transformer):
    def transform(self, database_mapping: DatabaseMapping) -> Dict[str, str]:
        raise NotImplementedError()
