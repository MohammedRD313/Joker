#الملف بحقوق سورس سبايدر @ZS_SQ بواسطة @l313l
import asyncio
import os
from secrets import choice
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVoice

from JoKeRUB import l313l

from ..core.logger import logging
from ..Config import Config
from . import ALIVE_NAME, mention
from ..helpers import get_user_from_event
from ..helpers.utils import _format

from . import reply_id


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الفاتحة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/26"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الفاتحة\n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة البقرة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/27"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة البقرة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة آل عمران$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/28"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة آل عمران \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة النساء$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/29"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة النساء \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة المائدة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/30"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة المائدة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الأنعام$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/31"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الأنعام \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الأعراف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/32"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الأعراف \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الأنفال$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/33"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الأنفال \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة التوبة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/34"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة التوبة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة يونس$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/35"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة يونس \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة هود$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/36"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة هود \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة يوسف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/37"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة يوسف \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الرعد$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/38"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الرعد \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة إبراهيم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/39"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة إبراهيم \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الحجر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/40"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الحجر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة النحل$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/41"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة النحل \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الإسراء$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/42"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الإسراء \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الكهف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/43"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الكهف \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة مريم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/44"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة مريم \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة طه$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/45"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة طه \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الأنبياء$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/46"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الأنبياء \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الحج$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/47"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الحج \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة المؤمنون$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/48"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة المؤمنون \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة النور$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/49"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة النور \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الفرقان$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/50"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الفرقان \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الشعراء$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/51"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الشعراء \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة النمل$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/52"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة النمل \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة القصص$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/53"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة القصص \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة العنكبوت$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/54"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة العنكبوت \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الروم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/55"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الروم \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة لقمان$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/56"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة لقمان \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة السجدة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/57"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة السجدة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الأحزاب$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/58"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الأحزاب \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة سبأ$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/59"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة سبأ \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة فاطر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/60"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة فاطر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة يس$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/61"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة يس \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الصافات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/62"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الصافات \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة ص$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/63"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة ص \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الزمر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/64"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الزمر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة غافر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/65"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة غافر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة فصلت$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/66"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة فصلت \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الشورى$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/67"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الشورى \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الزخرف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/68"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الزخرف \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الدخان$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/69"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الدخان \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الجاثية$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/70"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الجاثية \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الأحقاف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/71"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الأحقاف \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة محمد$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/72"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة محمد \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الفتح$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/73"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الفتح \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الحجرات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/74"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الحجرات \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة ق$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/75"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة ق \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الذاريات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/76"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الذاريات \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الطور$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/77"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الطور \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة النجم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/78"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة النجم \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة القمر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/79"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة القمر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الرحمن$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/80"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الرحمن \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الواقعة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/81"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الواقعة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الحديد$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/82"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الحديد \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة المجادلة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/83"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة المجادلة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الحشر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/84"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الحشر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الممتحنة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/85"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الممتحنة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الصف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/86"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الصف \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الجمعة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/87"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الجمعة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة المنافقون$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/88"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة المنافقون \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة التغابن$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/89"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة التغابن \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الطلاق$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/90"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الطلاق \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة التحريم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/91"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة التحريم \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الملك$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/92"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الملك \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة القلم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/93"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة القلم \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الحاقة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/94"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الحاقة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة المعارج$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/95"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة المعارج \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة نوح$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/96"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة نوح \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الجن$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/97"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الجن \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة المزمل$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/98"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة المزمل \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة المدثر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/99"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة المدثر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة القيامة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/100"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة القيامة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الإنسان$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/101"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الإنسان \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة المرسلات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/102"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة المرسلات \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة النبأ$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/103"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة النبأ \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة النازعات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/104"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة النازعات \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة عبس$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/105"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة عبس \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة التكوير$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/106"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة التكوير \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الإنفطار$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/107"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الإنفطار \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة المطففين$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/108"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة المطففين \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الإنشقاق$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/109"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الإنشقاق \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة البروج$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/110"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة البروج \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الطارق$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/111"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الطارق \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الأعلى$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/112"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الأعلى \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الغاشية$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/113"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الغاشية \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الفجر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/114"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الفجر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة البلد$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/115"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة البلد \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الشمس$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/116"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الشمس \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الليل$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/117"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الليل \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الضحى$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/118"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الضحى \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الشرح$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/119"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الشرح \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة التين$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/120"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة التين \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة العلق$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/121"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة العلق \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة القدر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/122"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة القدر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة البينة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/123"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة البينة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الزلزلة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/124"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الزلزلة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة العاديات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/125"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة العاديات \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة القارعة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/126"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة القارعة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة التكاثر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/127"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة التكاثر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة العصر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/128"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة العصر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الهمزة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/129"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الهمزة \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الفيل$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/130"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الفيل \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة قريش$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/131"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة قريش \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الماعون$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/132"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الماعون \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الكوثر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/133"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الكوثر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الكافرون$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/134"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الكافرون \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة النصر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/135"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة النصر \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة المسد$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/136"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة المسد \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الإخلاص$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/137"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الإخلاص \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الفلق$"))
async def jepvois(Voice):
  url = f"https://t.me/Scorpion_scorp"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الفلق \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سورة الناس$"))
async def jepvois(Voice):
  url = f"https://t.me/Scorpion_scorp"
  await Voice.client.send_file(Voice.chat_id,url,caption="✎┊‌ سورة الناس \n✎┊‌ بصوت القارئ ماهر المعيقلي\nBy : @Scorpion_scorp ✍🏻",parse_mode="html")
  await Voice.delete()
