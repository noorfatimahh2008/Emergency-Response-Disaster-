import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime
import os
import unicodedata

# Load incident data from DB (or previously exported CSV)
df = pd.read_csv("data/incidents.csv")  # Make sure this CSV is available

# Filter out missing times
df = df[df['time'].notna()]
df['time'] = pd.to_datetime(df['time'], errors='coerce')

# Most frequent locations
def clean_text(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

top_locations = df['location'].value_counts().head(10)

# Weekly trend
df['week'] = df['time'].dt.to_period('W').astype(str)
weekly_trend = df.groupby('week').size()

# Save weekly trend plot
plt.figure(figsize=(10, 5))
weekly_trend.plot(kind='line', marker='o')
plt.title("Weekly Disaster Trends")
plt.xlabel("Week")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("analytics/event_trends.png")
plt.close()

# ---------------- PDF GENERATION -------------------
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Emergency Incident Summary Report", ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", '', 12)

# Date Range
start_date = df['time'].min().strftime("%d %b %Y")
end_date = df['time'].max().strftime("%d %b %Y")
pdf.cell(0, 10, f"Date Range: {start_date} to {end_date}", ln=True)
pdf.ln(5)

# Top Locations
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Top 10 Frequent Locations:", ln=True)
pdf.set_font("Arial", '', 12)
for loc, count in top_locations.items():
    clean_loc = clean_text(loc)
    pdf.cell(0, 8, f"{clean_loc}: {count} incidents", ln=True)

# Map file mention (not embedding HTML)
pdf.ln(10)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, "Scatter Map: See scatter_map.html", ln=True)
pdf.cell(0, 10, "Heatmap: See hotspot_map.html", ln=True)

# Add correlation plot
pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Weather vs Earthquake Magnitude Correlation:", ln=True)
pdf.image("analytics/weather_earthquake_correlation.png", x=15, w=180)

# Save PDF
output_path = "analytics/summary_report.pdf"
pdf.output(output_path)
print(f"✅ PDF report saved at: {output_path}")

