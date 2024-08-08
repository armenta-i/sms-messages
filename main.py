from weather_info import weatherInfo
from maps import googleMaps
from quote_generator import getQuote
from send_sms import smsInfo

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
