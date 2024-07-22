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
@l313l.on(admin_cmd(outgoing=True, pattern="هتلر1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/3379ea7cadaf23b8a56ad.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="إيمانويل ماكرون1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/1e59c4d76bab7ce87284f.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="صدام حسين1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/20c018f6fe50a47e9dfbf.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ترامب1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/a264b7865506e7bdda8fb.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="كيم جونغ أون1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/23fe47c4e26ac601fb1c0.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="عبد الفتاح السيسي1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/0e8df65beb18ec2f83ef5.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="فلاديمير بوتين1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/a0c661feb63b9107cd6c3.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="محمد شياع1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://telegra.ph/file/fec4767e56f20daa41fd0.jpg"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()