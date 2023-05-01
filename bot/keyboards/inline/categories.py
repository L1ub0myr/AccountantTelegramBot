from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from mics.utils import text_message_by_language


def get_inline_keyboard(language: str):
    data = text_message_by_language(language, 'category')

    board_categories = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(f'🍴{data["food"]}', callback_data='food'),
         InlineKeyboardButton(f'🏠{data["utilities"]}', callback_data='utilities')],
        [InlineKeyboardButton(f'🚌{data["transport"]}', callback_data='transport'),
         InlineKeyboardButton(f'👕{data["clothes"]}', callback_data='clothes')],
        [InlineKeyboardButton(f'💊{data["health"]}', callback_data='health'),
         InlineKeyboardButton(f'🧴{data["personal_care"]}', callback_data='personal_care')],
        [InlineKeyboardButton(f'❔{data["other"]}', callback_data='other')],
        [InlineKeyboardButton(f'🛑{data["cancel"]}', callback_data='cancel')]
    ])

    return board_categories
