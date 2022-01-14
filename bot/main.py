import os
import shutil

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from loguru import logger

from bot import middlewares, handlers
from bot.config import BOT_TOKEN, DATA_DIR, SKIP_UPDATES
from bot.utils.commands import set_default_commands


async def on_startup(dp: Dispatcher):
    handlers.setup_handlers(dp)
    middlewares.setup_middlewares(dp)
    await set_default_commands(dp)
    logger.info("Steganography bot launched.")


async def on_shutdown(dp: Dispatcher):
    logger.info("Shutting down...")
    if os.path.isdir(DATA_DIR):
        try:
            shutil.rmtree(DATA_DIR)
        except OSError:
            logger.info("The bot was worked in the container with a tmpfs mount.")
        except Exception as e:
            logger.debug(
                "Unexpected error while deleting data:\n"
                f"{e}"
            )
    await dp.bot.session.close()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logger.info("Steganography bot finished.")


def main():
    logger.info("Starting steganography bot...")
    steganography_bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    steganography_dispatcher = Dispatcher(steganography_bot, storage=storage)
    executor.start_polling(steganography_dispatcher, skip_updates=SKIP_UPDATES, on_startup=on_startup, on_shutdown=on_shutdown)
