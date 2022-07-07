import csv
from pathlib import Path

from typing import List

from file_handler.base.analyser import Analyser
from models.file.file_config import FileConfig


class CSVAnalyser(Analyser):
    def extract_columns(self, file_config: FileConfig, file_path: Path) -> List[str]:
        columns = None

        with open(file_path, 'r', encoding=file_config.encoding) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=file_config.separator)
            columns = list(next(reader).keys())
        
        return columns
