import argparse
import json
from rootshell_platform_api.adapters.TestTypesAPIClient import TestTypesAPIClient

parser = argparse.ArgumentParser(description="Get a list of test types")
parser.add_argument("-l", "--limit", type=int, help="Pagination limit", default=10)
parser.add_argument("-p", "--page", type=int, help="Pagination page", default=1)
parser.add_argument("-s", "--search", type=str, help="Pagination search")
parser.add_argument(
    "-c", "--orderByColumn", type=str, help="Pagination order by column"
)
parser.add_argument(
    "-d",
    "--orderByDirection",
    type=str,
    help="Pagination order by direction",
    choices=["asc", "desc"],
)

args = parser.parse_args()
api_client = TestTypesAPIClient()

try:
    response = api_client.get_test_types(
        limit=args.limit,
        page=args.page,
        search=args.search,
        orderByColumn=args.orderByColumn,
        orderByDirection=args.orderByDirection,
    )
    print(json.dumps(response["data"], indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
