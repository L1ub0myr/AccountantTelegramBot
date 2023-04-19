from aiogram import Dispatcher, Bot
from aiogram.types import ParseMode

from data import TOKEN


bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)
