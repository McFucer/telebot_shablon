import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(commands="allusers", user_id=ADMINS,state=['Uzbek','Russian'])
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)

@dp.message_handler(commands="reklama", user_id=ADMINS,state=['Uzbek','Russian'])
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="Здесь могла быть ваша Реклама!")
        await asyncio.sleep(0.05)

@dp.message_handler(commands="cleandb", user_id=ADMINS,state=['Uzbek','Russian'])
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")