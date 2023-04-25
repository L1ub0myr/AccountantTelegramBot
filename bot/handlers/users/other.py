from aiogram import types

from loader import dp
from mics import utils


@dp.message_handler()
async def other_message(message: types.Message):
    await message.answer(utils.text_message_by_language('ua', 'other'))
