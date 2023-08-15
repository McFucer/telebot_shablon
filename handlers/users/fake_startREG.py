import asyncio
import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.contact import kb
from keyboards.default.menu_kb import menu, menu_uzb
from keyboards.inline.start_INKB import lang, starting_menu, starting_menu_uzb
from loader import dp, db, bot


@dp.message_handler(commands='start')
async def check_user_reg(msg: types.Message, state: FSMContext):
    user_id = msg.from_user.id
    if db.check_user_registration(user_id):
        await state.finish()
        await state.set_state('Language')
        await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)
    else:
        await state.set_state('Register')
        await msg.answer(
            'Напишите ваш номер телефона или нажмите кнопку "Отправить контакты":\nTelefon raqamingizni yozing yoki pastaga "Kontakt yuborish" tugmasini bosing:',
            reply_markup=kb)

@dp.message_handler(commands='start')
async def set_state(msg: types.Message, state: FSMContext):

    await state.set_state('Register')
    await msg.answer('Напишите ваш номер телефона или нажмите кнопку "Отправить контакты":\nTelefon raqamingizni yozing yoki pastaga "Kontakt yuborish" tugmasini bosing:',reply_markup=kb)

@dp.message_handler(content_types='contact',state='Register')
async def share_cont(msg:types.Message,state:FSMContext):
    await msg.answer('Ваши контакты были сохранены в базе данных \n Siznging kotaklaringiz malumotlar omboriga sahlandi')
    contact= msg.contact
    cont = contact.phone_number
    name = msg.from_user.full_name
    try:
        db.add_user(id=msg.from_user.id,
                    name=name,
                    phone=cont)
    except sqlite3.IntegrityError as err:
        print(err)
    await state.finish()
    await state.set_state('Language')
    await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)

@dp.message_handler(state='Register')
async def set_state(msg: types.Message, state: FSMContext):
    phone = msg.text
    name = msg.from_user.full_name
    try:
        db.add_user(id=msg.from_user.id,
                    name=name,
                    phone=phone)
    except sqlite3.IntegrityError as err:
        print(err)
    await state.finish()
    await state.set_state('Language')
    await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)

@dp.message_handler(state='Language')
async def user_in_while(msg:types.Message):
    await msg.delete()
    await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)


@dp.callback_query_handler(text='back',state='Russian')
@dp.callback_query_handler(text='rus',state='Language')
@dp.message_handler(commands=['menu','start'],state='Russian')
async def rus_contains(call:CallbackQuery, state: FSMContext):
    await call.message.answer('''Я бот - MR_IT.
Могу помочь вам в следующих операций👇:
<code>https://t.me/mr_it_uz</code>''',reply_markup=starting_menu)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer('Ожидаю ваш выбор...',reply_markup=menu)
    await state.finish()
    await state.set_state('Russian')


@dp.callback_query_handler(text='back_uzb',state='Uzbek')
@dp.callback_query_handler(text='uzbek',state='Language')
@dp.message_handler(commands=['menu','start'])
async def uzbek_contains(call:CallbackQuery,state:FSMContext):
    await call.message.answer('Men MR_IT - botiman.\nMen sizga quyidagi operatsiyalarda yordam bera olaman👇:\n<code>https://t.me/mr_it_uz</code>', reply_markup=starting_menu_uzb)
    await call.message.delete()
    #call.answer для таблички пользователю, + show alert True
    await call.answer(cache_time=60)
    await call.message.answer('Sizning tanlovingizni kutmoqdamiz...',reply_markup=menu_uzb)
    await state.finish()
    await state.set_state('Uzbek')


