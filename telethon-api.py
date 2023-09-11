from fastapi import FastAPI
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.types import InputChannel
import os


channel_id=1893146969
access_hash=3728222131404161188
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
proxy = {
    'proxy_type': 'http', # (mandatory) protocol to use (see above)
    'addr': '127.0.0.1',      # (mandatory) proxy IP address
    'port': 8889,           # (mandatory) proxy port number
}

app = FastAPI()

@app.get("/create-topic/{topic_name}")
async def create_topic(topic_name):
    async with TelegramClient('anon', api_id=api_id, api_hash=api_hash, proxy=proxy) as client:
        result = await client(functions.channels.CreateForumTopicRequest(
            channel=InputChannel(channel_id, access_hash),
            title=topic_name
            # icon_color=42,
            # icon_emoji_id=-12398745604826,
        ))
        print(result.updates[0].id)
        return {"Topic ID": result.updates[0].id}