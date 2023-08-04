from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.inline.start_INKB import lang
from loader import dp


@dp.message_handler(commands='lang',state=['Russian','Uzbek'])
async def set_state(msg: types.Message, state: FSMContext):
    await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)
    await state.set_state('Language')

@dp.callback_query_handler(text='rus',state='Language')
async def russian_plus(call:CallbackQuery,state: FSMContext):
    await call.message.answer('Язык был успешно изменен на русский.\nВы можете нажать Основное меню👇')
    await state.finish()
    await state.set_state('Russian')

@dp.callback_query_handler(text='uzbek',state='Language')
async def russian_plus(call:CallbackQuery,state: FSMContext):
    await call.message.answer('Til uzbek tiliga muvaffaqiyatli almashtirildi.\nAsosiy menyudan foydalanishingiz mumkin👇')
    await state.finish()
    await state.set_state('Uzbek')
