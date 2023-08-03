from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "🎬Запустить бота"),
            types.BotCommand('contacts','📱Наши социальные сети'),
            types.BotCommand('help', '🆘Ответим на ваши вопросы'),

        ]
    )
