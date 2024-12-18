import json
from data_visualization import Visualization
from data_processing import WeatherProcessing

class Weather:
    #my main function which will help to build the project and get it running

    def __init__(self):
        self.visualization = Visualization()
        self.data_processor = WeatherProcessing()

    def open_weather_data(self):
        # process the data from NOAA using the json file which i have saved all the data from the api in - retrieved from the website usign the api key they gave me when i signed up
        try:
            with open("noaa_weather_data_30_days.json", "r") as file:
                noaa_data = json.load(file)
            processed_noaa_data = self.data_processor.process_noaa_data(noaa_data)
            if not processed_noaa_data.empty:
                self.visualization.plot_noaa_data(processed_noaa_data)
        except Exception as e: 
            print(f"Error with NOAA data: {e}")

        # next up is to get the data from the meteo cvs, this one did not require an api key, so the csv file given was used. 
        try:
            self.data_processor.meteo_yearly_averages(
                "open_meteo_climate_data.csv", "open_meteo_yearly_averages.csv"
            )
            self.visualization.plot_meteo_yearly_averages("open_meteo_yearly_averages.csv")
        except Exception as e:
            print(f"Error with Open-Meteo data: {e}")

if __name__ == "__main__":
    #an instance 
    weather_info = Weather()
    weather_info.open_weather_data()
