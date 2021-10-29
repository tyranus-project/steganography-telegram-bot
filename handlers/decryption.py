from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from states.crypting import Decrypting

from functionality.backend_processes import download_document_as_image
from functionality.backend_processes import reset_state_delete_user_data
from functionality.backend_processes import decrypting_function

from keyboards.default.cryption import decryption_keyboard
from keyboards.default.main_menu import main_menu_keyboard


async def decrypting_start(message: types.Message, state: FSMContext):
    await reset_state_delete_user_data(message, state)
    await message.answer("Send image with encrypted message", reply_markup=decryption_keyboard)
    await message.answer("IMPORTANT!\nImage must be sent as a file")
    await Decrypting.waiting_for_image.set()


async def encrypted_image_entering(message: types.Message, state: FSMContext):
    await message.answer("Enter the password to find out the message hidden in the sent image")
    user_encrypted_image = await download_document_as_image(message, 'png')
    await state.update_data(image_to_decrypt=user_encrypted_image)
    await Decrypting.next()


async def decryption_password_entering_decrypting_end(message: types.Message, state: FSMContext):
    await state.update_data(password_to_decrypt=message.text)
    user_data = await state.get_data()
    decrypted_message = await decrypting_function(**user_data)
    if decrypted_message:
        await message.answer(f"Encrypted (secret) message:\n{decrypted_message}", reply_markup=main_menu_keyboard)
    else:
        await message.answer(f"Nothing is encrypted in the picture, or your password is incorrect",
                             reply_markup=main_menu_keyboard)
    await reset_state_delete_user_data(message, state)


def register_handlers_decryption(dp: Dispatcher):
    dp.register_message_handler(decrypting_start, Text(equals="Decrypt", ignore_case=True))
    dp.register_message_handler(decrypting_start, Text(equals="Start decryption again"), state="*")
    dp.register_message_handler(encrypted_image_entering, content_types=['document'], state=Decrypting.waiting_for_image)
    dp.register_message_handler(decryption_password_entering_decrypting_end, state=Decrypting.waiting_for_password)
