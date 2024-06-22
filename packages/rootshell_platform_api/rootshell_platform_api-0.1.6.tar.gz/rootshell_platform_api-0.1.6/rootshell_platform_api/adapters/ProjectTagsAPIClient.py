from typing import List, Dict, Union, Optional
from .BaseAPIClient import BaseAPIClient
from from rootshell_platform_api.config import API_ENDPOINT, BEARER_TOKEN import API_ENDPOINT, BEARER_TOKEN
import pandas as pd
from data_transfer_objects.ProjectDTO import ProjectDTO


class ProjectTagsAPIClient(BaseAPIClient):
    def __init__(self, project_id):
        super().__init__(base_url=f"{API_ENDPOINT}/projects/{project_id}/tags")

    def get_project_tags(self, limit: int = 10, page: int = 1) -> Union[Dict, str]:
        params = {"limit": limit, "page": page}

        return self.get("", params=params)

    from typing import Dict, Union, List, Optional

    def update_project_tag(self, tag_id: int) -> Union[Dict, str]:
        return self.put(f"/{tag_id}")

    def delete_project_tag(self, tag_id: int) -> Union[Dict, str]:
        return self.delete(f"/{tag_id}")

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
            items = self.get_projects(
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

        return f"Users exported to {file_path}"
