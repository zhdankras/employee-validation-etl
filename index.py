import json
from google.oauth2 import service_account
from service.update_info import UpdateInformation
from notification.slack_notification import SlackNotification

credentials = service_account.Credentials.from_service_account_file(
                'credentials.json', scopes=[
                        'https://www.googleapis.com/auth/admin.directory.user',
                        'https://www.googleapis.com/auth/drive',
                        'https://www.googleapis.com/auth/spreadsheets'
                    ], subject='ashishkarev@<YOUR_ORGANIZATION>.com'
        )

channels_ids_and_document_links = {
    'C05M9QSM0F9': 'https://docs.google.com/spreadsheets/d/<YOUR_ID>/edit#gid=150962675',
    'C05LU0VEW74': 'https://docs.google.com/spreadsheets/d/<YOUR_ID>/edit#gid=0'
}

def main(event, context):
    UpdateInformation(credentials=credentials).update_info_all_employees()
    SlackNotification(channels_ids_and_document_links=channels_ids_and_document_links).send_notification_to_the_channel()


    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }


