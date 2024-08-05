import asyncio
from telethon import events
from telethon.errors import FloodWaitError
from telethon.errors.rpcerrorlist import YouBlockedUserError

from JoKeRUB import l313l
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"

# يمكنك تعريف دالة مساعدة لإرسال الرسائل للبوتات المختلفة هنا إذا لزم الأمر
async def send_message_to_bot(bot, chat, message):
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message(message)
            response = await conv.get_response()
            return response
        except FloodWaitError as e:
            await asyncio.sleep(e.seconds)
            return await send_message_to_bot(bot, chat, message)
        except Exception as e:
            print(f"Error sending message: {e}")
            return None

@l313l.ar_cmd(pattern="سؤال(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@ScorGPTbot"  # يمكن تعديلها لتكون ديناميكية إذا لزم الأمر
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**✎┊‌ بالرد على السؤال او بأضافة سؤال \n يعني تكتب (`.سؤال`) وبعده سؤالك وخلص 😌 \n\n مثال : \n `.سؤال من هو مخترع الكهرباء`**")
    if not zilzal and event.reply_to_msg_id and zzz.text: 
        zilzal = zzz.text
    if not event.reply_to_msg_id: 
        zilzal = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**✎┊‌اصبر حبيبي هسة يجاوبك 😁**")
    
    bot = event.client  # يستخدم البوت الحالي أو يمكنك تحديد بوت آخر
    response = await send_message_to_bot(bot, chat, zilzal)
    if response:
        ahmed = response.text
        if "another 8 seconds" in ahmed: 
            aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌اصبر حبيبي هسة يجاوبك 😘**") 
            await event.delete()
            return await bot.send_message(event.chat_id, aa)
        await asyncio.sleep(15)
        response = await send_message_to_bot(bot, chat, zilzal)
        malath = response.text
        if "understanding" in malath:
            aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
            await event.delete()
            return await bot.send_message(event.chat_id, aa)
        await zed.delete()
        await bot.send_message(event.chat_id, f"**السؤال : {zilzal}\n\n{malath}**\n\n───────────────────\n")
    else:
        await zed.delete()
        await bot.send_message(event.chat_id, "**✎┊‌حدث خطأ في الحصول على رد من البوت.**")
