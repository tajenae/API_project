import requests
from API_KEYS import load_noaa_api_key

class NoaaData:
    #this class will handle NOAA data retrieval and processing as it uses an api key.

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = load_noaa_api_key()
        self.url = f"https://api.weather.gov/points/{latitude},{longitude}/forecast"
#use this function to get the noaa weather data needed. 
    def fetch_noaa_data(self):
        headers = {
            "User-Agent": "NOAA Data" ,
        }
        #get request to the noaa api for data i need
        response = requests.get(self.url, headers=headers)
        #ensuring that the response is good and returns the data needed 
        if response.status_code == 200:
            data = response.json()
            print("NOAA Data Response:", data)
            periods = data["properties"]["periods"]

            #returning the data i will need in this format
            return {
                "forecast_times": [p["startTime"] for p in periods],
                "temperature_max": [p["temperature"] for p in periods],
                "short_forecasts": [p["shortForecast"] for p in periods],
            }
        else:
            print("Error", response.status_code)
            return None
