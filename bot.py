from telethon import TelegramClient, events
from flask import Flask
import threading

# आपकी टेलीग्राम डिटेल्स
api_id = 15495534
api_hash = 'c25019764e04eced107942a9f359a485'

SOURCE_CHANNEL = -1003978465701
TARGET_CHANNEL = '@Black_Panther55'

# टेलीग्राम क्लाइंट
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def forward_message(event):
    try:
        await client.forward_messages(TARGET_CHANNEL, event.message)
        print("संदेश सफलतापूर्वक फॉरवर्ड हो गया।")
    except Exception as e:
        print(f"एरर आ गया: {e}")

def main():
    print("बॉट लाइव है...")
    client.start()
    print("नए मैसेज का इंतजार किया जा रहा है...")
    client.run_until_disconnected()

# Render के लिए नकली वेब सर्वर (ताकि फ्री सर्विस बंद न हो)
app = Flask(_name_)

@app.route('/')
def home():
    print("Bot is running!")
    return "Telegram Bot is running smoothly!"

def run_web():
    app.run(host='0.0.0.0', port=10000)

if _name_ == '_main_':
    threading.Thread(target=run_web).start()
    main()
