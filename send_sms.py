from twilio.rest import Client # type: ignore
from dotenv import load_dotenv # type: ignore
import os

# get variables 
load_dotenv()

# Class to get all info to create client and send message
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
    
    def sendCustomMessage(self, recipient, sender, body):
        message = self.client.messages.create(
            body = body,
            from_ = sender,
            to = recipient
        )
        return message.sid
    
    def sendDefaultMessage(self, body):
        message = self.client.messages.create(
            body = body,
            from_ = self.__twilio_phone,
            to = self.__recipient_phone
        )
        return message.sid
    

