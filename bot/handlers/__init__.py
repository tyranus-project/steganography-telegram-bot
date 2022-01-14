from aiogram import Dispatcher

from loguru import logger

from .common import register_common_handlers
from .decryption import register_decryption_handlers
from .encryption import register_encryption_handlers
from .exception import register_exception_handlers


def register_handlers(dp: Dispatcher):
    """Sets all bot handlers."""
    logger.info("Configuring handlers...")
    register_common_handlers(dp)
    register_encryption_handlers(dp)
    register_decryption_handlers(dp)
    register_exception_handlers(dp)
