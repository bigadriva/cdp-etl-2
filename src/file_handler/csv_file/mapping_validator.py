from models.mapping.database import DatabaseMapping

from file_handler.base.mapping_validator import MappingValidator


class CSVMappingValidator(MappingValidator):
    def validate_mapping(self, database_mapping: DatabaseMapping) -> bool:
        raise NotImplementedError()
