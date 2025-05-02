import asyncio
import signal
import logging

import bot
import api

logger = logging.getLogger(__name__)

async def shutdown(signal, loop):
    print(f"Received exit signal {signal.name}")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

    list(map(lambda task: task.cancel(), tasks))
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()

async def main():
    logging.basicConfig(filename="modbot.log", level=logging.INFO, format="%(asctime)-2s  %(levelname)-8s :: %(name)-15s :: %(message)s")
    logger.info("Starting")

    loop = asyncio.get_running_loop()

    for s in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(s, lambda s=s: asyncio.create_task(shutdown(s, loop)))

    try:
        await asyncio.gather(bot.run_bot(), api.run_api())
    except asyncio.CancelledError:
        print("Tasks were cancelled")

    logger.info("App stopped")

if __name__ == "__main__":
    asyncio.run(main())
