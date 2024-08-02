from . import fonts
from . import memeshelper as catmemes
from .aiohttp_helper import AioHttp
from .utils import *
from .some_module import post_to_telegraph
from .some_module import time_formatter
from .some_module import sanga_seperator
from .some_module import readable_time
from .some_module import media_type
flag = True
check = 0
while flag:
    try:
        from .chatbot import *
        from .functions import *
        from .memeifyhelpers import *
        from .progress import *
        from .qhelper import process
        from .tools import *
        from .utils import _cattools, _catutils, _format

        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break
