import click
import json
from rootshell_platform_api.adapters.ProjectsAPIClient import ProjectsAPIClient

@click.command()
@click.option("-f", "--path", required=True, help="File path")
@click.option("-l", "--limit", type=int, default=10, help="Pagination limit")
@click.option("-p", "--page", type=int, default=1, help="Pagination page")
@click.option("-s", "--search", type=str, help="Pagination search")
@click.option("-c", "--orderByColumn", type=str, help="Pagination order by column")
@click.option("-d", "--orderByDirection", type=str, help="Pagination order by direction")
def export_to_csv(path, limit, page, search, orderByColumn, orderByDirection):
    api_client = ProjectsAPIClient()

    try:
        response = api_client.export_to_csv(
            file_path=path,
            limit=limit,
            page=page,
            search=search,
            orderByColumn=orderByColumn,
            orderByDirection=orderByDirection,
        )
        click.echo(json.dumps(response["data"], indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    export_to_csv()
