from aiogram import types

from loader import dp
from keyboards import inline, reply
from models import User
from mics import utils


balance_menu_messages = ('BALANCE MENU 🪪', 'МЕНЮ БАЛАНСА 🪪')
balance_messages = ('BALANCE 💰', 'БАЛАНС 💰')
categories_messages = ('BALANCE BY CATEGORIES 🗄️', 'БАЛАНС ПО КАТЕГОРІЯМ 🗄️')
balance_clean_messages = ('CLEAN THE BALANCE 🆑', 'ОЧИСТИТИ БАЛАНС 🆑')
back_message = ('BACK 👈', 'НАЗАД 👈')


@dp.message_handler(lambda message: message.text in balance_menu_messages)
async def balance_menu(message: types.Message):
    user = User(message.from_user.id)
    data = utils.text_message_by_language(user.language.value, 'buttons')
    await message.delete()
    await message.answer(f'{data["balance_menu"]}',
                         reply_markup=reply.balance_menu.get_balance_menu_keyboard(user.language.value))


@dp.message_handler(lambda message: message.text in balance_messages)
async def get_balance(message: types.Message):
    user = User(message.from_user.id)
    data = utils.text_message_by_language(user.language.value, 'buttons')
    await message.delete()
    currency = '$' if user.language.value == 'en' else '₴'
    await message.answer(f'{data["balance"]}:  <b>{user.wallet.balance}</b> {currency}')


@dp.message_handler(lambda message: message.text in categories_messages)
async def get_balance_with_category(message: types.Message):
    user = User(message.from_user.id)
    data = utils.text_message_by_language(user.language.value, 'category')
    currency = '$' if user.language == 'en' else '₴'
    await message.answer('-' * 30)
    for key, value in data.items():
        if key == 'cancel':
            break
        money = user.buying_category.get_money_from_category(key)
        try:
            percentage = (money * 100)/user.wallet.balance
        except ZeroDivisionError:
            percentage = 0
        await message.answer(f"{value} - <b>{user.buying_category.get_money_from_category(key)}</b> {currency} "
                             f"({percentage:.1f}%)")
    await message.answer('-' * 30)


@dp.message_handler(lambda message: message.text in balance_clean_messages)
async def clean_balance(message: types.Message):
    user = User(message.from_user.id)
    data = utils.text_message_by_language(user.language.value, 'answer')
    await message.delete()
    await message.answer(data['sure'], reply_markup=inline.clean_balance.get_answer_keyboard(user.language.value))


@dp.message_handler(lambda message: message.text in back_message)
async def balance_menu(message: types.Message):
    user = User(message.from_user.id)
    await message.delete()
    await message.answer(message.text,
                         reply_markup=reply.menu.get_main_menu_keyboard(user.language.value))
