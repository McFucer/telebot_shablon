from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from loader import dp, db


from states.personal_Data import Personal


@dp.message_handler(commands='register')
async def entering(message: types.Message):
    await message.answer('Напишите свое имя:')
    await Personal.first_name.set()

@dp.message_handler(state=Personal.first_name)
async def answer_name(message: types.Message, state: FSMContext):
    first_name = message.text

    await state.update_data({'name': first_name})
    await message.answer('Ваш номер телефона:')

    await Personal.next()

@dp.message_handler(state=Personal.phone_n)
async def answer_name(message: types.Message, state: FSMContext):
    phone_n = message.text

    await state.update_data({'phone': phone_n})
    data = await state.get_data()
    name = data.get('name')
    phone_n = data.get('phone')

    # Создание пользователя и сохранение его в базе данных
    user = User(name=name, phone=phone_n)
    db.add(user)
    db.commit()

    msg = f'''Вот все ваши данные:
    Ваше имя - {name}
    Ваш номер телефона - {phone_n}'''
    await message.answer(msg)
    await state.finish()
