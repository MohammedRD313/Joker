# WRITE  BY JoKeRUB
# PLUGIN FOR JoKeRUB 
# @jepthon

from telethon import events
import random, re
from ..Config import Config

from JoKeRUB.utils import admin_cmd

import asyncio
from JoKeRUB import l313l
from random import choice

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus

plugin_category = "extra"

rehu = [ "𝗔𝗹𝘄𝗮𝘆𝘀 𝗢𝗻𝗲 𝗽𝗲𝗶𝗰𝗲 𝟯𝗺𝗸 💪🏻😉 ========================== ",]
@l313l.ar_cmd(pattern="الاوامر(?:\s|$)([\s\S]*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        Zo_r0 = random.choice(rehu)
        await event.edit(
        f" ****\n===========================         قائمة اوامر العقرب | 𝗦𝗰𝗼𝗿𝗽𝗶𝗼 𝗼𝗿𝗱𝗲𝗿𝘀 🦂\n ( `.م1` )  ⦙ **سِوٌآلَفُ آلَآدٍمًنِ**\n( `.م2` )  ⦙ **سِوٌآلَفُ آلَمًجّمًوٌعٌةّ**\n( `.م3` )  ⦙ **آلَتٌرحًيَبً وٌآلَردٍوٌدٍ**\n( `.م4` )  ⦙ **حًمًآيَةّ آلَخِآصّ وٌ آلَتٌلَکْرآفُ**\n( `.م5` )  ⦙ **مًنِشُنِ وٌ آلَآنِتٌحًآلَ**\n( `.م6` )  ⦙ **تٌحًمًيَلَ وٌ تٌرجّمًةّ**\n( `.م7` )  ⦙ **آوٌآمًر آلَمًنِعٌ وٌ آلَقُفُلَ**\n( `.م8` )  ⦙ **آوٌآمًر آلَتٌنِضيَفُ وٌ آلَتٌکْرآر**\n( `.م9` )  ⦙ **تٌخِصّيَصّ وٌ فُآرآتٌ**\n( `.م10` ) ⦙ **آلَوٌقُتٌيَ وٌ آلَتٌشُغُيَلَ**\n( `.م11` ) ⦙ **آلَکْشُفُ وٌ آلَروٌآبًطِ**\n( `.م12` ) ⦙ **آلَمًسِآعٌدٍةّ وٌآلَآذِآعٌةّ** \n( `.م13` ) ⦙ **آلَآرسِآلَ وٌآلَآذِکْآر**\n( `.م14` ) ⦙ **آوٌآمًر آلَمًلَصّقُآتٌ وٌ کْوٌکْلَ**\n( `.م15` ) ⦙ **تٌسِلَيَةّ وٌ مًيَمًزٍ** \n( `.م16` ) ⦙ **تٌحًوٌيَلَ صّيَغُ وٌ جّهّآتٌ**\n( `.م17` ) ⦙ **آوٌآمًر آلَتٌمًبًلَر وٌآلَزٍغُرفُةّ**\n( `.م18` ) ⦙ **سِوٌآلَفُ آلَحًسِآبً وٌ آلَتٌرفُيَهّ**\n( `.م19` ) ⦙ **مًيَوٌزٍکْ**\n( `.م20` ) ⦙ **بًصّمًآتٌ مًيَمًزٍ**\n( `.م21` ) ⦙ **سِوٌآلَفُ تٌجّمًيَعٌ نِقُآطِ بًوٌتٌآتٌ**** {Zo_r0} **"
)

@l313l.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الادمن | 𝗔𝗱𝗺𝗶𝗻 𝗼𝗿𝗱𝗲𝗿𝘀 🦂  **:\n \n** إختر احداها **:\n\n**- { `.اوامر الحظر` }**\n**- { `.اوامر الكتم` }**\n**- { `.اوامر التثبيت` }**\n**- { `.اوامر الاشراف` }**\n\n **العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
		
@l313l.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**أوامر المجـموعة | 𝗚𝗿𝗼𝘂𝗽 𝗢𝗿𝗱𝗲𝗿𝘀 🦂**:\n \n** إختر إحداها: **\n\n** - { `.اوامر التفليش` } **\n** - { `.اوامر المحذوفين` } **\n** - { `.اوامر الكروب` } **\n\n** العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الترحيب والردود| 𝗪𝗲𝗹𝗰𝗼𝗺𝗲,𝗿𝗲𝘀𝗽𝗼𝗻𝘀𝗲𝘀 🦂 **:\n \n ** إختر إحداها **\n\n- { `.اوامر الترحيب` }\n- { `.اوامر الردود` }\n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
@l313l.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الحماية والتلكراف | 𝗣𝗿𝗼𝘁𝗲𝗰𝘁𝗶𝗼𝗻 𝗼𝗿𝗱𝗲𝗿𝘀 🦂**:\n \n ** إختر إحداها : **\n\n**- { `.اوامر الحماية` }**\n**- { `.اوامر التلكراف` }** \n \n **العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
@l313l.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** المنشن والانتحال |  𝗠𝗲𝗻𝘁𝗶𝗼𝗻, 𝗽𝗹𝗮𝗴𝗶𝗮𝗿𝗶𝘀𝗺 🦂 **:\n \n ** اختر احداها : **\n\n**- { `.اوامر الانتحال` }**\n**- { `.اوامر التقليد` }**\n**- { `.اوامر المنشن` }** \n\n **العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** التحميل والترجمة | 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 , 𝘁𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗶𝗼𝗻 🦂 **:\n \n **اختر احداها :** \n\n**- { `.اوامر النطق` } **\n**- { `.اوامر التحميل` }**\n**- { `.اوامر الترجمة` }** \n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قفل ومنع | 𝗟𝗼𝗰𝗸 𝗮𝗻𝗱 𝗯𝗹𝗼𝗰𝗸 🦂 **:\n\n **أختر احداها : **\n\n** - { `.اوامر القفل` }**\n**- { `.اوامر الفتح` }\n**- { `.اوامر المنع` }** \n\n **العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** **:\n\n ****\n\n****\n**\n**** \n\n ****"
		)

@l313l.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**التنضيف والتكرار | 𝗖𝗹𝗲𝗮𝗻 𝗮𝗻𝗱 𝗿𝗲𝗽𝗲𝗮𝘁 🦂 **:\n\n ** اختر احداها: **\n\n**- { `.اوامر التكرار` }**\n**- { `.اوامر السبام` }**\n**- { `.اوامر التنظيف` }** \n**- { `.اوامر المسح` } \n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الفارات | 𝗩𝗮𝗿𝗮𝘁 🦂 **:\n \n ** اختر : **\n\n**- { `.اوامر التخصيص` }**\n **لتغير الصور والكلايش كل من الحماية والفحص والبنك**\n**- { `.اوامر الفارات` }**\n **- لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها**\n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
		)

@l313l.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الوقتي والتشغيل | 𝗧𝗶𝗺𝗶𝗻𝗴 , 𝗼𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻 🦂 **:\n \n ** اختر احداها :**\n\n**- { `.اوامر الاسم` }**\n**- { `.اوامر البايو` }**\n**- { `.اوامر الكروب الوقتي` }**\n**- { `.اوامر التشغيل` } **\n**- { `.اوامر الاطفاء` } **\n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)	

@l313l.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الكشف والروابط | 𝗦𝗵𝗼𝘄 𝗮𝗻𝗱 𝗹𝗶𝗻𝗸𝘀 🦂  **:\n \n **اختر احداها: **\n\n**- { `.اوامر الكشف` }**\n**- { `.اوامر الروابط` }** \n\n \n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
@l313l.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** اوامر المساعدة | 𝗛𝗲𝗹𝗽 𝗼𝗿𝗱𝗲𝗿𝘀 🦂  **:\n \n** اختر احداها :**\n\n**- { `.اوامر الوقت والتاريخ` }**\n**- { `.اوامر كورونا` }**\n**- { `.اوامر الصلاة` }** \n**- { `.اوامر مساعدة` }**\n**- { `.اوامر الاذاعه` }** \n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
@l313l.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** اوامر الارسال | 𝗧𝗿𝗮𝗻𝘀𝗺𝗶𝘀𝘀𝗶𝗼𝗻 𝗼𝗿𝗱𝗲𝗿𝘀 🦂 **:\n \n  ** اختر احداها **\n\n**- { `.امر الصورة الذاتية` }**\n**- { `.اوامر التحذيرات` }**\n**- { `.اوامر اللستة` }**\n**- { `.اوامر الملكية` } **\n**- { `.اوامر السليب` }** \n**- { `.اوامر الاذكار` }\n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
@l313l.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** ملصقات و گوگل | 𝗦𝘁𝗶𝗰𝗸𝗲𝗿𝘀 , 𝗚𝗼𝗼𝗴𝗹𝗲 🦂**:\n \n **اختر احداها :** \n\n**- { `.اوامر الملصقات` }**\n**- { `.اوامر كوكل` }**\n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** **:\n\n ****\n\n****\n**\n**** \n\n ****"
)

@l313l.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**تسلية وتحشيش | 𝗘𝗻𝗷𝗼𝘆 𝗮𝗻𝗱 𝗙𝘂𝗻𝗻𝘆 🦂 **:\n \n **اختر احداها :**\n\n**- { `.اوامر التسلية` }**\n**- { `.اوامر التحشيش` }\n**- { `.اوامر الميمز` }**\n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**  اوامر تحويل الصيغ و الجهات 🦂 **:\n \n **اختر احداها:**\n\n**- { `.اوامر التحويل` }**\n**- { `.اوامر الجهات` }** \n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**  اوامر الحساب و الترفيه 🦂**:\n\n **اختر احداها:**\n\n**- { `.اوامر الترفيه` }**\n**- { `.اوامر الحساب` }** \n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"

)

@l313l.ar_cmd(
    pattern="م19",
    command=("م19", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
      "**الميوزك | 𝗠𝘂𝘀𝗶𝗰 🦂 ** \n \n **اختر احداها:**\n ** قبل أستخدام هذه الاوامر يجب تفعيل المود بكتابة ألامر { `.ميوزك تفعيل` }** \n**- { `.تشغيل_المكالمة` }**\n**- لتشغيل المحادثة الصوتيه**\n**- { `.انهاء_المكالمة` }**\n**-لأنهاء المحادثه الصوتية **\n**- { `.دعوة` }**\n**- بالرد على الشخص لدعوته الى المكالمة **\n**- { `.معلومات_المكالمة` }**\n**- لعرض عنوان المكالمة وعدد لاشخاص الموجودين فيها** \n**- { `.تسمية_المكالمة` }**\n**- لتغير عنوان المكالمة** \n**- { `.انضمام` }**\n**- للأنضمام الى المحادثة الصوتية**\n**- { `.مغادرة` }**\n**- لمغادرة المحادثة الصوتية **\n**- { `.تشغيل` }**\n**-بالرد على رابط اليوتيوب او كتابة الامر مع رابط ليوتيوب لتشغيل الاغنيه** \n**- { `.قائمة_التشغيل` }**\n**- لعرض قائمة التشغيل** \n**- { `.ايقاف_مؤقت` }**\n **- لأيقاف الاغنية الحالية مؤقتا **\n**- { `.استمرار` }**\n **-لأستمرار الاغنيه التي تم ايقافها** \n**- { `.تخطي` }**\n**- لتخطي الاغنيه وتشغيل الاغنيه الموجوده في قائمة التشغيل** \n\n \n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"

)

@l313l.ar_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**🦂 𝗙𝘂𝗻𝗻𝘆 𝗮𝘂𝗱𝗶𝗼𝘀 | صوتيات ميمز  **:\n \n  **اختر احداها:**\n\n**- { `.بصمات ميمز` }**\n**- { `.بصمات ميمز2` }**\n**- { `.بصمات ميمز3` }**\n**- { `.بصمات ميمز4` }**\n**- { `.بصمات ميمز5` }**\n**- { `.بصمات انمي` } **\n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"

)

@l313l.ar_cmd(
    pattern="م21$",
    command=("م21", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "**  نقاط بوتات | 𝗖𝗼𝗹𝗹𝗲𝗰𝘁 𝗽𝗼𝗶𝗻𝘁𝘀 🦂 **:\n \n  **اختر احداها:**\n\n**- { `.اوامر التجميع` } **\n**- { `.اوامر وعد` }** \n\n**العقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
        )
