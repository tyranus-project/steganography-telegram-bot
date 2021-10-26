from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("/menu", "Main menu"),
            types.BotCommand("/help", "User manual"),
            types.BotCommand("/language", "Change language")
        ]
    )
