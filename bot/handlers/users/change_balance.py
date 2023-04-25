from aiogram import types

from loader import dp
from mics import utils
from models import Wallet


@dp.message_handler(lambda message: utils.number_is_message(message.text))
async def add_money(message: types.Message):
    user = Wallet(message.from_user.id)
    if message.text[0] == '-':
        user.minus(float(message.text[1:]))
    else:
        user.plus(float(message.text))
    await message.answer(f"Balance: {user.balance}")
