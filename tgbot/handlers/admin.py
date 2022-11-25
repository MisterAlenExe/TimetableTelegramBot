from aiogram import Dispatcher, types

from tgbot.utils.logger import logger, print_msg

from tgbot.database.storage import Database
from tgbot.keyboards.inline import add_delete_button


@print_msg
async def output_users_notify(message: types.Message):
    text = ""
    with Database() as db:
        for user_id, user_name in db.get_users_notify().items():
            text += f"{user_id} - {user_name}\n"
    if text == "":
        text = "There are no any users in database"
    await message.reply(text, reply_markup=add_delete_button())


def register_admin(dp: Dispatcher):
    dp.register_message_handler(output_users_notify, commands=['get_users'], is_admin=True)
