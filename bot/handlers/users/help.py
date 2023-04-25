from aiogram import types

from loader import dp
from mics import utils


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.answer(utils.text_message_by_language('ua', 'help'))
