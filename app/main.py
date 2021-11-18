from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app import middlewares, handlers
from app.config import BOT_TOKEN
from app.utils.set_bot_commands import set_default_commands


async def on_startup(dp: Dispatcher):
    handlers.setup_handlers(dp)
    middlewares.setup_middlewares(dp)
    await set_default_commands(dp)


def main():
    steganography_bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    steganography_dispatcher = Dispatcher(steganography_bot, storage=storage)
    executor.start_polling(steganography_dispatcher, on_startup=on_startup)
