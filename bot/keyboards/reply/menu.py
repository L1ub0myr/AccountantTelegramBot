from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from mics.utils import text_message_by_language


def get_menu_board(language: str):
    data = text_message_by_language(language, 'buttons')

    buttons = [
        [KeyboardButton(f'💰{data["balance"]}'), KeyboardButton(f'📑{data["categories"]}')],
        [KeyboardButton(f'🧽{data["clean_balance"]}')],
        [KeyboardButton(f'🔄{data["change_language"]}')]
    ]
    board_menu = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return board_menu
