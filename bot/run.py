from aiogram import executor

from loader import dp


async def on_startup(dp):
    pass


async def on_shutdown(dp):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
