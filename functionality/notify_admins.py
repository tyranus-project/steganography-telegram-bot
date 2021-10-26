import logging

from config import ADMINS


async def notify_admins_at_bot_start(dp):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot launched")
        except Exception as err:
            logging.exception(err)
