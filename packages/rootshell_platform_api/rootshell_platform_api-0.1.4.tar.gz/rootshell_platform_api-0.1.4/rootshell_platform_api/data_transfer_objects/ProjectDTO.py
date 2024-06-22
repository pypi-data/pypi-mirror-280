from typing import List, Optional


class ProjectDTO:
    def __init__(
        self,
        name: str,
        company_id: int,
        test_company_id: int,
        job_number: str,
        service_type: int,
        status: int,
        comment: Optional[str] = None,
        client_engagement_id: Optional[int] = None,
        dynamic_remediation: Optional[bool] = None,
        omit_asset_comparisons: Optional[bool] = None,
        executive_summary: Optional[str] = None,
        include_pmo: Optional[int] = None,
        email_reminder: Optional[int] = None,
        email_reminder_period: Optional[int] = None,
        email_reminder_recipients: Optional[List[int]] = None,
        scanner_auto_import: Optional[int] = None,
    ):
        self.name = name
        self.company_id = company_id
        self.test_company_id = test_company_id
        self.job_number = job_number
        self.comment = comment
        self.service_type = service_type
        self.status = status
        self.client_engagement_id = client_engagement_id
        self.dynamic_remediation = dynamic_remediation
        self.omit_asset_comparisons = omit_asset_comparisons
        self.executive_summary = executive_summary
        self.include_pmo = include_pmo
        self.email_reminder = email_reminder
        self.email_reminder_period = email_reminder_period
        self.email_reminder_recipients = email_reminder_recipients
        self.scanner_auto_import = scanner_auto_import

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}
