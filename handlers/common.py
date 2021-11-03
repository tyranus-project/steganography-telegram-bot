from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.dispatcher.filters.builtin import CommandStart

from functionality.backend_processes import reset_user_data

from keyboards.default.main_menu import main_menu_keyboard

from states.crypting import crypt_states


async def cmd_start(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer(
        "Welcome!\n\n"
        "This bot helps to hide your secret messages inside images!\n\n"
        "Also recommend subscribing to @durov to keep up to date with the latest changes."
    )
    await message.answer(
        "Useful commands to get started:\n\n"
        "/help - detailed instructions",
        reply_markup=main_menu_keyboard
    )


async def cmd_menu(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer(
        "Main menu",
        reply_markup=main_menu_keyboard
    )


async def cmd_help(message: types.Message):
    await message.answer(
        "Instructions: https://telegram.org/faq\n\n"
        "FAQ: https://telegram.org/faq"
    )


async def cancel(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer(
        "Action canceled",
        reply_markup=main_menu_keyboard
    )


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, CommandStart(), state="*")
    dp.register_message_handler(cmd_help, CommandHelp(), state="*")
    dp.register_message_handler(cmd_menu, commands=["menu"], state="*")
    dp.register_message_handler(cancel, Text(equals="cancel", ignore_case=True), state=crypt_states)
