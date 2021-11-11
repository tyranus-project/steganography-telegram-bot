from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.config import BOT_TOKEN
from app.handlers.common import register_handlers_common
from app.handlers.decryption import register_handlers_decryption
from app.handlers.encryption import register_handlers_encryption
from app.handlers.other import register_handlers_other
from app.handlers.settings import register_callback_query_handlers_settings
from app.handlers.support import register_callback_query_handlers_support
from app.utils.middlewares import set_middlewares
from app.utils.set_bot_commands import set_default_commands


async def setup(dp: Dispatcher):
    await set_default_commands(dp)
    register_handlers_common(dp)
    register_handlers_encryption(dp)
    register_handlers_decryption(dp)
    register_callback_query_handlers_settings(dp)
    register_callback_query_handlers_support(dp)
    register_handlers_other(dp)
    set_middlewares(dp)


if __name__ == '__main__':
    steganography_bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    steganography_dispatcher = Dispatcher(steganography_bot, storage=storage)
    executor.start_polling(steganography_dispatcher, on_startup=setup)
