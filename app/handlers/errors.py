from aiogram import Dispatcher, types
from aiogram.utils.exceptions import BotBlocked, FileIsTooBig

from loguru import logger

from app.utils.misc import reset_user_data


async def bot_blocked_exception(update: types.Update, exception: BotBlocked):
    await reset_user_data(update.message)
    logger.info(f"{exception}, all user data has been cleared")
    return True


async def big_file_exception(update: types.Update, exception: FileIsTooBig):
    await update.message.reply(f"{exception}. Please try another one!")
    return True


async def unexpected_exception(update: types.Update, exception: Exception):
    if isinstance(exception, (BotBlocked, FileIsTooBig)):
        return True
    await update.message.answer(
        "Sorry, something went wrong...\n"
        "It is better to restart the bot:\n\n"
        "/start to restart the bot"
    )
    logger.debug(f"Unexpected exception: {exception}")
    return True


def register_errors_handlers(dp: Dispatcher):
    dp.register_errors_handler(bot_blocked_exception, exception=BotBlocked)
    dp.register_errors_handler(big_file_exception, exception=FileIsTooBig)
    dp.register_errors_handler(unexpected_exception)
