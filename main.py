from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.types import InputChannel
import datetime
import os

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
proxy = {
    'proxy_type': 'http', # (mandatory) protocol to use (see above)
    'addr': '127.0.0.1',      # (mandatory) proxy IP address
    'port': 8889,           # (mandatory) proxy port number
}


# with TelegramClient('anon', api_id=api_id, api_hash=api_hash, proxy=proxy) as client:
#     result = client(functions.channels.CreateChannelRequest(
#         title='Nabaat Questions',
#         about='User\'s questions will appear here',
#         megagroup=True,
#         forum=True
#     ))
#     print(f"chat ID: {result.chats[0].id}")
#     print(f"chat access hash: {result.chats[0].access_hash}")
#     channel_id = result.chats[0].id
#     access_hash = result.chats[0].access_hash
#     with open('create-group.txt', 'w') as f:
#         f.write(result.stringify())

# with TelegramClient('anon', api_id=api_id, api_hash=api_hash, proxy=proxy) as client:
#     result = client.get_input_entity(-1940192438)
#     print(result.stringify())

channel_id=1893146969
access_hash=3728222131404161188


with TelegramClient('anon', api_id=api_id, api_hash=api_hash, proxy=proxy) as client:
    result = client(functions.channels.CreateForumTopicRequest(
        channel=InputChannel(channel_id, access_hash),
        title='getting ID (new)'
        # icon_color=42,
        # icon_emoji_id=-12398745604826,
    ))
    print(result.stringify())
    print(result.updates[0].id)
    with open('create-topic.txt', 'w') as f:
        f.write(result.stringify())

# with TelegramClient('anon', api_id=api_id, api_hash=api_hash, proxy=proxy) as client:
#     result = client(functions.channels.GetForumTopicsRequest(
#         channel=InputChannel(channel_id, access_hash),
#         offset_date=datetime.datetime(2018, 6, 25),
#         offset_id=0,
#         offset_topic=0,
#         limit=100,
#         # q='some string here'
#     ))
#     print(result.stringify())
#     with open('get-topics.txt', 'w') as f:
#         f.write(result.stringify())

# with TelegramClient('anon', api_id=api_id, api_hash=api_hash, proxy=proxy) as client:
#     result = client(functions.channels.GetForumTopicsByIDRequest(
#         channel=InputChannel(channel_id, access_hash),
#         topics=[1]
#     ))
#     print(result.stringify())
#     with open('get-topics-by-id.txt', 'w') as f:
#         f.write(result.stringify())