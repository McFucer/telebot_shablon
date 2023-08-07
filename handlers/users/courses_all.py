from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.menu_kb import menu, menu_uzb
from keyboards.inline.start_INKB import lang, starting_menu, starting_menu_uzb, mobilgr, scratch, founda, int_ext, front,pyth,video,pc,diza
from loader import dp

@dp.callback_query_handler(text='mobilgr',state='Russian')
async def mobilogr(call:CallbackQuery):
    await call.message.answer('Научитесь создавать высококачественные видео'
                              ' и изображения, а также редактировать их, '
                              'правильно используя возможности телефона.'
                              ' Кроме того, на курсе мобилографии за 2'
                              ' месяца вы научитесь работать с изображением,'
                              ' музыкой, звуком, цветом и другими эффектами'
                              ' в видео. Все темы проходят упрощенно, '
                              'начиная с нуля.', reply_markup=mobilgr)
@dp.callback_query_handler(text='scratch',state='Russian')
async def scratchv(call:CallbackQuery):
    await call.message.answer('Scratch-это курс для детей, где вы узнаете основы программирования, веселые игры, создание анимации и рисование на Scratch. Этот курс также поможет вам изучить алгоритмы, улучшив ваше логическое мышление. Все вышеперечисленное вы узнаете всего за 2 месяца. Все темы проходят упрощенно, начиная с нуля.'
                              ,reply_markup=scratch)

@dp.callback_query_handler(text='found',state='Russian')
async def Foundation(call:CallbackQuery):
    await call.message.answer('Изучите HTML (язык разметки, который создает текстовые информационные типы веб-страниц), CSS (набор каскадных стилей, которые влияют на визуальный вид веб-страниц), и базовые знания, навыки в Python, которые важны в программировании в курсе Foundation. Вас также ждет работа над реальными проектами на протяжении всего курса. И все это вы узнаете за 3 месяца. Все темы проходят упрощенно, начиная с нуля.'
                              ,reply_markup=founda)

@dp.callback_query_handler(text='dizayn',state='Russian')
async def scratchs(call:CallbackQuery):
    await call.message.answer('На курсе дизайна интерьера и экстерьера вы научитесь работать как с внутренним, так и с внешним дизайном зданий и сооружений. Также в ходе курса вас ждут интересные темы, такие как способы рисования чертежей зданий, знакомство с интерфейсами, а также Photoshop. Все это вы узнаете за 4 месяца. Все темы проходят упрощенно, начиная с нуля.'
                              ,reply_markup=int_ext)

@dp.callback_query_handler(text='front',state='Russian')
async def scratchcs(call:CallbackQuery):
    await call.message.answer('Front-end-это различные веб-сайты, которые являются видимой нам частью веб-приложений. Различные анимации, тексты, изображения и другой визуальный контент на всех сайтах, которые вы просматриваете, создаются разработчиками front – end. Если вы хотите углубиться в эту область, запишитесь на наш 6-месячный курс Front-End. Все темы проходят упрощенно, начиная с нуля.'
                              ,reply_markup=front)

@dp.callback_query_handler(text='pyth',state='Russian')
async def scratchascs(call:CallbackQuery):
    await call.message.answer('Python — популярный и знаменитый язык программирования. В ходе курса вы научитесь создавать современные веб-приложения, интернет-магазины и сложные боты Telegram. За 6 месяцев вы приобретете все необходимые навыки для одной из самых востребованных профессий современности.',
                              reply_markup=pyth)

@dp.callback_query_handler(text='montaj',state='Russian')
async def scratchascasas(call:CallbackQuery):
    await call.message.answer('В этом курсе вы научитесь создавать качественный и короткий видеоконтент для рекламных роликов, фильмов и музыкальных клипов. Также вы познакомитесь с профессиональными программами для создания различных эффектов и звукового оформления. После прохождения курса вы станете полноценным специалистом по видеомонтажу. Курс видеомонтажа длится 3 месяца. Все темы рассматриваются в упрощенной форме, начиная с нуля.',
                              reply_markup=video)

@dp.callback_query_handler(text='gramot',state='Russian')
async def scratchcascascsa(call:CallbackQuery):
    await call.message.answer('Все секреты и навыки работы с файлами, документами Microsoft, программными носителями на компьютере, а также того, как установить операционную систему, правильно пользоваться интернетом и общаться онлайн, вы узнаете за 2 месяца на курсе компьютерной грамотности. Все темы проходят упрощенно, начиная с нуля.',
                              reply_markup=pc)

@dp.callback_query_handler(text='grafic',state='Russian')
async def scratchacaax(call:CallbackQuery):
    await call.message.answer('Графический дизайн-это направление в области дизайна, в котором визуальный контент используется для передачи определенной информации. В этом курсе вы изучите плакаты, информационные бюллетени, логотипы брендов, рекламные изображения, анимацию, макеты и дизайн обложек за 4 месяца. Все темы проходят упрощенно, начиная с нуля.',
                              reply_markup=diza)

@dp.callback_query_handler(text='mobilgr_uzb',state='Uzbek')
async def mobilogrsaca(call:CallbackQuery):
    await call.message.answer('Telefon imkoniyatlaridan to’g’ri foydalanish orqali yuqori sifatli videolar va rasmlar yaratish, shuningdek, ularni tahrirlashni o’rganing. Bundan tashqari, mobilografiya kursida siz videodagi rasm, musiqa, tovush, rang va boshqa effektlar bilan ishlashni 2 oyda o’rganasiz. Barcha mavzular soddalashtirilgan tarzda, noldan boshlab o’tiladi.', reply_markup=mobilgr)
@dp.callback_query_handler(text='scratch_uzb',state='Uzbek')
async def scratchsac(call:CallbackQuery):
    await call.message.answer('Scratch – bu bolalar uchun mo’ljallangan kurs bo’lib, unda siz dasturlash asoslari, qiziqarli o’yinlar, animatsiyalar yaratish va Scratch da rasm chizishni o’rganasiz. Shuningdek, ushbu kurs sizning mantiqiy fikrlashingizni yaxshilab, algoritmlarni o’rganishingizga yordam beradi. Yuqorida keltirilgan barcha narsalarni siz atigi 2 oyda o’rganasiz. Barcha mavzular soddalashtirilgan tarzda, noldan boshlab o’tiladi.',
                              reply_markup=scratch)

@dp.callback_query_handler(text='found_uzb',state='Uzbek')
async def Foundationascacsa(call:CallbackQuery):
    await call.message.answer('Foundation kursida dasturlashda muhim ahamiyatga ega bo’lgan HTML (veb sahifalarning matnli axborot turlarini yaratuvchi belgili til), CSS (veb sahifalarning vizual ko’rinishiga ta’sir qiluvchi kaskadli stillar majmuasi) va Python da boshlang’ich bilim va ko’nikmalarni o’rganing. Shuningdek, kurs davomida real hayotdagi proyektlar bilan ishlash sizni kutmoqda. Va bularni barchasini siz 3 oyda o’rganasiz. Barcha mavzular soddalashtirilgan tarzda, noldan boshlab o’tiladi.'
                              ,reply_markup=founda)

@dp.callback_query_handler(text='dizayn_uzb',state='Uzbek')
async def scratchascacs(call:CallbackQuery):
    await call.message.answer('Interyer va Eksteryer dizayn kursida siz bino va inshootlarning ichki va tashqi dizaynlari ustida ishlashni o’rganasiz. Shuningdek, kurs davomida sizni bino chizmalarini chizish usullari, interfeyslar bilan tanishish, hamda, Photoshop kabi qiziqarli mavzular kutmoqda. Bularning barchasini siz 4 oyda o’rganasiz. Barcha mavzular soddalashtirilgan tarzda, noldan boshlab o’tiladi.',
                              reply_markup=int_ext)

@dp.callback_query_handler(text='front_uzb',state='Uzbek')
async def scratchcascsa(call:CallbackQuery):
    await call.message.answer('Front – end – bu turli xil veb-saytlar, veb-ilovalarning bizga ko’rinib turgan qismi hisoblanadi. Siz ko’rgan barcha saytlardagi turli xil animatsiyalar, matnlar, rasmlar va boshqa vizual kontentlar Front – end dasturchilari tomonidan qilinadi. Agar siz ushbu sohasini chuqurroq o’rganishni xohlasangiz, bizning 6 oylik Front-end kursimizga ro’yxatdan o’ting. Barcha mavzular soddalashtirilgan tarzda, noldan boshlab o’tiladi.',
                              reply_markup=front)

@dp.callback_query_handler(text='pyth_uzb',state='Uzbek')
async def scratchascascasasx(call:CallbackQuery):
    await call.message.answer('Python – ommabop va mashhur dasturlash tili hisoblanadi. Kurs davomida siz zamonaviy veb-ilovalar, onlayn do’konlar va murakkab Telegram botlarni yaratishni o’rganasiz. 6 oy davomida siz zamonamizning eng talab qilinadigan kasblaridan biri uchun barcha kerakli ko’nikmalarni o’zlashtirasiz.',
                              reply_markup=pyth)

@dp.callback_query_handler(text='montaj_uzb',state='Uzbek')
async def scratchSxq(call:CallbackQuery):
    await call.message.answer('Ushbu kursda siz reklama, kino va kliplar uchun sifatli va qisqa videokontentlarni yaratishni o’rganishingiz mumkin. Shuningdek, turli effektlar yaratish, ovoz dizayni bo’yicha professional dasturlar bilan tanishasiz. Kursni tamomlab, siz videomontaj bo’yicha to’liq mutaxassisga aylanasiz. Videomontaj kursi 3 oy davom etadi. Barcha mavzular soddalashtirilgan tarzda, noldan boshlab o’tiladi.',
                              reply_markup=video)

@dp.callback_query_handler(text='gramot_uzb',state='Uzbek')
async def scratchdcd(call:CallbackQuery):
    await call.message.answer('Kompyuterda fayllar, Microsoft dokumentlari, dasturlar mediasi bilan ishlashni, shuningdek, operatsion tizimni qanday o’rnatish, internetdan to’g’ri foydalanish va online muloqot qilishning barcha sir va ko’nikmalarini siz Kompyuter savodxonligi kursida 2 oy davomida o’rganasiz. Barcha mavzular soddalashtirilgan tarzda, noldan boshlab o’tiladi.',
                              reply_markup=pc)

@dp.callback_query_handler(text='grafic_uzb',state='Uzbek')
async def scratchkjun(call:CallbackQuery):
    await call.message.answer('Grafik dizayn - dizayn sohasining bir yo’nalishi bo’lib, unda ma’lum axborotlarni yetkazib berish uchun vizual kontentlardan foydalaniladi. Ushbu kursda siz plakatlar, axborot varaqalari, brend logotiplari, reklama tasvirlari, animatsiya, maket va muqova dizaynlarini 4 oyda o’rganasiz. Barcha mavzular soddalashtirilgan tarzda, noldan boshlab o’tiladi.',
                              reply_markup=diza)