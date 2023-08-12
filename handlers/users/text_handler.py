from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types import ReplyKeyboardRemove

from loader import dp

@dp.message_handler(Text(equals='Основное меню',ignore_case=True), state='Russian')
async def text_hand(msg: types.Message):
    await msg.reply('Я тоже за Узбекистан')
#startwith, endswith, contains