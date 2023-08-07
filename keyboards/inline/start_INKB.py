from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from keyboards.inline.callback_data import callbacks

starting_menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Тест по профессиональной ориентации👨🏼‍💻',callback_data='Test'),
    ],
    [
        InlineKeyboardButton(text='Курсы📋',callback_data='courses'),
        InlineKeyboardButton(text='У меня есть вопросы❓', url='https://telegra.ph/Voprosy-i-Otvety--MR-IT-08-04'),
    ],
    [
        InlineKeyboardButton(text='Наш сайт📎',web_app=WebAppInfo(url='https://www.mr-it.uz/home')),

    ],
    [
        InlineKeyboardButton(text='Прочие...',callback_data='another')
    ],
])
starting_menu_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Ishga yo'naltirish testi👨🏼‍💻",callback_data='Test_uzb'),
    ],
    [
        InlineKeyboardButton(text='Kurslar📋',callback_data='courses_uzb'),
        InlineKeyboardButton(text='Menda savollar bor❓', url='https://telegra.ph/Savol-va-javoblar--MR-IT-08-06'),
    ],
    [
        InlineKeyboardButton(text='Bizning veb-saytimiz📎',web_app=WebAppInfo(url='https://www.mr-it.uz/home')),

    ],
    [
        InlineKeyboardButton(text='Boshqalar...',callback_data='another_uzb')
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
        InlineKeyboardButton(text='🔙Orqaga',callback_data='back_uzb'),
    ],
])

# цикл
# books = {
#     dasfasd:dasdsad
# }
# booksMenu = InlineKeyboardMarkup(row_width=1)
# for key, value in books.items():
#     booksMenu.insert(InlineKeyboardButton(text=key,callback_data=callbacks.new(item_name=value)))

mobilgr = InlineKeyboardMarkup()
mobilgr.insert(InlineKeyboardButton('Посмотреть | Qarash',url='https://www.mr-it.uz/courses/1'))
mobilgr.insert(InlineKeyboardButton('Назад | Orqaga', callback_data='back_from_courses'))

scratch = InlineKeyboardMarkup()
scratch.insert(InlineKeyboardButton('Посмотреть | Qarash',url='https://www.mr-it.uz/courses/2'))
scratch.insert(InlineKeyboardButton('Назад | Orqaga', callback_data='back_from_courses'))

founda = InlineKeyboardMarkup()
founda.insert(InlineKeyboardButton('Посмотреть | Qarash',url='https://www.mr-it.uz/courses/3'))
founda.insert(InlineKeyboardButton('Назад | Orqaga', callback_data='back_from_courses'))

int_ext = InlineKeyboardMarkup()
int_ext.insert(InlineKeyboardButton('Посмотреть | Qarash',url='https://www.mr-it.uz/courses/4'))
int_ext.insert(InlineKeyboardButton('Назад | Orqaga', callback_data='back_from_courses'))

front = InlineKeyboardMarkup()
front.insert(InlineKeyboardButton('Посмотреть | Qarash',url='https://www.mr-it.uz/courses/5'))
front.insert(InlineKeyboardButton('Назад | Orqaga', callback_data='back_from_courses'))

pyth = InlineKeyboardMarkup()
pyth.insert(InlineKeyboardButton('Посмотреть | Qarash',url='https://www.mr-it.uz/courses/6'))
pyth.insert(InlineKeyboardButton('Назад | Orqaga', callback_data='back_from_courses'))

video = InlineKeyboardMarkup()
video.insert(InlineKeyboardButton('Посмотреть | Qarash',url='https://www.mr-it.uz/courses/7'))
video.insert(InlineKeyboardButton('Назад | Orqaga', callback_data='back_from_courses'))

pc = InlineKeyboardMarkup()
pc.insert(InlineKeyboardButton('Посмотреть | Qarash',url='https://www.mr-it.uz/courses/8'))
pc.insert(InlineKeyboardButton('Назад | Orqaga', callback_data='back_from_courses'))

diza = InlineKeyboardMarkup()
diza.insert(InlineKeyboardButton('Посмотреть | Qarash',url='https://www.mr-it.uz/courses/9'))
diza.insert(InlineKeyboardButton('Назад | Orqaga', callback_data='back_from_courses'))

