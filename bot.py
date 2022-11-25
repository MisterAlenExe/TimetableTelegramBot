import asyncio
import warnings
from pytz_deprecation_shim import PytzUsageWarning

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta

from tgbot.logger import logger
from tgbot.config import load_config

from tgbot.handlers.menu import register_menu
from tgbot.handlers.scheduler import register_schedulers
from tgbot.middlewares.apscheduler import SchedulerMiddleware


def register_all_middlewares(dp, scheduler):
    dp.setup_middleware(SchedulerMiddleware(scheduler))


def register_all_handlers(dp, bot, scheduler):
    register_menu(dp)
    register_schedulers(bot, scheduler)


async def main():
    warnings.filterwarnings(action="ignore", category=PytzUsageWarning)
    data_config = load_config()

    logger.info("Starting bot")

    bot = Bot(token=data_config['bot_token'])
    dp = Dispatcher(bot, storage=MemoryStorage())
    scheduler = AsyncIOScheduler(timezone="Asia/Almaty")

    register_all_middlewares(dp, scheduler)
    register_all_handlers(dp, bot, scheduler)

    try:
        scheduler.start()
        await dp.start_polling()
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped")
