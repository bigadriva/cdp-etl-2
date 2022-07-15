import csv
import tempfile
from typing import Dict
from models.file.file_config import FileConfig
from models.mapping.base import Mapping

from models.mapping.database import DatabaseMapping

from file_handler.base.transformer import Transformer
from processing.entity_parser import EntityParser
from processing.processor import Processor


class CSVTransformer(Transformer):
    def transform(self, company_name: str, database_mapping: DatabaseMapping, file_config: FileConfig, processor: Processor) -> Dict[str, str]:
        processed_models = processor.get_all_processed_models()
        mappings = {
            'products': database_mapping.products_mapping,
            'sales': database_mapping.sales_mapping,
            'salespeople': database_mapping.salespeople_mapping
        }
        for model in processed_models:
            mapping: Mapping = mappings[model]
            with tempfile.TemporaryFile('w+') as tmpfile:
                with open(f'data/{company_name}/{mapping.model_filename}', 'r', encoding=file_config.encoding) as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=file_config.separator, quotechar='"')
                    first_row = next(reader)
                    first_processed_row = processor.process(first_row)
                    writer = csv.DictWriter(
                        tmpfile,
                        list(first_processed_row.keys()),
                        delimiter=file_config.separator,
                        quotechar='"'
                    )
                    writer.writeheader()
                    writer.writerow(first_processed_row)
                    for row in reader:
                        processed_row = processor.process(row)
                        writer.writerow(processed_row)
                with open(f'data/{company_name}/{mapping.model_filename}', 'w', encoding=file_config.encoding) as csvfile:
                    tmpfile.seek(0)
                    reader = csv.DictReader(
                        tmpfile,
                        delimiter=file_config.separator,
                        quotechar='"'
                    )
                    writer = csv.DictWriter(
                        csvfile,
                        reader.fieldnames,
                        delimiter=file_config.separator,
                        quotechar='"'
                    )
                    writer.writeheader()
                    for row in reader:
                        writer.writerow(row)
