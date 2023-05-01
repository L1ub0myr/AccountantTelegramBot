from aiogram import types

from loader import dp
from mics import utils
from models import User
from keyboards.inline.categories import get_inline_keyboard
from .balance import get_balance


@dp.message_handler(lambda message: utils.number_is_message(message.text))
async def add_money(message: types.Message):
    user = User(message.from_user.id)
    await message.delete()
    await message.answer(message.text, reply_markup=get_inline_keyboard(user.language.value))


@dp.callback_query_handler(lambda callback: callback.data in ('yes', 'no'))
async def yes_no_answer(callback: types.CallbackQuery):
    if callback.data == 'yes':
        user = User(callback.from_user.id)
        data = utils.text_message_by_language(user.language.value, "answer")
        user.wallet.clean()
        user.buying_category.clean_all_categories()
        await callback.message.answer(data['completed'])
        await get_balance(callback.message)
    else:
        await callback.message.delete()
