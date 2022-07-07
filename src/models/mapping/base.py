import pydantic


from pydantic import BaseModel


class Mapping(BaseModel):
    local_data_path: str
