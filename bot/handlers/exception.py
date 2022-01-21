from aiogram import Dispatcher, types
from aiogram.types.message import ContentType
from aiogram.utils.exceptions import BotBlocked, FileIsTooBig

from loguru import logger

from bot.utils.misc import reset_user_data


async def undefined_request(message: types.Message):
    """Warns the user about invalid input."""
    await message.answer(
        "Use the menu buttons or commands and follow the instructions in the messages:\n"
        "/menu to return to the main menu\n"
        "/encrypt to start encryption process\n"
        "/decrypt to start decryption process"
    )


async def bot_blocked_exception(update: types.Update, exception: BotBlocked):
    """Catches and logs BotBlocked exception."""
    await reset_user_data(update.message)
    logger.info(f"{exception}. All user data has been cleared.")
    return True


async def big_file_exception(update: types.Update, exception: FileIsTooBig):
    """Catches FileIsTooBig exception."""
    await update.message.reply(f"{exception}. Please try another one.")
    return True


async def unexpected_exception(update: types.Update, exception: Exception):
    """Catches and logs unexpected errors and exceptions, warns the user if possible."""
    if isinstance(exception, (BotBlocked, FileIsTooBig)):
        return True
    try:
        await update.message.answer(
            "Sorry, something went wrong...\n\n"
            "It is better to restart the bot:\n"
            "/start to restart the bot"
        )
    finally:
        logger.debug(f"Unexpected exception: {exception}")
        return True


def register_exception_handlers(dp: Dispatcher):
    """Registers exception handlers."""
    dp.register_message_handler(undefined_request, content_types=ContentType.ANY, state="*")
    dp.register_errors_handler(bot_blocked_exception, exception=BotBlocked)
    dp.register_errors_handler(big_file_exception, exception=FileIsTooBig)
    dp.register_errors_handler(unexpected_exception)
