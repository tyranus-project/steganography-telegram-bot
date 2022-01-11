from aiogram import Dispatcher, types


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("/menu", "Main menu"),
            types.BotCommand("/help", "User manual"),
            types.BotCommand("/encrypt", "Start encryption process"),
            types.BotCommand("/decrypt", "Start decryption process")
        ]
    )
