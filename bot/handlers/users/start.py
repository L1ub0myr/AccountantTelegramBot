from aiogram import types

from loader import dp
from mics import utils


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(utils.text_message_by_language('ua', 'hello'))
