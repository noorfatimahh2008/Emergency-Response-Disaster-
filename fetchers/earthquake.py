import requests
import json
from datetime import datetime

class EarthquakeDataFetcher:
    def __init__(self):
        self.url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
        self.params = {
            "format": "geojson",
            "starttime": "2024-01-01",
            "endtime": datetime.utcnow().strftime("%Y-%m-%d"),
            "minmagnitude": 3.0,
            "limit": 250
        }

    def fetch(self):
        response = requests.get(self.url, params=self.params)
        data = response.json()
        with open("data/earthquakes.json", "w") as f:
            json.dump(data, f, indent=2)
        print(f"[Earthquake] ✅ Fetched {len(data['features'])} entries at {datetime.utcnow()}")
