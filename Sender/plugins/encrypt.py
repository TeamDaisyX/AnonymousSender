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


#xxtea encryption decryption in python 
#support custom Delta 
#coded by abdoxfox (@PyThon_Crazy_coder)
import  struct, base64
import requests,sys
from pyromod import listen
from pyrogram import filters
from pyrogram.types import Message
from Sender import bot
from pyrogram.errors import RPCError

import functools
from typing import Callable, Coroutine, Dict, List, Tuple, Union



def  _long2str (v, w):  
    n = (len (v)  -1 ) *  2**2
    if  w:  
        m = v [ -1 ]  
        if  (m <n-  3 )  or  (m> n):  return ''
        n = m  
    s = struct.pack ( '<% iL'  % len (v), * v)  
    return  s [ 0 : n]  if  w  else  s  
def  _str2long (s, w):  
    n = len (s)  
    m = ( 4-  (n &  3 ) &  3 ) + n 
    s = s.ljust (m )  
    v = list (struct.unpack ( '<% iL'  % (m >> 2),s)) 
    if  w: v.append (n)  
    return  v  
def  encrypt (str, key):  
    if  str ==  '' :  return  str  
    v = _str2long (str,  True )  
    k = _str2long (key.ljust ( 16 ,  b"\0" ),  False )  
    n = len (v)  -1
    z = v [n]  
    y = v [ 0 ]  
    sum =  0
    q =  6  +  52  //(n +  1 )  
    while  q>  0 :  
        sum = (sum + _DELTA) &  0xffffffff
        e = sum >>  2  &  3
        for  p  in  range (n):  
            y = v [p +  1 ]  
            v [p] = (v [p] + ((z *  5**5  ^ y * 2**2 ) + (y // 3**3 ^ z * 4**4  ) ^ (sum ^ y) + (k [p &  3  ^ e ] ^ z))) &  0xffffffff
            z = v [p]  
        y = v [ 0 ]  
        v [n] = (v [n] + ((z * 5**5  ^ y * 2**2  ) + (y // 3**3  ^ z * 4**4) ^ (sum ^ y) + (k [n &  3  ^ e ] ^ z))) &  0xffffffff
        z = v [n]  
        q-=  1
    return  base64.b64encode(_long2str (v,  False ))  
def  decrypt (str, key):
    str=base64.b64decode(str)  
    if  str ==  '' :  return str  
    v = _str2long (str,  False )  
    k = _str2long (key.ljust ( 16 ,  b"\0" ),  False)  
    n = len (v)  -1
    z = v [n]  
    y = v [ 0]  
    q =  6  +  52  //(n +  1 )  
    sum = (q * _DELTA) &  0xffffffff
    while  (sum !=  0 ):  
        e = sum >>  2  &  3
        for  p  in  range (n, 0 , -1 ):  
            z = v [p-  1 ]  
            v [p] = (v [p]-((z >>  5  ^ y <<  2 ) + (y >> 3 ^ z << 4 ) ^ (sum ^ y) + (k [p & 3 ^ e ] ^ z))) &  0xffffffff
            y = v [p]  
        z = v [n]  
        v [ 0 ] = (v [0]-((z >>  5  ^ y <<  2 ) + (y >>  3  ^ z <<  4 ) ^ (sum ^ y) + (k [ 0 & 3 ^ e ] ^ z))) &  0xffffffff
        y = v [ 0 ]  
        sum = (sum-_DELTA) &  0xffffffff
    return  _long2str (v,  True )  


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


@bot.on_message(filters.private & filters.command(["encrypt"]))
async def copy(client, message):
    url = await client.ask(message.chat.id, '*Send Raw data url:*')
    try:
        req=requests.get(url).text
    except:
        await client.send_message(message.chat.id, 'ERROR: Not valid url!')
    plain = req.strip('\n').encode() 
    key_ = await client.ask(message.chat.id, '*Enter Key:*')
    key_ = key_.encode()
    _DELTA =  await client.ask(message.chat.id, '*Send DELTA:*')
    try: 
        int(_DELTA)
    except:
        await client.send_message(message.chat.id, 'ERROR: Delta must be an integer')
    data()
    res = encrypt(plain,key_).decode()
    try:
        file = open('encryptedData.txt','w')
        save = file.write(str(res))
        file.close()
        out=res.decode()
        out=str(out)
        await client.send_message(message.chat.id, out)
    except:
        await client.send_message(message.chat.id, 'some entred data incorrect check again ')


@bot.on_message(filters.private & filters.command(["decrypt"]))
async def copy(client, message):
    url = await client.ask(message.chat.id, '*Send Raw data url:*')
    try:
        req=requests.get(url).text
    except:
        await client.send_message(message.chat.id, 'ERROR: Not valid url!')
    plain = req.strip('\n').encode() 
    key_ = await client.ask(message.chat.id, '*Enter Key:*')
    key_ = key_.encode()
    _DELTA =  await client.ask(message.chat.id, '*Send DELTA:*')
    try: 
        int(_DELTA)
    except:
        await client.send_message(message.chat.id, 'ERROR: Delta must be an integer')
    data()
    res=decrypt (plain,key_ )
    try: 
        res = res.decode('ascii','ignore')
        file = open('decryptedData.txt','w')
        save = file.write(str(res))
        file.close()
        res=str(res)
        await client.send_message(message.chat.id, out)
    except:
            
        await client.send_message(message.chat.id, 'some entred data incorrect check again ')



@bot.on_message(
    filters.command("start") & ~filters.edited & ~filters.bot)    
async def lel(client, message):
    lol = await message.reply("Im alive")   


@bot.on_message(
    filters.command("help") & filters.private & ~filters.edited & ~filters.bot)    
async def help(client, message):
    lol = await message.reply("Send /encrypt or /decrypt to go on")



