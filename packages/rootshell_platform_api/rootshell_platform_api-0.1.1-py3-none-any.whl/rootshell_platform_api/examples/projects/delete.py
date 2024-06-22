import argparse
import json
from rootshell_platform_api.adapters.ProjectsAPIClient import ProjectsAPIClient

parser = argparse.ArgumentParser(description="Delete a project")
parser.add_argument("--id", required=True, help="ID of the project to be deleted")
parser.add_argument("--name", required=True, help="Name of the project to be deleted")

args = parser.parse_args()

try:
    response = ProjectsAPIClient().delete_project(args.id, args.name)
    print(json.dumps(response, indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
