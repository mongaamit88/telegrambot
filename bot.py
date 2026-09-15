from telethon import TelegramClient, events

api_id = 35065334
api_hash = 'c250107a46a4aced107942a9f350af85'

SOURCE_CHANNEL = -1003978465701  
TARGET_CHANNEL = '@Black_Panther55'  

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def forward_message(event):
    try:
        await client.forward_messages(TARGET_CHANNEL, event.message)
        print("मैसेज सफलतापर्वूक फॉरवर्ड हो गया!")
    except Exception as e:
        print(f"एरर आ गया: {e}")

def main():
    print("बॉट लाइव है...")
    client.start()
    print("नए मैसेज का इंतज़ार किया जा रहा है...")
    client.run_until_disconnected()

main()
