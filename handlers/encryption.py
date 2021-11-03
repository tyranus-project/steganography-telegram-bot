from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import config

from functionality.backend_processes import create_encrypted_stego_image
from functionality.backend_processes import reset_user_data
from functionality.backend_processes import save_user_file_as_image

from keyboards.default.cryption import encryption_keyboard
from keyboards.default.main_menu import main_menu_keyboard

from states.crypting import Encrypt


async def encrypting_start(message: types.Message, state: FSMContext):
    await reset_user_data(message, state)
    await message.answer("Enter the text you want to encrypt", reply_markup=encryption_keyboard)
    await Encrypt.waiting_for_secret_message.set()


async def secret_message_entering(message: types.Message, state: FSMContext):
    await state.update_data(secret_message=message.text)
    await message.answer("Send an image in which the text will be encrypted")
    await Encrypt.next()


async def original_image_entering(message: types.Message, state: FSMContext):
    await message.answer("Enter the password with which you encrypt your text, and you can also decrypt later")
    original_image_as_document = await save_user_file_as_image(message, 'jpg')
    await state.update_data(image_container=original_image_as_document)
    await Encrypt.next()


async def encryption_password_entering_encrypting_end(message: types.Message, state: FSMContext):
    if config.USE_BOT_SALT:
        await state.update_data(encryption_key=message.text + config.BOT_SALT)
    else:
        await state.update_data(encryption_key=message.text)
    user_data = await state.get_data()
    encrypted_stego_container = create_encrypted_stego_image(**user_data)
    await message.answer_document(types.InputFile(encrypted_stego_container), reply_markup=main_menu_keyboard)
    await message.answer(f"Your text is encrypted in the file (image) above")
    await reset_user_data(message, state)


def register_handlers_encryption(dp: Dispatcher):
    dp.register_message_handler(encrypting_start, Text(equals="Encrypt", ignore_case=True))
    dp.register_message_handler(encrypting_start, Text(equals="Start encryption again"), state="*")
    dp.register_message_handler(secret_message_entering, state=Encrypt.waiting_for_secret_message)
    dp.register_message_handler(original_image_entering, content_types=['document'], state=Encrypt.waiting_for_image_container)
    dp.register_message_handler(encryption_password_entering_encrypting_end, state=Encrypt.waiting_for_encryption_key)
