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

rehu = []
@l313l.ar_cmd(pattern="الاوامر(?:\s|$)([\s\S]*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	Zo_r0 = random.choice(rehu)
        await event.edit(
        f": ** ===========================              اوامر العقرب | 𝗦𝗰𝗼𝗿𝗽𝗶𝗼 𝗼𝗿𝗱𝗲𝗿𝘀 🦂 **\n\n{ `.م1` }  ⦙ **سِوٌآلَفُ آلَآدٍمًنِ**\n{ `.م2` }  ⦙ **سِوٌآلَفُ آلَمًجّمًوٌعٌةّ**\n{ `.م3` }  ⦙ **آلَتٌرحًيَبً وٌآلَردٍوٌدٍ**\n{ `.م4` }  ⦙ **حًمًآيَةّ آلَخِآصّ وٌ آلَتٌلَکْرآفُ**\n{ `.م5` }  ⦙ **مًنِشُنِ وٌ آلَآنِتٌحًآلَ**\n{ `.م6` }  ⦙ **تٌحًمًيَلَ وٌ تٌرجّمًةّ**\n{ `.م7` }  ⦙ **آوٌآمًر آلَمًنِعٌ وٌ آلَقُفُلَ**\n{ `.م8` }  ⦙ **آوٌآمًر آلَتٌنِضيَفُ وٌ آلَتٌکْرآر**\n{ `.م9` }  ⦙ **تٌخِصّيَصّ وٌ فُآرآتٌ**\n{ `.م10` } ⦙ **اوامرآلَوٌقُتٌيَ وٌ آلَتٌشُغُيَلَ**\n{ `.م11` } ⦙ **آلَکْشُفُ وٌ آلَروٌآبًطِ**\n{ `.م12` } ⦙ **آلَمًسِآعٌدٍةّ وٌآلَآذِآعٌةّ ** \n{ `.م13` } ⦙ **آلَآرسِآلَ وٌآلَآذِکْآر**\n{ `.م14` } ⦙ **آوٌآمًر آلَمًلَصّقُآتٌ وٌ کْوٌکْلَ**\n{ `.م15` } ⦙ **تٌسِلَيَةّ وٌ مًيَمًزٍ ** \n{ `.م16` } ⦙ **تٌحًوٌيَلَ صّيَغُ وٌ جّهّآتٌ**\n{ `.م17` } ⦙ **آوٌآمًر آلَتٌمًبًلَر وٌآلَزٍغُرفُةّ**\n{ `.م18` } ⦙ **سِوٌآلَفُ آلَحًسِآبً وٌ آلَتٌرفُيَهّ**\n{ `.م19` } ⦙ **مًيَوٌزٍکْ**\n{ `.م20` } ⦙ **بًصّمًآتٌ مًيَمًزٍ**\n{ `.م21` } ⦙ **تٌجّمًيَعٌ نِقُآطِ بًوٌتٌآتٌ**\n**𝗔𝗹𝘄𝗮𝘆𝘀 𝗢𝗻𝗲 𝗽𝗲𝗶𝗰𝗲 𝟯𝗺𝗸 💪🏻😉 ==========================\n {Zo_r0} **"
)

@l313l.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** اوامر الادمن | 𝗔𝗱𝗺𝗶𝗻 𝗼𝗿𝗱𝗲𝗿𝘀 🦂:\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر الحظر` }\n- { `.اوامر الكتم` }\n- { `.اوامر التثبيت` }\n- { `.اوامر الاشراف` }\n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
		
@l313l.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** اوامر الكروب  | 𝗚𝗿𝗼𝘂𝗽 𝗢𝗿𝗱𝗲𝗿𝘀 🦂 :\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر التفليش` }\n- { `.اوامر المحذوفين` }\n- { `.اوامر الكروب` }\n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـترحيب والـردود **:\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر الترحيب` }\n- { `.اوامر الردود` }\n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂"
)
@l313l.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الحماية والتلغراف | 𝗣𝗿𝗼𝘁𝗲𝗰𝘁𝗶𝗼𝗻 , 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗽𝗵 🦂 \n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر الحماية` }\n- { `.اوامر التلكراف` } \n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
@l313l.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** المنشن والانتحال | 𝗠𝗲𝗻𝘀𝗵𝗶𝗻 , 𝗦𝗲𝗹𝗹𝗲𝗿 🦂 \n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر الانتحال` }\n- { `.اوامر التقليد` }\n- { `.اوامر المنشن` } \n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الترجمة والتحميل | 𝗧𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗲 , 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 🦂\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر النطق` }\n- { `.اوامر التحميل` }\n- { `.اوامر الترجمة` } \n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** المنع والقفل | 𝗕𝗹𝗼𝗰𝗸𝗲𝗱 , 𝗹𝗼𝗰𝗸 🦂 \n\n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر القفل` }\n- { `.اوامر الفتح` }\n- { `.اوامر المنع` } \n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** التنظيف والتكرار | 𝗖𝗹𝗲𝗮𝗻𝗶𝗻𝗴 , 𝗿𝗲𝗽𝗲𝘁𝗶𝘁𝗶𝗼𝗻 🦂 \n\n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر التكرار` }\n- { `.اوامر السبام` }\n- { `.اوامر التنظيف` } \n- { `.اوامر المسح` } \n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**الفارات | 𝗩𝗮𝗿𝗮𝘁 🦂 :\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر التخصيص` }\n لتغير الصور والكلايش كل من الحماية والفحص والبنك\n- { `.اوامر الفارات` }\n - لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها\n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
		)

@l313l.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الوقتي والتشغيل | 𝗧𝗶𝗺𝗶𝗻𝗴 , 𝗼𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻 🦂 :\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر الاسم` }\n- { `.اوامر البايو` }\n- { `.اوامر الكروب الوقتي` }\n- { `.اوامر التشغيل` } \n- { `.اوامر الاطفاء` } \n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)	

@l313l.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الكشف والروابط | 𝗦𝗵𝗼𝘄 𝗮𝗻𝗱 𝗹𝗶𝗻𝗸𝘀 🦂  :\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر الكشف` }\n- { `.اوامر الروابط` } \n\n \nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
@l313l.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** اوامر المساعدة | 𝗛𝗲𝗹𝗽 𝗢𝗿𝗱𝗲𝗿𝘀 🦂  :\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر الوقت والتاريخ` }\n- { `.اوامر كورونا` }\n- { `.اوامر الصلاة` } \n- { `.اوامر مساعدة` }\n- { `.اوامر الاذاعه` } \n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
@l313l.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** اوامر الارسال | 𝗧𝗿𝗮𝗻𝘀𝗺𝗶𝘁𝘁𝗲𝗿 𝗼𝗿𝗱𝗲𝗿𝘀 🦂 :\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.امر الصورة الذاتية` }\n- { `.اوامر التحذيرات` }\n- { `.اوامر اللستة` }\n- { `.اوامر الملكية` } \n- { `.اوامر السليب` } \n- { `.اوامر الاذكار` }\n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)
@l313l.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الملصقات وگوگل | 𝗦𝘁𝗶𝗰𝗸𝗲𝗿𝘀 , 𝗚𝗼𝗼𝗴𝗹𝗲 🦂:\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر الملصقات` }\n- { `.اوامر كوكل` }\n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂"
)

@l313l.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** اوامر التحشيش والتسلية 🦂 :\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر التسلية` }\n- { `.اوامر التحشيش` }\n- { `.اضافة ميمز` }\n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**  اوامر تحويل الصيغ و الجهات 🦂:\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر التحويل` }\n- { `.اوامر الجهات` } \n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
)

@l313l.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الحساب والترفيه | 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 , 𝗳𝘂𝗻 🦂:\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر الترفيه` }\n- { `.اوامر الحساب` } \n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂"

)

@l313l.ar_cmd(
    pattern="م19",
    command=("م19", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "** اوامر الميوزك | 𝗠𝘂𝘀𝗶𝗰 𝗢𝗿𝗱𝗲𝗿𝘀 🦂\n \n✎┊‌ اختر احدى هذه الاوامر\n ✎┊‌ قبل أستخدام هذه الاوامر يجب تفعيل المود بكتابة ألامر { `.ميوزك تفعيل` } \n- { `.تشغيل_المكالمة` }\n- لتشغيل المحادثة الصوتيه\n- { `.انهاء_المكالمة` }\n-لأنهاء المحادثه الصوتية \n- { `.دعوة` }\n- بالرد على الشخص لدعوته الى المكالمة \n- { `.معلومات_المكالمة` }\n- لعرض عنوان المكالمة وعدد لاشخاص الموجودين فيها \n- { `.تسمية_المكالمة` }\n- لتغير عنوان المكالمة \n- { `.انضمام` }\n- للأنضمام الى المحادثة الصوتية\n- { `.مغادرة` }\n- لمغادرة المحادثة الصوتية \n- { `.تشغيل` }\n-بالرد على رابط اليوتيوب او كتابة الامر مع رابط ليوتيوب لتشغيل الاغنيه \n- { `.قائمة_التشغيل` }\n- لعرض قائمة التشغيل \n- { `.ايقاف_مؤقت` }\n - لأيقاف الاغنية الحالية مؤقتا \n- { `.استمرار` }\n -لأستمرار الاغنيه التي تم ايقافها \n- { `.تخطي` }\n- لتخطي الاغنيه وتشغيل الاغنيه الموجوده في قائمة التشغيل \n\n \nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"



)

@l313l.ar_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** بصمات الميمز | 𝗙𝘂𝗻𝗻𝘆 𝗮𝘂𝗱𝗶𝗼𝘀 🦂:\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.بصمات ميمز` }\n- { `.بصمات ميمز2` }\n- { `.بصمات ميمز3` }\n- { `.بصمات ميمز4` }\n- { `.بصمات ميمز5` }\n- { `.بصمات انمي` } \n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"

)

@l313l.ar_cmd(
    pattern="م21$",
    command=("م21", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "**  تجميع النقاط | 𝗖𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗻𝗴 𝗽𝗼𝗶𝗻𝘁𝘀 🦂 **:\n \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.اوامر التجميع` } \n- { `.اوامر وعد` } \n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂"
        )
