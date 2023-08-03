from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
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
