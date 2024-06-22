import argparse
import json
from rootshell_platform_api.adapters.ProjectTagsAPIClient import ProjectTagsAPIClient

parser = argparse.ArgumentParser(description="Link a tag to a project")
parser.add_argument("-p", "--project_id", required=True, help="project id")
parser.add_argument("-t", "--tag_id", required=True, help="tag id")

args = parser.parse_args()
api_client = ProjectTagsAPIClient(args.project_id)

try:
    response = api_client.update_project_tag(tag_id=args.tag_id)
    print(json.dumps(response, indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
