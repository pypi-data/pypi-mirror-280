import pandas as pd
from typing import List, Dict

class CSVExporter(Exporter):
    def export(self, data: List[Dict], file_path: str) -> str:
        df = pd.DataFrame(data)
        df = df.fillna("")
        df.to_csv(file_path, index=False, encoding="utf-8")
        return f"Data exported to {file_path}"
