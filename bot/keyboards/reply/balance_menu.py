from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from mics.utils import text_message_by_language


def get_balance_menu_keyboard(language: str):
    data = text_message_by_language(language, 'buttons')

    buttons = [
        [KeyboardButton(f'{data["balance"]} 💰'), KeyboardButton(f'{data["categories"]} 🗄️')],
        [KeyboardButton(f'{data["clean_balance"]} 🆑')],
        [KeyboardButton(f'{data["back"]} 👈')]
    ]
    board_menu = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return board_menu
