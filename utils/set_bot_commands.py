from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота 🎬 Botni ishga tushish "),
            types.BotCommand('menu','Основное меню 💾 Asosiy menyu'),
            types.BotCommand('lang', "Изменить язык 🗣 Tilni o'zgartirish"),
            types.BotCommand('contact', "Связаться с нами 🆘 Biz bilan bog'lanish")
        ]
    )
