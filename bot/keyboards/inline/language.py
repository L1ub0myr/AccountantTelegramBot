from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


board_language = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('🇺🇦Українська', callback_data='ua'),
     InlineKeyboardButton('🇬🇧English', callback_data='en')]
])
