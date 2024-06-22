from typing import List, Dict, Union, Optional
from .BaseAPIClient import BaseAPIClient
from rootshell_platform_api.config import API_ENDPOINT, BEARER_TOKEN
import pandas as pd
from data_transfer_objects.ProjectDTO import ProjectDTO

class AssetGroupAssetsAPIClient(BaseAPIClient):
    def __init__(self, assetGroupId):
        super().__init__(base_url=f"{API_ENDPOINT}/assets/{assetGroupId}/assets")

    def get_entity(
        self,
        limit: int = 10,
        page: int = 1,
        orderByColumn: Optional[str] = "name",
        orderByDirection: Optional[str] = "asc",
        search: Optional[str] = None,
    ) -> Union[Dict, str]:
        params = {
            "limit": limit,
            "page": page,
            "orderBy[column]": orderByColumn,
            "orderBy[direction]": orderByDirection,
        }
        if search:
            params["search"] = search

        return self.get("", params=params)

    from typing import Dict, Union, List, Optional

    def update_entity(self, entity_id: int, entity: PhaseHostDTO) -> Union[Dict, str]:
        data = entity.to_dict()
        return self.put(f"/sync", data)

    def export_to_csv(
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
            items = self.get_entities(
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

        df = pd.DataFrame(all_items)
        df = df.fillna("")
        df.to_csv(file_path, index=False, encoding="utf-8")

        return f"Exported to {file_path}"
