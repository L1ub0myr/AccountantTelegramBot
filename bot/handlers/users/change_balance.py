from aiogram import types

from loader import dp
from mics import utils
from models import User
from keyboards.inline.categories import get_category_keyboard


@dp.message_handler(lambda message: utils.number_is_message(message.text))
async def add_money(message: types.Message):
    user = User(message.from_user.id)
    await message.delete()
    await message.answer(message.text, reply_markup=get_category_keyboard(user.language.value))


@dp.message_handler(lambda message: message.text[0] == '-')
async def minus_money(message: types.Message):
    user = User(message.from_user.id)
    await message.delete()
    try:
        user.wallet.minus(float(message.text[1:]))
        await message.answer(message.text)
    except ValueError:
        return


@dp.callback_query_handler(lambda callback: callback.data in ('yes', 'no'))
async def clean_balance_user(callback: types.CallbackQuery):
    if callback.data == 'yes':
        user = User(callback.from_user.id)
        data = utils.text_message_by_language(user.language.value, "answer")
        user.wallet.clean()
        user.buying_category.clean_all_categories()
        await callback.message.answer(data['completed'])
        await callback.message.delete()
    else:
        await callback.message.delete()
