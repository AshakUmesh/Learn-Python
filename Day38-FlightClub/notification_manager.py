import smtplib

from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv(dotenv_path="API_keys.env")


class NotificationManager:
    def __init__(self):
        self.client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        self.from_whatsapp = "whatsapp:+14155238886"
        self.to_whatsapp = f"whatsapp:{os.getenv('TWILIO_VERIFIED_NUMBER')}"
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.connection = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"])

    def send_whatsapp(self, message_body):
        self.client.messages.create(
            from_=self.from_whatsapp,
            body=message_body,
            to=self.to_whatsapp
        )

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
