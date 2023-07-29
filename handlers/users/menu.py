from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types import ReplyKeyboardRemove

from loader import dp
from keyboards.default.menu_kb import menu

@dp.message_handler(commands='menu')
async def show_menu(msg:types.Message):
    await msg.answer('Choose',reply_markup=menu)
