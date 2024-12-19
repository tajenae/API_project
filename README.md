# API_project
Project: API-Driven Application with OOP and Visualizations - 

Climate Change Api project using through Weather Data from Apis

This project aims to analyze weather data from APIs and use that data to look at climate change trends. By using the data collected, I was able to calculate yearly weather averages and create graphs to better understand how temperatures have changed over time and what that means for climate change. 

The data was sourced from:

- NOAA (National Oceanic and Atmospheric Administration) API: This website was only able to provide short-term weather forecasts as there were data limits due to the free subscription plan used. The current weather data is good for analyzing today’s weather patterns and compare it to historical and future forecasts.
- Open-Meteo: This website was able to provide historical climate and also forecasts ranging from 1950 to 2050. There were no limits to how much information I could retrieve. Therefore, despite not having an official API, the weather data from this website was also used to analysis climate changes. Note: The Meteo data was given via a csv file available on the NOAA official website. The original code for using this data was also provided on the website and I have also included it in the project as it proved to be useful in understanding the data.

What I used to complete this project:

- VS code, json and  Python libraries such as pandas, matplotlib, requests.
- The API for NOAA data was taken from the NOAA website after signing up, and it is now stored in the noaa_api_key.txt file and is apart of my .gitignore file as I don’t want it to be uploaded on Github.
- the weather data for Noaa and Meteo were save in separate files which I have listed below. 

How to run this project:

I used VS code for this project and ran many of my requests in the terminal by using my main.py file. This should run the code and show the graphs I created and save any updates to separate files. I then used those graphs to analyze the data, which will be attached just in case they don't properly load in the future. The API key needed for NOAA is also included in this submission. 

Challenges I encountered in completing this project: 

This project came with a few challenges for me as working with APIs have always seemed more complex than they actually are. Initially I started this project by exploring and experimenting with APIs like WeatherStack and OpenWeather, but their free plans had limitations, such as only providing 7 days of data, which wasn’t enough for meaningful analysis. This led me to switch to NOAA and Open-Meteo, which offered more useful data for me, even though meteo didn’t require the need for an API. Another challenge was understanding the data itself. NOAA temperatures were in Celsius, so I had to convert them to Fahrenheit for better readability as I wasn’t able to really figure out the highs and lows as i normally dont use celsius. 

Working with Open-Meteo’s vast dataset (1950 to 2050) was also tricky, as the range was too large to visualize easily. I addressed this by calculating yearly averages to simplify the data and stored it in a separate file than the one that was initially given. For some of the error handling code I had to search online as many times the code wasnt running or would output that the data wasn't available or that the files couldn't be read properly. Additionally, combining data into graphs was tough, especially when filtering and aligning the different datasets as the different factors in climate change such as humidity, precipitation and snow, make the graph far too confusing and jumbled. So finally, I chose to focus on just minimum and maximum temperatures because they were easier to interpret and provided clearer insights into climate trends, so hopefully that will suffice for the needs of this project as I was able to visualize historical temperatures and forecasts using meteo’s min and max temperatures in a better visual way. 

Files included in this project.
- API_KEYS.py
	- Handles loading the NOAA API key from a file as I didn’t want the API key to be in the documents I upload on Github. It hides the noaa_api_key.txt
- data_processing.py:
	- Contains the WeatherProcessing class to process NOAA and Meteo data.
- data_visualization.py:
	- this file has the Visualization class to create the graphs needed.
- noaa_data.py:
	- Contains the NoaaData class to fetch NOAA data using the API.
- main.py:
	- used to run the project and process the necessary data I needed to show the graphs. 
- .gitignore:
	- ensures that my api key isn’t gonna be uploaded to my GitHub.
	- noaa_weather_data_30_days.json: This was created to store the NOAA weather data given for up to 30 days.
	- open_meteo_climate_data.csv: This has historical climate data from Open-Meteo’s website.
I also included the original open-meteo file that was provided on the website as i used it to help with setting up some of the code and also to get a better idea of how to handle so much of the data.


Website links: 

- NOAA API: https://www.weather.gov/documentation/services-web-api
- Open-Meteo API: https://open-meteo.com/ 
