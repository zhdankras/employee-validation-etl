import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from typing import Optional

class GoogleWorkspaceRepository:

    def __init__(self, credentials):
        self.creds = credentials
    
    def get_employees_google_workspace_data(self) -> Optional[dict]: 

        logger = logging.getLogger(__name__)

        try:

            service_google_workspace = build('admin', 'directory_v1', credentials=self.creds)
            employees = service_google_workspace.users().list(
                customer='my_customer', maxResults=300, orderBy='email'
            ).execute()

            return {
                employee['primaryEmail'] : employee['name']['fullName'] 
                for employee in employees.get('users', [])
            }
        
        except HttpError as error:
            logger.error(F'An error occurred: {error}')
            return None
    

