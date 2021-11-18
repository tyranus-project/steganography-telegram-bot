from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app import middlewares
from app.config import BOT_TOKEN
from app.handlers.common import register_common_handlers
from app.handlers.decryption import register_decryption_handlers
from app.handlers.encryption import register_encryption_handlers
from app.handlers.errors import register_errors_handlers
from app.handlers.settings import register_settings_handlers
from app.handlers.support import register_support_handlers
from app.utils.set_bot_commands import set_default_commands


async def on_startup(dp: Dispatcher):
    await set_default_commands(dp)
    register_common_handlers(dp)
    register_encryption_handlers(dp)
    register_decryption_handlers(dp)
    register_settings_handlers(dp)
    register_support_handlers(dp)
    register_errors_handlers(dp)
    middlewares.setup_middlewares(dp)


if __name__ == '__main__':
    steganography_bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    steganography_dispatcher = Dispatcher(steganography_bot, storage=storage)
    executor.start_polling(steganography_dispatcher, on_startup=on_startup)
