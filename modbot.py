import asyncio
import logging

import bot
import api



async def main():
    await asyncio.gather(bot.run_bot(), api.run_api())

if __name__ == "__main__":
    asyncio.run(main())
