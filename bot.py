import os
from telethon import TelegramClient, events
from flask import Flask

# 1. आपकी डिटेल्स और सेटिंग्स
API_ID = 35065334
API_HASH = 'c250107a46a4aced107942a9f350af85'
SOURCE_CHAT_ID = -1003978465701
TARGET_CHANNEL = '@Black_Panther55'

# 2. Render के लिए हल्का सा वेब सर्वर (ताकि क्लाउड इसे बंद न करे)
app = Flask(__name__)

@app.route('/')
def home():
    return "Userbot is running!"

# 3. टेलीथॉन क्लाइंट सेटअप
client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def forward_message(event):
    try:
        await client.forward_messages(TARGET_CHANNEL, event.message)
        print("मैसेज सफलतापूर्वक फॉरवर्ड हो गया!")
    except Exception as e:
        print(f"एरर: {e}")

if __name__ == '__main__':
    # वेब सर्वर को बैकग्राउंड में चलाने के लिए पोर्ट सेट करना
    port = int(os.environ.get('PORT', 5000))
    
    # टेलीग्राम क्लाइंट स्टार्ट करना
    print("यूजरबोट शुरू हो रहा है...")
    client.start()
    
    # ऐप को रन करना
    app.run(host='0.0.0.0', port=port)
