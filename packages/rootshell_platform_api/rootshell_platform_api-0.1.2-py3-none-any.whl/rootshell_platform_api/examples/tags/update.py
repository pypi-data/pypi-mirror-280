import argparse
import json
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient

parser = argparse.ArgumentParser(description="Update an existing tag")
parser.add_argument("-i", "--id", required=True, help="tag id")
parser.add_argument("-n", "--name", required=True, help="tag name")

args = parser.parse_args()
tags_api_client = TagsAPIClient()

try:
    response = tags_api_client.update_tag(tag_id=args.id, new_name=args.name)
    print(json.dumps(response, indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
