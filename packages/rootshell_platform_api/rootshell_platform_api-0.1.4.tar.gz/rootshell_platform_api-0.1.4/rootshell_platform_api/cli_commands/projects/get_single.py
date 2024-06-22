import click
import json
from rootshell_platform_api.adapters.ProjectsAPIClient import ProjectsAPIClient

@click.command()
@click.option("--id", required=True, help="ID of the project")
def get_single(id):
    tags_api_client = ProjectsAPIClient()

    try:
        response = tags_api_client.get_project(project_id=id)
        click.echo(json.dumps(response["data"], indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    get_single()
