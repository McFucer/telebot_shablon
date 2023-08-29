import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer('dddddddd')