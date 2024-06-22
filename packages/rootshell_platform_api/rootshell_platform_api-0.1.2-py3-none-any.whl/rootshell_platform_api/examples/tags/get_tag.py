import argparse
import json
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient

parser = argparse.ArgumentParser(description="Get a tag")
parser.add_argument("--id", required=True, help="ID of the tag")

args = parser.parse_args()
tags_api_client = TagsAPIClient()

try:
    response = tags_api_client.get_tag(tag_id=args.id)
    print(json.dumps(response["data"], indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
