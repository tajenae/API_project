import matplotlib.pyplot as plt
import pandas as pd

class Visualization:
    #this class will be used to handle data visualization of my noaa data and the yearly avaerages for the meteo data.

    def plot_noaa_data(self, noaa_data):
        noaa_data[['TMAX', 'TMIN']].plot(title="NOAA Data - min and max temps")
        plt.xlabel("Date")
        plt.ylabel("Temp (°F)")
        plt.show()

    def plot_meteo_yearly_averages(self, meteo_file):
        #i will plot only the averages as the yearly data is way too much to fit on the graph
        meteo_data = pd.read_csv(meteo_file)
        plt.figure(figsize=(12, 6))
        plt.plot(
            meteo_data["year"],
            meteo_data["avg_temperature_max"],
            label="Average Max Temp",
            marker="o",
            linestyle="-",
        )
        plt.plot(
            meteo_data["year"],
            meteo_data["avg_temperature_min"],
            label="Average Min Temp",
            marker="o",
            linestyle="-",
        )
        plt.xlabel("Year")
        plt.ylabel("Temp (°F)")
        plt.title("Open Meteo's Yearly Average Temperatures (1950-2050)")
        plt.legend()
        plt.grid(True)
        plt.show()
