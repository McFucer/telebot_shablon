from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from data.config import CHANNELS
from keyboards.inline.start_INKB import courses, courses_uzb, contact_send, contact_senduz, seti

from keyboards.inline.start_INKB import starting_menu, lang, courses
from loader import dp, db, bot
from keyboards.default.menu_kb import menu

# SENDING TO THE DATABASE CHANNEL
@dp.message_handler(commands='contact', state='Russian')
async def take_contact_rus(msg: types.Message, state:FSMContext):
    await msg.answer('Если вы хотите, чтобы с вами связались, нажмите на кнопку ниже👇:',reply_markup=contact_send)
    await msg.delete()
@dp.callback_query_handler(text='sos',state='Russian')
async def take_contact_rus(call:CallbackQuery, state:FSMContext):
    await call.message.answer('Если вы хотите, чтобы с вами связались, нажмите на кнопку ниже👇:',reply_markup=contact_send)
    await call.message.delete()

@dp.callback_query_handler(text='contact_s',state="Russian")
async def contact_inline(call:CallbackQuery):
    user_id = call.from_user.id
    nick = call.from_user.username
    if db.check_user_registration(user_id):
        user_data = db.select_user(id=user_id)

        # Форматируйте данные пользователя для отправки в канал
        user_text = f"ID пользователя: {user_data[0]}\nИмя: {user_data[1]}\nusernick: @{nick}\nТелефон: {user_data[2]}\nЯзык: Русский"

        target_channel = CHANNELS[0]
        await bot.send_message(chat_id=target_channel, text=user_text)
        await call.answer('Мы скоро свяжемся с вами, нажмите "Основное меню"', show_alert=True)


@dp.callback_query_handler(text='sos_uzb',state='Uzbek')
@dp.message_handler(commands='contact', state='Uzbek')
async def take_contact_rus(msg: types.Message, state:FSMContext):
    await msg.answer("Agar siz bilan bog'lanishni istasangiz, quyidagi tugmani bosing👇:",reply_markup=contact_senduz)
    await msg.delete()

@dp.callback_query_handler(text='sos_uzb',state='Uzbek')
async def take_contact_rus(call: CallbackQuery, state:FSMContext):
    await call.message.answer("Agar siz bilan bog'lanishni istasangiz, quyidagi tugmani bosing👇:",reply_markup=contact_senduz)
    await call.message.delete()

@dp.callback_query_handler(text='contact_s',state="Uzbek")
async def contact_inline(call:CallbackQuery, state=FSMContext):
    user_id = call.message.from_user.id
    nick = call.from_user.username
    if db.check_user_registration(user_id):
        user_data = db.select_user(id=user_id)

        # Форматируйте данные пользователя для отправки в канал
        user_text = f"ID пользователя: {user_data[0]}\nИмя: {user_data[1]}\nusernick: @{nick}\nТелефон: {user_data[2]}\nЯзык: Uzbek"

        target_channel = CHANNELS[0]
        await bot.send_message(chat_id=target_channel, text=user_text)
        await call.answer('Yaqin vaqtda siz bilan aloqaga chiqamiz, "Asosiy menyu" tugmasini bosing',show_alert=True)


@dp.callback_query_handler(text='another',state='Russian')
async def another_menu(call:CallbackQuery):
    await call.message.edit_text('Снизу находятся наши социальные сети👇',reply_markup=seti)

@dp.callback_query_handler(text='another_uzb',state='Uzbek')
async def another_menu(call:CallbackQuery):
    await call.message.edit_text('Bizning ijtimoiy tarmoqlarimiz👇')
    await call.message.edit_reply_markup(reply_markup=seti)