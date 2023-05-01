from aiogram import types

from loader import dp
from mics import utils
from models import User


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    user = User(message.from_user.id)
    await message.answer(utils.text_message_by_language(user.language.value, 'help'))
