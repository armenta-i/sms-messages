import os
import requests # type: ignore
import googlemaps # type: ignore
import urllib.parse

google_maps_api_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

class googleMaps:
    def __init__(self):
        self.gmapsKey = os.getenv('GOOGLE_API')
        self.gmaps = googlemaps.Client(key=self.gmapsKey)

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
