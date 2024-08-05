import asyncio
from telethon import events
from telethon.errors import FloodWaitError
from telethon.errors.rpcerrorlist import YouBlockedUserError
import pytgpt.phind

# إنشاء كائن من PHIND
bot_gpt = pytgpt.phind.PHIND()

def gpt(message):
    try:
        response = bot_gpt.chat(message)
        return response
    except Exception as e:
        print(f"Error interacting with GPT: {e}")
        return None

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
    
    zed = await edit_or_reply(event, "**✎┊‌اصبر حبيبي هسة يجاوبك 😁**")
    
    try:
        # استخدام gpt للحصول على الرد
        response = gpt(zilzal)
        
        if response is None:
            await zed.delete()
            return await bot.send_message(event.chat_id, "**✎┊‌حدث خطأ في الحصول على رد من GPT.**")
        
        ahmed = response
        
        # التعامل مع الاستجابة من GPT
        if "another 8 seconds" in ahmed:
            aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌اصبر حبيبي هسة يجاوبك 😘**")
            await event.delete()
            return await bot.send_message(event.chat_id, aa)
        
        if "understanding" in ahmed:
            aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**")
            await event.delete()
            return await bot.send_message(event.chat_id, aa)
        
        await zed.delete()
        await bot.send_message(event.chat_id, f"**السؤال : {zilzal}\n\n{ahmed}**\n\n───────────────────\n")
    except Exception as e:
        await zed.delete()
        await bot.send_message(event.chat_id, f"**✎┊‌حدث خطأ في معالجة طلبك: {e}**")
