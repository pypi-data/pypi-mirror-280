import argparse
import json
from rootshell_platform_api.adapters.TestTypesAPIClient import TestTypesAPIClient

parser = argparse.ArgumentParser(description="Export test types to csv")
parser.add_argument("-f", "--path", required=True, help="File path")
parser.add_argument("-l", "--limit", type=int, help="Pagination limit", default=10)
parser.add_argument("-p", "--page", type=int, help="Pagination page", default=1)
parser.add_argument("-s", "--search", type=str, help="Pagination search")
parser.add_argument(
    "-c", "--orderByColumn", type=str, help="Pagination order by column"
)
parser.add_argument(
    "-d", "--orderByDirection", type=str, help="Pagination order by direction"
)

args = parser.parse_args()
api_client = TestTypesAPIClient()

try:
    response = api_client.export_to_csv(
        file_path=args.path,
        limit=args.limit,
        page=args.page,
        search=args.search,
        orderByColumn=args.orderByColumn,
        orderByDirection=args.orderByDirection,
    )
    print(json.dumps(response["data"], indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
