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

ist = pytz.timezone("Asia/Kolkata")
now = datetime.now(timezone.utc)

for contest in contests:

    # Contest time in UTC
    utc_time = datetime.fromtimestamp(
        contest["startTime"],
        tz=timezone.utc
    )

    # Convert to IST
    ist_time = utc_time.astimezone(ist)

    seconds_left = (utc_time - now).total_seconds()

    # Check reminder windows (10-minute window)
    if 24 * 3600 - 600 <= seconds_left <= 24 * 3600:
        reminder = "⏰ Contest starts in 24 Hours!"
    elif 3600 - 600 <= seconds_left <= 3600:
        reminder = "⏰ Contest starts in 1 Hour!"
    elif 1800 - 600 <= seconds_left <= 1800:
        reminder = "⏰ Contest starts in 30 Minutes!"
    elif 600 - 600 <= seconds_left <= 600:
        reminder = "🚀 Contest starts in 10 Minutes!"
    else:
        print(f"No reminder needed for {contest['title']}.")
        continue

    message = f"""🏆 LeetCode Contest Reminder

{reminder}

📌 {contest['title']}

📅 {ist_time.strftime('%d %b %Y')}
🕗 {ist_time.strftime('%I:%M %p IST')}

🔗 https://leetcode.com/contest/{contest['titleSlug']}

Good luck! 🚀
"""

    telegram_response = requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=20
    )

    telegram_response.raise_for_status()

    print(f"Reminder sent for {contest['title']}!")
