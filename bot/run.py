from aiogram import executor, Dispatcher

import handlers
from data import ADMIN
from loader import dp, bot
from services import setting_commands


async def on_startup(dispatcher: Dispatcher):
    await bot.send_message(ADMIN, '✅ BOT RUNNING')
    await setting_commands.set_default_commands(dispatcher)


async def on_shutdown(dispatcher: Dispatcher):
    await bot.send_message(ADMIN, '⛔️ BOT STOPPED')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
