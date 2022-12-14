from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def add_delete_button(kb: types.inline_keyboard = None):
    if kb is None:
        kb = InlineKeyboardMarkup()
    del_btn = InlineKeyboardButton("Delete", callback_data="delete")
    kb.add(del_btn)
    return kb


def add_menu_button():
    kb = InlineKeyboardMarkup()
    menu_btn = InlineKeyboardButton("Timetable", callback_data="timetable")
    kb.add(menu_btn)
    return kb


def add_subscription_button(kb, is_subcribed: bool):
    if is_subcribed:
        sub_btn = InlineKeyboardButton("Subscribe to notify ✔️", callback_data="sub_notify")
    else:
        sub_btn = InlineKeyboardButton("Subscribe to notify ❌", callback_data="sub_notify")
    kb.add(sub_btn)
    return kb


def add_timetable_buttons():
    kb = InlineKeyboardMarkup(inline_keyboard=[
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
    return kb


def add_back_button():
    kb = InlineKeyboardMarkup()
    back_btn = InlineKeyboardButton(text="Back", callback_data="back_to_timetable")
    kb.add(back_btn)
    return kb
