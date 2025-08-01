import json
import csv
from datetime import datetime

# Load JSON
with open("data/weather.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract relevant fields
timestamp = datetime.utcfromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S")
lat = data["coord"]["lat"]
lon = data["coord"]["lon"]
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
weather_main = data["weather"][0]["main"]
weather_description = data["weather"][0]["description"]

# CSV file path
csv_file = "data/weather.csv"

# Write header + row
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "lat", "lon", "temp", "humidity", "weather_main", "weather_description"])
    writer.writerow([timestamp, lat, lon, temp, humidity, weather_main, weather_description])

print("✅ weather.json converted to data/weather.csv")
