import click
import json
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient

@click.command(name="export_tags")
@click.option("-f", "--path", required=True, type=str, help="File path")
@click.option("-l", "--limit", default=10, type=int, help="Pagination limit")
@click.option("-p", "--page", default=1, type=int, help="Pagination page")
@click.option("-s", "--search", type=str, help="Pagination search")
def export_tags(path, limit, page, search):
    """Export tags to a CSV file."""
    tags_api_client = TagsAPIClient()

    try:
        response = tags_api_client.export_tags_to_csv(path, limit, page, search)
        print(json.dumps(response["data"], indent=4))
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == '__main__':
    export_tags()
