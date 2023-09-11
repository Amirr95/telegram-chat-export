import asyncio
import logging
from logging.handlers import RotatingFileHandler
from telegram.ext import (
    ContextTypes,
    ApplicationBuilder
)
from telegram.error import NetworkError
from telethon import TelegramClient
import os
import requests
import aiohttp


api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
proxy = {
    'proxy_type': 'http', # (mandatory) protocol to use (see above)
    'addr': '127.0.0.1',      # (mandatory) proxy IP address
    'port': 8889,           # (mandatory) proxy port number
}
proxy_url = 'http://127.0.0.1:8889'
TOKEN = os.environ["AGRIWEATHBOT_TOKEN"]

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    level=logging.INFO,
    handlers=[
        RotatingFileHandler(
            "bot_logs.log", maxBytes=512000, backupCount=5
        ),  # File handler to write logs to a file
        logging.StreamHandler(),  # Stream handler to display logs in the console
    ],
)
logger = logging.getLogger("agriWeather-bot")
logging.getLogger("httpx").setLevel(logging.WARNING)

###########################################################
############################################################
############################################################
async def create_topic(topic_name: str):
    async with aiohttp.ClientSession() as session:
        url = f"http://127.0.0.1:8000/create-topic/{topic_name}"
        async with session.get(url) as response:
            return await response.json()

async def send_message_to_group(context: ContextTypes.DEFAULT_TYPE):
    # res = requests.get("http://127.0.0.1:8000/create-topic/req-from-PTB")
    res = await create_topic('سلام امیر')
    await context.bot.send_message(chat_id=-1001893146969, text=res, message_thread_id=60)

def main():
    application = ApplicationBuilder().token(TOKEN).proxy_url(proxy_url).get_updates_proxy_url(proxy_url).build()
    job_queue = application.job_queue
    
    job_queue.run_once(send_message_to_group, when=5)
    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    try:
        main()
    except NetworkError:
        logger.error("A network error was encountered!")
    except ConnectionRefusedError:
        logger.error("A ConnectionRefusedError was encountered!")
    # except 
