import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv(dotenv_path="API_keys.env")

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message_body):

        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )
        print(message.sid)


    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_="whatsapp:+14155238886",
            body=message_body,
            to=os.getenv("NUMBER")
        )
        print(message.sid)