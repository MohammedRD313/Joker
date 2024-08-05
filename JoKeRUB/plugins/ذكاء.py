import asyncio
from telethon import events
from telethon.errors import FloodWaitError, YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "البوت"

@l313l.ar_cmd(pattern="سؤال(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    
    # الحصول على اسم البوت من إعدادات التكوين أو تعيين قيمة افتراضية
    bot_username = Config.BOT_USERNAME if hasattr(Config, 'BOT_USERNAME') else "@YourDefaultBot"

    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**✎┊‌ بالرد على السؤال او بأضافة سؤال \n يعني تكتب (`.سؤال`) وبعده سؤالك وخلص 😌 \n\n مثال : \n `.سؤال من هو مخترع الكهرباء`**")
    
    if not zilzal and event.reply_to_msg_id and zzz:
        zilzal = zzz.text
    elif not event.reply_to_msg_id:
        zilzal = event.pattern_match.group(1)
    
    # رسالة مبدئية للتأكيد
    zed = await edit_or_reply(event, "**✎┊‌ اصبر حبيبي هسة يجاوبك 😁**")
    
    async with borg.conversation(bot_username) as conv:
        try:
            # إرسال السؤال إلى البوت
            await conv.send_message(zilzal)
            
            # محاولة الحصول على رد من البوت مع مهلة محددة
            try:
                response = await asyncio.wait_for(conv.get_response(), timeout=30)  # زيادة المهلة
            except asyncio.TimeoutError:
                await borg.send_message(event.chat_id, "**✎┊‌ عذرًا، لم أتمكن من الحصول على رد من البوت في الوقت المحدد. حاول مرة أخرى لاحقًا.**")
                return
            
            response_text = response.text
            
            # التعامل مع الرسائل التي تطلب الانتظار
            if "another 8 seconds" in response_text:
                response_text = response_text.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌ اصبر حبيبي هسة يجاوبك 😘**")
                await event.delete()
                return await borg.send_message(event.chat_id, response_text)
            
            # الانتظار قبل محاولة الحصول على رد آخر
            await asyncio.sleep(5)
            try:
                response = await asyncio.wait_for(conv.get_response(), timeout=30)  # زيادة المهلة
            except asyncio.TimeoutError:
                await borg.send_message(event.chat_id, "**✎┊‌ عذرًا، لم أتمكن من الحصول على رد من البوت في الوقت المحدد. حاول مرة أخرى لاحقًا.**")
                return
            
            response_text = response.text
            
            # التعامل مع حالة عدم الفهم من البوت
            if "understanding" in response_text:
                response_text = response_text.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**")
                await event.delete()
                return await borg.send_message(event.chat_id, response_text)
            
            # حذف رسالة التأكيد
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {zilzal}\n\n{response_text}**\n\n───────────────────\n")
        
        except YouBlockedUserError:
            # التعامل مع حالة حظر المستخدم من قبل البوت
            await borg(UnblockRequest(bot_username))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(zilzal)
            
            try:
                response = await asyncio.wait_for(conv.get_response(), timeout=30)  # زيادة المهلة
            except asyncio.TimeoutError:
                await borg.send_message(event.chat_id, "**✎┊‌ عذرًا، لم أتمكن من الحصول على رد من البوت في الوقت المحدد. حاول مرة أخرى لاحقًا.**")
                return
            
            response_text = response.text
            
            if "another 8 seconds" in response_text:
                response_text = response_text.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌ اصبر حبيبي هسة يجاوبك 😁**")
                await event.delete()
                return await borg.send_message(event.chat_id, response_text)
            
            await asyncio.sleep(5)
            try:
                response = await asyncio.wait_for(conv.get_response(), timeout=30)  # زيادة المهلة
            except asyncio.TimeoutError:
                await borg.send_message(event.chat_id, "**✎┊‌ عذرًا، لم أتمكن من الحصول على رد من البوت في الوقت المحدد. حاول مرة أخرى لاحقًا.**")
                return
            
            response_text = response.text
            
            if "understanding" in response_text:
                response_text = response_text.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**")
                await event.delete()
                return await borg.send_message(event.chat_id, response_text)
            
            if "Please wait a moment" in response_text:
                await asyncio.sleep(5)
                try:
                    response = await asyncio.wait_for(conv.get_response(), timeout=30)  # زيادة المهلة
                except asyncio.TimeoutError:
                    await borg.send_message(event.chat_id, "**✎┊‌ عذرًا، لم أتمكن من الحصول على رد من البوت في الوقت المحدد. حاول مرة أخرى لاحقًا.**")
                    return
                
                response_text = response.text
            
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {zilzal}\n\n{response_text}**\n\n───────────────────\n")
