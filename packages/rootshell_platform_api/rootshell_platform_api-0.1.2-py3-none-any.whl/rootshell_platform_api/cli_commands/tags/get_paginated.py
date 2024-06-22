import click
import json
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient

@click.command()
@click.option('-l', '--limit', type=int, default=10, help='Pagination limit')
@click.option('-p', '--page', type=int, default=1, help='Pagination page')
@click.option('-s', '--search', type=str, help='Pagination search')
def get_paginated(limit, page, search):
    """
    Get a list of tags with pagination and optional search.
    """
    tags_api_client = TagsAPIClient()
    try:
        response = tags_api_client.get_tags(limit=limit, page=page, search=search)
        click.echo(json.dumps(response['data'], indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == '__main__':
    get_paginated()
