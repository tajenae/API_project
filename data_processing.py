import pandas as pd

class WeatherProcessing:
    #class to process the NOAA and Meteo weather data needed

    def process_noaa_data(self, data):
        #Process NOAA data and return a formatted dataframe.
        try:
            noaa_data = pd.DataFrame(data)
            noaa_data["date"] = pd.to_datetime(noaa_data["date"])
            noaa_data = noaa_data.pivot(index="date", columns="datatype", values="value")
            
            #focusing on temperature highs and lows 
            noaa_data.columns = ["PRCP","TMAX", "TMIN"]
            #As the temperature was not given in Fahrenheits, i used the formular to do so that way i could properly undertsnad the data.
            noaa_data["TMAX"] = (noaa_data["TMAX"] / 10) * 9 / 5 + 32  
            noaa_data["TMIN"] = (noaa_data["TMIN"] / 10) * 9 / 5 + 32  
            return noaa_data
        #erros message if the code was invalid, just incase the data wasnt fetched properly
        except KeyError:
            print("error processing NOAA data.")
            return pd.DataFrame()
        
    #used this function because the dataset was way too large and it was causing a lot of lagging issues when i ran it and 
    #it had the years all jumbled up on the axis because of how much data was being added to the graph. 
    #the yearly avaerage, still gave a pretty accurate figure while keeping the graph easy to understand for me.
    def meteo_yearly_averages(self, input_file, output_file):
        
        try:
            print(f"Reading from {input_file}...")
            data = pd.read_csv(input_file)
            if not {"temperature_2m_max", "temperature_2m_min", "date"}.issubset(data.columns):
                raise KeyError("Required columns: 'temperature_2m_max', 'temperature_2m_min', or 'date'.")
            #column titles needed from the csv file - min and max temperatures

            data['date'] = pd.to_datetime(data['date'])
            data['year'] = data['date'].dt.year

            # Similarly to what i did for noaa, i will also have to convert meteo's data to Fahrenheit
            data['temperature_2m_max'] = data['temperature_2m_max'] * 1.8 + 32
            data['temperature_2m_min'] = data['temperature_2m_min'] * 1.8 + 32

            yearly_averages = data.groupby("year").agg({
                "temperature_2m_max": "mean",
                "temperature_2m_min": "mean"
            }).reset_index()
            #use average temperature min and max to replace '2m' which was what was used on the meteo website 
            yearly_averages.rename(columns={
                "temperature_2m_max": "avg_temperature_max",
                "temperature_2m_min": "avg_temperature_min"
            }, inplace=True)

            #save this new data to a new file called open_meteo_yearly_averages.csv so as to not confuse the new 
            #calculations with the original csv.
            yearly_averages.to_csv(output_file, index=False)
            print(f"meteo's yearly averages saved to {output_file}")
        except FileNotFoundError:
            print(f"Error: file {input_file} not found.")
        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
