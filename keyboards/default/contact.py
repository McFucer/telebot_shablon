from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         keyboard=[
                             [
                                 KeyboardButton(text='Отправить контакты | Kontakt yuborish',
                                                request_contact=True)
                             ]
                         ])