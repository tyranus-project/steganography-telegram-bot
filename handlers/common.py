from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.builtin import CommandHelp

from functionality.backend_processes import reset_state_delete_user_data

from keyboards.default.main_menu import main_menu_keyboard


async def command_start(message: types.Message):
    channel_name = "@channel_name"
    start_welcome_message = ("Welcome!",
                             "This bot helps to hide your messages in images.",
                             f"Also recommend subscribing to {channel_name} to keep up to date with the latest changes.")
    start_useful_commands_message = ("Useful commands to get started:",
                                     "/language - change language\n/help - detailed instructions")
    await message.answer("\n\n".join(start_welcome_message))
    await message.answer("\n\n".join(start_useful_commands_message), reply_markup=main_menu_keyboard)


async def command_menu(message: types.Message):
    await message.answer("Main menu", reply_markup=main_menu_keyboard)


async def command_help(message: types.Message):
    instruction_url = "instruction_URL"
    faq_url = "FAQ_URL"
    help_message = (f"Instructions: {instruction_url}",
                    f"FAQ: {faq_url}")
    await message.answer("\n\n".join(help_message))


async def command_language(message: types.Message):
    pass


async def button_settings(message: types.Message):
    pass


async def button_support(message: types.Message):
    pass


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("No action has been taken yet")
    else:
        await reset_state_delete_user_data(message, state)
        await message.answer("Action canceled", reply_markup=main_menu_keyboard)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(command_start, CommandStart())
    dp.register_message_handler(command_help, CommandHelp())
    dp.register_message_handler(command_menu, commands="menu")
    dp.register_message_handler(cancel, Text(equals="Cancel", ignore_case=True), state="*")
