import calendar
from datetime import date

from aiogram import Dispatcher
from aiogram import types

from ..database.db import db_start, db_add_new_user_notify, db_get_users_notify, db_delete_user_notify
from .menu import data_timetable


async def cmd_add_new_user(message: types.Message):
    args = message.get_args().split()
    if args is None or not len(args) == 2 or not args[0].isdigit():
        await message.answer("Invalid arguments. Try again!")
    else:
        await db_add_new_user_notify(args[0], args[1])


async def cmd_delete_user(message: types.Message):
    args = message.get_args()
    if args is None or not args.isdigit():
        await message.answer("Invalid arguments. Try again!")
    else:
        await db_delete_user_notify(args)


async def cmd_create_db(message: types.Message):
    await db_start()
    await message.answer("Database is created.")


async def cmd_get_users(message: types.Message):
    users = await db_get_users_notify()
    await message.answer(users)


async def daily_notify(bot):
    my_date = calendar.day_name[date.today().weekday()].lower()
    for user_id in await db_get_users_notify():
        await bot.send_message(chat_id=user_id, text=f"Daily notify!!!\n\n"
                                                     f"Your timetable on {my_date[0].upper() + my_date[1:]}:\n\n"
                                                     f"{data_timetable[my_date]}")


def register_notify_cmd(dp: Dispatcher):
    dp.register_message_handler(cmd_add_new_user, commands=["add_user"], is_admin=True)
    dp.register_message_handler(cmd_create_db, commands=["create_db"], is_admin=True)
    dp.register_message_handler(cmd_get_users, commands=["get_users"], is_admin=True)
    dp.register_message_handler(cmd_delete_user, commands=["delete_user"], is_admin=True)
