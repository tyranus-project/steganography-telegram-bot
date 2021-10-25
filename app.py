from aiogram import executor
from loader import dp

from functionality.set_bot_commands import set_default_commands
from functionality.notify_admins import notify_admins_at_bot_start


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await notify_admins_at_bot_start(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
