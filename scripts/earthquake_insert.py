import sys
import os
import json
from datetime import datetime

# Allow module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.incident import Incident
from db.incident_db import IncidentDB

# Create DB connection
db = IncidentDB()

# Load earthquake data
with open("data/earthquakes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

earthquakes = data["features"]

for eq in earthquakes:
    props = eq["properties"]
    coords = eq["geometry"]["coordinates"]

    # Normalize fields
    lat = float(coords[1])
    lng = float(coords[0])
    magnitude = props.get("mag")
    location = props.get("place", "Unknown")
    time = datetime.utcfromtimestamp(props["time"] / 1000).isoformat() + "Z"
    source = "Earthquake"
    incident_type = "Earthquake"

    # ❌ DO NOT pass `id=` to Incident — it's auto-handled by SQLite
    incident = Incident(
        type=incident_type,
        lat=lat,
        lng=lng,
        magnitude=magnitude,
        location=location,
        time=time,
        source=source
    )

    # ✅ Insert into DB
    db.insert_incident(incident)

print("✅ Earthquake data inserted into disasters.db")
