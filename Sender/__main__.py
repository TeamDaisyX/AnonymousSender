

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Sender import bot as app
from Sender import LOGGER
from Sender.plugins import *

# Starting Client
app.start()
LOGGER.info("Anon Sender Bot is online.")
idle()
