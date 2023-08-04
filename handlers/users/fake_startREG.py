from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.menu_kb import menu, menu_uzb
from keyboards.inline.start_INKB import lang, starting_menu, starting_menu_uzb
from loader import dp


@dp.message_handler(commands='start')
async def set_state(msg: types.Message, state: FSMContext):
    await state.set_state('Register')
    await msg.answer('Registration')

@dp.message_handler(state='Register')
async def set_state(msg: types.Message, state: FSMContext):
    await msg.answer('Finish')
    await state.finish()
    await state.set_state('Language')
    await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)

@dp.callback_query_handler(text='back',state='Russian')
@dp.callback_query_handler(text='rus',state='Language')
@dp.message_handler(commands=['menu','start'],state='Russian')
async def rus_contains(call:CallbackQuery, state: FSMContext):
    await call.message.answer('''Я бот - MR_IT.
    Могу помочь вам в следующих операций👇:''',reply_markup=starting_menu)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer('Ожидаю ваш выбор...',reply_markup=menu)
    await state.finish()
    await state.set_state('Russian')

@dp.callback_query_handler(text='back_uzb',state='Uzbek')
@dp.callback_query_handler(text='uzbek',state='Language')
@dp.message_handler(commands=['menu','start'])
async def uzbek_contains(call:CallbackQuery,state:FSMContext):
    await call.message.answer('Men MR_IT - botiman.\nMen sizga quyidagi operatsiyalarda yordam bera olaman👇:', reply_markup=starting_menu_uzb)
    await call.message.delete()
    #call.answer для таблички пользователю, + show alert True
    await call.answer(cache_time=60)
    await call.message.answer('Sizning tanlovingizni kutmoqdamiz...',reply_markup=menu_uzb)
    await state.finish()
    await state.set_state('Uzbek')






