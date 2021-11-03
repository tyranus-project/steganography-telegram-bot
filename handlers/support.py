from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards.inline import donate_keyboard
from keyboards.inline import support_keyboard


async def support_menu(message: types.Message):
    await message.answer(
        "Support",
        reply_markup=support_keyboard
    )


async def donate_menu(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "Support bot development",
        reply_markup=donate_keyboard
    )


async def call_support_menu(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "Support",
        reply_markup=support_keyboard
    )


async def hide_menu(callback: types.CallbackQuery):
    await callback.message.delete()


def register_callback_query_handlers_support(dp: Dispatcher):
    dp.register_message_handler(support_menu, Text(equals="Support", ignore_case=True), state="*")
    dp.register_callback_query_handler(donate_menu, Text(equals="support the author"), state="*")
    dp.register_callback_query_handler(call_support_menu, Text(equals="back"), state="*")
    dp.register_callback_query_handler(hide_menu, Text(equals="hide"), state="*")
