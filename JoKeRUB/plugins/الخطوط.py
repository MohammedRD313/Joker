# Qrh9 - RIO
# © SHRU Team 2023
# ها شعدك داخل ع الملف تريد تخمط ؟ ابو زربة لهل درجة فاشل  
from telethon import events
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete
from telethon import functions
from telethon.errors.rpcerrorlist import MessageIdInvalidError
@l313l.on(admin_cmd(pattern="(إيقاف الخط الغامق|الخط الغامق)"))
async def btext(event):
    isbold = gvarstatus("bold")
    if not isbold:
        addgvar ("bold", "on")
        await edit_delete(event, "**✎┊‌ تم تفعيل خط الغامق بنجاح ✓**")
        return

    if isbold:
        delgvar("bold")
        await edit_delete(event, "**✎┊‌ تم اطفاء خط الغامق بنجاح ✓ **")
        return
@l313l.on(admin_cmd(pattern="(ايقاف خط البرمجة|خط البرمجة)"))
async def btext(event):
    isprogramming = gvarstatus("programming")
    if not isprogramming:
        addgvar("programming", "on")
        await edit_delete(event, "**✎┊‌ تم تفعيل خط البرمجة بنجاح ✓**")
        return

    if isprogramming:
        delgvar("programming")
        await edit_delete(event, "**✎┊‌ تم اطفاء خط البرمجة بنجاح ✓ **")
        return
@l313l.on(admin_cmd(pattern="(خط الرمز|ايقاف خط الرمز)"))
async def btext(event):
    isramz = gvarstatus("ramz")
    if not isramz:
        addgvar ("ramz", "on")
        await edit_delete(event, "**✎┊‌ تم تفعيل خط الرمز بنجاح ✓**")
        return

    if isramz:
        delgvar("ramz")
        await edit_delete(event, "**✎┊‌ تم اطفاء خط الرمز بنجاح ✓ **")
        return

@l313l.on(admin_cmd(pattern="(خط العقرب|ايقاف خط العقرب)"))
async def Aljoker(event):
    Aljoker = gvarstatus("ramz")
    if not Aljoker:
        addgvar ("ramz", "on")
        await edit_delete(event, "✎┊‌ تم تفعيل خط العقرب بنجاح ✓")
        return

    if Aljoker:
        delgvar("ramz")
        await edit_delete(event, "✎┊‌ تم اطفاء خط العقرب بنجاح ✓ ")
        return

@l313l.on(admin_cmd(pattern="(خط بايثون|ايقاف خط بايثون)"))
async def btext(event):
    ispython = gvarstatus("python")
    if not ispython:
        addgvar ("python", "on")
        await edit_delete(event, "**✎┊‌ تم تفعيل خط بايثون بنجاح ✓**")
        return

    if ispython:
        delgvar("python")
        await edit_delete(event, "**✎┊‌ تم اطفاء خط بايثون بنجاح ✓ **")
        return  
@l313l.on(events.NewMessage(outgoing=True))
async def reda(event):
    isbold = gvarstatus("bold")
    if isbold:
        try:
            await event.edit(f"**{event.message.message}**")
        except MessageIdInvalidError:
            pass

    isramz = gvarstatus("ramz")
    if isramz:
        try:
            await event.edit(f"`{event.message.message}`")
        except MessageIdInvalidError:
            pass

    ispython = gvarstatus("python")
    if ispython:
        try:
            await event.edit(f"```Python \n print('{event.message.message}') \n```")
        except MessageIdInvalidError:
            pass
    
    isprogramming = gvarstatus("programming")
    if isprogramming:
        try:
            await event.edit(f"```{event.message.message}```")
        except MessageIdInvalidError:
            pass
