# 🌍 Emergency Response & Disaster Data Fetchers (Week 1)

This project collects real-time data from multiple sources related to natural disasters and stores the raw information in JSON and CSV formats for further analysis and visualization.

## ✅ Purpose

To build a modular, extensible system for fetching disaster-related data that can be used in an Emergency Response & Disaster Dashboard.

## 📦 Project Structure


## 📊 Data Sources

### 1. USGS Earthquake API
- **URL:** https://earthquake.usgs.gov/fdsnws/event/1/
- **Data:** Earthquakes with magnitude ≥ 3.0 since Jan 1, 2024
- **Output:** `data/earthquakes.json`

### 2. OpenWeatherMap API
- **URL:** https://openweathermap.org/api
- **Data:** Weather information for a specific location (default: Karachi)
- **Output:** `data/weather.json`

### 3. Reddit API
- **Subreddit:** `r/naturaldisasters`
- **Authentication:** Reddit OAuth2
- **Data:** Top 10 recent posts with alerts
- **Outputs:**
  - `data/reddit_alerts.json`
  - `data/reddit_alerts.csv`

## 📁 Output Files

All data is saved in the `data/` folder:

- `earthquakes.json`
- `weather.json`
- `reddit_alerts.json`
- `reddit_alerts.csv`

## 🧠 Features

- Clean, modular code using OOP
- Uses OAuth2 authentication for Reddit
- Extracts and stores: timestamps, location, severity, and descriptions
- Logs fetch counts and last update times

## 🚀 How to Run

```bash
python main.py

---

Ab is file ko **README.md** ke naam se project ke root folder me rakh lo.

Tayyar ho to bolo — **Week 2 ka roadmap bhej dun?** 📊📂
