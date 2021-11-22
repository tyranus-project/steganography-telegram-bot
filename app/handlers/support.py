from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types.message import ContentType

from app.keyboards.inline import donate_keyboard
from app.keyboards.inline import support_keyboard


async def support_menu(message: types.Message):
    await message.answer(
        "Support:",
        reply_markup=support_keyboard
    )


async def undefined_request(message: types.Message):
    await message.answer(
        "Use the menu buttons and commands, and follow the instructions in the messages.\n\n"
        "/help to show user manual\n"
        "/start to restart the bot"
    )


async def donate_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("To support the development of the bot:")
    await callback.message.edit_reply_markup(donate_keyboard)


async def back_support_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("Support:")
    await callback.message.edit_reply_markup(support_keyboard)


def register_support_handlers(dp: Dispatcher):
    dp.register_message_handler(support_menu, Text(equals="Support", ignore_case=True), state="*")
    dp.register_message_handler(undefined_request, content_types=ContentType.ANY, state="*")
    dp.register_callback_query_handler(donate_menu, Text(equals="donate"), state="*")
    dp.register_callback_query_handler(back_support_menu, Text(equals="back"), state="*")
