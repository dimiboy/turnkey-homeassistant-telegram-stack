#!/usr/bin/env python3
"""
Telegram Broadcast Verification Tool
Tests Telegram bot credentials before starting Home Assistant.
"""
import sys
import json
import urllib.request
import urllib.parse

def test_telegram(token, chat_id):
    print("========================================")
    print("Testing Telegram Bot Connection...")
    print("========================================")
    
    url = f"https://api.telegram.org/bot{token}/getMe"
    try:
        req = urllib.request.urlopen(url, timeout=5)
        res = json.loads(req.read().decode())
        if res.get("ok"):
            bot_user = res["result"].get("username")
            print(f"✓ Bot Token Valid: @{bot_user}")
        else:
            print("✗ Token error:", res)
            return False
    except Exception as e:
        print(f"✗ Failed to connect to Telegram API: {e}")
        return False

    # Send test message
    send_url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": "🟢 <b>Test Alert: Home Assistant Sentinel Stack</b>\n\nYour Telegram credentials are fully validated and ready for Home Assistant!",
        "parse_mode": "HTML"
    }).encode()

    try:
        req = urllib.request.Request(send_url, data=payload)
        with urllib.request.urlopen(req, timeout=5) as response:
            result = json.loads(response.read().decode())
            if result.get("ok"):
                print(f"✓ Test message successfully delivered to Chat ID: {chat_id}")
                print("Everything is ready! You can now start docker compose.")
                return True
            else:
                print(f"✗ Failed to deliver message: {result}")
                return False
    except Exception as e:
        print(f"✗ Error sending test message: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        token = input("Enter your Telegram Bot Token: ").strip()
        chat_id = input("Enter your Telegram Chat ID: ").strip()
    else:
        token = sys.argv[1].strip()
        chat_id = sys.argv[2].strip()

    if not token or not chat_id:
        print("Error: Both Bot Token and Chat ID are required.")
        sys.exit(1)

    success = test_telegram(token, chat_id)
    sys.exit(0 if success else 1)
