from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart

from bot.utils.keyboards import main_menu_keyboard
from bot.utils.misc import reset_user_data
from bot.utils.states import cryption_states


async def cmd_start(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer(
        "<b>Welcome!</b>\n\n"
        "<b>Steganography</b> is the art and science of invisible communication. "
        "It is achieved by hiding the message information in some other carrier media.\n\n"
        "<b>Image steganography</b> is a subset of steganography where messages are hidden in image files. "
        "The original image, before any message is hidden in it, is referred to as the <b>cover image</b>. "
        "After hiding the message in it, it is referred to as the <b>stego image</b>. "
        "For human eye, these two images must be identical (in appearance at least).",
        reply_markup=main_menu_keyboard
    )
    await message.answer(
        "This bot provides <b>image steganography tools to hide secret text messages</b>, both for encryption and decryption. "
        "Additionally, this implementation also enhance the security of the steganography through data encryption.\n\n"
        "Just use the <b>menu buttons</b> or <b>commands</b> and follow the instructions in the messages:\n"
        "/encrypt to start encryption process\n"
        "/decrypt to start decryption process\n"
    )


async def cmd_main_menu(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer(
        "Main menu",
        reply_markup=main_menu_keyboard
    )


async def cancel_action(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer(
        "The current action has been cancelled.",
        reply_markup=main_menu_keyboard
    )


def register_common_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, CommandStart(), state="*")
    dp.register_message_handler(cmd_main_menu, commands=["menu"], state="*")
    dp.register_message_handler(cancel_action, Text(equals="Cancel", ignore_case=True), state=cryption_states)
