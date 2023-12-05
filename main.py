from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.types import InputChannel, User, MessageMediaDocument, MessageMediaPhoto

import datetime as dt
import gspread
import json
import os
from dotenv import load_dotenv

from logs import logger

load_dotenv()

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
proxy = {
    'proxy_type': 'http', # (mandatory) protocol to use (see above)
    'addr': '127.0.0.1',      # (mandatory) proxy IP address
    'port': 8889,           # (mandatory) proxy port number
}

def update_sheet(chats:list[dict], date: dt.datetime):
    worksheet = gspread.service_account(".gspread/sheet.json").open("Nabaat Admin History")
    sheet = worksheet.worksheet("chat history")
    logger.info("Connected to google sheet.")
    new_rows = []
    max_cell_length = 45000
    for chat in chats:
        name: str = list(chat.keys())[0]
        message_history = "\n".join(chat[name])
        row = [date.strftime("%Y-%m-%d"), name]
        _ = [row.append(message_history[i:i+max_cell_length]) for i in range(0, len(message_history), max_cell_length)]
        new_rows.append(row)
    logger.info(f"{len(new_rows)} rows to be added...")
    sheet.insert_rows(values=new_rows, row=2)
    

if __name__=="__main__":
    with TelegramClient('anon', api_id=api_id, api_hash=api_hash, proxy=proxy) as client:
        client.takeout(users=True)
        MESSAGE_OFFSET = dt.date.today() - dt.timedelta(days=31)
        DIALOG_OFFSET = dt.datetime.utcnow().replace(tzinfo=None) - dt.timedelta(days=31)
        dialogs = client.get_dialogs()
        chats: list[dict] = []
        for dialog in dialogs:
            if isinstance(dialog.entity, User):
                if dialog.date.replace(tzinfo=None) >= DIALOG_OFFSET:
                    # print('{}: {}'.format(dialog.id, dialog.title))
                    if not dialog.entity.bot and dialog.name != "NabaatAdmin" and dialog.name != "Telegram":
                        messages = []
                        logger.info(f"{dialog.name}: {dialog.date}")
                        for message in client.iter_messages(dialog.entity, reverse=True, offset_date=MESSAGE_OFFSET):
                            if message.from_id: sender = "نبات‌ادمین" 
                            else: sender = "مشتری"
                            if isinstance(message.media, MessageMediaPhoto):
                                messages.append(f"{sender}: ارسال عکس")
                            if isinstance(message.media, MessageMediaDocument):
                                messages.append(f"{sender}: ارسال سند")
                            elif message.message:
                                messages.append(f"{sender}: {message.message}")
                        if messages:
                            chats.append({dialog.name: messages})
        
    update_sheet(chats=chats, date=dt.datetime.today())
    # print(out[0])
# with open("out.json", "w", encoding="utf-8") as f:
#     f.write(json.dumps(out, indent=2, ensure_ascii=False))
        
