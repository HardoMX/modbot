import asyncio
import logging

import bot
import api

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(filename="modbot.log", level=logging.INFO, format="%(asctime)-2s  %(levelname)-8s :: %(name)-15s :: %(message)s")
    logger.info("Starting")
    await asyncio.gather(bot.run_bot(), api.run_api())
    logger.info("Finished")

if __name__ == "__main__":
    asyncio.run(main())
