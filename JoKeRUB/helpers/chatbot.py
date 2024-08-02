import asyncio
from randomstuff import AsyncClient
from .Config import Config

loop = asyncio.get_event_loop()
rs_client = None

async def initialize_client():
    global rs_client
    rs_client = AsyncClient(api_key=Config.RANDOM_STUFF_API_KEY, version="4")

# تأكد من استدعاء `initialize_client` في السياق المناسب
if not loop.is_running():
    loop.run_until_complete(initialize_client())
else:
    asyncio.ensure_future(initialize_client())
