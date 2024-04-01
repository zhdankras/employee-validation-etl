import logging
import time
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ.get('SLACK_TOKEN')

class SlackNotification:

    def __init__(self, channels_ids_and_document_links: dict):
        self.channels_ids_and_document_links = channels_ids_and_document_links

    def notification_to_the_channel(self, channel_id: str, link: str) -> None:
        
        try:
            
            WebClient(token=slack_token).chat_postMessage(
                channel=channel_id,
                text=":virtual-meeting: Hey there <!here>! View profiles updates " +
                f"<{link}|_*here*_>! Template:\n\n" +
                ":google: _Google:_\n>" +
                "*✕ – The first name and the last name in Google does not meet the standard!*\n>" +
                "*✓ – Success!*\n>" +
                "*Not Found – Employee is not found!*\n\n" +
                ":slack: _Slack:_\n>" +
                "*✕✓✓✓✓✓ – The real name in Slack does not meet the standard!*\n>" +
                "*✓✕✓✓✓✓ – The display name in Slack does not meet the standard!*\n>" +
                "*✓✓✕✓✓✓ – There is no description (position, where the person is from)!*\n>" +
                "*✓✓✓✕✓✓ – Description (position, where the person is from) is not set according to the standard!*\n>" +
                "*✓✓✓✓✕✓ – The location of the employee is set incorrectly(or the location not set at all)!*\n>" +
                "*✓✓✓✓✓✕ - Phone number not set!*\n>" + 
                "*✓✓✓✓✓✓ – Success!*\n>" +
                "*Not Found – Employee is not found!*\n\n"
                ":jira: _Attlassian(Jira+Confluence):_\n>" +
                "*✕✓ – The real name in Atlassian(Jira + Confluence) does not meet the standard!*\n>" +
                "*✓✕ – Profile without photo!*\n>" +
                "*✓✓ – Success!*\n>" +
                "*Not Found – Employee is not found!*\n\n" +
                ":googledrive: See the archive <https://drive.google.com/drive/folders/<YOUR_ID>|_*here*_>!\n" +
                ":exclamation: See <https://<YOUR_ORGANIZATION>.atlassian.net/wiki/spaces/ITA/pages/11124015146/Employee+Profile+Identification|_*instruction*_> for more information.\n" +
                "Have a great week!"
            )

        except SlackApiError as e:
            logging.error(f"Error posting message: {e}")

    def send_notification_to_the_channel(self):
        for channel_id in self.channels_ids_and_document_links:
            self.notification_to_the_channel(channel_id, self.channels_ids_and_document_links.get(channel_id))
            time.sleep(3)