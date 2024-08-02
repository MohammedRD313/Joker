import asyncio
from randomstuff import AsyncClient
from .Config import Config

async def main():
    rs_client = AsyncClient(api_key=Config.RANDOM_STUFF_API_KEY, version="4")
    # قم بإجراء عملياتك مع rs_client هنا

if __name__ == '__main__':
    asyncio.run(main())
