from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv(dotenv_path="API_keys.env")


class NotificationManager:
    def __init__(self):
        self.client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        self.from_whatsapp = "whatsapp:+14155238886"
        self.to_whatsapp = f"whatsapp:{os.getenv('TWILIO_VERIFIED_NUMBER')}"

    def send_whatsapp(self, message_body):
        self.client.messages.create(
            from_=self.from_whatsapp,
            body=message_body,
            to=self.to_whatsapp
        )
