from abc import ABC, abstractmethod
from typing import List, Dict

class Exporter(ABC):
    @abstractmethod
    def export(self, data: List[Dict], file_path: str) -> str:
        pass
