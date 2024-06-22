import click
import json
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient

@click.command()
@click.option('-i', '--id', required=True, help='ID of the tag')
@click.option('-n', '--name', required=True, help='New name for the tag')
def update(id, name):
    """
    Update an existing tag.
    """
    tags_api_client = TagsAPIClient()
    try:
        response = tags_api_client.update_tag(tag_id=id, new_name=name)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == '__main__':
    update()
