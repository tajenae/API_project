import requests
from API_KEYS import load_weatherstack_api_key
import json

def fetch_current_weather():
    api_key = load_weatherstack_api_key()  #load the Weatherstack API key

    # New York's exact loaction - latitude and longitude
    lat = 40.7128  
    lon = -74.0060 

    #URL for getting current weather data
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={lat},{lon}'
    response = requests.get(url)
    
    #check to make sure data is being fetched properly
    if response.status_code == 200:
        data = response.json()  
        print("Current weather data:", json.dumps(data, indent=4))
        
        # save the file for later
        with open('weatherstack_current_data.json', 'w') as file:
            json.dump(data, file, indent=4)
        print("Current weather data saved to weatherstack_current_data.json")
    else:
        print(f"Error fetching data: {response.status_code}")
        print(response.text)  

# call the function to fetch current weather data form Weatherstack
fetch_current_weather()
