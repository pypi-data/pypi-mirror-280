import click
import json
from rootshell_platform_api.adapters.TagsAPIClient import TagsAPIClient
from .. import Command

class CreateTagCommand(Command):
    def execute(self, name):
        try:
            response = TagsAPIClient().create_tag(name)
            print(json.dumps(response, indent=4))
        except Exception as e:
            print(f"Error occurred: {e}")

@click.command(name="create")
@click.option("-n", "--name", required=True, help="Tag name")
def create(name):
    """Create a new tag"""
    command = CreateTagCommand()
    command.execute(name)

if __name__ == '__main__':
    create()