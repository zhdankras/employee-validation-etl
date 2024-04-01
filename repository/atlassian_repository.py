import requests
import os
from requests.auth import HTTPBasicAuth

class AtlassianRepository:

    def __init__(self, email: str):
        self.email = email

    def get_employee_atlassian_data(self) -> dict:
        url = "https://<YOUR_ORGANIZATION>.atlassian.net/rest/api/3/user/search"
        auth = HTTPBasicAuth("ashishkarev@<YOUR_ORGANIZATION)>.com", os.environ.get('ATLASSIAN_TOKEN'))

        headers = {
            "Accept": "application/json"
        }

        query = {
            'query': self.email
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=auth
        )

        return response
    
