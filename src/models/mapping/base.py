from typing import Optional

from pydantic import BaseModel


class Mapping(BaseModel):
    local_data_path: Optional[str]
