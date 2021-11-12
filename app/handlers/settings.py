from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from app import config
from app.keyboards.inline import call_settings_keyboard


async def settings_menu(message: types.Message):
    await message.answer(
        "Settings:",
        reply_markup=call_settings_keyboard(config.USE_BOT_SALT)
    )


async def change_bot_salt_status(callback: types.CallbackQuery):
    config.USE_BOT_SALT = False if config.USE_BOT_SALT else True
    await callback.message.edit_reply_markup(call_settings_keyboard(config.USE_BOT_SALT))


async def hide_menu(callback: types.CallbackQuery):
    await callback.message.delete()


def register_settings_handlers(dp: Dispatcher):
    dp.register_message_handler(settings_menu, Text(equals="Settings", ignore_case=True), state="*")
    dp.register_message_handler(settings_menu, commands=["settings"], state="*")
    dp.register_callback_query_handler(change_bot_salt_status, Text(equals="change"), state="*")
    dp.register_callback_query_handler(hide_menu, Text(equals="hide"), state="*")
