from pathlib import Path
from typing import List
from abc import ABC, abstractmethod

from models.file.file_config import FileConfig


class Analyser(ABC):
    @abstractmethod
    def extract_columns(self, file_config: FileConfig, file_path: Path) -> List[str]:
        pass
