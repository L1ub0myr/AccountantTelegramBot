from aiogram import types

from loader import dp
from mics import utils
from keyboards import inline
from models import User


words = ('🔄Change Language', '🔄Змінити мову')


@dp.message_handler(lambda message: message.text in words)
async def command_language(message: types.Message):
    user = User(message.from_user.id)
    await message.delete()
    await message.answer(utils.text_message_by_language(user.language.value, 'language'),
                         reply_markup=inline.language.board_language)
