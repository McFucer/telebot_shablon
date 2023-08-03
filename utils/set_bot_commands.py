from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "🎬Запустить бота"),
            types.BotCommand('menu','💾Основное меню'),
            types.BotCommand('lang', '🗣Изменить язык'),
            types.BotCommand('contact', '🆘Связаться с нами')
        ]
    )
