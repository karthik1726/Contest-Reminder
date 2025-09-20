# 📅 Coding Contest WhatsApp Reminder App

A personal reminder application that notifies users of upcoming coding contests via WhatsApp. This app retrieves contest data from **Codeforces** and uses the **Twilio Sandbox** to send personalized reminders directly to the user's WhatsApp.

---

## 🚀 Features

- 🔔 Sends WhatsApp notifications for upcoming Codeforces contests  
- 📡 Fetches real-time contest data using Codeforces public API  
- 💬 Integrates Twilio Sandbox for WhatsApp messaging  
- 🕒 Automates reminders to keep users up-to-date with contest schedules

---

## 🛠️ Tech Stack

- **Backend:** Python / Node.js *(adjust based on your implementation)*  
- **API:** [Codeforces API](https://codeforces.com/apiHelp)  
- **Messaging:** [Twilio WhatsApp Sandbox](https://www.twilio.com/whatsapp)  
- **Scheduler:** Cron / Task Scheduler *(if automation is used)*

---

## ⚙️ How It Works

1. Fetches data about upcoming contests using the Codeforces API  
2. Parses the contest details (name, time, duration, etc.)  
3. Sends the contest details to the user's WhatsApp number via Twilio  
4. Optionally schedules reminders ahead of contest start time

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone [https://github.com/karthik1726/Contest-Reminder.git]
cd coding-contest-reminder
