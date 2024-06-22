import argparse
import json
from rootshell_platform_api.adapters.ProjectTagsAPIClient import ProjectTagsAPIClient

parser = argparse.ArgumentParser(
    description="Get a list of tags connected to a project"
)
parser.add_argument("--id", required=True, type=int, help="Project ID", default=10)
parser.add_argument("-l", "--limit", type=int, help="Pagination limit", default=10)
parser.add_argument("-p", "--page", type=int, help="Pagination page", default=1)

args = parser.parse_args()
api_client = ProjectTagsAPIClient(args.id)

try:
    response = api_client.get_project_tags(limit=args.limit, page=args.page)
    print(json.dumps(response["data"], indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
