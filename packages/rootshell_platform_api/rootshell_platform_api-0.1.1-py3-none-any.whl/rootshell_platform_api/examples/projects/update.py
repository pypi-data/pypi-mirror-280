import argparse
import json
from typing import List
from rootshell_platform_api.adapters.ProjectsAPIClient import ProjectsAPIClient
from data_transfer_objects.ProjectDTO import ProjectDTO

parser = argparse.ArgumentParser(description="Create a new project")
parser.add_argument("--id", required=True, help="Project ID")
parser.add_argument("--name", required=True, help="Project name")
parser.add_argument("--company_id", required=True, type=int, help="Company ID")
parser.add_argument(
    "--test_company_id", required=True, type=int, help="Test Company ID"
)
parser.add_argument("--job_number", required=True, type=str, help="Job Number")
parser.add_argument("--comment", help="Comment")
parser.add_argument("--service_type", required=True, type=int, help="Service Type")
parser.add_argument("--status", required=True, type=int, help="Status")
parser.add_argument("--client_engagement_id", type=int, help="Client Engagement ID")
parser.add_argument("--dynamic_remediation", type=bool, help="Dynamic Remediation")
parser.add_argument(
    "--omit_asset_comparisons", type=bool, help="Omit Asset Comparisons"
)
parser.add_argument("--executive_summary", help="Executive Summary")
parser.add_argument("--include_pmo", type=int, help="Include PMO")
parser.add_argument("--email_reminder", type=int, help="Email Reminder")
parser.add_argument("--email_reminder_period", type=int, help="Email Reminder Period")
parser.add_argument(
    "--email_reminder_recipients",
    type=lambda s: [int(item) for item in s.split(",")],
    help="Comma-separated list of Email Reminder Recipients",
)
parser.add_argument("--scanner_auto_import", type=int, help="Scanner Auto Import")

args = parser.parse_args()

project_dto = ProjectDTO(
    name=args.name,
    company_id=args.company_id,
    test_company_id=args.test_company_id,
    job_number=args.job_number,
    comment=args.comment,
    service_type=args.service_type,
    status=args.status,
    client_engagement_id=args.client_engagement_id,
    dynamic_remediation=args.dynamic_remediation,
    omit_asset_comparisons=args.omit_asset_comparisons,
    executive_summary=args.executive_summary,
    include_pmo=args.include_pmo,
    email_reminder=args.email_reminder,
    email_reminder_period=args.email_reminder_period,
    email_reminder_recipients=args.email_reminder_recipients,
    scanner_auto_import=args.scanner_auto_import,
)

try:
    response = ProjectsAPIClient().update_project(args.id, project_dto)
    print(json.dumps(response, indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
