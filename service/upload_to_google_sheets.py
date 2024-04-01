import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GoogleSheetsUpload:

    def __init__(
        self, credentials, 
        spreadsheets_ids: list,
        range_name: str,
        bamboo_emails: list,
        bamboo_first_names_and_last_names: dict,
        google_workspace_validation_list: list,
        slack_validation_list: list,
        atlassian_validation_list: list
    ):
        self.creds = credentials
        self.spreadsheet_ids = spreadsheets_ids
        self.range_name = range_name
        self.bamboo_emails = bamboo_emails
        self.bamboo_first_names_and_last_names = bamboo_first_names_and_last_names
        self.google_workspace_validation_list = google_workspace_validation_list
        self.slack_validation_list = slack_validation_list
        self.atlassian_validation_list = atlassian_validation_list

    def upload_to_list(self) -> None:

        logger = logging.getLogger(__name__)

        try:

            service = build('sheets', 'v4', credentials=self.creds)
            sheet = service.spreadsheets()

            for spreadsheet_id in self.spreadsheet_ids:
                sheet.values().batchUpdate(spreadsheetId=spreadsheet_id, body = {
                    "valueInputOption": "USER_ENTERED",
                    "data": [
                        {
                            "range": self.range_name,
                            "majorDimension": "COLUMNS",
                            "values": [
                                    self.bamboo_emails,
                                    self.bamboo_first_names_and_last_names,
                                    self.google_workspace_validation_list,
                                    self.slack_validation_list,
                                    self.atlassian_validation_list
                                ]
                        }
                    ]
                }).execute()
        
        except HttpError as err:
            logger.error(F'An error occurred: {err}')
            return None

    def upload_to_list_one_employee(self) -> None:
        pass
