import click
import json
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient

@click.command()
@click.option('--id', required=True, help='ID of the tag')
def get_single(id):
    """
    Get details of a tag by ID.
    """
    tags_api_client = TagsAPIClient()
    try:
        response = tags_api_client.get_tag(tag_id=id)
        click.echo(json.dumps(response["data"], indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == '__main__':
    get_single()
