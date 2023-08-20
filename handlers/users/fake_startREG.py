import asyncio
import sqlite3
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.contact import kb, kb_uzb
from keyboards.default.menu_kb import menu, menu_uzb
from keyboards.inline.start_INKB import lang, starting_menu, starting_menu_uzb, lang_start
from loader import dp, db, bot


@dp.message_handler(commands='start')
async def user_in_while(msg: types.Message, state: FSMContext):
    user_id = msg.from_user.id

    if db.check_user_registration(user_id):
        await state.finish()
        await state.set_state('Language')
        await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)
    await msg.delete()
    await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang_start)
    await state.set_state('Language')


@dp.callback_query_handler(text='start_rus', state='Language')
async def rus_start(call: CallbackQuery, state: FSMContext):
    phone_number_regex = re.compile(r"^(?:\+)?(998)\d{9}$")
    await state.set_state('ru') # not main state
    await call.message.answer('Напишите ваш номер телефона или нажмите кнопку "Отправить контакты":', reply_markup=kb)

@dp.callback_query_handler(text='start_uzb', state='Language')
async def rus_start(call: CallbackQuery, state: FSMContext):
    phone_number_regex = re.compile(r"^(?:\+)?(998)\d{9}$")
    await state.set_state('uz') # not main state
    await call.message.answer('Напишите ваш номер телефона или нажмите кнопку "Отправить контакты":', reply_markup=kb_uzb)

@dp.message_handler(content_types='contact',state='ru') # Another state, only for saving data
async def share_cont(msg:types.Message,state:FSMContext):
    await msg.answer('Ваши контакты были сохранены в базе данных. Если вы хотите что-бы мы с вами связались нажмите /contact')
    contact= msg.contact
    cont = contact.phone_number
    name = msg.from_user.full_name
    try:
        db.add_user(id=msg.from_user.id,
                    name=name,
                    phone=cont)
    except sqlite3.IntegrityError as err:
        print(err)
    await msg.answer('''Я бот - MR_IT.
    Могу помочь вам в следующих операций👇:
    <code>https://t.me/mr_it_uz</code>''',reply_markup=starting_menu)
    await msg.delete()
    await msg.answer('Ожидаю ваш выбор...',reply_markup=menu)
    await state.finish()
    await state.set_state('Russian')

@dp.message_handler(state='ru')
async def set_state(msg: types.Message, state: FSMContext):
    phone = msg.text
    phone_number_regex = re.compile(r"^(?:\+)?(998)\d{9}$")
    if phone_number_regex.match(phone):
        await msg.answer('Успешно сохранили ваш номер. Если вы хотите что-бы мы с вами связались нажмите /contact')
        name = msg.from_user.full_name
        try:
            db.add_user(id=msg.from_user.id,
                        name=name,
                        phone=phone)
        except sqlite3.IntegrityError as err:
            print(err)
        await state.set_state('Russian')
    else:
        await msg.answer('Напишите еще раз ваш номер телефона. Например: +998991234567')

@dp.message_handler(content_types='contact',state='uz') # Another state, only for saving data
async def share_cont(msg:types.Message,state:FSMContext):
    await msg.answer("Telefon raqamingizni saqlab oldik. Agar biz siz bilan bog'lanishimizdi hohlasangiz '/contact'ni bosing")
    contact= msg.contact
    cont = contact.phone_number
    name = msg.from_user.full_name
    try:
        db.add_user(id=msg.from_user.id,
                    name=name,
                    phone=cont)
    except sqlite3.IntegrityError as err:
        print(err)
    await msg.answer('Men MR_IT - botiman.\nMen sizga quyidagi operatsiyalarda yordam bera olaman👇:\n<code>https://t.me/mr_it_uz</code>', reply_markup=starting_menu_uzb)
    await msg.delete()
    await msg.answer('Sizning tanlovingizni kutmoqdamiz...',reply_markup=menu)
    await state.finish()
    await state.set_state('Uzbek')

@dp.message_handler(state='uz')
async def set_state(msg: types.Message, state: FSMContext):
    phone = msg.text
    phone_number_regex = re.compile(r"^(?:\+)?(998)\d{9}$")
    if phone_number_regex.match(phone):
        await msg.answer("Telefon raqamingizni saqlab oldik. Agar biz siz bilan bog'lanishimizdi hohlasangiz '/contact'ni bosing")
        name = msg.from_user.full_name
        try:
            db.add_user(id=msg.from_user.id,
                        name=name,
                        phone=phone)
        except sqlite3.IntegrityError as err:
            print(err)
    else:
        await msg.answer('Telefon raqamizngizni yana bir marta yozing. Masalan: +998991234567')




# @dp.message_handler(commands='start')
# async def check_user_reg(msg: types.Message, state: FSMContext):
#     user_id = msg.from_user.id
#     if db.check_user_registration(user_id):
#         await state.finish()
#         await state.set_state('Language')
#         await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)
#     else:
#         await state.set_state('Register')
#         await msg.answer(
#             'Напишите ваш номер телефона или нажмите кнопку "Отправить контакты":\nTelefon raqamingizni yozing yoki pastaga "Kontakt yuborish" tugmasini bosing:',
#             reply_markup=kb)
#
# @dp.message_handler(commands='start')
# async def set_state(msg: types.Message, state: FSMContext):
#
#     await state.set_state('Register')
#     await msg.answer('Напишите ваш номер телефона или нажмите кнопку "Отправить контакты":\nTelefon raqamingizni yozing yoki pastaga "Kontakt yuborish" tugmasini bosing:',reply_markup=kb)
#
# @dp.message_handler(content_types='contact',state='Register')
# async def share_cont(msg:types.Message,state:FSMContext):
#     await msg.answer('Ваши контакты были сохранены в базе данных \n Siznging kotaklaringiz malumotlar omboriga sahlandi')
#     contact= msg.contact
#     cont = contact.phone_number
#     name = msg.from_user.full_name
#     try:
#         db.add_user(id=msg.from_user.id,
#                     name=name,
#                     phone=cont)
#     except sqlite3.IntegrityError as err:
#         print(err)
#     await state.finish()
#     await state.set_state('Language')
#     await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)
#
# @dp.message_handler(state='Register')
# async def set_state(msg: types.Message, state: FSMContext):
#     phone = msg.text
#     name = msg.from_user.full_name
#     try:
#         db.add_user(id=msg.from_user.id,
#                     name=name,
#                     phone=phone)
#     except sqlite3.IntegrityError as err:
#         print(err)
#     await state.finish()
#     await state.set_state('Language')
#     await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)
#
# @dp.message_handler(state='Language')
# async def user_in_while(msg:types.Message):
#     await msg.delete()
#     await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)
#
#
@dp.callback_query_handler(text='back',state='Russian')
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
@dp.message_handler(commands=['menu','start'])
async def uzbek_contains(call:CallbackQuery,state:FSMContext):
    await call.message.answer('Men MR_IT - botiman.\nMen sizga quyidagi operatsiyalarda yordam bera olaman👇:\n<code>https://t.me/mr_it_uz</code>', reply_markup=starting_menu_uzb)
    await call.message.delete()
    #call.answer для таблички пользователю, + show alert True
    await call.answer(cache_time=60)
    await call.message.answer('Sizning tanlovingizni kutmoqdamiz...',reply_markup=menu_uzb)
    await state.finish()
    await state.set_state('Uzbek')


