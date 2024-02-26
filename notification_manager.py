
from twilio.rest import Client

ACCOUNT_SID = "YOUR SID"
AUTH_TOKEN = "YOUR AUTH TOKEN"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID,AUTH_TOKEN)

    def send_message(self,phone_num_from,phone_num_to,message):
        message = self.client.messages.create(
            body=message,
            from_=phone_num_from,
            to=phone_num_to
        )
        print(message.sid)
        print(message.status)