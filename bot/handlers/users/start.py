from aiogram import types

from loader import dp
from mics import utils
from keyboards import reply
from models import User
from .change_language import change_language


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    user = User(message.from_user.id)
    if message.from_user.language_code == 'uk':
        user.language.change('ua')
    await message.delete()
    await message.answer(text=utils.text_message_by_language(user.language.value, 'hello'),
                         reply_markup=reply.menu.get_main_menu_keyboard(user.language.value))
