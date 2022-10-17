from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline import menu, timetable, btnBackToTimetable

data_timetable = {
    'monday': "08:00-08:50 - Introduction to Programming - C1.2.237L",
    'tuesday': "09:00-09:50 - Foreign Language - C1.1.228P\n"
               "10:00-10:50 - Foreign Language - C1.1.228P\n"
               "11:00-11:50 - Psychology - C1.2.226P\n"
               "12:00-12:50 - Political Science - C1.1.344P ",
    'wednesday': "10:00-10:50 - Physical Culture - gym\n"
                 "11:00-11:50 - Physical Culture - gym",
    'thursday': "12:00-12:50 - Introduction to Programming - C1.2.229K",
    'friday': "08:00-08:50 - Information and Communication Technologies - C1.1.348K\n"
              "09:00-09:50 - Information and Communication Technologies - C1.1.348K\n"
              "10:00-10:50 - Foreign Language - C1.2.221P",
    'saturday': "08:00-08:50 - Discrete Mathematics - C1.1.328L\n"
                "09:00-09:50 - Discrete Mathematics - C1.1.328L\n"
                "10:00-10:50 - Introduction to Programming - C1.2.229"
}


async def show_menu(message: Message):
    await message.answer("Choose one button and click:", reply_markup=menu)


async def show_menu_talking(call: CallbackQuery):
    await call.answer(cache_time=0)
    await call.message.answer("You chose talking to AI")


async def show_menu_timetable(call: CallbackQuery):
    await call.message.edit_text("Choose day of week and click:", reply_markup=timetable)


async def show_timetable(call: CallbackQuery):
    if call.data != "back_to_menu":
        await call.message.edit_text(f"Your timetable on {call.data[0].upper() + call.data[1:]}:"
                                     f"\n\n{data_timetable[call.data]}", reply_markup=btnBackToTimetable)
    else:
        await call.message.edit_text("Choose one button and click", reply_markup=menu)


async def show_menu_settings(call: CallbackQuery):
    await call.answer(cache_time=0)
    await call.message.answer("You chose settings")


def register_menu(dp: Dispatcher):
    dp.register_message_handler(show_menu, commands=["menu"])


def register_callback_menu(dp: Dispatcher):
    dp.register_callback_query_handler(show_menu_talking, text="talking_to_ai")
    dp.register_callback_query_handler(show_menu_timetable, text=["timetable", "back_to_timetable"])
    dp.register_callback_query_handler(show_menu_settings, text="settings")
    dp.register_callback_query_handler(show_timetable, text=["monday", "tuesday", "wednesday", "thursday",
                                                             "friday", "saturday", "back_to_menu"])
