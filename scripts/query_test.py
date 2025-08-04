import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os

# Allow parent folder imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from db.incident_db import IncidentDB

# Create DB instance
db = IncidentDB()

print("🔍 Querying incidents...\n")

# 🔸 Query by type
incident_type = "Earthquake"
earthquakes = db.query_by_type(incident_type)
print(f"📌 {len(earthquakes)} records found for type = '{incident_type}'\n")
for row in earthquakes[:5]:  # Just show top 5
    print(f"[{row['time']}] {row['location']} (Mag: {row['magnitude']})")

# 🔸 Query by location keyword
keyword = "Japan"
results = db.query_by_location(keyword)
print(f"\n📌 {len(results)} records found with location LIKE '{keyword}'\n")
for row in results[:5]:
    print(f"[{row['time']}] {row['type']} - {row['location']}")

# 🔚 End
print("\n✅ Query test completed.")
