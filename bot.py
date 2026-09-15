import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from flask import Flask
import threading

# 1. Flask सर्वर ताकि Render पर पोर्ट की दिक्कत न आए
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

# 2. आपकी Telegram API डिटेल्स
API_ID = int(os.environ.get("API_ID", 35065334))
API_HASH = os.environ.get("API_HASH", "c250107a46a4aced107942a9f350af85")
SESSION_STRING = os.environ.get("SESSION_STRING")

# 3. आपकी सही चैट आईडी और ग्रुप यूजरनेम
SOURCE_CHAT = -1003978465701     # इस ग्रुप से मैसेज लिए जाएंगे
DESTINATION_CHAT = '@Black_Panther55' # इस ग्रुप में मैसेज भेजे जाएंगे

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

# मैसेज फॉरवर्ड करने का असली लॉजिक
@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def forward_message(event):
    try:
        await client.forward_messages(DESTINATION_CHAT, event.message)
        print("मैसेज सफलतापूर्वक फॉरवर्ड हो गया!")
    except Exception as e:
        print(f"फॉरवर्ड करने में एरर आया: {e}")

async def main():
    print("ऑटो-फॉरवर्डर बोट पूरी तरह चालू हो गया है और मैसेज का इंतज़ार कर रहा है...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    # Flask को बैकग्राउंड में चलाना
    t = threading.Thread(target=run_flask)
    t.start()
    
    # Telegram Client को चलाना
    client.start()
    client.loop.run_until_complete(main())
