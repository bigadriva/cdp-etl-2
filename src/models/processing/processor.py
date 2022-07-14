from typing import List, Union
from pydantic import BaseModel

from models.processing.date_formatter_parser import DateFormatterParserModel
from models.processing.field_aggregator_parser import FieldAggregatorParserModel


class ProcessorModel(BaseModel):
    field_aggregators: List[FieldAggregatorParserModel]
    date_formatters: List[DateFormatterParserModel]
    company_name: str
