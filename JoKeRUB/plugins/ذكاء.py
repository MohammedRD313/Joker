import asyncio
from telethon import events
from telethon.errors import FloodWaitError, YouBlockedUserError
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from . import l313l
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"

@l313l.ar_cmd(pattern="سؤال(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@ScorGPTbot"  # تأكد من تحديثه إلى اسم البوت الصحيح

    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**✎┊‌ بالرد على السؤال او بأضافة سؤال \n يعني تكتب (`.سؤال`) وبعده سؤالك وخلص 😌 \n\n مثال : \n `.سؤال من هو مخترع الكهرباء`**")

    if not zilzal and event.reply_to_msg_id and zzz.text:
        zilzal = zzz.text
    if not event.reply_to_msg_id:
        zilzal = event.pattern_match.group(1)

    zed = await edit_or_reply(event, "**✎┊‌ اصبر حبيبي هسة يجاوبك 😁**")

    async with l313l.client.conversation(chat) as conv:
        try:
            await conv.send_message(zilzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text:
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌ اصبر حبيبي هسة يجاوبك 😁**")
                await event.delete()
                return await l313l.client.send_message(event.chat_id, aa)
            
            await asyncio.sleep(5)
            l313l_response = await conv.get_response()
            malath = l313l_response.text
            if "understanding" in l313l_response.text:
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**")
                await event.delete()
                return await l313l.client.send_message(event.chat_id, aa)
            
            await zed.delete()
            await l313l.client.send_message(event.chat_id, f"**السؤال : {zilzal}\n\n{malath}**\n\n───────────────────\n")

        except YouBlockedUserError:
            await l313l.client(UnblockRequest(chat))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(zilzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text:
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌ اصبر حبيبي هسة يجاوبك 😁**")
                await event.delete()
                return await l313l.client.send_message(event.chat_id, aa)
            
            await asyncio.sleep(5)
            l313l_response = await conv.get_response()
            malath = l313l_response.text
            if "understanding" in l313l_response.text:
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**")
                await event.delete()
                return await l313l.client.send_message(event.chat_id, aa)
            
            if "Please wait a moment" in l313l_response.text:
                await asyncio.sleep(5)
                l313l_response = await conv.get_response()
                malath = l313l_response.text
            
            await zed.delete()
            await l313l.client.send_message(event.chat_id, f"**السؤال : {zilzal}\n\n{malath}**\n\n───────────────────\n")
