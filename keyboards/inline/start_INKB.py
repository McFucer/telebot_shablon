from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from keyboards.inline.callback_data import callbacks

starting_menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Тест по профессиональной ориентации',callback_data='Test'),
    ],
    [
        InlineKeyboardButton(text='Курсы',callback_data='courses'),
    ],
    [
        InlineKeyboardButton(text='Наш сайт',web_app=WebAppInfo(url='https://www.mr-it.uz/home'))
    ],
])
lang = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="O'zbek tili",callback_data='uzbek'),
        InlineKeyboardButton(text='Русский Язык',callback_data='rus'),
    ],
])

courses = InlineKeyboardMarkup(row_width=3,
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Мобилография',callback_data='mobilgr'),
        InlineKeyboardButton(text='Scratch',callback_data='scratch'),
        InlineKeyboardButton(text='Foundation',callback_data='found'),
    ],
    [
        InlineKeyboardButton(text='Дизайн интерьера и экстерьера',callback_data='dizayn'),
        InlineKeyboardButton(text='Front-end',callback_data='front'),
        InlineKeyboardButton(text='Python',callback_data='pyth'),
    ],
    [
        InlineKeyboardButton(text='Видеомонтаж',callback_data='montaj'),
        InlineKeyboardButton(text='Компьютерная грамотность',callback_data='gramot'),
        InlineKeyboardButton(text='Графический Дизайн',callback_data='grafic'),
    ],
    [
        InlineKeyboardButton(text='Назад',callback_data='back'),
    ],
])