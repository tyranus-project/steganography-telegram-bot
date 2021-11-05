from aiogram import types, Dispatcher

import logging

from config import ADMINS


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("/menu", "Main menu"),
            types.BotCommand("/help", "User manual"),
            types.BotCommand("/language", "Change language")
        ]
    )


async def notify_admins_at_bot_start(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot launched")
        except Exception as err:
            logging.exception(err)
