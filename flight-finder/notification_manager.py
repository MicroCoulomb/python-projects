from twilio.rest import Client
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ.get("TWILIO_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))
        self.smtp_address = os.environ.get("SMTP_ADDRESS")
        self.host_email = os.environ.get("EMAIL_HOST_ADDRESS")
        self.host_pw = os.environ.get("EMAIL_HOST_PW")

        self.connection = smtplib.SMTP(os.environ.get("EMAIL_PROVIDER"))

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_= os.environ.get("TWILIO_NUMBER"),
            body= message_body,
            to= os.environ.get("TWILIO_VIRTUAL")
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.host_email, self.host_pw)
            for email in email_list:
                self.connection.sendmail(
                    from_addr= self.host_email,
                    to_addrs= email,
                    msg= f"Subject:New Low Price Flight\n\n{email_body}".encode("utf-8")
                )
