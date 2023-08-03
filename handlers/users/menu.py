from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from keyboards.inline.start_INKB import courses

from keyboards.inline.start_INKB import starting_menu, lang, courses
from loader import dp
from keyboards.default.menu_kb import menu


@dp.callback_query_handler(text='Test',state='Testing')
async def test(call:CallbackQuery):
    await call.message.answer('Kakdela')
    await call.answer(cache_time=30)

@dp.callback_query_handler(text='courses',state='Testing')
async def test(call:CallbackQuery):
    await call.message.answer('Список курсов', reply_markup=courses)
    await call.answer(cache_time=30)

