# WRITE  BY VTVIT
# PLUGIN FOR IQUser
# @IQUSER0

from telethon import events
import random, re
from ..Config import Config

from iquser.utils import admin_cmd

import asyncio
from iquser import iqub
from random import choice

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus

plugin_category = "extra"

Command = Config.COMM_ET or "فەرمانەکان"

rehu = [
    "ئەوانەی لە ئازار تێ ئەگەن ...
 پاڵەوانی ڕاستەقینەن🖤.",
]
@iqub.on(admin_cmd(pattern=f"{Command}(?:\s|$)([\s\S]*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        VTVIT = random.choice(rehu)
        await event.edit(
        f": **🖥┊تـەخـتـەی فـەرمـانی 𝙄𝙌𝙐𝙎𝙀𝙍 メ \n🧑🏻‍💻┊بەکارھێـنەر ↶ {mention} \n\n**\n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n( `.م1` )  ⦙ **فـەرمـانـی بـەڕێـوبــەر👾**\n( `.م2` )  ⦙ **فـەرمـانـی گـرووپ👾**\n( `.م3` )  ⦙ **فـەرمـانـی بـەخـێرهاتن و وڵامدانەوە🤍**\n( `.م4` )  ⦙ **پـاراسـتـنی تـایبەت و تێـلەگـراف👾**\n( `.م5` )  ⦙ **فـەرمـانـی تـاگ و لاسـایـیـکردنەوە👾**\n( `.م6` )  ⦙ **فـەرمـانـی داگـرتـن و فـەرهەنگ👾**\n( `.م7` )  ⦙ **فـەرمـانـی ڕێـگـەگـرتـن و قـفل👾**\n( `.م8` )  ⦙ **فـەرمـانـی  پـاکـکردنـەوە و دووبـارەکـردنـەوە👾**\n( `.م9` )  ⦙ **فـەرمـانـی تـایبـەتـمەندی و ڤـار👾**\n( `.م10` ) ⦙ **فـەرمـانـی کـات و کـارکردن👾**\n( `.م11` ) ⦙ **فـەرمـانـی دۆزینەوە و بـەسـتەر👾**\n( `.م12` ) ⦙ **فـەرمـانی یـارمـەتـی و ڕادیـۆ👾** \n( `.م13` ) ⦙ **فـەرمـانـی نـاردنی زکـرەکان🤍**\n( `.م14` ) ⦙ **فـەرمـانـی سـتـیـکەر و گـوگـڵابـەسـتەر👾**\n( `.م15` ) ⦙ **فـەرمانی ڕابواردن میمز وەهەرا👾** \n( `.م16` ) ⦙ **فـەرمـانـی هـاوکـێشـەکان و قـەوارەکان👾**\n( `.م17` ) ⦙ **فەرمانی ناو و زەخرەفە و گیف👾**\n( `.م18` ) ⦙ **فـەرمـانـی ئـەکاونـت و زیـادەکـان👾**\n( `.م19` ) ⦙ **فـەرمـانـی مـیـوزیـك وەکارکردنی👾**\n( `.م20` ) ⦙ **فـەرمـانـی پـەنجەمۆری میمز👾**\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n **᯽︙ {vtvit} **"
)

@iqub.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**🖥 لـیـسـتی فـەرمـانـی بـەڕێـوبـەڕ**:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ یەکێك لەمانەی خوارەوە دابگرە🖤\n\n- ( `.فەرمانی دەرکردن` )\n- ( `.فەرمانی ئاگاداری` )\n- ( `.فەرمانی هەڵواسین` )\n- ( `.فەرمانی سەرپەرشتی` )\n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)
		
@iqub.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**🖥 لـیـسـتـی فـەرمـانـی گـرووپ  **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ یەکێك لە مانەی خوارەوە دابگرە\n\n- ( `.فەرمانی شکێنەر` )\n- ( `.فەرمانی قەدەغەکراوەکان` )\n- ( `.فەرمانی گرووپ` )\n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)

@jepiq.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**🖥 لـیسـتی فـەرمـانـی بـەخـێرھـاتن و وەڵامـدانەوە **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.فەرمانی بەخێرهاتن` )\n- ( `.فەرمانی وەڵامدانەوە` )\n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)
@jepiq.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** hddjj**:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحماية` )\n- ( `.اوامر التلكراف` ) \n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)
@jepiq.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـمنشن والانتحال **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)

@jepiq.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التحميل والترجمه **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر النطق` )\n- ( `.اوامر التحميل` )\n- ( `.اوامر الترجمة` ) \n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)

@jepiq.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر القفل والمنع **:\n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر القفل` )\n- ( `.اوامر الفتح` )\n- ( `.اوامر المنع` ) \n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)

@jepiq.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التكرار والتنظيف **:\n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التكرار` )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)

@jepiq.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة التخصيص والفارات **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التخصيص` )\n لتغير الصور والكلايش كل من الحماية والفحص والبنك\n- ( `.اوامر الفارات` )\n - لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها\n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
		)

@jepiq.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الوقتي والتشغيل **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الاسم` )\n- ( `.اوامر البايو` )\n- ( `.اوامر الكروب الوقتي` )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)	

@jepiq.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الكـشف و الروابط **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الكشف` )\n- ( `.اوامر الروابط` ) \n\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)
@jepiq.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المساعدة  **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الوقت والتاريخ` )\n- ( `.اوامر كورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر مساعدة` )\n- ( `.اوامر الاذاعه` ) \n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)
@jepiq.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الارسال **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.امر الصورة الذاتية` )\n- ( `.اوامر التحذيرات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` ) \n- ( `.اوامر الاذكار` )\n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)
@jepiq.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الملصقات وكوكل **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر كوكل` )\n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7mamo"
)

@jepiq.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التسلية والتحشيش **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n- ( `.اوامر الميمز` )\n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)

@jepiq.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر تحويل الصيغ و الجهات **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"
)

@jepiq.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الحساب و الترفيه **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترفيه` )\n- ( `.اوامر الحساب` ) \n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"

)

@jepiq.ar_cmd(
    pattern="م19",
    command=("م19", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر الميوزك والتشغيل 🎵\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n᯽︙ اختر احدى هذه الاوامر\n ᯽︙ قبل أستخدام هذه الاوامر يجب تفعيل المود بكتابة ألامر ( `.ميوزك تفعيل` ) \n- ( `.تشغيل_المكالمة` )\n- لتشغيل المحادثة الصوتيه\n- ( `.انهاء_المكالمة` )\n-لأنهاء المحادثه الصوتية \n- ( `.دعوة` )\n- بالرد على الشخص لدعوته الى المكالمة \n- ( `.معلومات_المكالمة` )\n- لعرض عنوان المكالمة وعدد لاشخاص الموجودين فيها \n- ( `.تسمية_المكالمة` )\n- لتغير عنوان المكالمة \n- ( `.انضمام` )\n- للأنضمام الى المحادثة الصوتية\n- ( `.مغادرة` )\n- لمغادرة المحادثة الصوتية \n- ( `.تشغيل` )\n-بالرد على رابط اليوتيوب او كتابة الامر مع رابط ليوتيوب لتشغيل الاغنيه \n- ( `.قائمة_التشغيل` )\n- لعرض قائمة التشغيل \n- ( `.ايقاف_مؤقت` )\n - لأيقاف الاغنية الحالية مؤقتا \n- ( `.استمرار` )\n -لأستمرار الاغنيه التي تم ايقافها \n- ( `.تخطي` )\n- لتخطي الاغنيه وتشغيل الاغنيه الموجوده في قائمة التشغيل \n\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"



)

@jepiq.ar_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر بصمات الميمز **:\n ◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.بصمات ميمز` )\n- ( `.بصمات انمي` ) \n◐━─━─━─━─━─**𝙄𝙌**─━─━─━─━─━─◐\n⌔︙CH : @xv7amo"

)
