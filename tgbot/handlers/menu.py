from aiogram import Dispatcher, types

from tgbot.logger import logger, print_msg

from tgbot.database.storage import Database
from tgbot.keyboards.inline import add_delete_button, add_menu_button, add_subscription_button


@print_msg
async def start(message: types.Message):
    text = "Hello!\n" \
           "I am Timetable Telegram Bot\n\n" \
           "My functions:\n" \
           "- providing timetable\n" \
           "- daily notifying about timetable"
    await message.reply(text, reply_markup=add_delete_button())


@print_msg
async def menu(message: types.Message):
    text = "Choose one button and click:"
    with Database() as db:
        if message.from_user.id in db.get_users_notify().keys():
            kb = add_subscription_button(add_menu_button(), is_subcribed=True)
        else:
            kb = add_subscription_button(add_menu_button(), is_subcribed=False)
    await message.reply(text, reply_markup=kb)


async def subscribe_notify(call: types.CallbackQuery):
    text = "Choose one button and click:"
    kb = add_menu_button()
    with Database() as db:
        if call.from_user.id in db.get_users_notify().keys():
            kb = add_subscription_button(kb, is_subcribed=False)
            await call.message.edit_text(text, reply_markup=kb)
            db.delete_user_notify(call.from_user.id)
        else:
            kb = add_subscription_button(kb, is_subcribed=True)
            await call.message.edit_text(text, reply_markup=kb)
            db.add_user_notify(call.from_user.id, call.from_user.full_name)
    await call.answer()


async def delete_message(call: types.CallbackQuery):
    try:
        await call.bot.delete_message(call.message.chat.id, call.message.message_id)
        if call.message.reply_to_message:
            await call.bot.delete_message(call.message.chat.id, call.message.reply_to_message.message_id)
        await call.answer()
    except Exception as error:
        logger.error(error)
        await call.answer("Error")


def register_menu(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(menu, commands=['menu'])

    dp.register_callback_query_handler(subscribe_notify, text='sub_notify')
    dp.register_callback_query_handler(delete_message, text='delete')
