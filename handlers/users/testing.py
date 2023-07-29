from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from loader import dp

@dp.message_handler(commands='testing')
async def set_state(msg: types.Message, state: FSMContext):
    await state.set_state('Testing')
    await msg.answer('Questions')

@dp.message_handler(state='Testing')
async def set_state(msg: types.Message, state: FSMContext):
    await msg.answer('Finish')
    await state.finish()