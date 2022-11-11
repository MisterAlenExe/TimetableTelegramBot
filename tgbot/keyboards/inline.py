from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Timetable",
                             callback_data="timetable")
    ],
    [
        InlineKeyboardButton(text="Subscribe to notify ❌",
                             callback_data="subscribe_notify")
    ]
])


menu_with_subscribe = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Timetable",
                             callback_data="timetable")
    ],
    [
        InlineKeyboardButton(text="Subscribe to notify ✔️",
                             callback_data="subscribe_notify")
    ]
])


timetable = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Monday",
                             callback_data="monday"),
        InlineKeyboardButton(text="Tuesday",
                             callback_data="tuesday"),
        InlineKeyboardButton(text="Wednesday",
                             callback_data="wednesday")
    ],
    [
        InlineKeyboardButton(text="Thursday",
                             callback_data="thursday"),
        InlineKeyboardButton(text="Friday",
                             callback_data="friday"),
        InlineKeyboardButton(text="Saturday",
                             callback_data="saturday")
    ],
    [
        InlineKeyboardButton(text="Back",
                             callback_data="back_to_menu")
    ]
])

btnBackToTimetable = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Back",
                             callback_data="back_to_timetable")
    ]
])

