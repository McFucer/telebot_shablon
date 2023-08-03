from aiogram import types
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.start_INKB import starting_menu, lang


# @dp.message_handler(CommandStart(),state='Language')
# async def start_lang(msg:types.Message,state: FSMContext):
#     await msg.answer("Выберите язык:\nTil tanlang:",reply_markup=lang)
#     await state.finish()
#     await state.set_state('Testing')


@dp.message_handler(CommandStart(),state='Testing')
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nВыберите язык ",reply_markup=starting_menu)
