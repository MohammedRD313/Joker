# فريق العقرب 
# علوش @ZS_SQ
# محمد @Zo_r0
import asyncio
import random
import re
import json
import base64
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from asyncio.exceptions import TimeoutError
from telethon import events
from ..sql_helper.memes_sql import get_link, add_link, delete_link, BASE, SESSION, AljokerLink
from telethon.errors.rpcerrorlist import YouBlockedUserError
# فريق العقرب 
# علوش @ZS_SQ
# محمد @Zo_r0
from JoKeRUB import l313l
from ..helpers.utils import reply_id
plugin_category = "tools"
# فريق العقرب 
# علوش @ZS_SQ
# محمد @Zo_r0
@l313l.on(admin_cmd(outgoing=True, pattern="المريخ1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/602571a60c082f02d6b4e.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ألأرض1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/b2c42e72d3ad6078f8574.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="زحل1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/ef3582525b26f6d07ed5d.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نبتون1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/c55356c922e099ca5c751.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="أورانوس1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/9bab980286a61716fdd01.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="عطارد1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/5a4ff979a293422d5d7bc.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ألمشتري1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/1960517a267d463f01153.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ألزهرة1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/468e13ed3afdb7d973b8c.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()