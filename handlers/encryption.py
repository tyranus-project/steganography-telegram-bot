from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from states.crypting import Encrypting

from functionality.backend_processes import download_document_as_image
from functionality.backend_processes import reset_state_delete_user_data
from functionality.backend_processes import encrypting_function

from keyboards.default.cryption import encryption_keyboard
from keyboards.default.main_menu import main_menu_keyboard


async def encrypting_start(message: types.Message, state: FSMContext):
    await reset_state_delete_user_data(message, state)
    await message.answer("Enter the text you want to encrypt", reply_markup=encryption_keyboard)
    await Encrypting.waiting_for_message.set()


async def secret_message_entering(message: types.Message, state: FSMContext):
    await state.update_data(message_to_encrypt=message.text)
    await message.answer("Send an image in which the text will be encrypted")
    await Encrypting.next()


async def original_image_entering(message: types.Message, state: FSMContext):
    await message.answer("Enter the password with which you encrypt your text, and you can also decrypt later")
    original_image_as_document = await download_document_as_image(message, 'jpg')
    await state.update_data(image_to_encrypt=original_image_as_document)
    await Encrypting.next()


async def encryption_password_entering_encrypting_end(message: types.Message, state: FSMContext):
    await state.update_data(password_to_encrypt=message.text)
    user_data = await state.get_data()
    encrypted_image = await encrypting_function(**user_data)
    await message.answer_document(types.InputFile(encrypted_image), reply_markup=main_menu_keyboard)
    await message.answer(f"Your text is encrypted in the file (image) above")
    await reset_state_delete_user_data(message, state)


def register_handlers_encryption(dp: Dispatcher):
    dp.register_message_handler(encrypting_start, Text(equals="Encrypt", ignore_case=True))
    dp.register_message_handler(encrypting_start, Text(equals="Start encryption again"), state="*")
    dp.register_message_handler(secret_message_entering, state=Encrypting.waiting_for_message)
    dp.register_message_handler(original_image_entering, content_types=['document'], state=Encrypting.waiting_for_image)
    dp.register_message_handler(encryption_password_entering_encrypting_end, state=Encrypting.waiting_for_password)
