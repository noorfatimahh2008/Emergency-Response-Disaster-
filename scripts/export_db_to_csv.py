# scripts/export_db_to_csv.py

import sqlite3
import pandas as pd
import os

# Ensure output folder exists
os.makedirs("data", exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect("data/disasters.db")

# Read all data from incidents table
df = pd.read_sql_query("SELECT * FROM incidents", conn)

# Save to CSV
df.to_csv("data/incidents.csv", index=False, encoding="utf-8")
print("✅ Exported incidents from DB to data/incidents.csv")


