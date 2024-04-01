import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GoogleSheetsRepository:

    def __init__(
            self, credentials, 
            spreadsheets_ids: list,
            range_name: str
        ):
            self.creds = credentials,
            self.spreadsheets_ids = spreadsheets_ids,
            self.range_name = range_name

    def check_employee(self):
        for spreadsheet_id in self.spreadsheets_ids:
            service = build('sheets', 'v4', credentials=self.creds)
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                        range=self.range_name).execute()
            values = result.get('values', [])
    