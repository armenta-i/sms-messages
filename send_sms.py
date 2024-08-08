from twilio.rest import Client # type: ignore
from dotenv import load_dotenv # type: ignore
from datetime import datetime
import os
import requests #type: ignore
import googlemaps
import urllib.parse

# get variables to create client
load_dotenv()

quote_api_url = "https://zenquotes.io/api/quotes/random"
weather_api_url = "https://api.weatherapi.com/v1/current.json?"
google_maps_api_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

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

class weatherInfo:
    def __init__(self):
        self.__weather_key = os.getenv('WEATHER_API_KEY')

    def getWeather(self):
        weather_response = requests.get(weather_api_url + "&q=El%20Paso&key=" + self.__weather_key)
        
        if(weather_response.status_code == 200):
            # Storing all weather data to put in message
            weather_data = weather_response.json()['current']
            weather_farenheit = weather_data['temp_f']
            weather_celsius = weather_data['temp_c']
            precip_mm = weather_data['precip_mm']

            # Calculate precipitation chances based of a simple model found online (Not accurate)
            if(precip_mm <= 2):
                chance_precipitation = '20%'
            elif(precip_mm <= 5):
                chance_precipitation = '50%'
            else:
                chance_precipitation = '80%'

            weather_message = (f'Expected temperature: F:  {str(weather_farenheit)}  | C: {str(weather_celsius)} \nChances of precipitation:  {str(chance_precipitation)}')
            return weather_message
        else:
            print("Error getting weather data", weather_response.status_code)


def getQuote():
    quote_response = requests.get(quote_api_url)

    if(quote_response.status_code == 200):
        data = quote_response.json()[0]
        quoteMessage = "Quote of the day: \"" + data['q'] + '\" -' + data['a']
        return quoteMessage
    else:
        print(f"Error getting quote of the day. Status code: {quote_response.status_code}")

class googleMaps:
    def __init__(self):
        self.gmapsKey = os.getenv('GOOGLE_API')
        self.gmaps = googlemaps.Client(key=self.gmapsKey)
        self.departureTime = datetime.now()

    def getDirections(self, origin, destination):
        self.destination = urllib.parse.quote(destination)
        self.origin = urllib.parse.quote(origin)  
        direction_result = requests.get(f'{google_maps_api_url}?departure_time=now&destinations={self.destination}&mode=driving&origins={self.origin}&key={self.gmapsKey}')
        parsed_direction_results = direction_result.json()
        if(direction_result.status_code == 200):
            self.travel_duration = parsed_direction_results.get('rows')[0].get('elements')[0].get('duration_in_traffic').get('text')
            self.travel_distance = parsed_direction_results.get('rows')[0].get('elements')[0].get('distance').get('text')
            
        else:
            return("Error fetching Distance Matrix", direction_result.status_code)

    def getTravelSummary(self, origin, destination):
        self.getDirections(origin, destination)
        travel_summary = (f'Journey from {urllib.parse.unquote(self.origin)} to {urllib.parse.unquote(self.destination)} covers {self.travel_distance} and will take approximately {self.travel_duration}')
        return travel_summary
    
if __name__ == "__main__":
    # Create objects to be able to create client and obtain necessary info for message
    sms = smsInfo()
    weather = weatherInfo()
    gMaps = googleMaps()
    quote_of_day = getQuote()
    weather_message_container = weather.getWeather()
    resultDirection = gMaps.getTravelSummary("601 White Cliffs Dr, El Paso, TX 79912, USA", "Unversity of Texas at El Paso")
    message_body = quote_of_day + '\n' + weather_message_container 
    message_body = (f'{quote_of_day}\n{weather_message_container}\n{resultDirection}')

    # Write body to send message to desire phone
    sid = sms.sendDefaultMessage(message_body)
    print(f'Message ID: {sid}')

