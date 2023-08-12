from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from data.config import CHANNELS
from keyboards.inline.start_INKB import courses, courses_uzb

from keyboards.inline.start_INKB import starting_menu, lang, courses
from loader import dp,db
from keyboards.default.menu_kb import menu


@dp.message_handler(commands='contact',state='Russian')
async def take_contact_rus(msg:types.Message):
    await msg.answer('Если вы хотите что-бы с вами свзялались нажмите на кнопку ниже👇:')
    user_id = msg.chat.id
    target_channel = CHANNELS[0]
    user = db.select_user(id=user_id)
    await msg.send_copy(chat_id=target_channel)
