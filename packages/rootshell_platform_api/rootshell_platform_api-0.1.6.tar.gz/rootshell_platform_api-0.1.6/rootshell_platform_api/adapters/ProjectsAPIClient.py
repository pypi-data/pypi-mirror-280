from typing import List, Dict, Union, Optional
from .BaseAPIClient import BaseAPIClient
from rootshell_platform_api.config import API_ENDPOINT, BEARER_TOKEN
import pandas as pd
from rootshell_platform_api.data_transfer_objects.ProjectDTO import ProjectDTO

class ProjectsAPIClient(BaseAPIClient):
    def __init__(self):
        super().__init__(base_url=f"{API_ENDPOINT}/projects")

    def get_projects(
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

    def create_project(self, project: ProjectDTO) -> Union[Dict, str]:
        data = project.to_dict()
        return self.post("", data)

    def get_project(self, project_id: int) -> Union[Dict, str]:
        return self.get(f"/{project_id}")

    def update_project(self, project_id: int, project: ProjectDTO) -> Union[Dict, str]:
        data = project.to_dict()
        return self.put(f"/{project_id}", data)

    def delete_project(self, project_id: int, project_name: str) -> Union[Dict, str]:
        data = {"project_name": project_name}
        return self.delete(f"/{project_id}", data=data)

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

    def get_project_remediation_types(self) -> Union[Dict, str]:
        return self.get(f"/dynamic-remediation-types")

    def get_project_service_types(self) -> Union[Dict, str]:
        return self.get(f"/service-types")

    def get_project_statuses(self) -> Union[Dict, str]:
        return self.get(f"/statuses")

    def list_projects(self):
        projects = self.get_projects()
        if not projects or not isinstance(projects, dict) or "data" not in projects:
            print("No projects found.")
            return []

        print("\nAvailable Projects:")
        for project in projects["data"]:
            print(f"- Project ID: {project['id']}, Project Name: {project['name']}")

        return projects["data"]

    def select_project(self):
        projects = self.list_projects()
        if not projects:
            return None

        while True:
            try:
                project_id = int(input("\nEnter the Project ID to link the tag: "))
                if any(project["id"] == project_id for project in projects):
                    return project_id
                else:
                    print("Invalid Project ID. Please select from the list.")
            except ValueError:
                print("Invalid input. Please enter a valid Project ID.")
