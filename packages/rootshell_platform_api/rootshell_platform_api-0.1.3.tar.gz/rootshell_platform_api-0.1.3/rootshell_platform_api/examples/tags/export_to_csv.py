import argparse
import json
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient

parser = argparse.ArgumentParser(description="Get a list of tags")
parser.add_argument("-f", "--path", required=True, help="File path")
parser.add_argument("-l", "--limit", help="Pagination limit", default=10)
parser.add_argument("-p", "--page", help="Pagination page", default=1)
parser.add_argument("-s", "--search", help="Pagination search")

args = parser.parse_args()
tags_api_client = TagsAPIClient()

try:
    response = tags_api_client.export_tags_to_csv(
        args.path, args.limit, args.page, args.search
    )
    print(json.dumps(response["data"], indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
