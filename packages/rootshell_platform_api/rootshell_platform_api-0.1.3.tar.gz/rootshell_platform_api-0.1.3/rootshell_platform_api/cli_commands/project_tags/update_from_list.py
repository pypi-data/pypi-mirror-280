import argparse
import json
from rootshell_platform_api.adapters.ProjectTagsAPIClient import ProjectTagsAPIClient
from rootshell_platform_api.adapters.ProjectsAPIClient import ProjectsAPIClient
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient

selected_project_id = ProjectsAPIClient().select_project()

selected_tag_id = TagsAPIClient().select_tag()

api_client = ProjectTagsAPIClient(selected_project_id)

try:
    response = api_client.update_project_tag(tag_id=selected_tag_id)
    print(json.dumps(response, indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
