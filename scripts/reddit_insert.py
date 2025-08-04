import sys
import os
import json
from time import sleep
from geopy.geocoders import Nominatim

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.incident import Incident
from db.incident_db import IncidentDB

# Initialize database and geolocator
db = IncidentDB()
geolocator = Nominatim(user_agent="FatimaDashboard")

def get_coordinates(location):
    try:
        loc = geolocator.geocode(location, timeout=10)
        if loc:
            return loc.latitude, loc.longitude
    except Exception as e:
        print(f"❌ Geocoding failed for {location}: {e}")
    return None, None

# Load Reddit alerts
with open("data/reddit_alerts.json", "r", encoding="utf-8") as f:
    reddit_data = json.load(f)

# Insert each alert with lat/lng
for alert in reddit_data:
    lat, lng = get_coordinates(alert["location"])
    sleep(1)  # avoid rate limiting

    incident = Incident(
        type=alert["type"],
        lat=lat,
        lng=lng,
        magnitude=None,
        location=alert["location"],
        time=alert["timestamp"],
        source="Reddit"
    )
    db.insert_incident(incident)

print("✅ Reddit data inserted into disasters.db with lat/lng")
