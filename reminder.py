print("VERSION 2 - NEW CODE")
import os
import requests
from datetime import datetime
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query {
  upcomingContests {
    title
    titleSlug
    startTime
  }
}
"""

response = requests.post(
    GRAPHQL_URL,
    json={"query": QUERY},
    timeout=20
)

data = response.json()

contests = data.get("data", {}).get("upcomingContests", [])

if not contests:
    print("No upcoming contests found.")
    exit()

contest = contests[0]

utc_time = datetime.utcfromtimestamp(contest["startTime"])
ist = pytz.timezone("Asia/Kolkata")
ist_time = pytz.utc.localize(utc_time).astimezone(ist)

message = f"""
🏆 LeetCode Contest

📌 {contest['title']}

📅 {ist_time.strftime('%d %b %Y')}
🕗 {ist_time.strftime('%I:%M %p IST')}

🔗 https://leetcode.com/contest/{contest['titleSlug']}
"""

requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": message
    },
    timeout=20
)

print("Telegram message sent successfully!")
