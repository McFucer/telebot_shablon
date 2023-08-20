from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.inline.start_INKB import lang, starting_menu_uzb, starting_menu
from loader import dp


@dp.message_handler(commands='lang',state=['Russian','Uzbek'])
async def set_state(msg: types.Message, state: FSMContext):
    await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)
    await state.set_state('Language')

@dp.callback_query_handler(text='rus',state='Language')
async def russian_plus(call:CallbackQuery,state: FSMContext):
    await call.message.answer('''Я бот - MR_IT.
    Могу помочь вам в следующих операций👇:
    <code>https://t.me/mr_it_uz</code>''',reply_markup=starting_menu)
    await state.finish()
    await state.set_state('Russian')

@dp.callback_query_handler(text='uzbek',state='Language')
async def russian_plus(call:CallbackQuery,state: FSMContext):
    await call.message.answer('Men MR_IT - botiman.\nMen sizga quyidagi operatsiyalarda yordam bera olaman👇:\n<code>https://t.me/mr_it_uz</code>', reply_markup=starting_menu_uzb)
    await state.finish()
    await state.set_state('Uzbek')
