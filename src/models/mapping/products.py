from models.mapping.base import Mapping


class ProductsMapping(Mapping):
    id: str
    type: str
    description: str
