import requests
import json
from datetime import datetime

class RedditMonitor:
    def __init__(self, client_id, client_secret, username, password, subreddit="naturaldisasters"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.subreddit = subreddit
        self.token = None
        self.headers = {
            "User-Agent": f"FatimaDashboard/0.1 by {self.username}"
        }

    def get_token(self):
        auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password
        }
        res = requests.post("https://www.reddit.com/api/v1/access_token",
                            auth=auth, data=data, headers=self.headers)
        if res.status_code == 200 and "access_token" in res.json():
            self.token = res.json()["access_token"]
            self.headers["Authorization"] = f"Bearer {self.token}"
            return True
        return False

    def classify_type(self, text):
        text = text.lower()
        if "earthquake" in text or "quake" in text:
            return "Earthquake"
        elif "flood" in text:
            return "Flood"
        elif "fire" in text or "wildfire" in text:
            return "Fire"
        elif "tornado" in text:
            return "Tornado"
        elif "eruption" in text or "volcano" in text:
            return "Volcano"
        else:
            return "Alert"

    def extract_location(self, text):
        locations = ["Pakistan", "India", "USA", "China", "Taiwan", "Florida", "Japan", "Sicily", "NY", "Kansas"]
        for loc in locations:
            if loc.lower() in text.lower():
                return loc
        return "Unknown"

    def fetch(self, max_posts=250):  # ✅ Now inside the class
        if not self.get_token():
            print("❌ Token fetch failed.")
            return

        all_alerts = []
        after = None

        while len(all_alerts) < max_posts:
            url = f"https://oauth.reddit.com/r/{self.subreddit}/new?limit=250"
            if after:
                url += f"&after={after}"

            res = requests.get(url, headers=self.headers)
            try:
                data = res.json()
            except json.JSONDecodeError:
                print("❌ Failed to parse JSON.")
                break

            posts = data.get("data", {}).get("children", [])
            if not posts:
                break

            for post in posts:
                p = post["data"]
                title = p.get("title", "")
                body = p.get("selftext", "")
                full_text = f"{title} {body}"
                alert = {
                    "timestamp": datetime.utcfromtimestamp(p["created_utc"]).isoformat(),
                    "type": self.classify_type(full_text),
                    "location": self.extract_location(full_text),
                    "description": body.strip() if body.strip() else title.strip()
                }
                all_alerts.append(alert)

            after = data["data"].get("after")
            if not after:
                break

        with open("data/reddit_alerts.json", "w", encoding="utf-8") as f:
            json.dump(all_alerts[:max_posts], f, indent=2)

        print(f"✅ Saved {len(all_alerts)} alerts to data/reddit_alerts.json")
