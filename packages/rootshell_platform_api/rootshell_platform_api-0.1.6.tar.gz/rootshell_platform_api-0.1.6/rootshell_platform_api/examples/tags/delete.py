import argparse
import json
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient

parser = argparse.ArgumentParser(description="Delete a tag")
parser.add_argument("--id", required=True, help="ID of the tag to be deleted")

args = parser.parse_args()

try:
    response = TagsAPIClient().delete_tag(args.id)
    print(json.dumps(response, indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
