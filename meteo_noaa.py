import pandas as pd
import json

# File path (use full path if needed)
file_path = "noaa_weather_data_7_days.json"

try:
    # Load NOAA data
    with open(file_path, "r") as file:
        noaa_raw_data = json.load(file)

    # Convert to DataFrame
    noaa_data = pd.DataFrame(noaa_raw_data)

    # Ensure 'date' column is in datetime format
    noaa_data['date'] = pd.to_datetime(noaa_data['date'])

    # Show the NOAA data for inspection
    print("NOAA Data:")
    print(noaa_data.head())

except FileNotFoundError:
    print(f"The file {file_path} was not found. Please verify its location.")
except ValueError as e:
    print("Error parsing the NOAA JSON file. Check its content and structure.")
    print(e)

# If the file is successfully loaded, continue with your data processing...
# Assuming you have the Open-Meteo data already in 'daily_dataframe'
# Example visualization or processing steps:
if 'noaa_data' in locals():
    # Merge NOAA data with Open-Meteo data (assuming 'daily_dataframe' exists)
    merged_data = pd.merge(daily_dataframe, noaa_data, on='date', how='inner')

    # Display merged data
    print("Merged Data:")
    print(merged_data)

    # Visualization example (temperature comparison)
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(merged_data['date'], merged_data['temperature_2m_max'], label="Open-Meteo Max Temp (°C)", color='blue')
    plt.plot(merged_data['date'], merged_data['temperature_2m_min'], label="Open-Meteo Min Temp (°C)", color='red')
    plt.plot(merged_data['date'], merged_data['value'][merged_data['datatype'] == 'TMAX'], label="NOAA Max Temp (°C)", color='green', linestyle='--')
    plt.plot(merged_data['date'], merged_data['value'][merged_data['datatype'] == 'TMIN'], label="NOAA Min Temp (°C)", color='orange', linestyle='--')

    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Comparison: Open-Meteo vs NOAA')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#this will plot historical data needed for analysis.