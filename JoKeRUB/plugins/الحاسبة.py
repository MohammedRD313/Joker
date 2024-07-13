import io
import sys
import traceback

from JoKeRUB import l313l
plugin_category = "الادوات"


@l313l.ar_cmd(pattern="الحاسبة")
async def hi(event):
    await edit_or_reply(
        event,
        "**الحاسبة | 𝗖𝗮𝗹𝗰𝘂𝗹𝗮𝘁𝗼𝗿 🦂**\n\nالامر:`.احسب` + حاصل جمع رقمين\n مثال :`.احسب 1+1`",
        link_preview=False,
    )

@l313l.ar_cmd(
    pattern="احسب ([\\s\\S]*)",
    command=("احسب", plugin_category),
    info={
        "header": "لـ حل المعـادلات والمسائـل الرياضيـه",
        "الاستخـدام": "{tr}احسب 2+9",
    },
)
async def calculator(event):
    "لـ حل المعـادلات والمسائـل الرياضيـه"
    cmd = event.text.split(" ", maxsplit=1)[1]
    event = await edit_or_reply(event, "**✎┊‌جـارِ الحـل .. انتظـر**")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    san = f"print({cmd})"
    try:
        await aexec(san, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "اسف لايمكنني حلها"
    final_output = "**📟╎المعـادلـة ⇜** `{}` \n\n**💡╎الحـل ⇜** `{}` \n".format(
        cmd, evaluation
    )
    await event.edit(final_output)


async def aexec(code, event):
    exec("async def __aexec(event): " + "".join(f"\n {l}" for l in code.split("\n")))

    return await locals()["__aexec"](event)
