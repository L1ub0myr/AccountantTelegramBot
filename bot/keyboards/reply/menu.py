from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from mics.utils import text_message_by_language


def get_main_menu_keyboard(language: str):
    data = text_message_by_language(language, 'buttons')

    buttons = [
        [KeyboardButton(f'{data["balance_menu"]} 🪪')],
        [KeyboardButton(f'{data["change_language"]} 🔄')]
    ]
    board_menu = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return board_menu
