from aiogram import Dispatcher

from .common import register_common_handlers
from .decryption import register_decryption_handlers
from .encryption import register_encryption_handlers
from .errors import register_errors_handlers
from .settings import register_settings_handlers
from .support import register_support_handlers


def setup_handlers(dp: Dispatcher):
    register_common_handlers(dp)
    register_encryption_handlers(dp)
    register_decryption_handlers(dp)
    register_settings_handlers(dp)
    register_support_handlers(dp)
    register_errors_handlers(dp)
