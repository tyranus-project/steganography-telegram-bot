from aiogram import types, Dispatcher

from keyboards.default.main_menu import main_menu_keyboard


async def command_start(message: types.Message):
    pass


async def command_menu(message: types.Message):
    await message.answer("Main menu", reply_markup=main_menu_keyboard)


async def command_help(message: types.Message):
    pass


async def command_language(message: types.Message):
    pass


async def button_settings(message: types.Message):
    pass


async def button_support(message: types.Message):
    pass


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(command_menu, commands="menu")
