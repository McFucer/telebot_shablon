from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo(msg: types.Message):
    await msg.answer('Красивое фото')

@dp.message_handler(content_types=types.ContentType.GAME)
@dp.message_handler(content_types=types.ContentType.STICKER)
async def stick(msg: types.Message):
    await msg.answer('Что за стикер')