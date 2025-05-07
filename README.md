# 📦 Unzip Telegram Bot

A fast and simple Telegram bot that lets users send `.zip` or `.rar` files and automatically receive the extracted content right in the chat.

---

## ✨ Features

- ✅ Accepts `.zip` and `.rar` files
- 📂 Automatically extracts files and sends them back
- 🔐 Keeps your bot token secure via `.env` and environment variables
- 🚀 Deployable to platforms like [Render](https://render.com), AWS, or any cloud VM
- 🧠 Built with `python-telegram-bot` (v20+)

---

## 📁 Project Structure
unzip_telegram_bot/
├── main.py             # Entry point of the bot
├── requirements.txt    # Dependencies
├── Procfile            # For Render deployment
├── .env                # Contains your TELEGRAM_TOKEN (add to .gitignore!)
├── .gitignore          # Excludes .env and cache folders
├── downloads/          # Temporary folder for received files
└── extracted/          # Folder for unzipped contents

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/yourusername/unzip_telegram_bot.git
cd unzip_telegram_bot

🔑 2. Create .env File
echo "TELEGRAM_TOKEN=your_telegram_bot_token_here" > .env

📦 3. Install Dependencies
pip install -r requirements.txt

python main.py
