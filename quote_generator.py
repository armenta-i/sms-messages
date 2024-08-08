import requests 

quote_api_url = "https://zenquotes.io/api/quotes/random"

def getQuote():
    quote_response = requests.get(quote_api_url)

    if(quote_response.status_code == 200):
        data = quote_response.json()[0]
        quoteMessage = "Quote of the day: \"" + data['q'] + '\" -' + data['a']
        return quoteMessage
    else:
        print(f"Error getting quote of the day. Status code: {quote_response.status_code}")
