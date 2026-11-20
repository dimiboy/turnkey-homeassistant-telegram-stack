# 🚀 Quick Start Guide: 1-Click Home Assistant & Telegram Alert Stack

Get production-grade Home Assistant uptime & health alerts in Telegram in under 3 minutes.

---

## 📋 Prerequisites
- A machine running Docker & Docker Compose (Linux, Raspberry Pi, macOS, Windows WSL2).
- A Telegram account and a Telegram Bot (created in 60s via `@BotFather`).
- Your Telegram numerical Chat ID (obtained in 5s via `@userinfobot`).

---

## ⚡ 3-Step Setup

### Step 1: Extract & Configure Secrets
1. Copy `config/secrets.yaml.example` to `config/secrets.yaml`:
   ```bash
   cp config/secrets.yaml.example config/secrets.yaml
   ```
2. Open `config/secrets.yaml` and set your credentials:
   ```yaml
   telegram_bot_token: "123456789:ABCdefGHIjklMNOpqrsTUVwxyz"
   telegram_chat_id: 123456789
   TIMEZONE: "Asia/Jerusalem"  # Or your local timezone
   ```

### Step 2: Validate Credentials (Optional but Recommended)
Run the pre-flight verification script to confirm your bot credentials before launching:
```bash
python3 test_telegram_broadcast.py "<YOUR_BOT_TOKEN>" "<YOUR_CHAT_ID>"
```
You should instantly receive a confirmation message in Telegram.

### Step 3: Launch the Stack
```bash
docker compose up -d
```
That's it! Home Assistant will start up, arm all monitoring automations, and send you a **"🟢 Home Sentinel Online"** message.

---

## 🛠️ Key Architectural Details

- **Why Broadcast Mode?**
  Unlike polling mode, `platform: broadcast` does not issue continuous `getUpdates` requests. This prevents `409 Conflict: terminated by other getUpdates request` if you use the same bot token across multiple automations or webhooks.
- **Resource Debouncing:**
  CPU and RAM alerts require sustained threshold breach (>85% for 3 continuous minutes) before firing, preventing annoying false alarms from momentary spikes.
- **Ping WAN Watchdog:**
  Monitors Internet stability using Cloudflare DNS (`1.1.1.1`) and alerts you when connections drop and recover.
