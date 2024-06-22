from typing import List, Dict, Union, Optional
from .BaseAPIClient import BaseAPIClient
from rootshell_platform_api.config import API_ENDPOINT, BEARER_TOKEN
import pandas as pd

class TagsAPIClient(BaseAPIClient):
    def __init__(self):
        super().__init__(base_url=f"{API_ENDPOINT}/tags")

    def get_tags(
        self, limit: int = 10, page: int = 1, search: Optional[str] = None
    ) -> Union[Dict, str]:
        params = {"limit": limit, "page": page}
        if search:
            params["search"] = search

        return self.get("", params=params)

    def create_tag(self, tag_name: str) -> Union[Dict, str]:
        data = {"name": tag_name}
        return self.post("", data)

    def get_tag(self, tag_id: int) -> Union[Dict, str]:
        return self.get(f"/{tag_id}")

    def update_tag(self, tag_id: int, new_name: str) -> Union[Dict, str]:
        data = {"name": new_name}
        return self.put(f"/{tag_id}", data)

    def delete_tag(self, tag_id: int) -> Union[Dict, str]:
        return self.delete(f"/{tag_id}")

    def export_tags_to_csv(
        self, file_path: str, limit: int = 10, page: int = 1, search: str = None
    ) -> str:
        all_tags = []
        current_page = page

        while True:
            tags = self.get_tags(limit=limit, page=current_page, search=search)

            if not tags.get("data"):
                break

            all_tags.extend(tags.get("data"))

            if not tags.get("links", {}).get("next"):
                break

            current_page += 1

        df = pd.DataFrame(all_tags)
        df.to_csv(file_path, index=False)

        return f"Tags exported to {file_path}"

    def list_tags(self):
        tags = self.get_tags(limit=100)
        if not tags or not isinstance(tags, dict) or "data" not in tags:
            print("No tags found.")
            return []

        print("\nAvailable Tags:")
        for tag in tags["data"]:
            print(f"- Tag ID: {tag['id']}, Tag Name: {tag['name']}")

        return tags["data"]

    def select_tag(self):
        tags = self.list_tags()
        if not tags:
            return None

        while True:
            try:
                tag_id = int(input("\nEnter the Tag ID to link the tag: "))
                if any(tag["id"] == tag_id for tag in tags):
                    return tag_id
                else:
                    print("Invalid Tag ID. Please select from the list.")
            except ValueError:
                print("Invalid input. Please enter a valid Tag ID.")
