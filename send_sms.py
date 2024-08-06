from twilio.rest import Client # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()
# Hide your sensitive information using env variables set before running script
class smsInfo:
    def __init__(self):
        self.__account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.__auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.__twilio_phone = os.getenv('TWILIO_PHONE')
        self.__recipient_phone = os.getenv('RECIPIENT_PHONE')

        self.client = Client(self.__account_sid, self.__auth_token)

    def get__sid__var(self):
        return self.__account_sid
    
    def get__token_var(self):
        return self.__auth_token
    
    def get__twilio_phone(self):
        return self.__twilio_phone
    
    def get__recipient_phone(self):
        return self.__recipient_phone
    
    def sendMessage(self, recipient, sender, body):
        message = self.client.messages.create(
            body = body,
            from_ = sender,
            to = recipient
        )
        return message.sid

if __name__ == "__main__":
# Create object to be able to get sensitive information
    sms = smsInfo()
    
    sid = sms.sendMessage('+15759155602', '+18556750732', 'Message set works')
    print(f'Message ID: {sid}')


