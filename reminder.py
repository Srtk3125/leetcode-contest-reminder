import os
import requests
from datetime import datetime, timezone

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

GRAPHQL_URL = "https://leetcode.com/graphql"

query = """
query {
  upcomingContests {
    title
    titleSlug
    startTime
  }
}
"""

try:
    response = requests.post(
        GRAPHQL_URL,
        json={"query": query},
        timeout=20
    )
    data = response.json()

    contests = data.get("data", {}).get("upcomingContests", [])

    if not contests:
        print("No upcoming contests found.")
        exit(0)

    contest = contests[0]

    start = datetime.fromtimestamp(contest["startTime"], tz=timezone.utc)
    message = (
        "🏆 Upcoming LeetCode Contest\n\n"
        f"📌 {contest['title']}\n"
        f"🕒 UTC Time: {start.strftime('%Y-%m-%d %H:%M UTC')}\n\n"
        f"🔗 https://leetcode.com/contest/{contest['titleSlug']}"
    )

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=20
    )

    print("Telegram message sent!")

except Exception as e:
    print(e)
