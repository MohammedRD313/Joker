# فريق العقرب 
# علوش @ZS_SQ
# محمد @Zo_r0

import asyncio
import os
import contextlib
import random
import sys
from asyncio.exceptions import CancelledError
import requests
import heroku3
import urllib3
from telethon import events 
from JoKeRUB import HEROKU_APP, UPSTREAM_REPO_URL, l313l
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import delgvar
plugin_category = "utils"
ashour = [
    "نبي الله آدم",
    "نبي الله أدريس",
    "نبي الله نوح",
    "نبي الله هود",
    "نبي الله صالح",
    "نبي الله محمد خاتم الأنبياء والرسل اللهم صلِّ على محمد وآله وصحبه أجمعين",
  "نبي الله ابراهيم",
    "نبي الله لوط",
    "نبي الله أسماعيل",
    "نبي الله أسحاق",
    "نبي الله يعقوب",
    "نبي الله يوسف", 
    "نبي الله أيوب", 
    "نبي الله شعيب", 
    "نبي الله موسى", 
    "نبي الله هارون", 
    "نبي الله يونس", 
    "نبي الله داود", 
    "نبي الله سليمان", 
    "نبي الله ألياس", 
    "نبي الله أليسع", 
    "نبي الله زكريا", 
    "نبي الله يحيى", 
    "نبي الله عيسى", 
    ""
]

@l313l.ar_cmd(
    pattern="نبي$",
    command=("نبي", plugin_category),
    info={
        "header": "Get random qusts about نبي (Ashura).",
        "usage": "{tr}نبي",
    },
)
async def ashura_info(event):
    ahsouralshen = random.choice(ashour)
    await edit_or_reply(event, ahsouralshen)