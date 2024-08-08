# Daily Message Sender with Day to Day Information

## Overview

This project is a Python application that sends a daily message containing a random quote, current weather information, and travel details between two locations. The message is sent via SMS using the Twilio API.

## Features

- Fetches a random quote from an API.
- Retrieves current weather conditions and precipitation chances.
- Calculates travel duration and distance between two locations using Google Maps API.
- Sends the collected information via SMS using Twilio API.

## Setup

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)
- A Twilio account with an SMS-enabled phone number
- A Google Maps API key
- A Weather API key

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Install the required packages:**

        pip install -r requirements.txt

3. **Create a `.env` file in the root directory and add your API keys:**

    ```TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_PHONE=your_twilio_phone_number
    RECIPIENT_PHONE=recipient_phone_number
    WEATHER_API_KEY=your_weather_api_key
    GOOGLE_API=your_google_maps_api_key

4. **Run the script:**

        python main.py

## Example Output

```mathematica
Message ID: SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

This ID will be printed when you message is send.

The message body will include: 
- A random quote of the day
- Current weather information including temperature and precipitation chances
- Travel details including distance and duration between the specified locations.

### Acknowledgements

- (Twilio API)[https://www.twilio.com/]
- (Weather API)[https://www.weatherapi.com/]
- (Google Maps API)[https://developers.google.com/maps]
- (ZenQuotes API)[https://zenquotes.io/]

### License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for details