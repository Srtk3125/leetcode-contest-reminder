import os
import requests
from datetime import datetime, timezone
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

# Fetch upcoming contests
response = requests.post(
    GRAPHQL_URL,
    json={"query": QUERY},
    timeout=20
)

response.raise_for_status()

data = response.json()
contests = data.get("data", {}).get("upcomingContests", [])

if not contests:
    print("No upcoming contests found.")
    exit()

contest = contests[0]

# Contest time in UTC
utc_time = datetime.fromtimestamp(
    contest["startTime"],
    tz=timezone.utc
)

# Convert to IST
ist = pytz.timezone("Asia/Kolkata")
ist_time = utc_time.astimezone(ist)

# Current time
now = datetime.now(timezone.utc)

seconds_left = (utc_time - now).total_seconds()

# Reminder windows (±60 seconds)
if not (
    86340 <= seconds_left <= 86460 or   # 24 hours
    3540 <= seconds_left <= 3660 or     # 1 hour
    1740 <= seconds_left <= 1860 or     # 30 minutes
    540 <= seconds_left <= 660          # 10 minutes
):
    print("No reminder needed now.")
    exit()

# Reminder text
if 86340 <= seconds_left <= 86460:
    reminder = "⏰ Contest starts in 24 Hours!"
elif 3540 <= seconds_left <= 3660:
    reminder = "⏰ Contest starts in 1 Hour!"
elif 1740 <= seconds_left <= 1860:
    reminder = "⏰ Contest starts in 30 Minutes!"
else:
    reminder = "🚀 Contest starts in 10 Minutes!"

# Telegram message
message = f"""🏆 LeetCode Contest Reminder

{reminder}

📌 {contest['title']}

📅 {ist_time.strftime('%d %b %Y')}
🕗 {ist_time.strftime('%I:%M %p IST')}

🔗 https://leetcode.com/contest/{contest['titleSlug']}

Good luck! 🚀
"""

# Send message
response = requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": message
    },
    timeout=20
)

response.raise_for_status()

print("Telegram message sent successfully!")
