from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards.inline.settings import call_settings_keyboard

import config


async def settings_menu(message: types.Message):
    await message.answer("Settings", reply_markup=call_settings_keyboard(config.USE_BOT_SALT))


async def change_crypt_status(callback: types.CallbackQuery):
    config.USE_BOT_SALT = False if config.USE_BOT_SALT else True
    # await callback.message.edit_text(text="Settings changed")
    await callback.message.edit_reply_markup(call_settings_keyboard(config.USE_BOT_SALT))


async def hide_call(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.delete()


def register_callback_query_handlers_settings(dp: Dispatcher):
    dp.register_message_handler(settings_menu, Text(equals="Settings", ignore_case=True), state="*")
    dp.register_callback_query_handler(change_crypt_status, Text(equals="change"), state="*")
    dp.register_callback_query_handler(hide_call, Text(equals="hide"), state="*")
