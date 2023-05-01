from aiogram import types

from loader import dp
from mics import utils
from models import User


@dp.message_handler()
async def other_message(message: types.Message):
    user = User(message.from_user.id)
    await message.delete()
    await message.answer(utils.text_message_by_language(user.language.value, 'other'))
