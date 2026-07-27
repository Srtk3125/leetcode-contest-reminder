# 🚀 LeetCode Contest Reminder Bot

Automatically receive **Telegram reminders** for upcoming **LeetCode Weekly and Biweekly Contests** using **Python** and **GitHub Actions**.

## ✨ Features

- 🏆 Monitors upcoming LeetCode contests
- 📅 Supports Weekly and Biweekly contests
- ⏰ Sends reminders:
  - 24 hours before
  - 1 hour before
  - 30 minutes before
  - 10 minutes before
- 🇮🇳 Displays contest time in IST (Indian Standard Time)
- 🔗 Includes the contest link
- 🤖 Runs automatically every 10 minutes using GitHub Actions
- 📩 Sends notifications directly to Telegram

---

## 🛠️ Tech Stack

- Python 3.12
- GitHub Actions
- Telegram Bot API
- LeetCode GraphQL API
- Requests
- pytz

---

## 📂 Project Structure

```text
leetcode-contest-reminder/
│
├── .github/
│   └── workflows/
│       └── reminder.yml
├── reminder.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Srtk3125/leetcode-contest-reminder.git
cd leetcode-contest-reminder
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a Telegram Bot

- Open Telegram
- Search for **@BotFather**
- Create a new bot using `/newbot`
- Copy your Bot Token

### 4. Get Your Chat ID

Send any message to your bot and open:

```
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
```

Copy the value of `chat.id`.

### 5. Add GitHub Secrets

Go to your GitHub repository:

**Settings → Secrets and variables → Actions**

Create these repository secrets:

| Name | Value |
|------|-------|
| BOT_TOKEN | Your Telegram Bot Token |
| CHAT_ID | Your Telegram Chat ID |

---

## ▶️ How It Works

1. GitHub Actions runs automatically every **10 minutes**.
2. The bot fetches all upcoming LeetCode contests.
3. It checks whether any contest starts in:
   - 24 hours
   - 1 hour
   - 30 minutes
   - 10 minutes
4. If a reminder is due, it sends a Telegram notification.
5. Otherwise, it exits without sending a message.

---

## 📷 Sample Notification

```text
🏆 LeetCode Contest Reminder

⏰ Contest starts in 1 Hour!

📌 Weekly Contest 513

📅 02 Aug 2026
🕗 08:00 PM IST

🔗 https://leetcode.com/contest/weekly-contest-513

Good luck! 🚀
```

---

## 📌 Future Improvements

- Prevent duplicate reminders
- Support multiple time zones
- Daily Challenge reminders
- Contest result notifications
- Docker support

---

## 🤝 Contributing

Contributions, issues, and suggestions are welcome.

Feel free to fork the repository and submit a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Sarthak Hole**

GitHub: https://github.com/Srtk3125

If you found this project useful, consider giving it a ⭐ on GitHub!
