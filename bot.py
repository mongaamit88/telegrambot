import os
from telethon import TelegramClient
from telethon.sessions import StringSession

# Render से आपकी API डिटेल्स और सेशन स्ट्रिंग खुद ले लेगा
API_ID = int(os.environ.get("API_ID", 35065334))
API_HASH = os.environ.get("API_HASH", "c250107a46a4aced107942a9f350af85")
SESSION_STRING = os.environ.get("SESSION_STRING")

# सेशन स्ट्रिंग के साथ क्लाइंट तैयार करना (ताकि दोबारा मोबाइल नंबर न मांगें)
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    print("बॉट शुरू हो रहा है...")
    me = await client.get_me()
    print(f"सफलतापूर्वक लॉगिन हो गया! यूजर का नाम: {me.first_name}")

with client:
    client.loop.run_until_complete(main())
