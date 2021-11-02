from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.dispatcher.filters.builtin import CommandStart

from functionality.backend_processes import reset_user_data
from keyboards.default.main_menu import main_menu_keyboard


async def command_start(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    channel_name = "@channel_name"
    start_welcome_message = ("Welcome!",
                             "This bot helps to hide your messages in images.",
                             f"Also recommend subscribing to {channel_name} to keep up to date with the latest changes.")
    start_useful_commands_message = ("Useful commands to get started:",
                                     "/language - change language\n/help - detailed instructions")
    await message.answer("\n\n".join(start_welcome_message))
    await message.answer("\n\n".join(start_useful_commands_message), reply_markup=main_menu_keyboard)


async def command_menu(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer("Main menu", reply_markup=main_menu_keyboard)


async def command_help(message: types.Message):
    instruction_url = "instruction_URL"
    faq_url = "FAQ_URL"
    help_message = (f"Instructions: {instruction_url}",
                    f"FAQ: {faq_url}")
    await message.answer("\n\n".join(help_message))


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("No action has been taken yet")
    else:
        await reset_user_data(message, state)
        await message.answer("Action canceled", reply_markup=main_menu_keyboard)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(command_start, CommandStart(), state="*")
    dp.register_message_handler(command_help, CommandHelp(), state="*")
    dp.register_message_handler(command_menu, commands="menu", state="*")
    dp.register_message_handler(cancel, Text(equals="Cancel", ignore_case=True), state="*")
