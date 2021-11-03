from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import config

from functionality.backend_processes import decrypt_stego_image
from functionality.backend_processes import reset_user_data
from functionality.backend_processes import save_user_file_as_image

from keyboards.default.cryption import decryption_keyboard
from keyboards.default.main_menu import main_menu_keyboard

from states.crypting import Decrypt


async def start_decrypt(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer(
        "Send the image with a hidden and encrypted message in it",
        reply_markup=decryption_keyboard
    )
    await message.answer(
        "IMPORTANT!\n"
        "Image must be sent as a file"
    )
    await Decrypt.waiting_for_stego_image.set()


async def enter_stego_image(message: types.Message, state: FSMContext):
    await message.answer("Enter the password to find out the message hidden in the sent image")
    user_document_as_image = await save_user_file_as_image(message, 'png')
    await state.update_data(stego_image=user_document_as_image)
    await Decrypt.next()


async def enter_decryption_key(message: types.Message, state: FSMContext):
    await state.update_data(decryption_key=message.text)
    user_data = await state.get_data()
    decrypted_message_text = decrypt_stego_image(**user_data, bot_salt=config.BOT_SALT)
    if decrypted_message_text:
        await message.answer(
            "The message that the image contained:\n"
            f"{decrypted_message_text}",
            reply_markup=main_menu_keyboard
        )
    else:
        await message.answer(
            "Nothing is encrypted in the image, or your password is incorrect",
            reply_markup=main_menu_keyboard
        )
    await reset_user_data(message, state)


def register_handlers_decryption(dp: Dispatcher):
    dp.register_message_handler(start_decrypt, Text(equals="Decrypt", ignore_case=True))
    dp.register_message_handler(start_decrypt, Text(equals="Start decryption again"), state="*")
    dp.register_message_handler(enter_stego_image, content_types=['document'], state=Decrypt.waiting_for_stego_image)
    dp.register_message_handler(enter_decryption_key, state=Decrypt.waiting_for_decryption_key)
