import os
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from typing import Optional

class SlackRepository:
    
    def get_employees_slack_data() -> Optional[dict]:

        logger = logging.getLogger(__name__)

        try:

            client = WebClient(token = os.environ.get('SLACK_TOKEN'))
            result = client.users_list()
            employees = [employee.get('profile') for employee in result['members']]
            
            return {
                employee['email'] : [employee['real_name'], employee['display_name'], employee['title'], employee['phone']] 
                for employee in employees if employee.get('email') != None
            }
        
        except SlackApiError as e:
            logger.error("Error creating conversation: {}".format(e))
            return None