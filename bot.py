import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from flask import Flask

# 1. Flask सर्वर ताकि Render का पोर्ट वाला चक्कर खत्म हो जाए
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

# 2. Telegram Bot की डिटेल्स
API_ID = int(os.environ.get("API_ID", 35065334))
API_HASH = os.environ.get("API_HASH", "c250107a46a4aced107942a9f350af85")
SESSION_STRING = os.environ.get("SESSION_STRING")

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    print("बॉट शुरू हो रहा है...")
    me = await client.get_me()
    print(f"सफलतापूर्वक लॉगिन हो गया! यूजर का नाम: {me.first_name}")
    
    print("बॉट अब एक्टिव है और लगातार चल रहा है...")
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    # Flask को बैकग्राउंड में चलाना
    import threading
    t = threading.Thread(target=run_flask)
    t.start()
    
    # Telegram Client को चलाना
    with client:
        client.loop.run_until_complete(main()
