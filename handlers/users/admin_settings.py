# если админ захочет получить db или любую инфу, он
# может написать сообщение определенное и только он
# будет принимать это сообщение

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

@dp.message_handler(commands='database',is_chat_admin=True)
async def chat_admin(msg: types.Message):
    await msg.answer('Админ всегда прав')