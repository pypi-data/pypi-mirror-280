import click
import json
from rootshell_platform_api.adapters.ProjectsAPIClient import ProjectsAPIClient

@click.command()
@click.option("--id", required=True, help="ID of the project to be deleted")
@click.option("--name", required=True, help="Name of the project to be deleted")
def delete(id, name):
    try:
        response = ProjectsAPIClient().delete_project(id, name)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    delete()
