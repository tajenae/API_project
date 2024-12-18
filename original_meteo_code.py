import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

#This is the original code provided by the official Open-meteo website.

# Using openmetro to fetch historical data, the website indicated there are no Api key needed. 
# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# All required weather variables are listed below such the max tmeperature recorded for a certain date.
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://climate-api.open-meteo.com/v1/climate"
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"start_date": "1950-01-01",
	"end_date": "2050-12-31",
	"models": "CMCC_CM2_VHR4",
	"daily": ["temperature_2m_max", "temperature_2m_min", "relative_humidity_2m_max", "relative_humidity_2m_min", "rain_sum", "snowfall_sum", "pressure_msl_mean"]
}
responses = openmeteo.weather_api(url, params=params)

# Fetch the location needed (New york), and a for-loop is added for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process all daily data needed in the same order that they were requested.
daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
daily_relative_humidity_2m_max = daily.Variables(2).ValuesAsNumpy()
daily_relative_humidity_2m_min = daily.Variables(3).ValuesAsNumpy()
daily_rain_sum = daily.Variables(4).ValuesAsNumpy()
daily_snowfall_sum = daily.Variables(5).ValuesAsNumpy()
daily_pressure_msl_mean = daily.Variables(6).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_data["temperature_2m_min"] = daily_temperature_2m_min
daily_data["relative_humidity_2m_max"] = daily_relative_humidity_2m_max
daily_data["relative_humidity_2m_min"] = daily_relative_humidity_2m_min
daily_data["rain_sum"] = daily_rain_sum
daily_data["snowfall_sum"] = daily_snowfall_sum
daily_data["pressure_msl_mean"] = daily_pressure_msl_mean

daily_dataframe = pd.DataFrame(data = daily_data)
print(daily_dataframe)


# Save the daily dataframe to a CSV file
csv_filename = "open_meteo_climate_data.csv"
daily_dataframe.to_csv(csv_filename, index=False)
print(f"Data saved to {csv_filename}")
