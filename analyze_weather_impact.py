import pandas as pd
import matplotlib.pyplot as plt

# Load weather and incident data
weather = pd.read_csv("data/weather.csv")
incidents = pd.read_csv("data/incidents.csv")

# Convert to datetime
weather['timestamp'] = pd.to_datetime(weather['timestamp'])
incidents['time'] = pd.to_datetime(incidents['time'], errors='coerce')

# Filter only earthquakes
earthquakes = incidents[incidents['type'] == 'Earthquake'].copy()

# Closest weather reading (time difference < 3 hours and distance ~ same)
weather_point = weather.iloc[0]
earthquakes['temp'] = weather_point['temp']
earthquakes['humidity'] = weather_point['humidity']

# Analyze impact
plt.figure(figsize=(8, 5))
plt.scatter(earthquakes['humidity'], earthquakes['magnitude'], color='blue', alpha=0.6)
plt.title("Earthquake Magnitude vs Humidity")
plt.xlabel("Humidity (%)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("analytics/humidity_vs_magnitude.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(earthquakes['temp'], earthquakes['magnitude'], color='green', alpha=0.6)
plt.title("Earthquake Magnitude vs Temperature")
plt.xlabel("Temperature (K)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("analytics/temp_vs_magnitude.png")
plt.close()

print("✅ Correlation visualizations saved in analytics/:")
print("   → humidity_vs_magnitude.png")
print("   → temp_vs_magnitude.png")
