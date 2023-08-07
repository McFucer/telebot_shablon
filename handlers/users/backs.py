from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from keyboards.inline.start_INKB import courses, courses_uzb, starting_menu_uzb

from keyboards.inline.start_INKB import starting_menu, lang, courses
from loader import dp
from keyboards.default.menu_kb import menu, menu_uzb


@dp.message_handler(commands=['menu','start'],state='Russian')
async def rus_contain(msg:types.Message):
    await msg.answer('''Я бот - MR_IT.
Могу помочь вам в следующих операций👇:
<code>https://t.me/mr_it_uz</code>''',reply_markup=starting_menu)
    await msg.delete()


@dp.message_handler(commands=['menu','start'],state='Uzbek')
async def uzbek_contains(msg:types.Message):
    await msg.answer('Men MR_IT - botiman.\nMen sizga quyidagi operatsiyalarda yordam bera olaman👇:\n<code>https://t.me/mr_it_uz</code>', reply_markup=starting_menu_uzb)
    await msg.delete()

WARNING = '''EDIT_REPLY_MARKUP ДЛЯ ИЗМЕНЕНИЕ инлайн кнопок'''
@dp.callback_query_handler(text='back_from_courses',state='Uzbek')
@dp.callback_query_handler(text='back_uzb',state='Uzbek')
async def uzbek_contains(call:CallbackQuery,state:FSMContext):
    await call.message.edit_text('Men MR_IT - botiman.\nMen sizga quyidagi operatsiyalarda yordam bera olaman👇:\n<code>https://t.me/mr_it_uz</code>')
    await call.message.edit_reply_markup(reply_markup=starting_menu_uzb)


@dp.callback_query_handler(text='back_from_courses',state='Russian')
@dp.callback_query_handler(text='back',state='Russian')
async def rus_contains(call:CallbackQuery, state: FSMContext):

    await call.message.edit_text('Я бот - MR_IT.\nМогу помочь вам в следующих операций👇:<code>https://t.me/mr_it_uz</code>')

    await call.message.edit_reply_markup(reply_markup=starting_menu)


