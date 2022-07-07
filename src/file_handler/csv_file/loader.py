from models.mapping.database import DatabaseMapping

from file_handler.base.loader import Loader


class CSVLoader(Loader):
    def load(self, company_name: str, database_mapping: DatabaseMapping):
        raise NotImplementedError()
