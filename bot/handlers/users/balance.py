from aiogram import types

from loader import dp
from keyboards import inline
from models import User
from mics import utils


message_balance = ('💰Balance', '💰Баланс')
message_categories = ('📑Balance by categories', '📑Баланс по категоріям')
message_clean = ('🧽Очистити баланс', '🧽Clean the balance')


@dp.message_handler(lambda message: message.text in message_balance)
async def get_balance(message: types.Message):
    user = User(message.from_user.id)
    data = utils.text_message_by_language(user.language.value, 'buttons')
    await message.delete()
    currency = '$' if user.language == 'en' else '₴'
    await message.answer(f'<i>{data["balance"]}</i>: <b>{user.wallet.balance}</b> {currency}')


@dp.message_handler(lambda message: message.text in message_categories)
async def get_balance_with_category(message: types.Message):
    user = User(message.from_user.id)
    data = utils.text_message_by_language(user.language.value, 'category')
    currency = '$' if user.language == 'en' else '₴'
    await message.answer('-' * 30)
    for key, value in data.items():
        if key == 'cancel':
            break
        money = user.buying_category.get_money_from_category(key)
        percentage = (money * 100)/user.wallet.balance if money != 0 else 0
        await message.answer(f"{value} - <b>{user.buying_category.get_money_from_category(key)}</b> {currency} "
                             f"({percentage:.2f}%)")
    await message.answer('-' * 30)


@dp.message_handler(lambda message: message.text in message_clean)
async def clean_balance(message: types.Message):
    user = User(message.from_user.id)
    data = utils.text_message_by_language(user.language.value, 'answer')
    await message.delete()
    await message.answer(data['sure'], reply_markup=inline.clean_balance.get_answer_board(user.language.value))
