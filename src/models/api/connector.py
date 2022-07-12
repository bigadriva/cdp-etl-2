from typing import Optional

from pydantic import BaseModel

from models.file.file_config import FileConfig
from models.mapping.database import DatabaseMapping


class APIConnector(BaseModel):
    company_name: str
    type: str
    host: str
    port: int
    directory: str
    user: str
    password: str
    file_config: FileConfig
    database_mapping: Optional[DatabaseMapping]
