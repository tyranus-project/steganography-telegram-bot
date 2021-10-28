from aiogram import executor
from loader import dp

from functionality.set_bot_commands import set_default_commands
from functionality.notify_admins import notify_admins_at_bot_start

from handlers.common import register_handlers_common
from handlers.encryption import register_handlers_encryption
from handlers.decryption import register_handlers_decryption
from handlers.other import register_handlers_other


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await notify_admins_at_bot_start(dispatcher)

    register_handlers_common(dispatcher)
    register_handlers_encryption(dispatcher)
    register_handlers_decryption(dispatcher)
    register_handlers_other(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
