import os
from flask import Flask
import threading
from telethon import TelegramClient, events

api_id = 15495534
api_hash = 'c25019764e04eced107942a9f359a485'
BOT_TOKEN = '8260517674:AAFbQxxpDuYv4bY_BXv-QnxQuvEJ9Wn7BZY'

SOURCE_CHANNEL = -1003978465701
TARGET_CHANNEL = '@Black_Panther55'

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def forward_message(event):
    try:
        await client.forward_messages(TARGET_CHANNEL, event.message)
        print("संदेश सफलतापूर्वक फॉरवर्ड हो गया।")
    except Exception as e:
        print(f"एरर आ गया: {e}")

app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram Bot is running smoothly!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def main():
    print("बॉट लाइव है...")
    print("नए मैसेज का इंतजार किया जा रहा है...")
    client.run_until_disconnected()

if __name__ == '__main__':
    threading.Thread(target=run_web).start()
    main()
