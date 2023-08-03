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
    [
        InlineKeyboardButton(text='Прочие',callback_data='another')
    ],
])
starting_menu_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Ishga yo'naltirish testi",callback_data='Test_uzb'),
    ],
    [
        InlineKeyboardButton(text='Kurslar',callback_data='courses_uzb'),
    ],
    [
        InlineKeyboardButton(text='Bizning veb-saytimiz',web_app=WebAppInfo(url='https://www.mr-it.uz/home'))
    ],
    [
        InlineKeyboardButton(text='Boshqalar',callback_data='another_uzb')
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
        InlineKeyboardButton(text='📱Мобилография',callback_data='mobilgr'),
        InlineKeyboardButton(text='👩‍🦲Scratch',callback_data='scratch'),
        InlineKeyboardButton(text='🧑🏼‍🏫Foundation',callback_data='found'),
    ],
    [
        InlineKeyboardButton(text='🏫Дизайн интерьера и экстерьера',callback_data='dizayn'),
        InlineKeyboardButton(text='🧑‍💻Front-end',callback_data='front'),
        InlineKeyboardButton(text='👨🏼‍💻Python',callback_data='pyth'),
    ],
    [
        InlineKeyboardButton(text='🎥Видеомонтаж',callback_data='montaj'),
        InlineKeyboardButton(text='🖥Компьютерная грамотность',callback_data='gramot'),
        InlineKeyboardButton(text='📸Графический Дизайн',callback_data='grafic'),
    ],
    [
        InlineKeyboardButton(text='🔙Назад',callback_data='back'),
    ],
])
courses_uzb = InlineKeyboardMarkup(row_width=3,
    inline_keyboard=[
    [
        InlineKeyboardButton(text='📱Mobilografiya',callback_data='mobilgr_uzb'),
        InlineKeyboardButton(text='👩‍🦲Scratch',callback_data='scratch_uzb'),
        InlineKeyboardButton(text='🧑🏼‍🏫Foundation',callback_data='found_uzb'),
    ],
    [
        InlineKeyboardButton(text='🏫Interyer va Eksteryer dizayn',callback_data='dizayn_uzb'),
        InlineKeyboardButton(text='‍💻Front-end',callback_data='front_uzb'),
        InlineKeyboardButton(text='👨🏼‍💻Python',callback_data='pyth_uzb'),
    ],
    [
        InlineKeyboardButton(text='🎥Videomontaj',callback_data='montaj_uzb'),
        InlineKeyboardButton(text='🖥Kompyuter savodxonligi',callback_data='gramot_uzb'),
        InlineKeyboardButton(text='📸Grafik dizayn',callback_data='grafic_uzb'),
    ],
    [
        InlineKeyboardButton(text='🔙Назад',callback_data='back_uzb'),
    ],
])

# цикл
# books = {
#     dasfasd:dasdsad
# }
# booksMenu = InlineKeyboardMarkup(row_width=1)
# for key, value in books.items():
#     booksMenu.insert(InlineKeyboardButton(text=key,callback_data=callbacks.new(item_name=value)))