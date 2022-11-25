import json
import calendar
from datetime import date

from aiogram import Bot

from tgbot.utils.logger import logger
from tgbot.database.storage import Database
from tgbot.keyboards.inline import add_delete_button


async def send_message_cron(bot: Bot):
    today_date = calendar.day_name[date.today().weekday()].lower()
    with open(r"tgbot/handlers/timetable.json") as file:
        text = json.load(file)[today_date]
    with Database() as db:
        for user_id in db.get_users_notify().keys():
            await bot.send_message(chat_id=user_id, text=text, reply_markup=add_delete_button())
            logger.info(f"{user_id} - notify submitted")


def register_schedulers(bot, scheduler):
    scheduler.add_job(send_message_cron, 'cron', day_of_week='mon-sat', hour=7, minute=0, kwargs={'bot': bot})
