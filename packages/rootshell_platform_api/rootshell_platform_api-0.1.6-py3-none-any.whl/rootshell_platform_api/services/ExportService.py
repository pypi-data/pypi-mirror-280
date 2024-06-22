from typing import Optional, List, Dict, Callable

class ExportService:
    def __init__(self, client, exporter: Exporter, fetch_method: Callable[..., Union[Dict, str]]):
        self.client = client
        self.exporter = exporter
        self.fetch_method = fetch_method

    def export_data(
        self,
        file_path: str,
        limit: int = 10,
        page: int = 1,
        orderByColumn: Optional[str] = "name",
        orderByDirection: Optional[str] = "asc",
        search: Optional[str] = None,
    ) -> str:
        all_items = []
        current_page = page

        while True:
            items = self.fetch_method(
                limit=limit,
                page=current_page,
                search=search,
                orderByDirection=orderByDirection,
                orderByColumn=orderByColumn,
            )

            if not isinstance(items, dict) or not items.get("data"):
                break

            all_items.extend(items.get("data"))

            if not items.get("links", {}).get("next"):
                break

            current_page += 1

        return self.exporter.export(all_items, file_path)
