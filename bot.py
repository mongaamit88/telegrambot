import os
from telethon import TelegramClient, events

# आपकी दी गई डिटेल्स
API_ID = 35065334
API_HASH = 'c250107a46a4aced107942a9f350af85'

# सोर्स ग्रुप और टारगेट चैनल
SOURCE_CHAT_ID = -1003978465701
TARGET_CHANNEL = '@Black_Panther55'

# क्लाइंट सेटअप
client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def forward_message(event):
    try:
        # मैसेज को सीधे टारगेट चैनल पर फॉरवर्ड करना
        await client.forward_messages(TARGET_CHANNEL, event.message)
        print("मैसेज सफलतापूर्वक फॉरवर्ड हो गया!")
    except Exception as e:
        print(f"एरर: {e}")

if __name__ == '__main__':
    print("यूजरबोट शुरू हो रहा है...")
    client.start()
    client.run_until_disconnected()
