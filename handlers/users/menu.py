from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from keyboards.inline.start_INKB import courses, courses_uzb

from keyboards.inline.start_INKB import starting_menu, lang, courses
from loader import dp
from keyboards.default.menu_kb import menu


@dp.callback_query_handler(text='courses',state='Russian')
async def test(call:CallbackQuery):
    await call.message.answer('Вот список курсов которые у нас имеются👇:',reply_markup=courses)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='courses_uzb',state='Uzbek')
async def test(call:CallbackQuery):
    await call.message.answer("Mana bizda mavjud bo'lgan kurslar ro'yxati👇:", reply_markup=courses_uzb)
    await call.message.delete()
    await call.answer(cache_time=60)

