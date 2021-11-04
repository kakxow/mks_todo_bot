import logging
import os

from dotenv import load_dotenv
from telegram.ext import Updater

import commands


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
LOGGING_LEVEL = int(os.getenv("LOGGING_LEVEL", logging.INFO))
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=LOGGING_LEVEL
)

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(commands.start)
dispatcher.add_handler(commands.mark_complete)
dispatcher.add_handler(commands.unmark_complete)

updater.start_polling()