import requests
import json
from datetime import datetime

class WeatherDataFetcher:
    def __init__(self, api_key, city="Karachi"):
        self.api_key = api_key
        self.city = city

    def fetch(self):
        url=f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={self.api_key}"
        response = requests.get(url)
        data = response.json()
        with open("data/weather.json", "w") as f:
            json.dump(data, f, indent=2)
        print(f"[Weather] ✅ Fetched weather for {self.city} at {datetime.utcnow()}")
