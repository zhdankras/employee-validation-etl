import logging
from datetime import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from typing import Optional

class GoogleDriveUpload:

    def __init__(
        self, credentials, book,
        bamboo_emails: list,
        bamboo_first_names_and_last_names: dict,
        google_workspace_validation_list: list,
        slack_validation_list: list,
        atlassian_validation_list: list
    ):
        self.creds = credentials
        self.book = book
        self.bamboo_emails = bamboo_emails
        self.bamboo_first_names_and_last_names = bamboo_first_names_and_last_names
        self.google_workspace_validation_list = google_workspace_validation_list
        self.slack_validation_list = slack_validation_list
        self.atlassian_validation_list = atlassian_validation_list

    def upload_logs_to_the_document(self) -> None:
        logs = self.book.add_sheet('Employee Profile Validation')
        logs.write(0, 0, 'All accounts(BambooHR)')
        logs.write(0, 1, 'BambooHR')
        logs.write(0, 2, 'Google')
        logs.write(0, 3, 'Slack')
        logs.write(0, 4, 'Atlassian(Jira + Confluence)')
        for row in range(len(self.bamboo_emails)):
             logs.write(row+1, 0, self.bamboo_emails[row])
             logs.write(row+1, 1, self.bamboo_first_names_and_last_names[row])
             logs.write(row+1, 2, self.google_workspace_validation_list[row])
             logs.write(row+1, 3, self.slack_validation_list[row])
             logs.write(row+1, 4, self.atlassian_validation_list[row])
        self.book.save(f'logs({datetime.now().day}-{datetime.now().month}-{datetime.now().year}).xls')

    def upload_to_folder(self, folder_id: str) -> Optional[str]:

        logger = logging.getLogger(__name__)
        self.upload_logs_to_the_document()

        try:

            service = build('drive', 'v3', credentials=self.creds)

            file_metadata = {
                'name': f'logs({datetime.now().day}-{datetime.now().month}-{datetime.now().year}).xls',
                'parents': [folder_id]
            }
            media = MediaFileUpload(f'logs({datetime.now().day}-{datetime.now().month}-{datetime.now().year}).xls',
                                mimetype='xls/xlsx', resumable=True)

            file = service.files().create(body=file_metadata, media_body=media,
                                        fields='id').execute()
            logger.info(F'File ID: "{file.get("id")}".')
            return file.get('id')

        except HttpError as error:
            logger.error(F'An error occurred: {error}')
            return None