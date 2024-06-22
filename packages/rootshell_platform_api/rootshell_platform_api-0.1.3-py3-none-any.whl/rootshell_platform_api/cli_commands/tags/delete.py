import click
import json
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient

@click.command()
@click.option('--id', required=True, type=str, help='ID of the tag to be deleted')
def delete(id):
    """
    Delete a tag with the given ID.
    """
    try:
        response = TagsAPIClient().delete_tag(id)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == '__main__':
    delete()
