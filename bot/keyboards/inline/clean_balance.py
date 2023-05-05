from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from mics import utils


def get_answer_keyboard(language: str):
    data = utils.text_message_by_language(language, 'answer')

    answer = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(f'{data["yes"]} ✅', callback_data='yes'),
         InlineKeyboardButton(f'{data["no"]} ⛔️', callback_data='no')]
    ])

    return answer
