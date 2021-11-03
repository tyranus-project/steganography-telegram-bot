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


async def decrypting_start(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer("Send image with encrypted message", reply_markup=decryption_keyboard)
    await message.answer("IMPORTANT!\nImage must be sent as a file")
    await Decrypt.waiting_for_stego_image.set()


async def encrypted_image_entering(message: types.Message, state: FSMContext):
    await message.answer("Enter the password to find out the message hidden in the sent image")
    user_encrypted_image = await save_user_file_as_image(message, 'png')
    await state.update_data(stego_image=user_encrypted_image)
    await Decrypt.next()


async def decryption_password_entering_decrypting_end(message: types.Message, state: FSMContext):
    await state.update_data(decryption_key=message.text)
    user_data = await state.get_data()
    decrypted_message = decrypt_stego_image(**user_data, bot_salt=config.BOT_SALT)
    if decrypted_message:
        await message.answer(f"Encrypted (secret) message:\n{decrypted_message}", reply_markup=main_menu_keyboard)
    else:
        await message.answer(f"Nothing is encrypted in the picture, or your password is incorrect",
                             reply_markup=main_menu_keyboard)
    await reset_user_data(message, state)


def register_handlers_decryption(dp: Dispatcher):
    dp.register_message_handler(decrypting_start, Text(equals="Decrypt", ignore_case=True))
    dp.register_message_handler(decrypting_start, Text(equals="Start decryption again"), state="*")
    dp.register_message_handler(encrypted_image_entering, content_types=['document'], state=Decrypt.waiting_for_stego_image)
    dp.register_message_handler(decryption_password_entering_decrypting_end, state=Decrypt.waiting_for_decryption_key)
