import requests
import json
from datetime import datetime, timedelta
from API_KEYS import load_noaa_api_key  

def load_noaa_data():
    # loading the NOAA API key from the function created
    api_key = load_noaa_api_key()

    # the given station ID for New york city (NYC)
    station_id = 'GHCND:USW00094728'

    #requesting a 30 day range of information from the noaa website.
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30) 
    end_date_str = end_date.strftime('%Y-%m-%d')
    start_date_str = start_date.strftime('%Y-%m-%d')

    #URL
    url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TMAX,TMIN,PRCP&startdate={start_date_str}&enddate={end_date_str}&stationid={station_id}'
    headers = {'token': api_key}

    # making the API request
    response = requests.get(url, headers=headers)

    # Handling the response - there were lots of errors and trials in getting the information needed at first. As a lot of the times it 
    # didnt retrieve any data as my range was too wide for the free plan for collecting information using API's on the Noaa website. 
    if response.status_code == 200:
        data = response.json()

        # save the data if results are found
        if "results" in data and data["results"]:
            with open('noaa_weather_data_30_days.json', 'w') as f:
                json.dump(data["results"], f, indent=4)
            print(f"Weather data saved for the last 30 days ({start_date_str} to {end_date_str}).")
        else:
            print("No results found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# calling the function needed to fetch the Noaa data
load_noaa_data()

