import pytgpt.phind
import requests
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from JoKeRUB import l313l
from . import l313l
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"

# إنشاء بوت جديد من pytgpt.phind
bot = pytgpt.phind.PHIND()

def gpt(message):
    return bot.chat(f'{message}')

@l313l.ar_cmd(pattern="سؤال(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**✎┊‌ بالرد على السؤال او بأضافة سؤال \n يعني تكتب (`.سؤال`) وبعده سؤالك وخلص 😌 \n\n مثال : \n `.سؤال من هو مخترع الكهرباء`**")
    if not zilzal and event.reply_to_msg_id and zzz.text:
        zilzal = zzz.text
    if not event.reply_to_msg_id:
        zilzal = event.pattern_match.group(1)

    zed = await edit_or_reply(event, "**✎┊‌ اصبر حبيبي هسة يجاوبك 😁**")

    try:
        # استخدام البوت الجديد للإجابة على الأسئلة
        response = gpt(zilzal)
        await asyncio.sleep(5)
        malath = response
        
        if "Please wait another 8 seconds" in malath:
            await zed.delete()
            return await borg.send_message(event.chat_id, "**✎┊‌ اصبر حبيبي هسة يجاوبك 😁**")
        
        if "understanding" in malath:
            await zed.delete()
            return await borg.send_message(event.chat_id, "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**")
        
        await zed.delete()
        await borg.send_message(event.chat_id, f"**السؤال : {zilzal}\n\n{malath}**\n\n───────────────────\n")

    except Exception as e:
        await zed.delete()
        await borg.send_message(event.chat_id, f"**حدث خطأ: {str(e)}**")
