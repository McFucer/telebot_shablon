from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from loader import dp

@dp.message_handler(Text(equals='Узбекистан',ignore_case=True))
async def text_hand(msg: types.Message):
    await msg.reply('Я тоже за Узбекистан')
#startwith, endswith, contains