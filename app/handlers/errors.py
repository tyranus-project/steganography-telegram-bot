from aiogram import Dispatcher, types
from aiogram.utils.exceptions import BotBlocked, FileIsTooBig


async def bot_blocked_exception(update: types.Update, exception: BotBlocked):
    return True


async def big_file_exception(update: types.Update, exception: FileIsTooBig):
    await update.message.reply(f"{exception}, please try another one!")
    return True


def register_errors_handlers(dp: Dispatcher):
    dp.register_errors_handler(bot_blocked_exception, exception=BotBlocked)
    dp.register_errors_handler(big_file_exception, exception=FileIsTooBig)
