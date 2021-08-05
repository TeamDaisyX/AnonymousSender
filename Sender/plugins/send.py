'''
The Giant Penis License (GPL)
Copyright (c) 2021 @InukaAisth
                ▄▄██▄██▄▄
              ▄█    █    █▄
             ▄█           █▄
             █             █
            █               █
            █               █
            █               █
            █               █
             █▄     █     ▄█
              █    ▄▄▄    █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
        ▄████▄█           █▄████▄
      ▄█                         █▄
     █                             █
    █                               █
    █                               █
    █                               █
    █             ▄▄█▄▄             █
     █           █     █           █
      █▄       ▄█       █▄       ▄█
        █▄▄▄▄▄█           █▄▄▄▄▄█
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
😂 There is no such penis lisence do anything you like
'''


from pyrogram import filters
from pyrogram.types import Message

from Sender import bot
from pyrogram.errors import RPCError

import functools
from typing import Callable, Coroutine, Dict, List, Tuple, Union

def is_admin(func):
    @functools.wraps(func)
    async def oops(client,message):
        is_admin = False
        try:
            user = await message.chat.get_member(message.from_user.id)
            admin_strings = ("creator", "administrator")
            if user.status not in admin_strings:
                is_admin = False
            else:
                is_admin = True

        except ValueError:
            is_admin = True
        if is_admin:
            await func(client,message)
        else:
            await message.reply("Only Admins can execute this command!")
    return oops

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@bot.on_message(
    filters.command("send") & ~filters.edited & ~filters.bot)
@is_admin
async def send(client, message):
    if message.reply_to_message:
            reply = message.reply_to_message
            try:
                await reply.copy(message.chat.id)
            except RPCError as i:
                await message.reply(i)
                return

    else:
        args = get_text(message)
        await client.send_message(message.chat.id, text=args)

@bot.on_message(filters.private & ~filters.command(["start","help","edit"]))
async def copy(client, message):
    try:
        await message.copy(message.chat.id)
    except RPCError as i:
        await message.reply(i)
        return

@bot.on_message(
    filters.command("edit") & ~filters.edited & ~filters.bot)
@is_admin
async def loltime(client, message):
    lol = await message.reply("Processing please wait")
    cap = get_text(message)
    if not message.reply_to_message:
        await lol.edit("reply to any message to edit caption")
    reply = message.reply_to_message
    try:
        await reply.copy(message.chat.id,caption= cap)
        await lol.delete()
    except RPCError as i:
        await lol.edit(i)
        return

@bot.on_message(
    filters.command("start") & ~filters.edited & ~filters.bot)    
async def lel(client, message):
    lol = await message.reply("forward any file to get it without tag. \nCheck /help to know more")   

@bot.on_message(
    filters.command("help") & filters.private & ~filters.edited & ~filters.bot)    
async def hulp(client, message):
    lol = await message.reply("""
Help of Anon Sender

Forward any message to me to get it without forward tag

Extras:
  - /send <reply> : Sends Given text by bot
  - /send <reply> : Sends given message by bot
  - /edit <caption> <reply to media> : Edit caption of replied media
Note Extras only work for admins in groups
""")

@bot.on_message(
    filters.command("help") & ~filters.private & ~filters.edited & ~filters.bot)    
async def help(client, message):
    lol = await message.reply("Send /help in my inbox to get help")
