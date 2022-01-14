from aiogram import Dispatcher, types


async def set_default_commands(dp: Dispatcher):
    """Sets the bot commands to the bot user interface."""
    await dp.bot.set_my_commands(
        [
            types.BotCommand("/menu", "Main menu"),
            types.BotCommand("/encrypt", "Encrypt stego image"),
            types.BotCommand("/decrypt", "Decrypt stego image")
        ]
    )
