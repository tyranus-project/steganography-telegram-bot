from aiogram import Dispatcher

from loguru import logger

from .common import register_common_handlers
from .decryption import register_decryption_handlers
from .encryption import register_encryption_handlers
from .errors import register_errors_handlers


def setup_handlers(dp: Dispatcher):
    logger.info("Configuring handlers...")
    register_common_handlers(dp)
    register_encryption_handlers(dp)
    register_decryption_handlers(dp)
    register_errors_handlers(dp)
