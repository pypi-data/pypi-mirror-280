import argparse
import json
from rootshell_platform_api.adapters.ProjectsAPIClient import ProjectsAPIClient

parser = argparse.ArgumentParser(description="Get a project")
parser.add_argument("--id", required=True, help="ID of the tag")

args = parser.parse_args()
tags_api_client = ProjectsAPIClient()

try:
    response = tags_api_client.get_project(project_id=args.id)
    print(json.dumps(response["data"], indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
