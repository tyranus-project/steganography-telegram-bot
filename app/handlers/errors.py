from aiogram import Dispatcher, types
from aiogram.utils.exceptions import BotBlocked, FileIsTooBig

from app.utils.misc import reset_user_data


async def bot_blocked_exception(update: types.Update, exception: BotBlocked):
    return True


async def big_file_exception(update: types.Update, exception: FileIsTooBig):
    await update.message.reply(f"{exception}, please try another one!")
    return True


async def unexpected_exception(update: types.Update, error: Exception):
    if isinstance(error, (BotBlocked, FileIsTooBig)):
        return True
    await update.message.answer(
        "Sorry, something went wrong...\n"
        "It is better to restart the bot:\n\n"
        "/start to restart the bot"
    )
    await reset_user_data(update.message)
    return True


def register_errors_handlers(dp: Dispatcher):
    dp.register_errors_handler(bot_blocked_exception, exception=BotBlocked)
    dp.register_errors_handler(big_file_exception, exception=FileIsTooBig)
    dp.register_errors_handler(unexpected_exception)
