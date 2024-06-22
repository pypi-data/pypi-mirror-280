import click
import json
from rootshell_platform_api.adapters.ProjectsAPIClient import ProjectsAPIClient
from rootshell_platform_api.data_transfer_objects.ProjectDTO import ProjectDTO

@click.command()
@click.option("--id", required=True, help="Project ID")
@click.option("--name", required=True, help="Project name")
@click.option("--company_id", required=True, type=int, help="Company ID")
@click.option("--test_company_id", required=True, type=int, help="Test Company ID")
@click.option("--job_number", required=True, type=str, help="Job Number")
@click.option("--comment", help="Comment")
@click.option("--service_type", required=True, type=int, help="Service Type")
@click.option("--status", required=True, type=int, help="Status")
@click.option("--client_engagement_id", type=int, help="Client Engagement ID")
@click.option("--dynamic_remediation", type=bool, help="Dynamic Remediation")
@click.option("--omit_asset_comparisons", type=bool, help="Omit Asset Comparisons")
@click.option("--executive_summary", help="Executive Summary")
@click.option("--include_pmo", type=int, help="Include PMO")
@click.option("--email_reminder", type=int, help="Email Reminder")
@click.option("--email_reminder_period", type=int, help="Email Reminder Period")
@click.option(
    "--email_reminder_recipients",
    type=str,
    help="Comma-separated list of Email Reminder Recipients",
    callback=lambda ctx, param, value: [int(item) for item in value.split(",")] if value else None,
)
@click.option("--scanner_auto_import", type=int, help="Scanner Auto Import")
def update(**kwargs):
    project_id = kwargs.pop('id')
    project_dto = ProjectDTO(**kwargs)

    try:
        response = ProjectsAPIClient().update_project(project_id, project_dto)
        click.echo(json.dumps(response, indent=4))
    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    update()
