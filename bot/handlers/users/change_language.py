from aiogram import types

from loader import dp
from models import User
from . import start


@dp.callback_query_handler(lambda callback: callback.data in ("en", "ua"))
async def change_language(callback: types.CallbackQuery):
    user = User(callback.from_user.id)
    user.language.change(callback.data)
    await callback.answer(callback.data)
    await start.command_start(callback.message)
