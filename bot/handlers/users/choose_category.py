from aiogram import types

from loader import dp
from models import User
from mics import utils


@dp.callback_query_handler(lambda callback: callback.data == "cancel")
async def cancel(callback: types.CallbackQuery):
    user = User(callback.from_user.id)
    data = utils.text_message_by_language(user.language.value, 'category')
    await callback.answer(data['cancel'])
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data)
async def choose_language(callback: types.CallbackQuery):
    user = User(callback.from_user.id)
    value = callback.message.text
    if ',' in value:
        value = value.replace(',', '.')
    if value[0] == '-':
        user.wallet.minus(float(value[1:]))
    else:
        user.wallet.plus(float(value))
    user.buying_category.add_money_for_category(float(value), callback.data)
    await callback.answer(f'+ {callback.message.text} - {callback.data.title()}', show_alert=True)
    await callback.message.delete()
