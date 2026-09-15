import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = int(os.environ.get("API_ID", 35065334))
API_HASH = os.environ.get("API_HASH", "c250107a46a4aced107942a9f350af85")
SESSION_STRING = os.environ.get("SESSION_STRING")

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    print("बॉट शुरू हो रहा है...")
    me = await client.get_me()
    print(f"सफलतापूर्वक लॉगिन हो गया! यूजर का नाम: {me.first_name}")
    
    # यह लूप बोट को हमेशा ऑनलाइन रखेगा और बंद नहीं होने देगा
    print("बॉट अब एक्टिव है और लगातार चल रहा है...")
    while True:
        await asyncio.sleep(3600)

with client:
    client.loop.run_until_complete(main())
