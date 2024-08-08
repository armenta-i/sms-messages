from dotenv import load_dotenv # type: ignore
import os
import requests #type: ignore

weather_api_url = "https://api.weatherapi.com/v1/current.json?"
load_dotenv()

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
