import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
csv_filename = "open_meteo_climate_data.csv"
data = pd.read_csv(csv_filename)

# Convert 'date' to a datetime object for better handling
data['date'] = pd.to_datetime(data['date'], errors='coerce')  # Handle invalid dates

# Drop rows with any missing values in relevant columns
data.dropna(subset=['temperature_2m_max', 'temperature_2m_min', 'relative_humidity_2m_max', 'pressure_msl_mean'], inplace=True)

# Display the first few rows to understand the structure
print(data.head())

# Line plot for Temperature (Max and Min), Humidity, and Pressure
plt.figure(figsize=(12, 8))

# Plot Max and Min temperatures
plt.plot(data['date'], data['temperature_2m_max'], label="Max Temperature (°C)", color='red', linewidth=2)
plt.plot(data['date'], data['temperature_2m_min'], label="Min Temperature (°C)", color='blue', linewidth=2)

# Plot Relative Humidity (Max)
plt.plot(data['date'], data['relative_humidity_2m_max'], label="Max Relative Humidity (%)", color='green', linestyle='--', linewidth=2)

# Customize the plot
plt.title("Daily Temperature and Humidity Trends")
plt.xlabel("Date")
plt.ylabel("Temperature (°C) / Humidity (%)")
plt.legend(loc="upper left")
plt.xticks(rotation=45, ha='right')
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()


# Combined Line Plot for Temperature and Pressure
fig, ax1 = plt.subplots(figsize=(12, 6))

# Primary axis for Temperature (Max and Min)
ax1.plot(data['date'], data['temperature_2m_max'], label="Max Temperature (°C)", color='red', linewidth=2)
ax1.plot(data['date'], data['temperature_2m_min'], label="Min Temperature (°C)", color='blue', linewidth=2)
ax1.set_xlabel("Date")
ax1.set_ylabel("Temperature (°C)")
ax1.tick_params(axis='y', labelcolor='black')
ax1.legend(loc="upper left")

# Secondary axis for Pressure
ax2 = ax1.twinx()
ax2.plot(data['date'], data['pressure_msl_mean'], label="Mean Sea-Level Pressure (hPa)", color='purple', linestyle='--', linewidth=2)
ax2.set_ylabel("Pressure (hPa)")
ax2.tick_params(axis='y', labelcolor='purple')
ax2.legend(loc="upper right")

# Title and grid
fig.suptitle("Temperature and Pressure Trends")
fig.tight_layout()

# Show the plot
plt.show()


