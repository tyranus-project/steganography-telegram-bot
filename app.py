from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

from handlers.common import register_handlers_common
from handlers.decryption import register_handlers_decryption
from handlers.encryption import register_handlers_encryption
from handlers.other import register_handlers_other
from handlers.settings import register_callback_query_handlers_settings
from handlers.support import register_callback_query_handlers_support

from utils.middlewares import set_middlewares
from utils.set_bot_commands import set_default_commands


async def setup(dp: Dispatcher):
    await set_default_commands(dp)
    register_handlers_common(dp)
    register_handlers_encryption(dp)
    register_handlers_decryption(dp)
    register_callback_query_handlers_settings(dp)
    register_callback_query_handlers_support(dp)
    register_handlers_other(dp)
    set_middlewares(dp)


steganography_bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
steganography_dispatcher = Dispatcher(steganography_bot, storage=storage)


if __name__ == '__main__':
    executor.start_polling(steganography_dispatcher, on_startup=setup)
