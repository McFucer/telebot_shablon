from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Основное меню'),
        ],
    ],
    resize_keyboard=True
)

menu_uzb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Asosiy menyu'),
        ],
    ],
    resize_keyboard=True
)
