import os
import requests
from flask import Flask
import threading
import time

BOT_TOKEN = '8260517674:AAFbQxxpDuYv4bY_BXv-QnxQuvEJ9Wn7BZY'
TARGET_CHANNEL = '@Black_Panther55'

app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram Bot is running smoothly!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def forward_loop():
    print("बॉट शुरू हो गया है और मैसेज चेक कर रहा है...")
    last_update_id = 0
    
    while True:
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={last_update_id + 1}&timeout=30"
            response = requests.get(url, timeout=35)
            data = response.json()
            
            if data.get("ok"):
                for result in data.get("result", []):
                    last_update_id = result["update_id"]
                    
                    message = result.get("channel_post") or result.get("message")
                    if message:
                        text = message.get("text", "")
                        
                        if text:
                            send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                            payload = {
                                "chat_id": TARGET_CHANNEL,
                                "text": text
                            }
                            requests.post(send_url, json=payload)
                            print("संदेश सफलतापूर्वक फॉरवर्ड कर दिया गया!")
                            
        except Exception as e:
            print(f"एरर: {e}")
            time.sleep(5)

if __name__ == '__main__':
    threading.Thread(target=run_web).start()
    forward_loop()
