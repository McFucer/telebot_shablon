from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         keyboard=[
                             [
                                 KeyboardButton(text='Отправить контакты📝',
                                                request_contact=True)
                             ]
                         ])

kb_uzb = ReplyKeyboardMarkup(resize_keyboard=True,
                         keyboard=[
                             [
                                 KeyboardButton(text='Kontakt yuborish📝',
                                                request_contact=True)
                             ]
                         ])