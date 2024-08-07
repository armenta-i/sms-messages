from twilio.rest import Client # type: ignore
from dotenv import load_dotenv # type: ignore
import os
import requests

# get variables to create client
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

def getQuote():
    quote_api_url = requests.get("https://zenquotes.io/api/quotes/random")
    data = quote_api_url.json()[0]
    quoteMessage = "\"" + data['q'] + '\" by: ' + data['a']
    print("Quote API reponse code: ", quote_api_url.status_code)
    return quoteMessage

if __name__ == "__main__":
    # Create object to be able to create client
    sms = smsInfo()
    # Write body to send message to desire phone
    # sid = sms.sendDefaultMessage('Good Morning')      REMOVE TO SEND MESSAGE DONT FORGET
    # print(f'Message ID: {sid}')
    print(getQuote())

