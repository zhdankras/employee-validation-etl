import os
import requests

headers = {
            "Authorization": os.environ.get('BAMBOOHR_TOKEN'),
            "Accept": "application/json"
}

class BamboohrRepository:

    def get_employees_bamboo_data() -> dict:
        url = "https://api.bamboohr.com/api/gateway.php/<YOUR_ORGANIZATION>/v1/reports/custom?format=json&onlyCurrent=true"
        
        payload = {
            "title": "string",
            "filters": { "lastChanged": {
                    "includeNull": "string",
                    "value": "string"
                } },
            "fields": ["workEmail", "firstName", "lastName", "city", "country", "status"]
        }

        response = requests.post(url, json=payload, headers=headers)

        return {
            employee["workEmail"] : [employee["firstName"] +' '+ employee["lastName"], employee["city"], employee["country"]] 
            for employee in response.json()["employees"] if employee["workEmail"] != None and employee['status'] == 'Active'
        }

    def upload_bamboo_emails(employees_data: dict) -> list:
        return [
            employee_key for employee_key in employees_data 
        ]
    
    def upload_bamboo_first_names_and_last_names(employees_data: dict) -> list:
        return [
            employees_data.get(employee_key)[0] for employee_key in employees_data
        ]


