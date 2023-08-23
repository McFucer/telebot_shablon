from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from keyboards.inline.callback_data import callbacks

starting_menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Тест по профессиональной ориентации👨🏼‍💻',web_app=WebAppInfo(url='https://www.profguide.io/test/klimov.html')),
    ],
    [
        InlineKeyboardButton(text='Курсы📋',callback_data='courses'),
        InlineKeyboardButton(text='У меня есть вопросы❓', url='https://telegra.ph/Voprosy-i-Otvety--MR-IT-08-04'),
    ],
    [
        InlineKeyboardButton(text='Наш сайт📎',web_app=WebAppInfo(url='https://www.mr-it.uz/home')),

    ],
    [
        InlineKeyboardButton(text='Свяжитесь со мной☎️',callback_data='sos')
    ],
    [
        InlineKeyboardButton(text='Прочие...',callback_data='another')
    ],
])
starting_menu_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Ishga yo'naltirish testi👨🏼‍💻",web_app=WebAppInfo(url='https://proweb.uz/uz/tests')),
    ],
    [
        InlineKeyboardButton(text='Kurslar📋',callback_data='courses_uzb'),
        InlineKeyboardButton(text='Menda savollar bor❓', url='https://telegra.ph/Savol-va-javoblar--MR-IT-08-06'),
    ],
    [
        InlineKeyboardButton(text='Bizning veb-saytimiz📎',web_app=WebAppInfo(url='https://www.mr-it.uz/home')),

    ],
    [
        InlineKeyboardButton(text="Men bilan bog'laning☎️",callback_data='sos_uzb')
    ],
    [
        InlineKeyboardButton(text='Boshqalar...',callback_data='another_uzb')
    ],
])
lang = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🇺🇿O'zbek tili",callback_data='uzbek'),
        InlineKeyboardButton(text='🇷🇺Русский язык',callback_data='rus'),
    ],
])

lang_start = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🇺🇿O'zbek tili",callback_data='start_uzb'),
        InlineKeyboardButton(text="🇷🇺Русский язык",callback_data='start_rus'),
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

contact_send = InlineKeyboardMarkup()
contact_send.insert(InlineKeyboardButton('Отправить данные☑️',callback_data='contact_s'))
contact_send.insert(InlineKeyboardButton('Основное меню💾',callback_data='back'))

contact_senduz = InlineKeyboardMarkup()
contact_senduz.insert(InlineKeyboardButton("Ma'lumotlarni yuborish☑️",callback_data='contact_s_uzb'))
contact_senduz.insert(InlineKeyboardButton('Asosiy menyu💾',callback_data='back_uzb'))


seti = {
    'Instagram':'https://www.instagram.com/mr_it/',
    'Telegram':'https://t.me/mr_it_uz',
    'TikTok':'https://www.tiktok.com/@upteaapie0f?_r=1&_d=e60j77hc5cld6m&language=en&sec_uid=MS4wLjABAAAAlwMAuiB5meF-Ir14V_aSk9ksj_qC3k3TE2pNSXhniuxJ7sNXfSN8P1iABZoRsrN7&share_author_id=7214041436219425793&source=h5_m&u_code=dgmi7hlj53dj2l&timestamp=1680603913&user_id=6924828201664939014&sec_user_id=MS4wLjABAAAAExZC3qoEjIDkHRM17dsuRUoFQg7F8ykOR2Y0n4S6pNBR2WFnOctXYVsjrpf4B6qe&utm_source=telegram&utm_campaign=client_share&utm_medium=android&share_iid=7217638088586643201&share_link_id=5da424b4-20d5-435b-aa1b-0a658bc3b300&share_app_id=1233&ugbiz_name=Account&ug_btm=b6880%2Cb5836&social_share_type=5',
    'FaceBook':'https://www.facebook.com/people/Mister_itschool/100090913510545/',
    'YouTube':'https://www.youtube.com/channel/UCF3Fco5fpdooBEG78ov1q9g',
}
seti_menu = InlineKeyboardMarkup(row_width=1)
for key, value in seti.items():
    seti_menu.insert(InlineKeyboardButton(text=key,url=value))