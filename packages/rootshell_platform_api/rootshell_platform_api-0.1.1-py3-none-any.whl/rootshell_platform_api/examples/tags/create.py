import argparse
import json
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient

parser = argparse.ArgumentParser(description="Create a new tag")
parser.add_argument("-n", "--name", required=True, help="tag name")

args = parser.parse_args()

try:
    response = TagsAPIClient().create_tag(args.name)
    print(json.dumps(response, indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
