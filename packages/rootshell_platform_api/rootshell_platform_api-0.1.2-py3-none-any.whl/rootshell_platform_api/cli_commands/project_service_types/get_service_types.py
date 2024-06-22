import argparse
import json
from rootshell_platform_api.adapters.ProjectsAPIClient import ProjectsAPIClient

api_client = ProjectsAPIClient()

try:
    response = api_client.get_project_service_types()
    print(json.dumps(response["data"], indent=4))
except Exception as e:
    print(f"Error occurred: {e}")
